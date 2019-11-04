import sys

func_id = None
func_tipo = None
var_id = None
var_tipo = None
var_space = None
is_local = False

symbol_table = {}

class Entry():
    def __init__(self, id, tipo, value = None, space = None):
        self.id = id
        self.tipo = tipo
        self.value = value
        self.space = space

class FunctionEntry:
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo
    dict = {}

def validar(tipo, valor):
    if str(type(valor)) == "<class 'float'>" and tipo == 'float':
        return True
    if str(type(valor)) == "<class 'int'>" and tipo == 'int':
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
    if(is_local):
        if symbol_table.get(id):
            return false
        else:
            symbol_table[id] = FunctionEntry(id, tipo)
    else:
        if symbol_table.get(id):
            return false
        else:
            symbol_table[id] = Entry(id, tipo)

def update(id, value):
    if(is_local):
        if(validar(symbol_table[func_id].dict[id].tipo, value)):
            symbol_table[func_id].dict[id].value = value
    else:
        if(validar(symbol_table[id].tipo, value)):
            symbol_table[id].value = value

def getAttributes(id):
    return (symbol_table[id].value)

def show():
    for i in symbol_table:
        if (str((type(symbol_table[i]))) == "<class 'varsTable.FunctionEntry'>"):
            print(i, "{")
            for j in symbol_table[i].dict:
                print(symbol_table[i].dict[j].id, symbol_table[i].dict[j].tipo, symbol_table[i].dict[j].value)
            print("}")
        else:
            print(symbol_table[i].id, symbol_table[i].tipo, symbol_table[i].value)

def insertVarInFunc(tipo, id):
    if symbol_table[func_id].dict.get(id):
        return false
    else:
        symbol_table[func_id].dict[id] = Entry(id, tipo)
