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
exist_GLOBAL = False

symbol_table = {}
param_table = {}
param_cont = 0
arrparam = []

class Entry():
    def __init__(self, id, tipo, value = None, space = None, isParam = False, isvector = False):
        self.id = id
        self.tipo = tipo
        self.value = value
        self.space = space
        self.isParam = isParam
        self.dirs = []
        self.isVector = isvector
#Cambiar returno por una pila para almacenar en recursividad
class FunctionEntry:
    def __init__( self, id, tipo, cuadno = 0, paramno = 0, returno = 0, isReturn = False ):
        self.id = id
        self.tipo = tipo
        self.dict = {}
        self.cuadno = cuadno
        self.paramno = paramno
        self.returno = returno
        self.isReturn = isReturn

class Param:
    def __init__(self,id, num = 0):
        self.id = id
        self.dict = []
        self.num = num

#Valida que el tipo del valor sea el correcto
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

#Borra id / No se usa
def delete(id):
    del symbol_table[id]

#Funcion que permite enviar el valor de un id / No se usa
def look(id):
    if symbol_table.get(id):
      return (symbol_table[id].id, symbol_table[id].tipo, symbol_table[id].value)
    else:
      return None

#Funcion que agrega una funcion global, main o local a la symbol_table
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

#Funcion que recibe un id y valor y actualiza el valor de ese id en la funcion actual
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
        if(validar(symbol_table[func_id].tipo, value)):
            dir = symbol_table[id].value
            if (symbol_table[func_id].tipo == "int"):
                Memoria.global_memroy.ints[dir] = value
            else:
                #print("Valos ", dir, value)
                symbol_table[id].value = value

#Funcion que consigue la direccion
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

#Funcion que consigue el valor
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

#funcion que regresa el tipo de funcion
def getType(id):
    return (symbol_table[id].tipo)

#funcion que regrea el tipo de variable
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
        return "string"
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

#Funcion que imprime la vars table
def show():
#    print(symbol_table["global"].dict, symbol_table["main"].dict)
    for i in symbol_table:
        if (str((type(symbol_table[i]))) == "<class 'varsTable.FunctionEntry'>"):
            print(i, getType(i), symbol_table[i].cuadno,symbol_table[i].paramno,symbol_table[i].returno,"{")
            for j in symbol_table[i].dict:
                print(symbol_table[i].dict[j].id, symbol_table[i].dict[j].tipo, symbol_table[i].dict[j].value, symbol_table[i].dict[j].space, symbol_table[i].dict[j].isParam,symbol_table[i].dict[j].dirs)
            print("}")
        else:
            print(symbol_table[i].id, symbol_table[i].tipo, symbol_table[i].value)

