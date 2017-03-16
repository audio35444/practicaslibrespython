class UnoError(Exception):
	def __init__(self,valor):
		self.valorError=valor
	def __str__(self):
		return ("No puede dividir por 1 a "+str(self.valorError))

print "Hola mundo"
d=5
n=1
try:
	if n == 1:
		raise UnoError(5)
	print d/n
except (TypeError,NameError):
	print "error en tipo de dato" 
except ZeroDivisionError:
	print "no puede dividir por cero"
except UnoError as msg:
	print msg
else: #se ejecuta el else si no se ejecuto con error
	print "no hubo error"
finally:
	print "siempre se ejecuta","usar para cerrar conexiones por ejemplo"


numero = 11
calculo = 5.126545456
name= "Juan Emmanuel"
print "el Numero es: %d - calculo: %.3f\nrealizado por: %.6s"%(numero,calculo,name)