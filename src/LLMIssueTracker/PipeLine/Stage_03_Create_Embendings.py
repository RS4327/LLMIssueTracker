import os
os.chdir(r"C:\Users\RSR\PYTHON\LLMIssueTracker/src")
from LLMIssueTracker.Entity.Config_Entity import *
from LLMIssueTracker.Config.ConfigurationManager import ConfigurationManager
from LLMIssueTracker.Components.Create_Embendings import CreateEmbedings
from LLMIssueTracker import logger




Stage_Name ="Data Create Embendings"



class CreateEmbendingsPipeLine:
    def __init__(self):
        pass
    def main(self):

        try:
            config = ConfigurationManager().get_create_embendings_config()
            embendings = CreateEmbedings(config)
            embendings.Create_Embendings()
           
            
        except Exception as e:
            raise e


if __name__=="__main__":
    try :
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
        obj=CreateEmbendingsPipeLine()
        df=obj.main()
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
        
    except Exception as e:
        logger.info(e)
        raise e
        