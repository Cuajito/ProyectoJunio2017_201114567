class NodoLista:
	def __init__(self, dato):
		self.dato = dato
		self.siguiente = None
		self.anterior = None

class NodoArbol:
	def __init__(self, valor=None, parent=None, is_root=False, is_left=False, is_right=False):
		self.valor = valor
		self.right = None
		self.left = None
		self.parent = parent
		self.is_root = is_root
		self.is_left = is_left
		self.is_right = is_right

class NodoOrtogonal:
	def __init__(self, dato, posx, posy ):
		self.dato = dato
		self.anterior = None
		self.siguiente = None
		self.derecha = None
		self.izquierda = None
		self.adelante = None
		self.atras = None
		self.posx = posx
		self.posy = posy

class NodoCabecera:
	
	def __init__(self, posx):
		self.posx = posx
		columna=ListaVertical()
		self.derecha=None
		self.izquierda=None

class NodoLateral:

	def __init__(self, posy):
		self.posy = posy
		fila=ListaHorizontal()
		self.siguiente=None
		self.anterior=None	

class Cabeceras:

	def __init__(self):
		self.primero = None
		self.ultimo = None

	def vacia(self):
		return self.primero == None

	def insertar(self, posx):
		
		nodo = NodoCabecera(posx)

		if self.vacia():
			self.primero=self.ultimo=nodo
		else:
			if nodo.posx<self.primero.posx:
				self.agregar_inicio(nodo)
			elif nodo.posx>self.ultimo.posx:
				self.agregar_final(nodo)
			else:
				self.agregar_medio(nodo)

	def agregar_inicio(self, nodo):
		aux = nodo
		aux.derecha = self.primero
		self.primero.izquierda = aux
		self.primero = aux						

	def agregar_final(self, nodo):
		aux = self.ultimo
		self.ultimo = aux.derecha = nodo
		self.ultimo.izquierda = aux
		
	def agregar_medio(self, nodo):
		temporal1=self.primero
		while temporal1.posx<nodo.posx:
			temporal1=temporal1.derecha

		temporal2=temporal1.izquierda
		
		temporal2.derecha=nodo
		temporal1.izquierda=nodo
		nodo.derecha=temporal1
		nodo.izquierda=temporal2		
			
	def recorrer_inicio_fin(self):
		aux = self.primero
		while aux!=None :
			print str(aux.posx)
			aux = aux.derecha

class Laterales:
	def __init__(self):
		self.primero = None
		self.ultimo = None

	def vacia(self):
		return self.primero == None

	def insertar(self, posy):
		
		nodo = NodoLateral(posy)

		if self.vacia():
			self.primero=self.ultimo=nodo
		else:
			if nodo.posy<self.primero.posy:
				self.agregar_inicio(nodo)
			elif nodo.posy>self.ultimo.posy:
				self.agregar_final(nodo)
			else:
				self.agregar_medio(nodo)

	def agregar_inicio(self, nodo):
		
		aux = nodo
		aux.siguiente = self.primero
		self.primero.anterior = aux
		self.primero = aux						

	def agregar_final(self, nodo):
		
		aux = self.ultimo
		self.ultimo = aux.siguiente = nodo
		self.ultimo.anterior = aux
		
	def agregar_medio(self, nodo):
		temporal1=self.primero
		while temporal1.posy<nodo.posy:
			temporal1=temporal1.siguiente

		temporal2=temporal1.anterior
		
		temporal2.siguiente=nodo
		temporal1.anterior=nodo
		nodo.siguiente=temporal1
		nodo.anterior=temporal2		
			
	def recorrer_inicio_fin(self):
		aux = self.primero
		while aux!=None :
			print str(aux.posy)
			aux = aux.siguiente					

class ListaVertical:
	def __init__(self):
		self.primero = None
		self.ultimo = None

	def vacia(self):
		return self.primero == None

	def insertar(self, dato, posx, posy):
		
		nodo = NodoOrtogonal(dato, posx, posy)

		if self.vacia():
			self.primero=self.ultimo=nodo
		else:
			if nodo.posy<self.primero.posy:
				self.agregar_inicio(nodo)
			elif nodo.posy>self.ultimo.posy:
				self.agregar_final(nodo)
			else:
				self.agregar_medio(nodo)

	def agregar_inicio(self, nodo):
		
		aux = nodo
		aux.siguiente = self.primero
		self.primero.anterior = aux
		self.primero = aux						

	def agregar_final(self, nodo):
		
		aux = self.ultimo
		self.ultimo = aux.siguiente = nodo
		self.ultimo.anterior = aux
		
	def agregar_medio(self, nodo):
		temporal1=self.primero
		while temporal1.posy<nodo.posy:
			temporal1=temporal1.siguiente

		temporal2=temporal1.anterior
		
		temporal2.siguiente=nodo
		temporal1.anterior=nodo
		nodo.siguiente=temporal1
		nodo.anterior=temporal2		
			
	def recorrer_inicio_fin(self):
		aux = self.primero
		while aux!=None :
			print str(aux.posy) + "---" + str(aux.dato)
			aux = aux.siguiente		
		
