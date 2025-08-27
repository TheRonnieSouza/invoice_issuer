from sqlalchemy.orm import  Mapped
from sqlalchemy.orm import  mapped_column
from Core.base import Base
from sqlalchemy import String, Integer
from uuid import uuid4


class Clients(Base):
    __tablename__ = "clients"
    
    id: Mapped[str] = mapped_column(String, primary_key=True,default=lambda: uuid4().hex)
    name: Mapped[str] = mapped_column(String(50))
    cnpj: Mapped[str] = mapped_column(String(20))
    city_code: Mapped[str] = mapped_column(String(20))