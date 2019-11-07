import sys

vart = None

class Entry:
    def __init__(self, id, tipo, value = None):
        self.id = id
        self.tipo = tipo
        self.value = value

class FunctionEntry:
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo
    dict = {}

symbol_table = {}

def validar(tipo, valor):
    if str(type(valor)) == "<class 'float'>" and tipo == 'float':
        return True
    if str(type(valor)) == "<class 'int'>" and tipo == 'int':
        #print("valido")
        return True
    if str(type(valor)) == "<class 'str'>" and tipo == 'string':
        return True
    if str(type(valor)) == "<class 'bool'>" and tipo == 'bool':
        return True
    else:
        return False

def delete(id):
    del symbol_table[id]

def look(id):
    if symbol_table.get(id):
      return (symbol_table[id].id, symbol_table[id].tipo, symbol_table[id].value)
    else:
      return None

def insert(tipo, id):
    if symbol_table.get(id):
        pass
    else:
        symbol_table[id] = Entry(id, tipo)

def update(id, value):
  if(validar(symbol_table[id].tipo, value)):
    symbol_table[id].value = value

def getAttributes(id):
    return (symbol_table[id].value)

def show():
    for i in symbol_table:
        print(symbol_table[i].id, symbol_table[i].tipo, symbol_table[i].value)

