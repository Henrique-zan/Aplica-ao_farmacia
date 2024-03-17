from models.db import db

class Cliente(db.Model):
    __tablename__ = "clientes"
    cpf = db.Column("cpf",db.String(11), primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    contact = db.Column(db.String(50))
    birth_date = db.Column(db.DateTime(), nullable = False)

    vendas = db.relationship("Vendas", backref="clientes", lazy=True)
    
    def get_clientes():
        clientes = Cliente.query.select_from(Cliente)\
                    .add_columns(Cliente.cpf, Cliente.name,Cliente.address,Cliente.contact,
                                 Cliente.birth_date,).all()
        
        return clientes
    
    def save_cliente(cpf,name, address,contact,birth_date):
    
        cliente = Cliente(cpf=cpf,name=name,address=address,contact=contact,birth_date=birth_date)
        
        db.session.add(cliente)
        db.session.commit()


    def delete_cliente(cpf):
        try:
            Cliente.query.filter_by(cpf=cpf).delete()
            db.session.commit()
            return True
        except:
            return False

    def update_cliente(data):
        Cliente.query.filter_by(cpf=data['cpf'])\
                .update(dict(cpf = data['cpf'],name = data['name'], address=data['address'], contact = data['contact'],birth_date = data['birth_date']))
        db.session.commit()