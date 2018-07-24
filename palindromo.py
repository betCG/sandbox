#!/usr/bin/python
import sys

def palindromo(numero):
	temp = numero
	invertido = 0

	while(numero > 0):
		digito = numero%10
		invertido = invertido*10+digito
		numero = numero/10
	if(temp == invertido):
		print "palindromo"
	else:
		print "No palindromo"


def main():
	numero = input("Ingrese un numero ")
	palindromo(numero)
main()

