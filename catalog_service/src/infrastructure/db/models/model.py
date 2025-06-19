import uuid

from sqlalchemy import (
    Column,
    String,
    Integer, ForeignKey,
)
from sqlalchemy.dialects.postgresql import UUID, MONEY
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class GoodCategoryModel(Base):
    __tablename__ = "good_category"
    __table_args__ = {"schema": "goods"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(254), nullable=False, unique=True)


class GoodsModel(Base):
    __tablename__ = "goods"
    __table_args__ = {"schema": "goods"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category_id = Column(UUID(as_uuid=True), ForeignKey("goods.good_category.id"), nullable=False)
    name = Column(String, nullable=False, unique=True)
    photo_url = Column(String, nullable=True, unique=True)
    price = Column(MONEY, nullable=True)
    amount = Column(Integer, nullable=False, default=0)
