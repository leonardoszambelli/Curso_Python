# ! = diferente
# = = igual
# > = maior
# < = menor
# >= = maior igual
# <= = menor igual

mediaAluno = int( input("Qual a média do aluno: \nR: ") ) #\n = pula linha
freqAluno = int( input("Qual a frequência do aluno: \nR: ") )
mediaCorte = 7
freqCorte = 70

if mediaAluno >= mediaCorte and freqAluno >= freqCorte: 
    print ('Aprovado')
else: 
    print ('Reprovado')
    