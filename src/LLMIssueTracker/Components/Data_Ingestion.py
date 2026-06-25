import os
from pathlib import Path

import oracledb
import pandas as pd

from LLMIssueTracker.Config.ConfigurationManager import *
from LLMIssueTracker.Utils.Common import *

os.chdir(r"C:\Users\RSR\PYTHON\LLMIssueTracker\src")


class DataIngestion:

    def __init__(self, config: DataIngestionConfig):

        self.config = config
        self.save_file = Path(self.config.local_data_file)

    # ----------------------------------
    # ORACLE CONNECTION
    # ----------------------------------
    def get_connection(self):

        dsn = oracledb.makedsn(
            self.config.oracledbconnection.host,
            self.config.oracledbconnection.port,
            service_name=self.config.oracledbconnection.service
        )

        conn = oracledb.connect(
            user=self.config.oracledbconnection.username,
            password=self.config.oracledbconnection.password,
            dsn=dsn
        )

        return conn

    # ----------------------------------
    # CREATE TABLE (RUN ONCE)
    # ----------------------------------
    def create_table(self):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE COM_LOG (
                ID NUMBER,
                TYPE VARCHAR2(50),
                PROCESS VARCHAR2(4000),
                SUB_PROCESS VARCHAR2(4000),
                LOG_TIME TIMESTAMP(6),
                UPDATE_TIMESTAMP TIMESTAMP,
                USER_NAME VARCHAR2(100),
                LOG_TEXT VARCHAR2(4000),
                PARAMETERS VARCHAR2(4000),
                STATUS VARCHAR2(4000),
                COMMENTS VARCHAR2(4000),
                PURGE_FLAG VARCHAR2(10)
            )
        """)

        conn.commit()

        cursor.close()
        conn.close()

        print("Table COM_LOG created successfully")

    # ----------------------------------
    # EXTRACT DATA FROM ORACLE
    # ----------------------------------
    def LogDataFrame(self):

        conn = self.get_connection()
        cursor = conn.cursor()

        try:

            cursor.execute("""
                SELECT OWNER, TABLE_NAME
                FROM ALL_TABLES
                WHERE TABLE_NAME = 'COM_LOG'
            """)

            print("Table check:", cursor.fetchall())

            query = f"""
                SELECT
                    ID,
                    TYPE,
                    PROCESS,
                    SUB_PROCESS,
                    LOG_TEXT,
                    STATUS,
                    COMMENTS
                FROM {self.config.source_table}
                WHERE STATUS = 'ERROR'
            """

            df = pd.read_sql(query, conn)

            # Create directory if not exists
            # self.save_file.parent.mkdir(
            #     parents=True,
            #     exist_ok=True
            # )

            df.to_csv(
                self.save_file,
                index=False
            )

            print(f"CSV saved successfully: {self.save_file}")
            print(f"Total Records: {len(df)}")

            return df

        except Exception as e:
            print(f"Error: {e}")
            raise e

        finally:
            cursor.close()
            conn.close()