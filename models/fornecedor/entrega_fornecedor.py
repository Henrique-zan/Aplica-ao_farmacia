from models.db import db
from models import Entrega
from models import Fornecedor

class EntregaFornecedor(db.Model):
    __tablename__ = 'entrega_fornecedor'
    id_entrega = db.Column("id_entrega",db.Integer(), db.ForeignKey(Entrega.id, ondelete='CASCADE'),primary_key=True)
    cnpj_fornecedor = db.Column("cnpj_fornecedor",db.String(15), db.ForeignKey(Fornecedor.cnpj, ondelete='CASCADE'),primary_key=True)

