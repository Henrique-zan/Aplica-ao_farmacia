from models.db import db
from models import Produto
from models import Fornecedor

class ProdutosEntrega(db.Model):
    __tablename__ = 'produtos_entrega'
    id_produto = db.Column("id_produto",db.Integer(), db.ForeignKey(Produto.id, ondelete='CASCADE'),primary_key=True)
    cnpj_fornecedor = db.Column("cnpj_fornecedor",db.String(15), db.ForeignKey(Fornecedor.cnpj, ondelete='CASCADE'),primary_key=True)

