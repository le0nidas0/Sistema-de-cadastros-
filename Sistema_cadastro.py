import math
import pandas as pd
import numpy as np
from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, diaNasc: int, sexo: str):
        self.__nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.__anoNasc = anoNasc
        self.__mesNasc = mesNasc
        self.__diaNasc = diaNasc
        self.__sexo = sexo
    @abstractmethod
    def Cadastrar(self):
        pass

    def Cadastro(self):
        aluno = ['Nome:', 'RG:', 'CPF:', 'Data de Nascimento:', 'Sexo:']
        dados = [self.__nome, self.__rg, self.__cpf, f'{self.__diaNasc}/{self.__mesNasc}/{self.__anoNasc}', self.__sexo]
        
        df = pd.DataFrame({'Pessoa': aluno, 'DADOS': dados})
        df.to_csv("dadosPessoais.csv", index=False)

    def exibir(self):
        print('Informações:')
        print(f'Nome: {self.__nome}.\nRg: {self.__rg}.\nCpf: {self.__cpf}.')
        print(f'Dia de nascimento: {self.__diaNasc}.\nMês de nascimento: {self.__mesNasc}.\nAno de nascimento: {self.__anoNasc}.\nSexo: {self.__sexo}.')

class Aluno(Pessoa):
    def __init__(self, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, diaNasc: int, sexo: str, codigo: int, interesse: str, desconto: float):
        super().__init__(nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo)
        self.__codigo = codigo
        self.__interesse = interesse
        self.__desconto = desconto

    def CadastrarAluno(self):
        self.Cadastrar()
    
    def Cadastrar(self):
        self.Cadastro()

        aluno = ['Codigo', 'Interesse', 'Desconto']
        dados = [self.__codigo, self.__interesse, self.__desconto]
        df_addAluno = pd.DataFrame({'Pessoa': aluno, 'DADOS': dados})
        df = pd.read_csv("dadosPessoais.csv")
        df = pd.concat([df, df_addAluno], ignore_index=True)
        df.to_csv("dadosPessoais.csv", index=False)

    def ExibirAluno(self):
        super().exibir()
        print(f'Código: {self.__codigo}.\nInteresse: {self.__interesse}.\nDesconto: {self.__desconto}.')


class Funcionario(Pessoa):
    def __init__(self, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, diaNasc: int, sexo: str,
             matricula: int, setor: str, cargo: str, nivel: str):
        super().__init__(nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo)        
        self.__matricula = matricula
        self.__setor = setor
        self.__cargo = cargo
        self.__nivel = nivel
        
    def CadastrarFuncionario(self):
        self.Cadastrar()

    def Cadastrar(self):
        self.Cadastro()
        funcionario = ['Matrícula','Setor','Cargo','Nivel']
        dados = [self.__matricula, self.__setor, self.__cargo, self.__nivel]
        df_addFnc = pd.DataFrame({'Pessoa': funcionario, 'DADOS': dados})

        df = pd.read_csv("dadosPessoais.csv")
        df = pd.concat([df, df_addFnc], ignore_index=True)
        df.to_csv("dadosPessoais.csv", index=False)

    def exibirFuncionario(self):
        print(f'Nome do funcionário: {self._Pessoa__nome}.\nSetor: {self._Funcionario__setor}.\nCargo: {self._Funcionario__cargo}.\nNível: {self._Funcionario__nivel}.')
        print(f'RG: {self._Pessoa__rg}.\nCPF: {self._Pessoa__cpf}.\nMatrícula: {self._Funcionario__matricula}\nData de nascimento: {self._Pessoa__diaNasc}/{self._Pessoa__mesNasc}/{self._Pessoa__anoNasc}.')
        print(f'Sexo: {self._Pessoa__sexo}.')


