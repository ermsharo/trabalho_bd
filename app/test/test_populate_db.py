
import unittest
from flask_sqlalchemy import SQLAlchemy
from models import  PACIENTE
from sqlalchemy import create_engine, Column, Text, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


def add_paciente(id_paciente, cpf, endereco, nome_paciente, telefone_paciente, sexo, idade):
    new_paciente = PACIENTE(id_paciente=id_paciente, cpf=cpf, endereco=endereco, nome_paciente=nome_paciente,
                            telefone_paciente=telefone_paciente, sexo=sexo, idade=idade)
    db.session.add(new_paciente)
    db.session.commit()
    
    
def update_pacient_data():
    # Read CSV into pandas DataFrame
    df = pd.read_csv("data_ref/pacients.csv")
    
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Access values in each row
        id_paciente = row['id_paciente']
        cpf = row['cpf']
        endereco = row['endereco']
        nome_paciente = row['nome_paciente']
        telefone_paciente = row['telefone_paciente']
        sexo = row['sexo']
        idade = row['idade']
        print(f"ID: {id_paciente}, CPF: {cpf}, Endereço: {endereco}, Nome: {nome_paciente}, Telefone: {telefone_paciente}, Sexo: {sexo}, Idade: {idade}")
        add_paciente(id_paciente, cpf, endereco, nome_paciente, telefone_paciente, sexo, idade)


class TestPoupulateData(unittest.TestCase):
    
    def test_add_pacient(self):
        print("Add pacientes")
        update_pacient_data()
        





if __name__ == "__main__":
    unittest.main()
