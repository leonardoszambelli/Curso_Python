# ! = diferente
# = = igual
# > = maior
# < = menor
# >= = maior igual
# <= = menor igual

tipoEscola = input("Qual o tipo do colégio: \n [1] Público \n [2] Particular: \nR: ")
mediaAluno = int( input("Qual a média do aluno: \nR: ") ) #\n = pula linha
freqAluno = int( input("Qual a frequência do aluno: \nR: ") )
mediaCorte = 7
freqCorte = 70

if tipoEscola=="2" :
    if mediaAluno >= mediaCorte and freqAluno >= freqCorte: 
        print ('Aprovado')
    else: 
        print ('Reprovado')
if tipoEscola=="1":
    if mediaAluno>= mediaCorte or freqAluno >= freqCorte:
        print ("Aprovado")
    else:
        print("Reprovado")