class ListaHorizontal:
	def __init__(self):
		self.primero = None
		self.ultimo = None

	def vacia(self):
		return self.primero == None

	def insertar(self, dato, posx, posy):
		
		nodo = NodoOrtogonal(dato, posx, posy)

		if self.vacia():
			self.primero=self.ultimo=nodo
		else:
			if nodo.posx<self.primero.posx:
				self.agregar_inicio(nodo)
			elif nodo.posx>self.ultimo.posx:
				self.agregar_final(nodo)
			else:
				self.agregar_medio(nodo)

	def agregar_inicio(self, nodo):
		aux = nodo
		aux.derecha = self.primero
		self.primero.izquierda = aux
		self.primero = aux						

	def agregar_final(self, nodo):
		aux = self.ultimo
		self.ultimo = aux.derecha = nodo
		self.ultimo.izquierda = aux
		
	def agregar_medio(self, nodo):
		temporal1=self.primero
		while temporal1.posx<nodo.posx:
			temporal1=temporal1.derecha

		temporal2=temporal1.izquierda
		
		temporal2.derecha=nodo
		temporal1.izquierda=nodo
		nodo.derecha=temporal1
		nodo.izquierda=temporal2		
			
	def recorrer_inicio_fin(self):
		aux = self.primero
		while aux!=None :
			print str(aux.posx) + "---" + str(aux.dato)
			aux = aux.derecha


class ListaDoblementeEnlazada:
	def __init__(self):
		self.primero = None
		self.ultimo = None
		self.size = 0

	def vacia(self):
		return self.primero == None

	def agregar_final(self, dato):
		if self.vacia():
			self.primero = self.ultimo = NodoLista(dato)
		else:
			aux = self.ultimo
			self.ultimo = aux.siguiente = NodoLista(dato)
			self.ultimo.anterior = aux
		self.size += 1

	def eliminar_final(self):
		if self.vacia():
			print ("esta vacia")
		elif self.primero.siguiente == None :
			self.primero = self.ultimo = None
			self.size = 0
		else:
			self.ultimo = self.ultimo.anterior
			self.ultimo.siguiente = None
			self.size -= 1
		
	def agregar_inicio(self, dato):
		if self.vacia():
			self.primero = self.ultimo = NodoLista(dato)
		else:
			aux = NodoLista(dato)
			aux.siguiente = self.primero
			self.primero.anterior = aux
			self.primero = aux
		self.size += 1

	def eliminar_inicio(self):
		if self.vacia():
			print ("esta vacia")
		elif self.primero.siguiente == None :
			self.primero = self.ultimo = None
			self.size = 0
		else:
			self.primero = self.primero.siguiente
			self.primero.anterior = None
			self.size -= 1

		
	def recorrer_inicio_fin(self):
		aux = self.primero
		while aux :
			print(aux.dato)
			aux = aux.siguiente

	def recorrer_fin_inicio(self):
		aux	= self.ultimo
		while aux :
			print (aux.dato)
			aux = aux.anterior	

class ArbolBinario:
	def __init__(self):
		self.root = None

	def empty(self):
		if self.root == None:
			return True
		else:
			return False

	def add(self, valor):
		if self.empty():
			self.root = NodoArbol(valor=valor, is_root=True)
		else:
			nodo = self.__get_place(valor)
			if valor <= nodo.value:
				nodo.left = NodoArbol(valor=valor, parent=nodo, is_left=True)
			else:
				nodo.right = NodoArbol(valor=valor, parent=nodo, is_right=True)

	def __get_place(self, valor):
		aux =self.root
		while aux:
			temp = aux
			if valor <= aux.valor:
				aux = aux.left
			else
			aux = aux.right
		return temp

	def show_in_order(self, nodo):#izq, raiz, der

		if nodo:
			self.show_in_order(nodo.left)
			print (nodo.valor)
			self.show_in_order(nodo.right)

	def show_post_order(self, nodo):#izq, der, raiz
		if nodo:
			print (nodo.valor)
			self.show_pre_order(nodo.left)
			self.show_pre_order(nodo.right)

	def show_pre_order(self, nodo):#raiz, izq, der
		if nodo:
			self.show_post_order(nodo.left)
			self.show_post_order(nodo.right)
			print (nodo.valor)

	def buscar(self, nodo, valor):
		if nodo == None:
			return None
		else:
			if nodo.valor == valor:
				return nodo
			elif valor <= nodo.valor:
				return self.buscar(nodo.left, valor)
			else:
				return self.buscar(nodo.right, valor)
