from pathlib import Path
import os 
from LLMIssueTracker.Utils.Common import *
from LLMIssueTracker.Constant import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from LLMIssueTracker.Entity.Config_Entity import (
    DataIngestionConfig,
    oracleDBconnection
    )
from LLMIssueTracker.Entity.Config_Entity import DataCleaningConfig
from LLMIssueTracker.Entity.Config_Entity import CreateEmbedingsConfig
from LLMIssueTracker.Entity.Config_Entity import CreateVectorsConfig
from LLMIssueTracker.Entity.Config_Entity import CreateRagEngineConfig

class ConfigurationManager:

    def __init__(
        self,
        Config_Path=CONFIG_FILE_PATH,
        Param_Path=PARAMS_FILE_PATH
    ):
        # Project Root Directory
        # C:\Users\RSR\PYTHON\LLMIssueTracker
        ROOT_DIR = Path(__file__).resolve().parents[3]
        # Read configuration files
        print("ROOT_DIR :", ROOT_DIR)

        config_path = ROOT_DIR / "Config" / "Config.yaml"
        params_path = ROOT_DIR / "Params.yaml"

        print("Config Path :", config_path)
        print("Config Exists :", config_path.exists())

        self.config = Read_Yaml(config_path)
        self.params = Read_Yaml(params_path)
        
          

        print("Current Working Directory:", os.getcwd())

        for p in Path(".").rglob("*.yaml"):
            print("Found YAML:", p.resolve())
        # self.config=Read_Yaml(Path("Config/Config.yaml"))
        # #self.config = Read_Yaml(Path(Config_Path))
        # self.params = Read_Yaml(Path(Param_Path))

        # Load Data_Ingestion section from Config.yaml
        self.Data_Ingestion = self.config.Data_Ingestion
        self.Data_Cleaning = self.config.Data_Cleaning
        self.Create_Embendings=self.config.Create_Embendings
        self.Create_Vectors=self.config.Create_Vectors
        self.Create_Rag_Engine =self.config.Create_Rag_Engine

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = self.Data_Ingestion
        print("get Current Working Directory:", os.getcwd())
        os.chdir("c:\\Users\\RSR\\PYTHON\\LLMIssueTracker")
        create_directories([config.root_dir])
        
        oracle_config = oracleDBconnection(
            host=config.oracledbconnection.host,
            port=config.oracledbconnection.port,
            service=config.oracledbconnection.service,
            username=config.oracledbconnection.username,
            password=config.oracledbconnection.password
        )

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            oracledbconnection=oracle_config,
            source_table=config.source_table,
            local_data_file=config.local_data_file
        )

        return data_ingestion_config
    def get_data_cleaning_config(self) -> DataCleaningConfig:

        config = self.Data_Cleaning
        os.chdir("c:\\Users\\RSR\\PYTHON\\LLMIssueTracker")
        create_directories([config.root_dir])

        data_cleaning_config = DataCleaningConfig(
            root_dir=config.root_dir,
            source_path=config.source_path,
            local_data_file=config.local_data_file
            
        )

        return data_cleaning_config
    def get_create_embendings_config(self)->CreateEmbedingsConfig:
        config=self.Create_Embendings
        os.chdir("c:\\Users\\RSR\\PYTHON\\LLMIssueTracker")
        create_directories([config.root_dir])

        create_embendings_config=CreateEmbedingsConfig(
            root_dir=config.root_dir,
            source_path=config.source_path,
            local_data_file=config.local_data_file
        )
        return create_embendings_config
    def get_create_vectors_config(self) -> CreateVectorsConfig:

        config=self.Create_Vectors
        os.chdir("c:\\Users\\RSR\\PYTHON\\LLMIssueTracker")
        create_directories([config.root_dir])
        create_vectors_config=CreateVectorsConfig(
            root_dir=config.root_dir,
            faiss_index=config.faiss_index,
            source_path=config.source_path,
            local_data_file=config.local_data_file
        )
        return create_vectors_config
    def get_create_rag_engine(self)-> CreateRagEngineConfig:
        config=self.config.Create_Rag_Engine

        create_directories([config.root_dir])
        create_rag_engine=CreateRagEngineConfig(
            root_dir=config.root_dir,
            faiss_index=config.faiss_index,
            source_path=config.source_path,
            local_data_file=config.local_data_file
        )        

        return create_rag_engine
        

