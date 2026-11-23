
def minhaFuncao(curso):
    print("Curso de "+ curso + " na Clarify")
    
minhaFuncao("Python")
minhaFuncao("SQL")
minhaFuncao("Claude")


cidades = ['São Paulo', 'Ribeirão Pires', 'Mauá', 'Cotia', 'Poá']
contador = 0

def minhaFuncaoMelhorada(item01,item02):
    print(str(item02) + " - " + item01)

for cidade in cidades:
    contador = contador+1
    minhaFuncaoMelhorada(cidade, contador)
    
#desafio 07 
nome=input("Qual é o seu nome: ")
anoNasc=input("Em que ano você nasceu: ")
anoAtual=2026
idade=anoAtual-int(anoNasc)
print('Olá '+ nome + ' você tem '+ str(idade) + ' anos')
continuar = input("Quer fazer novamente: ")
botao = True
resposta = "sim"
while botao:
    print (resposta)

#resposta correta no 07_desafio