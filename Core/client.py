from sqlalchemy.orm import  Mapped
from sqlalchemy.orm import  mapped_column
from sqlalchemy.orm import  Optional
from Core.base import Base


class Client(Base):
    __table__ = "Client"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    cnpj: Mapped[str]
    city_code: Mapped[Optional[str]]