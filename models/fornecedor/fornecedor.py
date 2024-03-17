from models.db import db

class Fornecedor(db.Model):
    __tablename__ = "fornecedor"
    cnpj = db.Column("cnpj",db.String(15), primary_key=True) # primary keys are required by SQLAlchemy
    nome = db.Column(db.String(40))
    endereço = db.Column(db.String(100))
    contato = db.Column(db.String(40))

    entrega_fornecedor = db.relationship("EntregaFornecedor", backref="fornecedor", lazy=True)
    produtos_fornecedor = db.relationship("ProdutosFornecedor", backref="fornecedor", lazy=True)

    def get_fornecedores():
        fornecedores = Fornecedor.query.select_from(Fornecedor)\
                    .add_columns(Fornecedor.cnpj, Fornecedor.nome,Fornecedor.endereço,Fornecedor.contato).all()
        
        return fornecedores
    
    def save_fornecedor(cnpj,nome, endereço,contato):
    
        fornecedor = Fornecedor(cnpj=cnpj,nome=nome,endereço=endereço,contato=contato)
        
        db.session.add(fornecedor)
        db.session.commit()


    def delete_fornecedor(cnpj):
        try:
            Fornecedor.query.filter_by(cnpj=cnpj).delete()
            db.session.commit()
            return True
        except:
            return False

    def update_fornecedor(data):
        Fornecedor.query.filter_by(cnpj=data['cnpj'])\
                .update(dict(cnpj = data['cnpj'],nome = data['nome'], endereço=data['endereço'], contato = data['contato']))
        db.session.commit()