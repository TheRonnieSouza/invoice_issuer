from Core.base import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Integer
from uuid import uuid4
class Services(Base):
    __tablename__ = "services"
    
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: uuid4().hex)
    description:  Mapped[str] = mapped_column(String(100))
    service_code: Mapped[int] = mapped_column(Integer)
    service_description: Mapped[str] = mapped_column(String(100))
    nbs_code: Mapped[int] = mapped_column(Integer)
    nbs_description: Mapped[str] = mapped_column(String(100))
    
    