import pandas as pd

df=pd.read_csv('salarios.csv')


print(df)

#traz os primeiros itens
print("-----HEAD-----")
print(df.head())

#informacoes do dataframe
print("-----INFO-----")
print(df.info())

#estatisticas
print("-----DESCRIBE-----")
print(df.describe())

#dois filtros juntos
print("-----FILTROS-----")
print(df[(df ['Idade']>20)&(df['Salario']>6000)])

#classificar as pessoas pela idade (Funcao LAMBDA)
print("-----Classificador-----")
df['Classificacao'] = df['Idade'].apply(
    lambda idade: 'Maior de idade' if idade>= 18 else 'Menor de idade'
)
print (df[['Nome', 'Idade', 'Classificacao']])

#Usando lambda com for
print("-----LAMBDA DO FOR-----")
notas=[4,5,7,2,9]
df2=pd.DataFrame({'Notas': notas})
df2['Resultado'] = df2['Notas'].apply(
    lambda nota:'Aprovado' if nota >=7 else 'Reprovado'
)

print("-----Salários do maior para o menor-----")
print(df.sort_values(by='Salario', ascending=False))

#Acessar linhas especificas
print('Primeiro Funcionário')
print(df.iloc[0])
print('Primeiro 3 Funcionários')
print(df.iloc[:3])

print("-----Idade Média-----")
print( df['Salario'].count())
print( df['Idade'].mean())
print( df['Salario'].sum())
#alem desses temos: min e max tambem

#temos duas formas para salvar
#ou criamos um novo
df.to_csv('salarios atualizados.csv')
#ou sobrescrevemos o arquivo original. 
df.to_csv('salarios.csv', index=False)