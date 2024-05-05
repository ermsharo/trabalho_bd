from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Index

db = SQLAlchemy()

class ESPECIALIDADE(db.Model):
    __tablename__ = "especialidade"
    nome_especialidade = db.Column(db.Text)
    id_especialidade =  db.Column(db.Text, primary_key=True)
    # id_especialidade = db.Column(db.Text, db.ForeignKey("client_by_cc.CC"))


class AGENDA(db.Model):
    __tablename__ = "agenda"
    id_agenda = db.Column(db.Integer, primary_key=True)
    dia_semana = db.Column(db.Text)
    hora_inicio = db.Column(db.Text)
    hora_fim = db.Column(db.Text)
    crm = db.Column(db.Text, db.ForeignKey("medico.crm"))

class EXERC_ESP(db.Model):
    __tablename__ = "exerc_esp"
    id = db.Column(db.Integer, primary_key=True)
    crm = db.Column(db.Text, db.ForeignKey("medico.crm"))
    id_especialidade = db.Column(db.Text, db.ForeignKey("especialidade.id_especialidade"))

class MEDICO(db.Model):
    __tablename__ = "medico"
    crm = db.Column(db.Text, primary_key=True)
    nome_medico = db.Column(db.Text)
    telefone_medico = db.Column(db.Text)
    porcentual = db.Column(db.Float)

class DOENCA(db.Model):
    __tablename__ = "doenca"
    id_doenca = db.Column(db.Text, primary_key=True)
    nome_doenca = db.Column(db.Text)



class DIAGNOSTICA(db.Model):
    __tablename__ = "diagnostica"
    id = db.Column(db.Integer, primary_key=True)
    id_diagnostico = db.Column(db.Text, db.ForeignKey("diagnostico.id_diagnostico"))
    id_doenca = db.Column(db.Text, db.ForeignKey("doenca.id_doenca"))


class CONSULTA(db.Model):
    __tablename__ = "consulta"
    id_consulta = db.Column(db.Integer, primary_key=True)
    crm = db.Column(db.Text)
    id_especialidade = db.Column(db.Text)
    id_paciente =  db.Column(db.Text)
    data = db.Column(db.Date)
    hora_inicio =  db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    hora_fim = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    pagou = db.Column(db.Text)
    valor_pago = db.Column(db.Text)
    forma_pagamento = db.Column(db.Text)

class DIAGNOSTICO(db.Model):
    __tablename__ = "diagnostico"
    id_diagnostico = db.Column(db.Text, primary_key=True)
    tratamento_recomendado = db.Column(db.Text)
    remedios_receitados = db.Column(db.Text)
    observacoes =  db.Column(db.Text)
    id_consulta = db.Column(db.Text)


class PACIENTE(db.Model):
    __tablename__ = "paciente"
    id_paciente = db.Column(db.Text, primary_key=True)
    cpf = db.Column(db.Text)
    endereco = db.Column(db.Text)
    nome_paciente  = db.Column(db.Text)
    telefone_paciente = db.Column(db.Text)
    sexo = db.Column(db.Text)
    idade = db.Column(db.Integer)
