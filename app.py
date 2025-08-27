from sqlalchemy import create_engine
from Core.base import Base
from Core.client import Clients
from Core.invoice import Invoices
from Core.service import Services
from sqlalchemy.orm import Session

engine = create_engine("")
    
Base.metadata.create_all(engine)
clients = Clients(name="K2",cnpj="123456",city_code="999888")
invoices = Invoices(month="august", year=2025,value=16000.00, status="pending", 
                    xml_path="C:\\Projetos\\Python\\invoice_issuer\\Core",
                    pdf_path="C:\\Projetos\\Python\\invoice_issuer\\Core")    
services = Services(description="Desenvolvimento de software",service_code= 123, 
                    service_description="serviço de software",nbs_code=1234, nbs_description="teste")    

with Session(engine) as session:
    session.add(clients)
    session.add(invoices)
    session.commit()
    session.close()