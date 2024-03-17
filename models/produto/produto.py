from models.db import db

class Produto(db.Model):
    __tablename__ = "produtos"
    id = db.Column("id",db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(50))
    type = db.Column(db.String(50))
    sector = db.Column(db.String(50))
    current_price = db.Column(db.Float)
    available_quantity = db.Column(db.Integer)
    batch_date = db.Column(db.DateTime(), nullable = False)

    vendas = db.relationship("Vendas", backref="produtos", lazy=True)
    produtos_fornecedor = db.relationship("ProdutosFornecedor", backref="produtos", lazy=True)
    produtos_entrega = db.relationship("ProdutosEntrega", backref="produtos", lazy=True)
    
    
    def get_produtos():
        produtos = Produto.query.select_from(Produto)\
                    .add_columns(Produto.id, Produto.name,Produto.type,Produto.sector, Produto.current_price, Produto.available_quantity, 
                                 Produto.batch_date,).all()
        
        return produtos
    
    def save_produto(name, type,sector, current_price, available_quantity,batch_date):
    
        produto = Produto(name=name,type=type,sector=sector,current_price=current_price,available_quantity=available_quantity,batch_date=batch_date)
        
        db.session.add(produto)
        db.session.commit()


    def delete_produto(id):
        try:
            Produto.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False

    def update_produto(data):
        Produto.query.filter_by(id=data['id'])\
                .update(dict(name = data['name'], type=data['type'], sector = data['sector'], 
                        current_price = data['current_price'], available_quantity = data['available_quantity'], 
                        batch_date = data['batch_date']))
        db.session.commit()