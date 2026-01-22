# 1337Jury - Resource Model
# This file is for: ZERO (Backend Dev 2)
# Description: Learning resources model with type classification

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Enum
from sqlalchemy.sql import func
from app.database import Base
import enum


class ResourceType(str, enum.Enum):
    VIDEO = "video"
    ARTICLE = "article"
    DOCUMENTATION = "documentation"
    TUTORIAL = "tutorial"
    OTHER = "other"