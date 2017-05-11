# -*- coding: utf-8 -*-
# Ejercicio 1: Tipo de numero.
import math
import numpy

# Funcion original
def listNumeberChecker(list): 
	try : 
		for item in numList :
			print "El numero seleccionado,",item,":"
			total = 0
			i=1
			while i < item :
				if((item % i) == 0) :
					total += i
				i+=1
			if(total == item) : 
				print("\tes un numero Perfecto")
			elif(total > item) :
				print("\tes un numero Abundante")
			elif(total < item) : 
				print("\tes un numero Defectivo")
			else :
				print("Error")
	except Exception as e:
		print"ERROR en lista: ",e

# Funcion definida de obtención de primos
def getPrimes(n_item):
    """ Input n_item>=6, Returns a array of primes, 2 <= p < n_item """
    sieve = numpy.ones(n_item/3 + (n_item%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n_item**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

# Funciones obtenidas en Stackoverflow
def getFactors(n_item, primes):
    factors = []
    for p in primes:
        if p*p > n_item: break
        i = 0
        while n_item % p == 0:
            n_item //= p
            i+=1
        if i > 0:
            factors.append((p, i));
    if n_item > 1: factors.append((n_item, 1))
    return factors

def getDivisors(factors):
    div = [1]
    for (p, r) in factors:
        div = [d * p**e for d in div for e in range(r + 1)]
    return div

# Funcion principal con algoritmos
def listNumeberCheckerFaster4(list): 
	try : 
		for item in numList :
			print "El numero seleccionado,",item,":"
			total = 0
			primes = []
			factors = []
			divisors = []

			primes = getPrimes(item)
			factors = getFactors(item, primes)
			divisors = getDivisors(factors)

			total = sum(divisors) - item
			if(total == item) : 
				print("\tes un numero Perfecto")
			elif(total > item) :
				print("\tes un numero Abundante")
			elif(total < item) : 
				print("\tes un numero Defectivo")
			else :
				print("Error")
	except Exception as e:
		print"ERROR en lista: ",e

# Método poco eficiente: revisar factorización por números primos

# UnitTesting
print("\n---TEST 0---")
numList = [6, 12, 16] # Perfecto, Abundante y Defectivo
listNumeberCheckerFaster4(numList)

print("\n---TEST 1---")
numList = [10000] # Cinco cifras
listNumeberCheckerFaster4(numList)

print("\n---TEST 2---")
numList = [10000000] # Ocho cifras
listNumeberCheckerFaster4(numList)

print("\n---TEST 3---")
numList = [100000000] # Nueve cifras
listNumeberCheckerFaster4(numList)

# Tiempos: 
# 			listNumeberChecker .........7.7s
#			listNumeberCheckerFaster....31s
#			listNumeberCheckerFaster2...5.7s
#			listNumeberCheckerFaster3...5.2s Aprox
#			listNumeberCheckerFaster4...0.8s Aprox			