from models.db import db
from models import Funcionarios
class Gerente(db.Model):
    __tablename__ = "gerente"
    cpf_funcionario = db.Column("cpf_funcionario",db.String(11),db.ForeignKey(Funcionarios.cpf), primary_key=True) # primary keys are required by SQLAlchemy
    login = db.Column(db.String(30))
    senha = db.Column(db.String(20))
    data_inicio = db.Column(db.DateTime(), nullable = False)
