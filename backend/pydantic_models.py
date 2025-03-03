from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

class ModelName(str, Enum):
    llama3 = "llama3-8b-8192"

class QueryInput(BaseModel):
    question: str
    session_id: str = Field(default=None)
    model_name: ModelName = Field(default=ModelName.llama3)

class QueryResponse(BaseModel):
    answer: str
    session_id: str
    model_name: ModelName

class DocumentInfo(BaseModel):
    id: str
    filename: str
    upload_timestamp: datetime

class DeleteFileRequest(BaseModel):
    file_id: str 
