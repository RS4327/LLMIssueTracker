import os 
from pathlib import Path 
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
        self.index=faiss.read_index(self.config.faiss_index)
        with open(self.config.source_path,'rb') as file:
            self.docs=pickle.load(file)
        
           
    def search_similar(self, issue):

        # Create embedding for the new issue
        query_vector = self.model.encode([issue])

        # Search Top 5 similar incidents
        distances, indices = self.index.search(query_vector, k=5)

        # Retrieve similar documents
        results = []

        for idx in indices[0]:
            if idx != -1:
                results.append(self.docs[idx])

        # Prepare context
        context = "\n\n".join(results)

        # Prompt for LLM
        prompt = f"""
You are an Oracle Production Support Expert.

Below are historical production incidents.

Historical Incidents:
{context}

New Incident:
{issue}

Based on the historical incidents, provide:

1. Root Cause
2. Resolution Steps
3. SQL Fix (if required)
4. Oracle Package/Object Impact
5. Prevention Steps

Give the answer in a professional format.
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
 