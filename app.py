from sqlalchemy import create_engine

from sqlalchemy.orm import  Mapped
from sqlalchemy.orm import  mapped_column
from Core.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Session


engine = create_engine("")


class Clients(Base):
    __tablename__ = "Clients"
    id: Mapped[str] = mapped_column(String,primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    cnpj: Mapped[str] = mapped_column(String(20))
    city_code: Mapped[str] = mapped_column(String(20))
    
    
Base.metadata.create_all(engine)
clients = Clients(id="1",name="K2",cnpj="123456",city_code="999888")
    
with Session(engine) as session:
    session.add(clients)
    session.commit()
    session.close()