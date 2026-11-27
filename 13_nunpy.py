import numpy as np

#vamos criar uma array (vetor)

arr=np.array([1,2,3,4,5])

print(f"Array: {arr}")

#vamos multiplicar nossa array
print(arr*2)

#vamos somar duas array
arr2=np.array([10,20,30,40,50])
print(arr+arr2)

#vamos criar uma matriz 2d (matriz 2x3)
matriz=np.array([[1,2,3] , [4,5,6]])
print(matriz)

#transposta da matriz
print(matriz.T)

#gerando uma matriz com valores aleatorios
print(np.random.rand(3,3))

