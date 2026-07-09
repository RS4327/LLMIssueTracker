import os 
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from LLMIssueTracker.Entity.Config_Entity import CreateEmbedingsConfig
from LLMIssueTracker.Config.ConfigurationManager import ConfigurationManager
from LLMIssueTracker.Constant import *

class CreateEmbedings:
    def __init__(self,
                 config : CreateEmbedingsConfig
                 ):
        self.config=config
    
    def Create_Embendings(self):
        model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

        df=pd.read_csv(self.config.source_path)

        documents=[]
        for _,row in df.iterrows():
             text = f"""
             Issue: {row['COMMENTS']}
             Root Cause: {row['PROCESS']}
             Resolution: {row['LOG_TEXT']}
             """

             documents.append(text)
        embendings=model.encode(
            documents,
            show_progress_bar=True
        )
        print(embendings.shape)

        # Save embeddings
        embedding_path = self.config.local_data_file
        np.save(embedding_path, embendings)

        print(f"Embeddings saved at: {embedding_path}")

