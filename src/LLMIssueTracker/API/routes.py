import os 
os.chdir("c:\\Users\\RSR\\PYTHON\\LLMIssueTracker")
from fastapi import APIRouter
from pydantic import BaseModel

from LLMIssueTracker.services.issue_service import IssueService


router = APIRouter()

service = IssueService()


class IssueRequest(BaseModel):

    issue: str


@router.post("/analyze")

def analyze(request: IssueRequest):

    response = service.process_issue(request.issue)

    return {
        "status": "SUCCESS",
        "issue": request.issue,
        "solution": response
    }