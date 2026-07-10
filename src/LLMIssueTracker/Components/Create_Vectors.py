from LLMIssueTracker.Utils.Common import *
from LLMIssueTracker.Entity.Config_Entity import *
from LLMIssueTracker.Constant import * 
from sentence_transformers import SentenceTransformer
import pickle
import numpy as np
import pandas as pd
import faiss


class CreateVectors:
    def __init__(self,
                 config : CreateVectorsConfig
                 ):
        self.config=config
    def Create_Vectors(self):
        model =SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"    
        )
        df =pd.read_csv(self.config.source_path)
        docs=[]

        for _,row in df.iterrows():
            docs.append(f"""
             Issue: {row['COMMENTS']}
             Root Cause: {row['PROCESS']}
             Resolution: {row['LOG_TEXT']}
             """
             )
        vectors=model.encode(docs)
        dimentions =vectors.shape[1]
        index=faiss.IndexFlatL2(dimentions)
        index.add(vectors)

        faiss.write_index(
            index,
            self.config.faiss_index
        )

        with open(
            self.config.local_data_file,
            "wb"
        ) as f:
            pickle.dump(docs,f)

        print("FAISS index created")

        