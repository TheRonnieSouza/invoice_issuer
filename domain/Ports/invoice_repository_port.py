from abc import ABC, abstractmethod
from typing import List, Optional
from Domain.Entities.invoice import Invoice

class InvoiceRepositoryPort(ABC):
    """Port para o repositório de notas fiscais"""
    
    @abstractmethod
    async def save(self, invoice: Invoice) -> Invoice:
        """Salva uma nota fiscal"""
        pass
    
    @abstractmethod
    async def get_by_id(self, invoice_id: str) -> Optional[Invoice]:
        """Busca uma nota fiscal por ID"""
        pass
    
    @abstractmethod
    async def get_by_rps(self, rps: str, serie_rps: str) -> Optional[Invoice]:
        """Busca uma nota fiscal por RPS"""
        pass
    
    @abstractmethod
    async def get_by_nf_number(self, numero_nf: str, serie_nf: str) -> Optional[Invoice]:
        """Busca uma nota fiscal por número"""
        pass
    
    @abstractmethod
    async def update(self, invoice: Invoice) -> Invoice:
        """Atualiza uma nota fiscal"""
        pass
    
    @abstractmethod
    async def list_all(self) -> List[Invoice]:
        """Lista todas as notas fiscais"""
        pass
