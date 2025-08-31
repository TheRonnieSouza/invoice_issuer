from abc import ABC, abstractmethod
from typing import Optional
from Domain.Entities.invoice import Invoice
from Domain.ValueObjects.responses import InvoiceResponse, AuthResponse

class InvoiceServicePort(ABC):
    """Port para o serviço de emissão de notas fiscais"""
    
    @abstractmethod
    async def authenticate(self, cnpj: str, password: str) -> AuthResponse:
        """Autentica no webservice"""
        pass
    
    @abstractmethod
    async def issue_invoice(self, invoice: Invoice, token: str) -> InvoiceResponse:
        """Emite uma nota fiscal"""
        pass
    
    @abstractmethod
    async def get_invoice_pdf(self, numero_nf: str, serie: str, token: str) -> Optional[bytes]:
        """Obtém o PDF da nota fiscal"""
        pass
    
    @abstractmethod
    async def get_invoice_xml(self, numero_rps: str, serie_rps: str, token: str) -> Optional[str]:
        """Obtém o XML da nota fiscal pelo RPS"""
        pass
    
    @abstractmethod
    async def get_invoice_xml_by_nf(self, numero_nf: str, serie_nf: str, token: str) -> Optional[str]:
        """Obtém o XML da nota fiscal pelo número da NF"""
        pass
    
    @abstractmethod
    async def cancel_invoice(self, numero_nf: str, serie: str, motivo: str, token: str) -> bool:
        """Cancela uma nota fiscal"""
        pass
