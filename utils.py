from models import Pessoas, Usuarios
#insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Guilherme', idade=28)
    print(pessoa)
    pessoa.save()

# Consulta dados na tabela Pessoa
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    #pessoa = Pessoas.query.filter_by(nome='Alberto').first()
    print(pessoa)

#Altera dados na tabela Pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Gustavo').first()
    pessoa.nome = 'Alberto'
    pessoa.save()

#Exclui dados na tabela Pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Alberto').first()
    pessoa.delete()
def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    #insere_usuario('aaaa','bbbb')
    #insere_usuario('abner', 'rrr')
    consulta_todos_usuarios()
    #exclui_pessoa()
    #insere_pessoas()
    #consulta_pessoas()
    #altera_pessoa()
