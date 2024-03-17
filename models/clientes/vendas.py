from models.db import db
from models import Produto,Vendas,Funcionarios
class Vendas(db.Model):
    __tablename__ = "vendas"
    id = db.Column("id",db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    data_venda = db.Column(db.DateTime(), nullable = False)
    id_produtos = db.Column(db.Integer, db.ForeignKey(Produto.id))
    cpf_cliente = db.Column("cpf_cliente",db.String(11), db.ForeignKey(Vendas.cpf))
    cpf_funcionario = db.Column("cpf_funcionario",db.String(11), db.ForeignKey(Funcionarios.cpf))
    valor = db.Column(db.Float)

    def get_vendas():
        vendas = Vendas.query.select_from(Vendas)\
                    .add_columns(Vendas.data_venda, Vendas.id_produtos,Vendas.cpf_cliente,Vendas.cpf_funcionario,
                                 Vendas.valor,).all()
        
        return vendas
    
    def save_venda(data_venda,id_produtos, cpf_cliente,cpf_funcionario,valor):
    
        venda = Vendas(data_venda=data_venda,id_produtos=id_produtos,cpf_cliente=cpf_cliente,cpf_funcionario=cpf_funcionario,valor=valor)
        
        db.session.add(venda)
        db.session.commit()