#Funcion que añade a dir de un FunctionEntry un Entry
def insertVarInFunc(tipo, id, funt, espacio = None):
    if(exist_GLOBAL == True):
        if (symbol_table[funt].dict.get(id) or symbol_table["global"].dict.get(id)):
            print ("variable ya declarada")
            sys.exit()
        else:
            if (funt == "main" and is_vector == False):
                dir = Memoria.global_memroy.insert_main(id,tipo)
                symbol_table[funt].dict[id] = Entry(id, tipo, dir)
            elif (funt == "global" and is_vector == False):
                dir = Memoria.global_memroy.insert_global(0,tipo)
                symbol_table[funt].dict[id] = Entry(id, tipo, dir)
            elif (funt == "main" and is_vector == True):
                dir = Memoria.global_memroy.insert_main(id,tipo,espacio)
                symbol_table[funt].dict[id] = Entry(id, tipo, dir)
                symbol_table[funt].dict[id].space = espacio
                Llenado(id,tipo,dir+1,espacio,funt)
                #symbol_table[funt].dict[id].dirs.clear()
            elif (funt == "global" and is_vector == True):
                dir = Memoria.global_memroy.insert_global(0,tipo,espacio)
                symbol_table[funt].dict[id] = Entry(id, tipo, dir)
                symbol_table[funt].dict[id].space = espacio
                Llenado(id,tipo,dir,espacio,funt)
            else:
                if is_vector == False:
                    dir = Memoria.global_memroy.insert_local(0,tipo)
                    symbol_table[funt].dict[id] = Entry(id, tipo, dir)
                else:
                    dir = Memoria.global_memroy.insert_local(id,tipo)
                    symbol_table[funt].dict[id] = Entry(id, tipo, dir)
                    symbol_table[funt].dict[id].space = espacio
                    Llenado(id,tipo,dir+1,espacio,funt)
    else:
        if (symbol_table[funt].dict.get(id)):
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
                Llenado(id,tipo,dir,espacio,funt)
                #symbol_table[funt].dict[id].dirs.clear()
            elif (funt == "global" and is_vector == True):
                dir = Memoria.global_memroy.insert_global(None,tipo,espacio)
                symbol_table[funt].dict[id] = Entry(id, tipo, dir)
                symbol_table[funt].dict[id].space = espacio
                Llenado(id,tipo,dir,espacio,funt)
            else:
                if is_vector == False:
                    dir = Memoria.global_memroy.insert_local(0,tipo)
                    symbol_table[funt].dict[id] = Entry(id, tipo, dir)
                else:
                    dir = Memoria.global_memroy.insert_local(id,tipo)
                    symbol_table[funt].dict[id] = Entry(id, tipo, dir)
                    symbol_table[funt].dict[id].space = espacio
                    Llenado(id,tipo,dir,espacio,funt)

#checa si una funcion ya existe con ese id
def CheckExistIdFunc(id):
    if (symbol_table.get(id)):
        return True
    else:
        return False

#Checa si el id existe en una variable dentro de la funcion (funt)
def existeID(funt,id):
    tipo = symbol_table[funt].dict[id].tipo
    if ((tipo == getTypeVar3(funt,id))):
        print("correct")
    else:
        print("mal")
#Imprime la funcion donde es llamada
def ImprimirLcalTable(funt):
    for i in symbol_table[funt].dict:
        print(symbol_table[funt].dict[i].id, symbol_table[funt].dict[i].tipo, symbol_table[funt].dict[i].value)

#Inserta un parametro
def InsertParam(funt):
    param_table[funt] = Param(funt)

#Inserta el tipo de parametro
def InsertTypParam(tipo):
    param_table[func_id].dict.append(tipo)
    param_table[func_id].num = param_table[func_id].num + 1

#Actualiza el valor de un parametro al momento de llamarlo
def UpdateParam():
    #for i in symbol_table[func_id]
    if(symbol_table[fun_name].paramno > 0):
        cont = 1
        tam = len(arrparam)
        for i in symbol_table[fun_name].dict:
            if(symbol_table[fun_name].dict[i].isParam == True):
                    dirval = symbol_table[fun_name].dict[i].value
                    valor = Memoria.getValor(arrparam[tam-cont])
                    Memoria.updateVal(dirval,valor)
                    #print("yoe",fun_name,symbol_table[fun_name].dict[i].id,dirval,valor)
                    cont = cont + 1
    else:
        print("LE")

#Llena las direcciones de un vector e inserta el numero correcto de direcciones
def Llenado(id,tipo,dir,espacio,funt):
    i = 1
    dir2 = 0
    dir = dir + 1
    while ( i <= espacio ):
        if ( funt == "global"):
            if ( i == 0):
                dir2 = dir
                Memoria.updateVal(dir,0)
            else:
                dir2 = Memoria.global_memroy.insert_global(0,tipo)
        elif ( funt == "main"):
            if ( i == 0):
                dir2 = dir
                Memoria.updateVal(dir,0)
            else:
                dir2 = Memoria.global_memroy.insert_main(0,tipo)
        else:
            if ( i == 0):
                dir2 = dir
                Memoria.updateVal(dir,0)
            else:
                dir2 = Memoria.global_memroy.insert_local(0,tipo)
        symbol_table[funt].dict[id].dirs.append(dir2)
        #print("LLENADO",id,symbol_table[funt].dict[id].dirs)
        i = i + 1
