from datetime import datetime
from decimal import Decimal
from typing import Optional
from dataclasses import dataclass

@dataclass
class Invoice:
    """Entidade de domínio para Nota Fiscal"""
    cnpj_cpf_prestador: str
    cnpj_cpf_destinatario: str
    razao_social_destinatario: str
    endereco_destinatario: str
    numero_ende_destinatario: str
    bairro_destinatario: str
    cep_destinatario: str
    cidade_destinatario: str
    uf_destinatario: str
    email_destinatario: str
    valor_nf: Decimal
    valor_servico: Decimal
    descricao: str
    id_codigo_servico: str
    data_emissao: str
    # Campos obrigatórios adicionais
    codigo_nbs: Optional[str] = None
    cidade_prestacao_servico: Optional[str] = None
    uf_prestacao_servico: Optional[str] = None
    # Dados do prestador
    pessoa_prestador: str = "J"
    ie_prestador: Optional[str] = None
    im_prestador: Optional[str] = None
    razao_social_prestador: Optional[str] = None
    endereco_prestador: Optional[str] = None
    numero_ende_prestador: Optional[str] = None
    complemento_ende_prestador: Optional[str] = None
    bairro_prestador: Optional[str] = None
    cep_prestador: Optional[str] = None
    cidade_prestador: Optional[str] = None
    uf_prestador: Optional[str] = None
    email_prestador: Optional[str] = None
    # Dados do destinatário
    pessoa_destinatario: str = "J"
    exterior_dest: str = "0"
    ie_destinatario: Optional[str] = None
    im_destinatario: Optional[str] = None
    complemento_ende_destinatario: Optional[str] = None
    pais_destinatario: str = "Brasil"
    fone_destinatario: Optional[str] = None
    deducao: Decimal = Decimal("0.00")
    forma_de_pagamento: str = "10 DDD"
    cancelada: str = "N"
    iss_retido: str = "N"
    aliq_iss: Decimal = Decimal("0.00")
    valor_iss: Decimal = Decimal("0.00")
    bc_pis: Decimal = Decimal("0.00")
    aliq_pis: Decimal = Decimal("0.00")
    valor_pis: Decimal = Decimal("0.00")
    bc_cofins: Decimal = Decimal("0.00")
    aliq_cofins: Decimal = Decimal("0.00")
    valor_cofins: Decimal = Decimal("0.00")
    bc_csll: Decimal = Decimal("0.00")
    aliq_csll: Decimal = Decimal("0.00")
    valor_csll: Decimal = Decimal("0.00")
    bc_irrf: Decimal = Decimal("0.00")
    aliq_irrf: Decimal = Decimal("0.00")
    valor_irrf: Decimal = Decimal("0.00")
    bc_inss: Decimal = Decimal("0.00")
    aliq_inss: Decimal = Decimal("0.00")
    valor_inss: Decimal = Decimal("0.00")
    sistema_gerador: str = "Invoice Issuer System"
    serie_rps: str = "RP"
    rps: Optional[str] = None
    numero_nf: Optional[str] = None
    serie_nf: Optional[str] = None
    xml_content: Optional[str] = None
    pdf_content: Optional[bytes] = None

    def to_sigissweb_json(self) -> dict:
        """Converte a entidade para o formato JSON do SigissWeb"""
        return {
            # Dados do prestador
            "cnpj_cpf_prestador": self.cnpj_cpf_prestador,
            "pessoa_prestador": self.pessoa_prestador,
            "ie_prestador": self.ie_prestador or "isento",
            "im_prestador": self.im_prestador or "",
            "razao_social_prestador": self.razao_social_prestador or "",
            "endereco_prestador": self.endereco_prestador or "",
            "numero_ende_prestador": self.numero_ende_prestador or "",
            "complemento_ende_prestador": self.complemento_ende_prestador or "",
            "bairro_prestador": self.bairro_prestador or "",
            "cep_prestador": self.cep_prestador or "",
            "cidade_prestador": self.cidade_prestador or "",
            "uf_prestador": self.uf_prestador or "",
            "email_prestador": self.email_prestador or "",
            # Dados do destinatário
            "exterior_dest": self.exterior_dest,
            "cnpj_cpf_destinatario": self.cnpj_cpf_destinatario,
            "pessoa_destinatario": self.pessoa_destinatario,
            "ie_destinatario": self.ie_destinatario or "",
            "im_destinatario": self.im_destinatario or "",
            "razao_social_destinatario": self.razao_social_destinatario,
            "endereco_destinatario": self.endereco_destinatario,
            "numero_ende_destinatario": self.numero_ende_destinatario,
            "complemento_ende_destinatario": self.complemento_ende_destinatario or "",
            "bairro_destinatario": self.bairro_destinatario,
            "cep_destinatario": self.cep_destinatario,
            "cidade_destinatario": self.cidade_destinatario,
            "uf_destinatario": self.uf_destinatario,
            "pais_destinatario": self.pais_destinatario,
            "fone_destinatario": self.fone_destinatario or "",
            "email_destinatario": self.email_destinatario,
            # Dados da nota fiscal
            "valor_nf": f"{self.valor_nf:.2f}".replace(".", ","),
            "deducao": f"{self.deducao:.2f}".replace(".", ","),
            "valor_servico": f"{self.valor_servico:.2f}".replace(".", ","),
            "data_emissao": self.data_emissao,
            "forma_de_pagamento": self.forma_de_pagamento,
            "descricao": self.descricao,
            "id_codigo_servico": self.id_codigo_servico,
            "cancelada": self.cancelada,
            "iss_retido": self.iss_retido,
            # Impostos
            "aliq_iss": f"{self.aliq_iss:.2f}".replace(".", ","),
            "valor_iss": f"{self.valor_iss:.2f}".replace(".", ","),
            "bc_pis": f"{self.bc_pis:.2f}".replace(".", ","),
            "aliq_pis": f"{self.aliq_pis:.2f}".replace(".", ","),
            "valor_pis": f"{self.valor_pis:.2f}".replace(".", ","),
            "bc_cofins": f"{self.bc_cofins:.2f}".replace(".", ","),
            "aliq_cofins": f"{self.aliq_cofins:.2f}".replace(".", ","),
            "valor_cofins": f"{self.valor_cofins:.2f}".replace(".", ","),
            "bc_csll": f"{self.bc_csll:.2f}".replace(".", ","),
            "aliq_csll": f"{self.aliq_csll:.2f}".replace(".", ","),
            "valor_csll": f"{self.valor_csll:.2f}".replace(".", ","),
            "bc_irrf": f"{self.bc_irrf:.2f}".replace(".", ","),
            "aliq_irrf": f"{self.aliq_irrf:.2f}".replace(".", ","),
            "valor_irrf": f"{self.valor_irrf:.2f}".replace(".", ","),
            "bc_inss": f"{self.bc_inss:.2f}".replace(".", ","),
            "aliq_inss": f"{self.aliq_inss:.2f}".replace(".", ","),
            "valor_inss": f"{self.valor_inss:.2f}".replace(".", ","),
            "sistema_gerador": self.sistema_gerador,
            "serie_rps": self.serie_rps,
            "rps": self.rps,
            "codigo_nbs": self.codigo_nbs,
            "cidade_prestacao_servico": self.cidade_prestacao_servico or self.cidade_prestador,
            "uf_prestacao_servico": self.uf_prestacao_servico or self.uf_prestador
        }
