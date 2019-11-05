import sys

func_id = None
func_tipo = None
var_id = None
var_tipo = None
var_space = None
is_local = False

symbol_table = {}

#Tamaño de memoria por tipo
MRY_SIZE = 150

# Demostracion grafica de memoria
# *************** GLOBALES
# global int      + mmry_size [0 - 149]
# ---------------
# global float    + mmry_size [150 - 299]
# ---------------
# global bool     + mmry_size [300 - 449]
# ---------------
# global string   + mmry_size [450 - 599]

# *************** LOCALES
# local int       + mmry_size [600 - 749]
# ---------------
# local float     + mmry_size [750 - 899]
# ---------------
# local bool      + mmry_size [900 - 1049]
# ---------------
# local string    + mmry_size [1050 - 1199]

# *************** TEMPORALES
# temporal int    + mmry_size
# ---------------
# temp float      + mmry_size
# ---------------
# temp bool       + mmry_size
# ---------------
# temp string     + mmry_size
# ---------------

#Declaracion de estapcios de memoria
index_globalInt = MRY_SIZE
index_globalFloat = index_globalInt + MRY_SIZE
index_globalBool = index_globalFloat + MRY_SIZE
index_globalString = index_globalBool + MRY_SIZE
index_localInt = index_globalString + MRY_SIZE
index_localFloat = index_localInt + MRY_SIZE
index_localBool = index_localFloat + MRY_SIZE
index_localString = index_localBool + MRY_SIZE
index_tempInt = index_localString + MRY_SIZE
index_tempFloat = index_tempInt + MRY_SIZE
index_tempBool = index_tempFloat + MRY_SIZE
index_tempString = index_tempBool + MRY_SIZE

#contadores para asignar direccion de memoria
count_global={
    'int' : 0,
    'float' : MRY_SIZE * 1,
    'bool' : MRY_SIZE * 2,
    'string' : MRY_SIZE * 3
}

count_locales={
    'int' : MRY_SIZE * 4,
    'float' : MRY_SIZE * 5,
    'bool' : MRY_SIZE * 6,
    'string' : MRY_SIZE * 7
}

class Entry:
    def __init__(self, id, tipo, dir, value = None, space = None):
        self.id = id
        self.tipo = tipo
        self.dir = dir
        self.value = value
        self.space = space #if is a vector

class FunctionEntry:
    def __init__(self, id, tipo, dir, value = None):
        self.id = id
        self.tipo = tipo
        self.value = value
        self.dir = dir
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

def addAddress(local, tipo):
    if(local):
        count_locales[tipo] = count_locales[tipo]+1
        return count_locales[tipo]-1
    else:
        count_global[tipo] = count_global[tipo] + 1
        return count_global[tipo]-1

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
            symbol_table[id] = FunctionEntry(id, tipo, addAddress(False, tipo))
    else:
        if symbol_table.get(id):
            return false
        else:
            symbol_table[id] = Entry(id, tipo, addAddress(False, tipo))

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
                print(symbol_table[i].dict[j].id, symbol_table[i].dict[j].tipo, symbol_table[i].dict[j].dir)
            print("}")
        else:
            print(symbol_table[i].id, symbol_table[i].tipo, symbol_table[i].dir)

def insertVarInFunc(tipo, id):
    if symbol_table[func_id].dict.get(id):
        return false
    else:
        symbol_table[func_id].dict[id] = Entry(id, tipo, addAddress(True, tipo))
