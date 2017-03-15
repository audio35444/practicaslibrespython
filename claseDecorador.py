
#Decorador a traves de una clase decoradora

class Decorator(object):
	"""Clase Decorator"""
	def __init__(self,funcion):
		self.funcion = funcion
	def __call__(self,*args,**kwargs): #es la funcion decoradora la que decora a resta
		print "La funcion es: ",self.funcion.__name__
		self.funcion(*args,**kwargs)


@Decorator
def resta(n,m):
	print n-m

resta(3,5)