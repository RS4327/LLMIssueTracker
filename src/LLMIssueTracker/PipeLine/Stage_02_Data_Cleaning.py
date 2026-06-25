import os
os.chdir(r"C:\Users\RSR\PYTHON\LLMIssueTracker/src")
from LLMIssueTracker.Entity.Config_Entity import *
from LLMIssueTracker.Config.ConfigurationManager import ConfigurationManager
from LLMIssueTracker.Components.Data_Cleaning import DataCleaning
from LLMIssueTracker import logger




Stage_Name ="Data Cleaning"



class DataCleaningPipeLine:
    def __init__(self):
        pass
    def main(self):

        try:
            config = ConfigurationManager().get_data_cleaning_config()
            preprocessing = DataCleaning(config)
            df = preprocessing.Data_Preprocessing()
            return df
            
        except Exception as e:
            raise e


if __name__=="__main__":
    try :
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
        obj=DataCleaningPipeLine()
        df=obj.main()
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
        
    except Exception as e:
        logger.info(e)
        raise e
        