class Salario(Funcionario):
    def __init__(self, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, diaNasc: int, sexo: str,
                 matricula: int, setor: str, cargo: str, nivel: str, salarioBruto: float, salarioLiquido: float,
                 inss: float, irrf: float, plano_saude: float):
        super().__init__(nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, nivel)
        self.__salarioBruto = salarioBruto
        self.__salarioLiquido = salarioLiquido
        self.__inss = inss
        self.__irrf = irrf
        self.__plano_saude = plano_saude
        self.__nivel = nivel
        self.__salarioCordenador = 0
        self.__salarioProfessor = 0
        self.__salarioTecnico = 0
        self.__salarioCordenadorAdm = 0
        self.__cargo = cargo
    
    def CadastrarSalario(self):
        self.CadastrarFuncionario()
        professor = ['Salario Burto','Salario Liquido']
        dados = [self.__salarioBruto, self.__salarioLiquido]
        df_addProf = pd.DataFrame({'Pessoa': professor, 'DADOS': dados})

        df = pd.read_csv("dadosPessoais.csv")
        df = pd.concat([df, df_addProf], ignore_index=True)
        df.to_csv("dadosPessoais.csv", index=False)

    def calcular_salario(self):
        if self.__nivel == "I":
            salarioProfessor = 6500
            salarioCordenador = (0.15 * salarioProfessor) + salarioProfessor
        elif self.__nivel == "II":
            salarioProfessor = 8325.5
            salarioCordenador = (0.15 * salarioProfessor) + salarioProfessor
        elif self.__nivel == "III":
            salarioProfessor = 12568.43
            salarioCordenador = (0.15 * salarioProfessor) + salarioProfessor
        elif self.__nivel == "A":
            salarioTecnico = 1520.25
            self.__salarioCordenadorAdm = (0.135 * salarioTecnico) + salarioTecnico
        elif self.__nivel == "B":
            salarioTecnico = 2362.67
            self.__salarioCordenadorAdm = (0.135 * salarioTecnico) + salarioTecnico
        elif self.__nivel == "C":
            salarioTecnico = 2988.92
            self.__salarioCordenadorAdm = (0.135 * salarioTecnico) + salarioTecnico
        elif self.__nivel == "D":
            salarioTecnico = 3572.77
            self.__salarioCordenadorAdm = (0.135 * salarioTecnico) + salarioTecnico
        elif self.__nivel == "E":
            salarioTecnico = 4878.67
            self.__salarioCordenadorAdm = (0.135 * salarioTecnico) + salarioTecnico
        
        if self.__cargo.lower() == "professor":
            salarioBruto = salarioProfessor
        elif self.__cargo.lower() == "coordenador":
            salarioBruto = salarioCordenador
        elif self.__cargo.lower() == "tecnico":
            salarioBruto = salarioTecnico
        elif self.__cargo.lower() == "coordenadoradministrativo":
            salarioBruto = self.__salarioCordenadorAdm

        self.__salarioLiquido = self.__salarioBruto - self.__inss - self.__irrf 


class Professor(Funcionario):
    def __init__(self, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, diaNasc: int, sexo: str,
             matricula: int, setor: str, cargo: str, nivel: str, formacao:str, disciplina:str):
        super().__init__(nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, nivel)
        self.__formacao = formacao
        self.__disciplina = disciplina
        self.salarioProfessor = 0
        self.__nivel = nivel

    def CadastrarProfessor(self):
        self.CadastrarFuncionario()
        professor = ['Formação','Disciplina']
        dados = [self.__formacao, self.__disciplina]
        df_addProf = pd.DataFrame({'Pessoa': professor, 'DADOS': dados})

        df = pd.read_csv("dadosPessoais.csv")
        df = pd.concat([df, df_addProf], ignore_index=True)
        df.to_csv("dadosPessoais.csv", index=False)

        if self.__nivel == "I":
            self.salarioProfessor = 6500
        elif self.__nivel == "II":
            self.salarioProfessor = 8325.5
        elif self.__nivel == "III":
            self.salarioProfessor = 12568.43

    def ExibirProfessor(self):
        super().exibirFuncionario()
        print(f'Formação: {self._Professor__formacao}.\nNível: {self._Funcionario__nivel}.\nDisciplina: {self._Professor__disciplina}.')
        print(f'\nSalário: R$ {self.salarioProfessor}.')


class Matricula(Aluno):
    def __init__(self, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, diaNasc: int, sexo: str, codigo: int, interresse: str, desconto: float,
                 id: int, mesMatricula: int, anoMatricula: int):
        super().__init__(nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, codigo, interresse, desconto)

        self.__id = id
        self.__mesMatricula = mesMatricula
        self.__anoMatricula = anoMatricula
    
    def Matricular(self):
        self.CadastrarAluno()
        matricula = ['ID', 'Mês Matricula', 'Ano Matricula']
        dados = [self.__id, self.__mesMatricula, self.__anoMatricula]
        df_addMat = pd.DataFrame({'Pessoa': matricula, 'DADOS': dados})

        df = pd.read_csv("dadosPessoais.csv")
        df = pd.concat([df, df_addMat], ignore_index=True)
        df.to_csv("dadosPessoais.csv", index=False)


