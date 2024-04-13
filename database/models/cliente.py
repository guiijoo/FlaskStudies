from peewee import CharField, DateField, Model
from database.database import db

class Cliente(Model):
    name = CharField()
    email = CharField()
    data_registro = DateField()
    
    class Meta:
        database = db