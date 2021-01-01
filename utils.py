from models import Pessoas, db_session
#insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Gustavo', idade=17)
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


if __name__ == '__main__':
    #exclui_pessoa()
    #insere_pessoas()
    consulta_pessoas()
    #altera_pessoa()