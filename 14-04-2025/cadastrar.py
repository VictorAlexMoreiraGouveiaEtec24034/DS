from modelo import *
import sqlite3

# Função que trata o input verificando se foi digitado somente texto
def Tratamento_Data(Dia = int, Mes = int, Ano = int) -> bool:
    if ((Dia == 0) and (Mes == 0) and (Ano == 0)):
        print("Dado vazio não é permitido")
        return False

    else:
        if DiaNascimento < 1 or DiaNascimento > 31:
            raise ValueError("Dia inválido.")
            return False
        if MesNascimento < 1 or MesNascimento > 12:
            raise ValueError("Mês inválido.")
            return False
        if AnoNascimento < 1900 or AnoNascimento > 2025:
            raise ValueError("Ano inválido.")
            return False

    return True
def Tratamento_Nomes(conteudo = str) -> str:
    try:
        formatado = conteudo.replace(" ", "")

        if not formatado:
            raise ValueError("Dados não preenchido")

        assert formatado.isalpha() == True

    except AssertionError:
        print("Somente é permitido palavras")

    except TypeError:
        print("Essa função não trata esse tipo de dado. Ele vai tratar somente strings")

    except ValueError:
        print("Ops! Aconteceu um erro no valor")

    else:
        return conteudo.replace(conteudo[0], conteudo[0].upper())


def validar_input(conteudo: str, tipo: str) -> str:
    """
    Função genérica para validar e tratar inputs.
    - conteudo: o valor fornecido pelo usuário.
    - tipo: o tipo do input (ex: 'empresa', 'cargo', 'trabalha').
    """
    try:
        # Remove espaços no início e fim
        conteudo = conteudo.strip()

        # Verifica se o campo está vazio
        if not conteudo:
            raise ValueError("O campo não pode estar vazio.")

        # Validações específicas com base no tipo
        if tipo == "empresa" or tipo == "cargo":
            if not conteudo.replace(" ", "").isalnum():
                raise ValueError(f"O campo '{tipo}' só pode conter letras, números e espaços.")

        elif tipo == "trabalha":
            if conteudo.lower() not in ["sim", "não"]:
                raise ValueError("A resposta deve ser 'Sim' ou 'Não'.")

        # Formatar campo para que a primeira letra seja maiúscula
        conteudo = conteudo.capitalize()

    except ValueError as e:
        print(f"Erro: {e}")
        return None

    else:
        return conteudo


# Sistema de cadastro de usuário
try:
    print("Por favor, Preencha os dados.")
    print("")

    # Coleta os dados do usuário e em seguida já fará o tratamente para ver se o dado é válido
    Nome = input("Nome-Completo: ")
    Tratamento_Nomes(Nome)

    NomePai = input("Nome do Pai: ")
    Tratamento_Nomes(NomePai)

    NomeMae = input("Nome da Mãe: ")
    Tratamento_Nomes(NomeMae)

    DiaNascimento = int(input("Dia de Nascimento: "))
    MesNascimento = int(input("Mês de Nascimento: "))
    AnoNascimento = int(input("Ano de Nascimento: "))
    Tratamento_Data(DiaNascimento, MesNascimento, AnoNascimento)

    Pais = input("País de origem: ")
    Tratamento_Nomes(Pais)

    Cidade = input("Cidade atual: ")
    Tratamento_Nomes(Cidade)

    Trabalha = input("Trabalha? (Sim/Não): ").strip().lower()

    
    # Verificando se o usuário trabalha
    Empresa = validar_input(input("Digite o nome da empresa: "), "empresa")
    if Empresa:
        print(f"Nome da empresa validado: {Empresa}")

    Cargo = validar_input(input("Digite seu cargo: "), "cargo")
    if Cargo:
        print(f"Cargo validado: {Cargo}")

    Trabalha = validar_input(input("Você trabalha? (Sim/Não): "), "trabalha")
    if Trabalha:
        print(f"Resposta validada: {Trabalha}")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

except KeyboardInterrupt:
    print("Programa interrompido")
    
except ValueError:
    print("Valor inválido.")
    
except AssertionError:
    print("Dado preenchido de maneire incorreta. Por, favor inserir somente letras")

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