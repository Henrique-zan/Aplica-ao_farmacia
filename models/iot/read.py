from models import db, Sensor, User
from datetime import datetime

class Read(db.Model):
    __tablename__ = "reads"
    id = db.Column("id", db.Integer(), primary_key=True)
    temperatura = db.Column("temperatura", db.Float(), nullable=False, default=0.0)
    humidade = db.Column("humidade", db.Float(), nullable=False, default=0.0)
    date_time = db.Column("date_time", db.DateTime(), nullable=False, default=datetime.now())