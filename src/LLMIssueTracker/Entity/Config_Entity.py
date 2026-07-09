from pathlib import Path 
import os 
from dataclasses import dataclass

@dataclass
class oracleDBconnection:
    host : str
    port : 1521
    service : str 
    username : str 
    password : str 

@dataclass
class DataIngestionConfig:
    root_dir : Path
    oracledbconnection : oracleDBconnection 
    source_table : str 
    local_data_file : str 
    
@dataclass
class DataCleaningConfig:
    root_dir : Path
    source_path : str
    local_data_file : str
    
@dataclass
class CreateEmbedingsConfig:
    root_dir : Path 
    source_path : str
    local_data_file : str
@dataclass
class CreateVectorsConfig:
    root_dir : Path 
    source_path : str
    local_data_file : str 