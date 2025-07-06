import uuid

from sqlalchemy import (
    Column,
    String,
    UUID,
    CheckConstraint, ForeignKey, Index
)
from sqlalchemy.orm import declarative_base

from src.core.config import DB_SCHEMA

Base = declarative_base()
Base.metadata.schema = DB_SCHEMA


class UserModel(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)
    password = Column(String(128), nullable=False)

    __table_args__ = (
        CheckConstraint("length(email) > 5", name="email_min_length"),
        Index("idx_user_email", "email")
    )


class TokenModel(Base):
    __tablename__ = "tokens"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey(f"{DB_SCHEMA}.users.id"),
        unique=True,
        nullable=False,
        index=True
    )
    access_token = Column(String(512), nullable=False, unique=True)
    refresh_token = Column(String(512), nullable=False, unique=True)

    __table_args__ = (
        Index("idx_tokens_user_id", "user_id"),
    )
