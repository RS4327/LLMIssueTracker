import os 
from pathlib import Path 
import os 

os.chdir("c:\\Users\\RSR\\PYTHON\\LLMIssueTracker")
import pandas as pd 
from LLMIssueTracker.Utils.Common import * 
from LLMIssueTracker.Entity.Config_Entity import *
from sentence_transformers import SentenceTransformer
import faiss 
import pickle 

class CreateRagEngine:
    def __init__(self, 
                 config : CreateRagEngineConfig
                 ):
        self.config=config
        create_directories([self.config.root_dir])
        self.model=SentenceTransformer("Sentence-transformers/all-miniLM-L6-v2") 
        

        print("Current Working Directory :", os.getcwd())
        print("Configured FAISS Path     :", self.config.faiss_index)
        print("Absolute Path             :", Path(self.config.faiss_index).resolve())
        print("File Exists               :", Path(self.config.faiss_index).exists())

        self.index=faiss.read_index(self.config.faiss_index)
        
        with open(self.config.source_path,'rb') as file:
            self.docs=pickle.load(file)
        
           
    def search_similar(self, issue):

        # Create embedding for the new issue
        query_vector = self.model.encode([issue])

        # Search Top 5 similar incidents
        distances, indices = self.index.search(query_vector, k=5)

        # Retrieve similar documents
        best_match = ""

        if indices[0][0] != -1:
            best_match = self.docs[indices[0][0]]

        context = best_match

        # Prompt for LLM
        
        prompt = f"""
You are an Oracle Production Support Expert.

A historical incident matching the user's issue is shown below.

{context}

The user reported:

{issue}

If the historical incident already contains the answer, DO NOT create a new solution.

Return ONLY this format:

Issue:
Root Cause:
Resolution:
SQL Query:
Package:

Do not add explanations.
Do not summarize.
Do not invent information.
"""
        
        print("Total documents :", len(self.docs))
        print("Top matched indexes :", indices[0])
        print("Distances :", distances[0])

        print("\nMatched Incidents:\n")

        for i in indices[0]:
            print("="*80)
            print(self.docs[i])
            
        try:
            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response["message"]["content"]

        except Exception as e:
            print(f"Error: {e}")
            return None
 