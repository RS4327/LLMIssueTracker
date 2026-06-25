import os
from LLMIssueTracker.Entity.Config_Entity import *
from LLMIssueTracker.Utils.Common import *
import pandas as pd
import re


class DataCleaning:
    def __init__(self,config:DataCleaningConfig):
        self.config=config
        self.save_file = Path(self.config.local_data_file)
        

    def Data_Preprocessing(self)->pd.DataFrame:
        file=Path(self.config.source_path)
        print("Reading:", file)

        #file_path = Path(r"C:\Users\RSR\PYTHON\LLMIssueTracker\artifacts\DataIngestion\com_data_log.csv")

        print(file.exists())

        df = pd.read_csv(file)

        print(df.head())
        # df = pd.read_csv(file)
        # #df = pd.read_csv(file)
        # print(df.head(1))
            
        def Clean_text(text):
            if pd.isna(text):
                return "" 
            text=str(text)

            text=re.sub(r'\n',' ',text)
            text=re.sub(r'\t',' ',text)
            text=re.sub(r'\s+',' ',text)

            return text.strip()
        df['COMMENTS']=df['COMMENTS'].apply(Clean_text)
        df['PROCESS']=df['PROCESS'].apply(Clean_text)
        df['LOG_TEXT']=df['LOG_TEXT'].apply(Clean_text)

        df['Document']=("Issue : " + df['COMMENTS'] +
                        "ROOT Casue :"+df['PROCESS']+
                        "Pkg : "+df['LOG_TEXT']
                        )
        df.to_csv(self.save_file,index=False)


        return df


        
        


