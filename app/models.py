from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Index

db = SQLAlchemy()

class ESPECIALIDADE(db.Model):
    indice = db.Column(db.Integer, primary_key=True)
    nome_especialidade = db.Column(db.Text)
    id_especialidade = db.Column(db.Integer)

class AGENDA(db.Model):
    id_agenda = db.Column(db.Integer, primary_key=True)
    dia_semana = db.Column(db.Text)
    hora_inicio = db.Column(db.Text)
    hora_fim = db.Column(db.Text)
    crm = db.Column(db.Text)

class EXERC_ESP(db.Model):
    crm = db.Column(db.Integer, primary_key=True)
    id_especialidade = db.Column(db.Text)

class MEDICO(db.Model):
    crm = db.Column(db.Text, primary_key=True)
    nome_medico = db.Column(db.Text)
    telefone_medico = db.Column(db.Text)
    porcentual = db.Column(db.float)

class DOENCA(db.Model):
    id_doenca = db.Column(db.Integer, primary_key=True)
    nome_doenca = db.Column(db.Text)


class CONSULTA(db.Model):
    id_consulta = db.Column(db.Integer, primary_key=True)
    crm = db.Column(db.Text)
    id_especialidade = db.Column(db.Text)
    id_paciente =  db.Column(db.Text)
    data = db.Column(db.Date)
    hora_inicio =  db.Column(db.Datetime)
    hora_fim = db.Column(db.Datetime)
    pagou = db.Column(db.Text)
    valor_pago = db.Column(db.Text)
    forma_pagamento = db.Column(db.Text)

class DIAGNOSTICO(db.Model):
    id_diagnostico = db.Column(db.Integer, primary_key=True)
    tratamento_recomendado = db.Column(db.Text)
    remedios_receitados = db.Column(db.Text)
    observacoes =  db.Column(db.Text)
    id_consulta = db.Column(db.Text)


class PACIENTE(db.Model):
    id_paciente = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.Text)
    endereco = db.Column(db.Text)
    nome_paciente  = db.Column(db.Text)
    telefone_paciente = db.Column(db.Text)
    sexo = db.Column(db.Text)
    idade = db.Column(db.Text)