class Curso(Professor):

    def __init__(self, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, diaNasc: int, sexo: str,
             matricula: int, setor: str, cargo: str, nivel: str, formacao:str, disciplina:str
             ,titulo: str, descricao: str, valor: float, sala: str):
        super().__init__(nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, nivel, formacao,
                         disciplina)

        self.__titulo = titulo
        self.__descricao = descricao
        self.__valor = valor
        self.__sala = sala

    def CadastrarCurso(self):
        curso = ['Titulo', 'Descrição', 'valor', 'Sala']
        dados = [self.__titulo, self.__descricao, self.__valor, self.__sala]

        df = pd.DataFrame({'Curso': curso, 'DADOS': dados})
        df.to_csv("dadosDoCurso.csv", index=False)

    def ExibirCurso(self):
        print(f'Título: {self.__titulo}.\nDescrição: {self.__descricao}.')
        print(f'Valor: {self.__valor}.\nSala: {self.__sala}.')

    def CalcularNumMinAlunos(self):
        if self._Funcionario__nivel == 'I':
            print(f'Serão necessários {math.ceil(6500 / self.__valor)} alunos.')
        elif self._Funcionario__nivel == 'II':
            print(f'Serão necessários {math.ceil(8325.50 / self.__valor)} alunos.')
        elif self._Funcionario__nivel == 'III':
            print(f'Serão necessários {math.ceil(12568.43 / self.__valor)} alunos.')


class Coordenador(Professor):
    def __init__(self, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, diaNasc: int, sexo: str,
                 matricula: int, setor: str, cargo: str, nivel: str, formacao: str, disciplina: str,
                 area: str, plusSalario: float):
        super().__init__(nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, nivel, formacao,
                         disciplina)
        self.area = area
        self.plusSalario = plusSalario
        self.__nivel = nivel

    def CadastrarCoordenador(self):
        self.CadastrarProfessor()
        coordenador = ['Área', 'Plus Salário']
        dados = [self.area, self.plusSalario]
        df_addCoord = pd.DataFrame({'Pessoa': coordenador, 'DADOS': dados})

        df = pd.read_csv("dadosPessoais.csv")
        df = pd.concat([df, df_addCoord], ignore_index=True)
        df.to_csv("dadosPessoais.csv", index=False)

        if self.__nivel == "I":
            salarioProfessor = 6500
            self.salarioCordenador = (0.15 * salarioProfessor) + salarioProfessor
        elif self.__nivel == "II":
            salarioProfessor = 8325.5
            self.salarioCordenador = (0.15 * salarioProfessor) + salarioProfessor
        elif self.__nivel == "III":
            salarioProfessor = 12568.43
            self.salarioCordenador = (0.15 * salarioProfessor) + salarioProfessor

    def ExibirCoordenadorProf(self):
        super().ExibirProfessor()
        print(f'Área: {self.area}.')



class coordenadorAdm(Salario, Funcionario):
    def __init__(self, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, diaNasc: int, sexo: str,
                 matricula: int, setor: str, cargo: str, nivel: str, salarioBruto: float, salarioLiquido: float,
                 inss: float, irrf: float, plano_saude: float, area: str, plusSalario: float):
        super().__init__(nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, nivel, salarioBruto,
                         salarioLiquido, inss, irrf, plano_saude)
        self.__area = area
        self.__plusSalario = plusSalario
        self.__nivel = nivel

    def cadastrarCoordenadorAdm(self):
        self.CadastrarSalario()
        funcionario = ['area', 'Plus Salario']
        dados = [self.__area, self.__plusSalario]
        df_addFnc = pd.DataFrame({'Pessoa': funcionario, 'DADOS': dados})

        df = pd.read_csv("dadosPessoais.csv")
        df = pd.concat([df, df_addFnc], ignore_index=True)
        df.to_csv("dadosPessoais.csv", index=False)

        if self.__nivel == "A":
            salarioTecnico = 1520.25
            self.__salarioCordenadorAdm = (0.135 * salarioTecnico) + salarioTecnico
        elif self.__nivel == "B":
            salarioTecnico = 2362.67
            self.__salarioCordenadorAdm = (0.135 * salarioTecnico) + salarioTecnico
        elif self.__nivel == "C":
            salarioTecnico = 2988.92
            self.__salarioCordenadorAdm = (0.135 * salarioTecnico) + salarioTecnico
        elif self.__nivel == "D":
            salarioTecnico = 3572.77
            self.__salarioCordenadorAdm = (0.135 * salarioTecnico) + salarioTecnico
        elif self.__nivel == "E":
            salarioTecnico = 4878.67
            self.__salarioCordenadorAdm = (0.135 * salarioTecnico) + salarioTecnico

    def exibirCoordenadorAdm(self):
        super().exibirFuncionario()
        print(f'Área: {self._coordenadorAdm__area}')
        print(f'Plus Salário: {self._coordenadorAdm__plusSalario}')
    
    def calcularPlusSalario(self):
        print(f'Salário final: R${self.__salarioCordenadorAdm}')
