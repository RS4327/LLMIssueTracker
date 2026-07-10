import os
import sys
from pathlib import Path

# Project Root
PROJECT_ROOT = Path(r"C:\Users\RSR\PYTHON\LLMIssueTracker")

# Change working directory
os.chdir(PROJECT_ROOT)

# Add src folder to Python Path
sys.path.insert(0, str(PROJECT_ROOT / "src"))

# Imports
from LLMIssueTracker.PipeLine.Stage_01_Data_Ingestion import DataIngestionPipeLine
from LLMIssueTracker.PipeLine.Stage_02_Data_Cleaning import DataCleaningPipeLine
from LLMIssueTracker.PipeLine.Stage_03_Create_Embendings import CreateEmbendingsPipeLine
from LLMIssueTracker.PipeLine.Stage_04_Create_Vectors import CreateVectorsPipeLine
from LLMIssueTracker.PipeLine.Stage_05_Create_Rag_Engine import CreateRagEnginePipeLine
from LLMIssueTracker import logger

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f">>>>>>>>>> Stage : {STAGE_NAME} Started <<<<<<<<<<")

    obj = DataIngestionPipeLine()
    df=obj.main()
    print(df)

    logger.info(
        f">>>>>>>>>> Stage : {STAGE_NAME} Completed Successfully <<<<<<<<<<"
    )

except Exception as e:
    logger.exception(e)
    raise

STAGE_NAME = "Data Cleaning"

try:
    logger.info(f">>>>>>>>>> Stage : {STAGE_NAME} Started <<<<<<<<<<")

    obj = DataCleaningPipeLine()
    df=obj.main()
    print(df)

    logger.info(
        f">>>>>>>>>> Stage : {STAGE_NAME} Completed Successfully <<<<<<<<<<"
    )

except Exception as e:
    logger.exception(e)
    raise



STAGE_NAME = "Data Creaet Embendings"

try:
    logger.info(f">>>>>>>>>> Stage : {STAGE_NAME} Started <<<<<<<<<<")

    obj = CreateEmbendingsPipeLine()
    obj.main()
    #print(df)

    logger.info(
        f">>>>>>>>>> Stage : {STAGE_NAME} Completed Successfully <<<<<<<<<<"
    )

except Exception as e:
    logger.exception(e)
    raise


STAGE_NAME = "Data Creaet Vectors"

try:
    logger.info(f">>>>>>>>>> Stage : {STAGE_NAME} Started <<<<<<<<<<")

    obj = CreateVectorsPipeLine()
    obj.main()
    #print(df)

    logger.info(
        f">>>>>>>>>> Stage : {STAGE_NAME} Completed Successfully <<<<<<<<<<"
    )

except Exception as e:
    logger.exception(e)
    raise



STAGE_NAME = "Creaet Rag Engine"

try:
    logger.info(f">>>>>>>>>> Stage : {STAGE_NAME} Started <<<<<<<<<<")

    obj = CreateRagEnginePipeLine()
    results =obj.main()
    print(f'Old Earlier Incident : {results}')

    logger.info(
        f">>>>>>>>>> Stage : {STAGE_NAME} Completed Successfully <<<<<<<<<<"
    )

except Exception as e:
    logger.exception(e)
    raise