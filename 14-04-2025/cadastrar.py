from modelo import *
import sqlite3

# Sistema de cadastro de usuário
try:
    print("Por favor, Preencha os dados.")
    Nome = input("Nome-Completo: ")
    NomePai = input("Nome do Pai: ")
    NomeMae = input("Nome da Mãe: ")
    DiaNascimento = int(input("Dia de Nascimento: "))
    MesNascimento = int(input("Mês de Nascimento: "))
    AnoNascimento = int(input("Ano de Nascimento: "))
    Pais = input("País de origem: ")
    Cidade = input("Cidade atual: ")
    Trabalha = input("Trabalha? (Sim/Não): ").strip().lower()
    
    # Função que verifica se o Nome foi preenchido corretamente
    def verifica_nomes(nome, nome_pai, nome_mae, pais, cidade):
        if not nome or not nome.replace(" ", "").isalpha():
            raise ValueError("Nome inválido.")
        
        if not nome_pai or not nome_pai.replace(" ", "").isalpha():
            raise ValueError("Nome do pai inválido.")
        
        if not nome_mae or not nome_mae.replace(" ", "").isalpha():
            raise ValueError("Nome da mãe inválido.")
        
        if not pais or not pais.replace(" ", "").isalpha():
            raise ValueError("País inválido.")
        
        if not cidade or not cidade.replace(" ", "").isalpha():
            raise ValueError("Cidade inválida.")
        
        return True
        
    
    # função que verificando se data de nascimento é válida  
    if DiaNascimento < 1 or DiaNascimento > 31:
        raise ValueError("Dia inválido.")
    if MesNascimento < 1 or MesNascimento > 12:
        raise ValueError("Mês inválido.")
    if AnoNascimento < 1900 or AnoNascimento > 2025:
        raise ValueError("Ano inválido.")
    
    # Verificando se o usuário trabalha
    if (Trabalha == 'sim'):
        Cargo = input("Cargo: ")
        Empresa = input("Empresa: ")
        
        # Criando objeto da classe Profissão
        colaborador = Profissao(Nome, DiaNascimento, MesNascimento, AnoNascimento, Pais, Cidade, Cargo, Empresa)
        colaborador.Dados_Colaborador()
    
    if (Trabalha == 'não'):
        individuo = Pessoa(Nome, DiaNascimento, MesNascimento, AnoNascimento, Pais, Cidade)
        individuo.Trabalha = False
        individuo.Cargo = None
        individuo.Empresa = None
        
    else:
        print("Opção inválida. Por favor, insira 'sim' ou 'não'.")
                
except KeyboardInterrupt:
    print("Programa interrompido")
    
except ValueError:
    print("Valor inválido.")
    
    
except TypeError:
    print("Erro ao preencher, por favor varifique se as informações estão corretas.")

else:
    # Banco de dados SQLite para armazenar os dados
    try:
        conn = sqlite3.connect('cadastro.db')
        cursor = conn.cursor()
        
        # Criando tabela se não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                nome_pai TEXT,
                nome_mae TEXT,
                dia_nascimento INTEGER,
                mes_nascimento INTEGER,
                ano_nascimento INTEGER,
                pais TEXT,
                cidade TEXT,
                trabalha BOOLEAN,
                cargo TEXT,
                empresa TEXT
            )
        ''')
        
        # Inserindo dados na tabela
        cursor.execute('''
            INSERT INTO usuarios (nome, nome_pai, nome_mae, dia_nascimento, mes_nascimento, ano_nascimento, pais, cidade, trabalha, cargo, empresa)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (Nome, NomePai, NomeMae, DiaNascimento, MesNascimento, AnoNascimento, Pais, Cidade, Trabalha == 'sim', Cargo if Trabalha == 'sim' else None, Empresa if Trabalha == 'sim' else None))
        
        conn.commit()
        print("Dados salvos com sucesso.")
        
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
                
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    
    finally:
        if conn:
            conn.close()
            print("Conexão com o banco de dados fechada.")
            print("Fim do programa.")