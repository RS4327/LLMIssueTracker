import os
os.chdir(r"C:\Users\RSR\PYTHON\LLMIssueTracker/src")
from LLMIssueTracker.Entity.Config_Entity import *
from LLMIssueTracker.Config.ConfigurationManager import ConfigurationManager
from LLMIssueTracker.Components.Create_Rag_Engine import CreateRagEngine
from LLMIssueTracker import logger




Stage_Name ="Data Create Rag Engine"



class CreateRagEnginePipeLine:
    def __init__(self):
        pass
    def main(self):
        incidents ='ORA-01722: invalid number'
        try:
            config = ConfigurationManager().get_create_rag_engine()
            RagEngine = CreateRagEngine(config)
            results = RagEngine.search_similar(incidents)
            return results
            
        except Exception as e:
            raise e


if __name__=="__main__":
    try :
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
        obj=CreateRagEnginePipeLine()
        df=obj.main()
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
        
    except Exception as e:
        logger.info(e)
        raise e
        