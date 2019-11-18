import sys
import execMemory as Memoria

func_id = None
func_tipo = None
var_id = None
var_tipo = None
var_space = None
is_local = False
is_main = False
is_global = False

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
        self.dict = {}

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
            print ("variable ya declarada")
            sys.exit()
        else:
            symbol_table[id] = FunctionEntry(id, tipo)
    elif(is_main):
        if symbol_table.get(id):
            print ("variable ya declarada")
            sys.exit()
        else:
            symbol_table[id] = FunctionEntry("main",tipo)
    elif(is_global):
        if symbol_table.get(id):
            print ("variable ya declarada")
            sys.exit()
        else:
            symbol_table[id] = FunctionEntry("global",tipo)


def update(id, value):
    if(is_local):
        if(validar(symbol_table[func_id].dict[id].tipo, value)):
            if (symbol_table[func_id].dict.get(id)):
                symbol_table[func_id].dict[id].value = value
            else:
                symbol_table["global"].dict[id].value = value
    elif(is_main):
        if (symbol_table[func_id].dict.get(id)):
            if(validar(symbol_table[func_id].dict[id].tipo, value)):
                symbol_table[func_id].dict[id].value = value
        else:
            if(validar(symbol_table["global"].dict[id].tipo, value)):
                symbol_table["global"].dict[id].value = value
    else:
        if(validar(symbol_table[func_id].tipo, value)):
            symbol_table[id].value = value

def getAttributes(id):
    if (symbol_table[func_id].dict.get(id)):
        return (symbol_table[func_id].dict[id].value)
    else:
        return (symbol_table["global"].dict[id].value)

def getType(id):
    return (symbol_table[id].tipo)

def getTypeVar(id):
    if (symbol_table[func_id].dict.get(id)):
        return (symbol_table[func_id].dict[id].tipo)
    else:
        return (symbol_table["global"].dict[id].tipo)

def getTypeVar2(tipo):
    if tipo == "<class 'float'>" :
        return "float"
    if tipo == "<class 'int'>" :
        return "int"
    if tipo == "<class 'str'>" :
        return "str"
    if tipo == "<class 'bool'>" :
        return "bool"
    else:
        return False

def show():
#    print(symbol_table["global"].dict, symbol_table["main"].dict)
    for i in symbol_table:
        if (str((type(symbol_table[i]))) == "<class 'varsTable.FunctionEntry'>"):
            print(i, getType(i) ,"{")
            for j in symbol_table[i].dict:
                print(symbol_table[i].dict[j].id, symbol_table[i].dict[j].tipo, symbol_table[i].dict[j].value)
            print("}")
        else:
            print(symbol_table[i].id, symbol_table[i].tipo, symbol_table[i].value)

def insertVarInFunc(tipo, id, funt):
    if (symbol_table[funt].dict.get(id) or symbol_table["global"].dict.get(id)):
        print ("variable ya declarada")
        sys.exit()
    else:
        if (funt == "main"):
            dir = Memoria.global_memroy.insert_main(id,tipo)
            symbol_table[funt].dict[id] = Entry(id, tipo, dir)
        elif (funt == "global"):
            dir = Memoria.global_memroy.insert_global(id,tipo)
            symbol_table[funt].dict[id] = Entry(id, tipo, dir)
        else:
            dir = Memoria.global_memroy.insert_local(id,tipo)
            symbol_table[funt].dict[id] = Entry(id, tipo, dir)
