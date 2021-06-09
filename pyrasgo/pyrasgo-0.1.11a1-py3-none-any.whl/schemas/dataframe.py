from enum import Enum
from pydantic import BaseModel
from typing import Optional

class ShareStatus(Enum):
    PRIVATE = 'private'
    ORGANIZATION = 'organization'
    PUBLIC = 'public'

class Dataframe(BaseModel):
    id: int
    name: Optional[str]
    uniqueId: str
    authorId: int
    authorName: Optional[str]
    organizationId: int
    sharedStatus: str
    columnHash: Optional[str]


class DataframeCreate(BaseModel):    
    name: Optional[str] = None
    uniqueId: str
    sharedStatus: str = 'organization'
    columnHash: Optional[str] = None


class DataframeUpdate(BaseModel):
    name: Optional[str]
    uniqueId: Optional[str]
    sharedStatus: Optional[str]
    columnHash: Optional[str]