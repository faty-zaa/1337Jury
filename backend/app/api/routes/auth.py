# 1337Jury - Authentication Routes
# This file is for: ADMIRAL (Backend Dev 1)
# Description: 42 OAuth authentication endpoints

from fastapi import APIRouter, HTTPException, Depends, Query
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.config import settings
from app.database import get_db
from app.models.user import User
from app.services.ft_api import ft_api
from app.services.jwt_service import create_access_token, verify_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.get("/login")
async def login():
    return RedirectResponse(url=ft_api.get_authorization_url())