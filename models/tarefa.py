from sqlalchemy import Column, Integer, String, Boolean, Date
from datetime import date
from models.base import Base

class Tarefa(Base):
    __tablename__ = 'tarefa'

    id = Column('pk_tarefa', Integer, primary_key=True)
    data_criacao = Column(Date, default=date.today)
    data_conclusao = Column(Date, nullable=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(String(1000), nullable=False)
    status = Column(Boolean, default=False)


    def __init__(self, titulo: str, descricao: str) -> None:
        self.titulo = titulo
        self.descricao = descricao


    def atualiza_data_conclusao(self) -> None:
        self.data_conclusao = date.today()
