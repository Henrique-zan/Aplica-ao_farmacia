from models.db import db
from models import Produto,Funcionarios,Cliente
from sqlalchemy import func
from datetime import date

class Vendas(db.Model):
    __tablename__ = "vendas"
    id = db.Column("id",db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    data_venda = db.Column(db.Date(), nullable = False)
    id_produtos = db.Column(db.Integer, db.ForeignKey(Produto.id))
    cpf_cliente = db.Column("cpf_cliente",db.String(11), db.ForeignKey(Cliente.cpf))
    cpf_funcionario = db.Column("cpf_funcionario",db.String(11), db.ForeignKey(Funcionarios.cpf))
    valor = db.Column(db.Float)

    def get_vendas():
        vendas = Vendas.query.select_from(Vendas)\
                    .add_columns(Vendas.data_venda, Vendas.id_produtos,Vendas.cpf_cliente,Vendas.cpf_funcionario,
                                 Vendas.valor,).all()
        return vendas


    def get_soma_vendas_hoje():
        hoje = date.today().strftime("%Y/%m/%d")
        soma = Vendas.query.with_entities(func.sum(Vendas.valor)).filter(Vendas.data_venda == hoje).scalar()
        return soma



    def get_soma_vendas():
        soma = Vendas.query.with_entities(func.sum(Vendas.valor)).scalar()
        return soma

    def get_ultimas_vendas():
        ultimas_vendas = Vendas.query.join(Cliente, Vendas.cpf_cliente == Cliente.cpf) \
                        .join(Funcionarios, Vendas.cpf_funcionario == Funcionarios.cpf) \
                        .join(Produto, Vendas.id_produtos == Produto.id) \
                        .add_columns(
                                     Cliente.name.label('cliente_nome'), 
                                     Produto.name.label('produto_nome'), 
                                     Vendas.valor.label('valor')) \
                        .order_by(Vendas.data_venda.desc()) \
                        .limit(7) \
                        .all()
        return ultimas_vendas

    
    def save_venda(id_produtos,cpf_cliente,cpf_funcionario,valor):
    
        venda = Vendas(data_venda=date.today(),id_produtos=id_produtos,cpf_cliente=cpf_cliente,cpf_funcionario=cpf_funcionario,valor=valor)
        
        db.session.add(venda)
        db.session.commit()