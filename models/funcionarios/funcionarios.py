from models.db import db

class Funcionarios(db.Model):
    __tablename__ = "funcionarios"
    cpf = db.Column("cpf",db.String(11), primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(50))
    numero_carteira = db.Column(db.String(20))
    contato = db.Column(db.String(50))
    salario = db.Column(db.Float)
    birth_date = db.Column(db.DateTime(), nullable = False)

    vendas = db.relationship("Vendas", backref="funcionarios", lazy=True)
    farmaceutico = db.relationship("Farmaceutico", backref="funcionarios", lazy=True)
    gerente = db.relationship("Gerente", backref="funcionarios", lazy=True)

    def get_funcionarios():
        funcionarios = Funcionarios.query.select_from(Funcionarios)\
                    .add_columns(Funcionarios.cpf, Funcionarios.name,Funcionarios.numero_carteira,Funcionarios.contato,
                                 Funcionarios.salario,Funcionarios.birth_date,).all()
        
        return funcionarios
    
    def save_funcionario(cpf,name, numero_carteira,contato,salario,birth_date):
    
        funcionario = Funcionarios(cpf=cpf,name=name,numero_carteira=numero_carteira,contato=contato,salario=salario,birth_date=birth_date)
        
        db.session.add(funcionario)
        db.session.commit()


    def delete_funcionario(cpf):
        try:
            Funcionarios.query.filter_by(cpf=cpf).delete()
            db.session.commit()
            return True
        except:
            return False

    def update_funcionario(data):
        Funcionarios.query.filter_by(cpf=data['cpf'])\
                .update(dict(cpf = data['cpf'],name = data['name'], numero_carteira=data['numero_carteira'], contato = data['contato'],salario = data['salario'],birth_date = data['birth_date']))
        db.session.commit()