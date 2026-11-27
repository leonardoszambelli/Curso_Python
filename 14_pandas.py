import pandas as pd


data = {
    'Nome': ['Caio', 'Lucas', 'Nicole', 'Leonardo','Rafael'],
    'Idade': [39,25,16,35,20],
    'Salario':[5000,6000,7000,8000,9000]
}

df=pd.DataFrame(data)
print(f"Dataframe bruto: \n{df}")

print(f"Coluna nome: \n{df['Nome']}")

print("Apenas com idade maior que 30")
print(df[df['Idade']>30])

#adicionar mais uma coluna
df['Imposto']=df['Salario']*0.1
print(f"O imposto a pagar é: {df}")

df.to_csv('salarios.csv', index=False)

