import os
import numpy as np
from euclides_extendido import inverso_multiplicativo



class MatrizLlave:

	matriz = [[]]
	matrizAdj = [[]]
	matrizInversa = [[]]
	det = 0
	inverso = 0
	n = 0
	m = 0									#	Cardinalidad

	def __init__(self, matriz, m):


		self.matriz = matriz
		self.n = len(self.matriz)

		self.m = m

		self.matrizAdj = [[0 for col in range(self.n)] for row in range(self.n)]
		self.matrizInversa = [[0 for col in range(self.n)] for row in range(self.n)]

		self.det = self.determinante(self.matriz, self.n) % self.m
		if(self.det == 0):
			raise ValueError('El determinante de la matriz es 0, por lo que no se puede calcular su inversa')

		inverso = inverso_multiplicativo(self.det, self.m)
		if(not inverso[0]):
			raise ValueError('La matriz no tiene inverso multiplicativo')

		self.inverso = inverso[1]

		

	def calcularCofactor(self, matriz, temp, p, q, n):
	
		i = 0
		j = 0
		
		for row in range(n):
					
			for col in range(n):
		
				# Matriz temporal con elementos que no estan el la fila ni columna actual
				if (row != p and col != q):
		
					temp[i][j] = matriz[row][col]
					j += 1
		
					# Fila llena, incrementar su indice y resetear indice de columna 
					if (j == n - 1):
						j = 0
						i += 1

	
	def determinante(self, matriz, n):
	
		det = 0
	
		# Caso base : matriz con solo un elemento
		if (n == 1):
			return matriz[0][0]
	
		temp = []   # Lista de cofactores
		for i in range(n):
			temp.append([None for _ in range(n)])
	
		signo = 1   # Signo multiplicador
	
		for i in range(n):
	
			# Calcular cofactor de matriz[0][i]
			self.calcularCofactor(matriz, temp, 0, i, n)
			det += signo * matriz[0][i] * self.determinante(temp, n - 1)
	
			# cambiar de signo
			signo = -signo
	
		return det
	

	def adjunta(self, matriz, adj):
		if (self.n == 1):
			adj[0][0] = 1
			return
	
		signo = 1
		temp = []   # Guardar cofactores de matriz[][]
		for i in range(self.n):
			temp.append([None for _ in range(self.n)])
	
		for i in range(self.n):
			for j in range(self.n):
				# Calcular cofactor de matriz[i][j]
				self.calcularCofactor(matriz, temp, i, j, self.n)
	
				# El signo de adj[j][i] es positivo si la suma de los indices de la fila y la columna es par.
				signo = [1, -1][(i + j) % 2]
	
				# Intercalar filas y columnas para obtener la transpuesta de la matriz cofactor
				adj[j][i] = (signo * self.determinante(temp, self.n-1)) % self.m
	
	
	def inversa(self):
		
		self.adjunta(self.matriz, self.matrizAdj)

		# Multiplicar matriz de adyacencia por inverso multiplicativo mod m y hacer mod m
		for i in range(self.n):
			for j in range(self.n):
				self.matrizInversa[i][j] = (self.matrizAdj[i][j] * self.inverso) % self.m