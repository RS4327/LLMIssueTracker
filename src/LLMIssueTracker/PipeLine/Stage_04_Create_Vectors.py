import os
os.chdir(r"C:\Users\RSR\PYTHON\LLMIssueTracker/src")
from LLMIssueTracker.Entity.Config_Entity import *
from LLMIssueTracker.Config.ConfigurationManager import ConfigurationManager
from LLMIssueTracker.Components.Create_Vectors import CreateVectors
from LLMIssueTracker import logger




Stage_Name ="Data Create Vectors"



class CreateVectorsPipeLine:
    def __init__(self):
        pass
    def main(self):

        try:
            config_manager = ConfigurationManager()
            config = config_manager.get_create_vectors_config()
            vectors = CreateVectors(config)
            vector = vectors.Create_Vectors()
           
            
        except Exception as e:
            raise e


if __name__=="__main__":
    try :
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
        obj=CreateVectorsPipeLine()
        obj.main()
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
        
    except Exception as e:
        logger.info(e)
        raise e
        