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
        #PACKAGE, SQL_QUERY, ISSUE, ROOT_CAUSE, RESOLUTION
        df['PACKAGE']=df['PACKAGE'].apply(Clean_text)
        df['SQL_QUERY']=df['SQL_QUERY'].apply(Clean_text)
        df['ISSUE']=df['ISSUE'].apply(Clean_text)
        df['ROOT_CAUSE']=df['ROOT_CAUSE'].apply(Clean_text)
        df['RESOLUTION']=df['RESOLUTION'].apply(Clean_text)

        df['Document']=("PACKAGE : " + df['PACKAGE'] +
                        "SQL_QUERY :"+df['SQL_QUERY']+
                        "ISSUE : "+df['ISSUE']+
                        "ROOT_CAUSE : "+df['ROOT_CAUSE']+
                        "RESOLUTION : "+df['RESOLUTION']
                        )
        df.to_csv(self.save_file,index=False)


        return df


        
        


