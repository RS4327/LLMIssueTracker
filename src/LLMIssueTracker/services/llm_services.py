import json
import os 

os.chdir("c:\\Users\\RSR\\PYTHON\\LLMIssueTracker\\src")

from LLMIssueTracker.Components.Create_Rag_Engine import CreateRagEngine
from LLMIssueTracker.Config.ConfigurationManager import ConfigurationManager


class LLMService:

    def __init__(self):

        config = ConfigurationManager()

        rag_config = config.get_create_rag_engine()

        self.rag_engine = CreateRagEngine(rag_config)

    def analyze_issue(self, issue: str):

        response = self.rag_engine.search_similar(issue)

        return response