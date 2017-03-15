#################################################################################################
#########################Metodo Plantilla con funciones de orden superior########################
"""
def metodoPlantilla(f1,f2,f3):
	valorSuma=f1()
	valorResta=f2()
	valorMultiplicacion=f3()

	return "Funcion1: %s | Funcion2: %s | Funcion3: %s"%(valorSuma,valorResta,valorMultiplicacion)

def suma():
	return 2+3

def resta():
	return 2-3

def multiplicacion():
	return 2*3

print metodoPlantilla(suma,resta,multiplicacion)

"""
#################################################################################################
###############################funcion de   acuerdo a un parametro###############################

#que me devuelva la funcion que yo quiero de acuerdo a un parametro
"""
def seleccion(opcion):
	def suma(n,m):
		return n+m
	def multiplicacion(n,m):
		return n*m
	if opcion == "sum":
		return suma
	elif opcion == "multi":
		return multiplicacion

valor = raw_input("Selecciona:\n1- sum\n2-multi\n>")
funcionGuardada = seleccion(valor)

print funcionGuardada(2,3)
"""
#################################################################################################
##################################Funcion de Orden Superior MAP##################################
"""
def operador(n,m):
	if n == None:
		n=0
	if m == None:
		m=0
	return n+m

lst1=[1,2,3,4]
lst2= (4,5,3)

lstResult = map(operador,lst1,lst2)

print lstResult


"""
#################################################################################################
#################################Funcion de Orden Superior FILTER#################################
"""
def filtro(element):
	return (element >0)

lst = [1,-2,4,-2,4,-5,10]

lstResult = filter(filtro,lst)

print lstResult
"""
#################################################################################################
#################################Funcion de Orden Superior REDUCE#################################
"""
lstString = ('H','o','l','a',' ','M','u','n','d','o')#no necesitan ser pares

def concatenar(a,b):
	return a+b

stringResult = reduce(concatenar,lstString)
print type(stringResult)
print stringResult
"""
#################################################################################################
################################Funcion de Orden Superior LAMBDA#################################
#una sola linea, para reemplazar funciones de 1 linea
"""
lst1=[1,-2,1,-4]
lst2=[5,3,6,7]
lstString ='Hoola Mundo'
sumaLambda = lambda n,m:n+m
filtro = lambda n:n=='o'
print map(lambda n,m:n+m ,lst1,lst2)
print filter(filtro,lstString)
print reduce(sumaLambda,lst2)

print sumaLambda(1,67)
"""
#################################################################################################
#####################################Comprension de Listas#######################################
#reemplaza map y filter

lst1 = [1,2,3,-1,4]
#lstString = ['H','o','l','a']
lstString ='Hola'
"""
#lstResult=[item for item in lst1 if item >0]

lstResult=[caracter*num for caracter in lstString
							for num in lst1
								if num>0]
print lst1
print lstResult
"""
##########################################Generador############################################
#ejecutar hasta el next, demora el for hasta que sea necesario recorrer la lista, y lo ejecuta de a pasos
"""
lstResult=(caracter*num for caracter in lstString
							for num in lst1
								if num>0)


print lst1
print lstResult.next()

for item in lstResult:
	print item
"""
#simular esa pausa con comando YIELD
"""
def factorial(n):
	i=1
	while n>1:
		i=n*i
		yield i
		n-=1

for elemento in factorial(5):
	print elemento


lstGenerador = [elemento for elemento in factorial(5)]

print lstGenerador

"""
#################################################################################################
#######################################Funcion Decorator#########################################

def decorator(funcion):
	def funcionDecorada(*args,**kwargs):#(NroAtributos,Diccionario)
		print "Funcion ejecutada",funcion.__name__
		funcion(*args,**kwargs)

	return funcionDecorada
"""
def resta(n,m):
	print n-m


def suma(n,m):
	print n+m
#Decorado

decoradaResta=decorator(resta)

decoradaResta(5,2)

#decorada sin parametros
decoradaConPar = decoradaResta(6,9)

#decorada con parametros
decoradaConPar

print "----------------------"

#otra decorada con otra funcion
decorator(suma)(4,8)


#otra forma de decorar

@decorator
def multiplicacion(n,m):  #seria como hacer decorador(multiplicacion)(5,7)
	print n*m

multiplicacion(5,7)

"""

#######################################Simulando Validacion Django#########################################

loggeado = False
usuario = "Emmanuel"

def admin(f):
	def isLogged(*args,**kwargs):
		if loggeado:
			f.__name__
			f(*args,**kwargs)
		else:
			print f.__name__
			print "usted no esta logueado"
	return isLogged


#usamos doble de corador va primero por admin luego por decorator y finalmente restar
@admin
@decorator
def restar(n,m):
	print n+m

restar(4,1)

loggeado=True

restar(4,1)