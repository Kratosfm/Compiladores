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
fun_name = None
is_param = False
is_vector = False

symbol_table = {}
param_table = {}
param_cont = 0

class Entry():
    def __init__(self, id, tipo, value = None, space = None, isParam = False):
        self.id = id
        self.tipo = tipo
        self.value = value
        self.space = space
        self.isParam = isParam

class FunctionEntry:
    def __init__(self, id, tipo, cuadno = 0, paramno = 0):
        self.id = id
        self.tipo = tipo
        self.dict = {}
        self.cuadno = cuadno
        self.paramno = paramno

class Param:
    def __init__(self,id, num = 0):
        self.id = id
        self.dict = []
        self.num = num

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
        if (symbol_table[func_id].dict.get(id)):
            dir = symbol_table[func_id].dict[id].value
            if(validar(symbol_table[func_id].dict[id].tipo, value)):
                if (symbol_table[func_id].dict[id].tipo == "int"):
                    Memoria.global_memroy.ints[dir] = value
                elif (symbol_table[func_id].dict[id].tipo == "float"):
                    Memoria.global_memroy.floats[dir] = value
                elif (symbol_table[func_id].dict[id].tipo == "bool"):
                    Memoria.global_memroy.bools[dir] = value
                elif (symbol_table[func_id].dict[id].tipo == "string"):
                    Memoria.global_memroy.strings[dir] = value
                else:
                    symbol_table[func_id].dict[id].value = value
            else:
                dir = symbol_table["global"].dict[id].value
                if(validar(symbol_table["global"].dict[id].tipo, value)):
                    if (symbol_table["global"].dict[id].tipo == "int"):
                        Memoria.global_memroy.ints[dir] = value
                    elif (symbol_table["global"].dict[id].tipo == "float"):
                        Memoria.global_memroy.floats[dir] = value
                    elif (symbol_table["global"].dict[id].tipo == "bool"):
                        Memoria.global_memroy.bools[dir] = value
                    elif (symbol_table["global"].dict[id].tipo == "string"):
                        Memoria.global_memroy.strings[dir] = value
                    else:
                        symbol_table["global"].dict[id].value = value
    elif(is_main):
        if (symbol_table[func_id].dict.get(id)):
            dir = symbol_table[func_id].dict[id].value
            if(validar(symbol_table[func_id].dict[id].tipo, value)):
                if (symbol_table[func_id].dict[id].tipo == "int"):
                    Memoria.global_memroy.ints[dir] = value
                elif (symbol_table[func_id].dict[id].tipo == "float"):
                    Memoria.global_memroy.floats[dir] = value
                elif (symbol_table[func_id].dict[id].tipo == "bool"):
                    Memoria.global_memroy.bools[dir] = value
                elif (symbol_table[func_id].dict[id].tipo == "string"):
                    Memoria.global_memroy.strings[dir] = value
                else:
                    symbol_table[func_id].dict[id].value = value
        else:
            dir = symbol_table["global"].dict[id].value
            if(validar(symbol_table["global"].dict[id].tipo, value)):
                if (symbol_table["global"].dict[id].tipo == "int"):
                    Memoria.global_memroy.ints[dir] = value
                elif (symbol_table["global"].dict[id].tipo == "float"):
                    Memoria.global_memroy.floats[dir] = value
                elif (symbol_table["global"].dict[id].tipo == "bool"):
                    Memoria.global_memroy.bools[dir] = value
                elif (symbol_table["global"].dict[id].tipo == "string"):
                    Memoria.global_memroy.strings[dir] = value
                else:
                    symbol_table["global"].dict[id].value = value
    else:
        print("muere")
        if(validar(symbol_table[func_id].tipo, value)):
            dir = symbol_table[id].value
            if (symbol_table[func_id].tipo == "int"):
                Memoria.global_memroy.ints[dir] = value
            else:
                #print("Valos ", dir, value)
                symbol_table[id].value = value

def getAttributes(id):
    if (symbol_table[func_id].dict.get(id)):
        dir = symbol_table[func_id].dict[id].value
        tipo = symbol_table[func_id].dict[id].tipo
        #return (symbol_table[func_id].dict[id].value)
        if(tipo == "int"):
            return (dir)
        elif(tipo == "float"):
            return dir
        elif(tipo == "bool"):
            return dir
        elif(tipo == "string"):
            return dir
    else:
        dir = symbol_table["global"].dict[id].value
        tipo = symbol_table["global"].dict[id].tipo
        if(tipo == "int"):
            return (dir)
        elif(tipo == "float"):
            return dir
        elif(tipo == "bool"):
            return dir
        elif(tipo == "string"):
            return dir
        else:
            return (symbol_table["global"].dict[id].value)

