# Recode Requests Routes - Mock Evaluation & Recoding
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models.recode_request import RecodeRequest
from app.models.user import User
from app.models.project import Project
from app.middleware.auth import get_current_user, get_staff_user
from pydantic import BaseModel

router = APIRouter(prefix="/recodes", tags=["Recode Requests"])

class RecodeCreate(BaseModel):
    project_id: int
    campus: str
    meeting_platform: str
    meeting_link: str | None = None
    description: str | None = None


class RecodeUpdate(BaseModel):
    campus: str | None = None
    meeting_platform: str | None = None
    meeting_link: str | None = None
    description: str | None = None
