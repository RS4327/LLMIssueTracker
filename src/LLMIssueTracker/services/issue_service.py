import os 

os.chdir("c:\\Users\\RSR\\PYTHON\\LLMIssueTracker\\src")
from LLMIssueTracker.services.llm_services import LLMService


class IssueService:

    def __init__(self):

        self.llm = LLMService()

    def process_issue(self, issue):

        return self.llm.analyze_issue(issue)