def getValue(id):
    if (symbol_table[func_id].dict.get(id)):
        dir = symbol_table[func_id].dict[id].value
        tipo = symbol_table[func_id].dict[id].tipo
        if(tipo == "int"):
            return Memoria.global_memroy.ints[dir]
        elif(tipo == "float"):
            return Memoria.global_memroy.floats[dir]
        elif(tipo == "string"):
            return Memoria.global_memroy.strings[dir]
        elif(tipo == "bool"):
            return Memoria.global_memroy.bools[dir]
        else:
            print("error")
    else:
        dir = symbol_table["global"].dict[id].value
        tipo = symbol_table["global"].dict[id].tipo
        if(tipo == "int"):
            return Memoria.global_memroy.ints[dir]
        elif(tipo == "float"):
            return Memoria.global_memroy.floats[dir]
        elif(tipo == "string"):
            return Memoria.global_memroy.strings[dir]
        elif(tipo == "bool"):
            return Memoria.global_memroy.bools[dir]
        else:
            print("error")
            #return (symbol_table["global"].dict[id].value)

def getType(id):
    return (symbol_table[id].tipo)

def getTypeVar(id):
    if (symbol_table[func_id].dict.get(id)):
        return (symbol_table[func_id].dict[id].tipo)
    else:
        return (symbol_table["global"].dict[id].tipo)
#Funcion para conseguir el tipo de variable y comprobarlo con el cubo semantico
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
#funcion para conseguir el tipo de variable y comprobarlo para modulos
def getTypeVar3(funcion,id):
    if (symbol_table[funcion].dict.get(id)):
        return (symbol_table[funcion].dict[id].tipo)
    else:
        return (symbol_table["global"].dict[id].tipo)

def show():
#    print(symbol_table["global"].dict, symbol_table["main"].dict)
    for i in symbol_table:
        if (str((type(symbol_table[i]))) == "<class 'varsTable.FunctionEntry'>"):
            print(i, getType(i), symbol_table[i].cuadno,symbol_table[i].paramno,"{")
            for j in symbol_table[i].dict:
                print(symbol_table[i].dict[j].id, symbol_table[i].dict[j].tipo, symbol_table[i].dict[j].value, symbol_table[i].dict[j].space, symbol_table[i].dict[j].isParam)
            print("}")
        else:
            print(symbol_table[i].id, symbol_table[i].tipo, symbol_table[i].value)

def insertVarInFunc(tipo, id, funt, espacio = None):
    if (symbol_table[funt].dict.get(id) or symbol_table["global"].dict.get(id)):
        print ("variable ya declarada")
        sys.exit()
    else:
        if (funt == "main" and is_vector == False):
            dir = Memoria.global_memroy.insert_main(id,tipo)
            symbol_table[funt].dict[id] = Entry(id, tipo, dir)
        elif (funt == "global" and is_vector == False):
            dir = Memoria.global_memroy.insert_global(None,tipo)
            symbol_table[funt].dict[id] = Entry(id, tipo, dir)
        elif (funt == "main" and is_vector == True):
            dir = Memoria.global_memroy.insert_main(id,tipo,espacio)
            symbol_table[funt].dict[id] = Entry(id, tipo, dir)
            symbol_table[funt].dict[id].space = espacio
        elif (funt == "global" and is_vector == True):
            dir = Memoria.global_memroy.insert_global(None,tipo,espacio)
            symbol_table[funt].dict[id] = Entry(id, tipo, dir)
            symbol_table[funt].dict[id].space = espacio
        else:
            if is_vector == False:
                dir = Memoria.global_memroy.insert_local(id,tipo)
                symbol_table[funt].dict[id] = Entry(id, tipo, dir)
            else:
                dir = Memoria.global_memroy.insert_local(id,tipo)
                symbol_table[funt].dict[id] = Entry(id, tipo, dir)
                symbol_table[funt].dict[id].space = espacio

def CheckExistIdFunc(id):
    if (symbol_table.get(id)):
        return True
    else:
        return False

def existeID(funt,id):
    tipo = symbol_table[funt].dict[id].tipo
    if ((tipo == getTypeVar3(funt,id))):
        print("correct")
    else:
        print("mal")

def ImprimirLcalTable(funt):
    for i in symbol_table[funt].dict:
        print(symbol_table[funt].dict[i].id, symbol_table[funt].dict[i].tipo, symbol_table[funt].dict[i].value)

def InsertParam(funt):
    param_table[funt] = Param(funt)

def InsertTypParam(tipo):
    param_table[func_id].dict.append(tipo)
    param_table[func_id].num = param_table[func_id].num + 1

def ImprimirParamsType():
    for element in param_table[func_id].dict:
        print ("hey ",element)
