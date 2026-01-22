# 1337Jury - Resources Routes
# This file is for: ZERO (Backend Dev 2)
# Description: Learning resources hub with upvote/downvote system

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models.resource import Resource, ResourceType
from app.models.resource_vote import ResourceVote
from app.models.user import User
from app.middleware.auth import get_current_user, get_current_user_optional
from pydantic import BaseModel

router = APIRouter(prefix="/resources", tags=["Resources"])


class ResourceCreate(BaseModel):
    title: str
    url: str
    description: str | None = None
    resource_type: str = "other"
    project_id: int
