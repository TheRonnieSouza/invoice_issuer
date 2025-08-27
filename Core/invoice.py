from Core.base import Base
from uuid import uuid4
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Integer, Float

class Invoices(Base):
    __tablename__ = "invoices"
    
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: uuid4().hex)
    month: Mapped[str] = mapped_column(String(15))
    year: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String(50))
    value: Mapped[float] = mapped_column(Float)
    xml_path: Mapped[str] = mapped_column(String(100))
    pdf_path: Mapped[str] = mapped_column(String(100))