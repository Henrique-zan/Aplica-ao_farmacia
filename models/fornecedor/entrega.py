from models.db import db
from models import Fornecedor
class Entrega(db.Model):
    __tablename__ = "entrega"
    id = db.Column("id",db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    date = db.Column(db.DateTime(), nullable = False)
    cnpj_fornecedor = db.Column("cnpj_fornecedor",db.String(15), db.ForeignKey(Fornecedor.cnpj))

    entrega_fornecedor = db.relationship("EntregaFornecedor", backref="entrega", lazy=True)