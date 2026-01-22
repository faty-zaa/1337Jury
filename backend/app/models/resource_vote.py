# 1337Jury - Resource Vote Model
# This file is for: ZERO (Backend Dev 2)
# Description: Upvote/downvote model for resources

from sqlalchemy import Column, Integer, ForeignKey, Boolean, DateTime, UniqueConstraint
from sqlalchemy.sql import func
from app.database import Base


class ResourceVote(Base):
    __tablename__ = "resource_votes"

    id = Column(Integer, primary_key=True, index=True)
    resource_id = Column(Integer, ForeignKey("resources.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    is_upvote = Column(Boolean, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        UniqueConstraint('resource_id', 'user_id', name='unique_resource_vote'),
    )