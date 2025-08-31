from dataclasses import dataclass

@dataclass
class InvoiceResponse:
    """Resposta da emissão de nota fiscal"""
    success: bool
    numero_nf: str = None
    serie_nf: str = None
    rps: str = None
    serie_rps: str = None
    message: str = None
    error: str = None

@dataclass
class AuthResponse:
    """Resposta da autenticação"""
    success: bool
    token: str = None
    error: str = None
