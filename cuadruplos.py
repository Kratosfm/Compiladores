import sys

import varsTable as varsTable
import semantic_Cube as semantic
import execMemory as Memory

pos_vect = 0
popper = []
pilaid = []
pilaTipos = []
pilaSaltos = []
ptemp = []
pilaVal = []
pilacuadruplos = []
contador = 0
vector_id = None

class Cuadrupl:
    def __init__(self, left, operator, right, resultado, num):
        self.left = left
        self.operator = operator
        self.right = right
        self.resultado = resultado
        self.num = num

#Funcion que imprime el arreglo de cuadruplos
def imprimirtodocuadr():
    for i in range(len(pilacuadruplos)):
        imprimircuadruplo(pilacuadruplos[i].num,pilacuadruplos[i].left,pilacuadruplos[i].operator,pilacuadruplos[i].right,pilacuadruplos[i].resultado)

#Funcion que imprime cuadruplos, ya no se usa
def imprimircuadruplo(num,left, operator, right, resultado):
    print (num,operator, left, right, resultado)

#Mete el id a la pila id y de igual forma su valor y tipo
def pushID(id):
    global contador
    pilaid.append(varsTable.getAttributes(id))
    pilaVal.append(varsTable.getValue(id))
    pilaTipos.append(varsTable.getTypeVar(id))
    contador = contador + 1
    #print (contador,str(pilaid)[1:-1])
    #print(contador,str(pilaVal)[1:-1])

# Funcion que obtiene elipo de un cte

# Funcion que verifica si el CTE ya se encuentra en la memoria
def verificarValorCte(cte,tipo):
    if tipo == "int":
        dir = 0
        for key1, val in Memory.global_memroy.ints.items():
            if val == cte:
                dir = key1
        if( dir >= 4000 and dir < 4100):
            return True
        else:
            return False
    elif tipo == "float":
        dir = 0
        for key1, val in Memory.global_memroy.floats.items():
            if val == cte:
                dir = key1
        if( dir >= 4100 and dir < 4200):
            return True
        else:
            return False
    elif tipo == "bool":
        dir = 0
        for key1, val in Memory.global_memroy.bools.items():
            if val == cte:
                dir = key1
        if( dir >= 4300 and dir < 4400):
            return True
        else:
            return False
    elif tipo == "string":
        dir = 0
        for key1, val in Memory.global_memroy.strings.items():
            if val == cte:
                dir = key1
        if( dir >= 4200 and dir < 4300):
            return True
        else:
            return False
    else:
        print("falla")

# Funcion que mete las constantes y su tipo a las pilas correspondientes, tambien el valor lo agrega a una pila
def pushCTE(var):
    global contador
    if (var == 'true' or var == 'false'):
        pilaTipos.append("bool")
        pilaVal.append(var)
        pilaid.append(var)
    else:
        if str(type(var)) == "<class 'float'>":
            if (verificarValorCte(var,"float")):
                dir = Memory.GetDir(var,"float")
                pilaVal.append(var)
                pilaid.append(dir)
                crearTipo(var)
            else:
                dir = Memory.global_memroy.insert_const(var,"float")
                pilaVal.append(var)
                pilaid.append(dir)
                crearTipo(var)
        elif str(type(var)) == "<class 'int'>":
            if (verificarValorCte(var,"int") == True):
                dir = Memory.GetDir(var,"int")
                pilaVal.append(var)
                pilaid.append(dir)
                crearTipo(var)
            else:
                dir = Memory.global_memroy.insert_const(var,"int")
                valor = Memory.global_memroy.ints.get(var)
                pilaVal.append(var)
                pilaid.append(dir)
                crearTipo(var)
        elif str(type(var)) == "<class 'bool'>":
            if (verificarValorCte(var,"bool")):
                dir = Memory.GetDir(var,"bool")
                pilaVal.append(var)
                pilaid.append(dir)
                crearTipo(var)
            else:
                dir = Memory.global_memroy.insert_const(var,"bool")
                valor = Memory.global_memroy.bools.get(var)
                pilaVal.append(var)
                pilaid.append(dir)
                crearTipo(var)
        elif str(type(var)) == "<class 'str'>":
            if (verificarValorCte(var,"string")):
                dir = Memory.GetDir(var,"string")
                pilaVal.append(var)
                pilaid.append(dir)
                crearTipo(var)
            else:
                dir = Memory.global_memroy.insert_const(var,"string")
                valor = Memory.global_memroy.strings.get(var)
                pilaVal.append(var)
                pilaid.append(dir)
                crearTipo(var)
        else:
            print("bye")
    #print (contador,str(pilaid)[1:-1])
    #print(contador,str(pilaVal)[1:-1])

#Funcion que crea el tipo de una variable a traves de lo que consigue y lo agrega a la pila
def crearTipo(var):
    tipo = str(type(var))
    tipo1 = varsTable.getTypeVar2(tipo)
    pilaTipos.append(tipo1)
    #print (str(pilaid)[1:-1])
    #print (str(pilaTipos)[1:-1])

#Funcion que usa el yacc para meter un operador
def pushPoper(oper):
    popper.append(oper)

#Cuadruplo de "=" que envia un valor de regreso
def resolverasignacion():
    global contador
    tam = len(popper)
    if tam > 0:
        if popper[tam-1] == '=':
            valor = pilaVal.pop()
            #Sacar temporal final de resultado id
            id2 = pilaid.pop()
            av = pilaVal.pop()
            tipo_res = pilaTipos.pop()
            tipo_id = pilaTipos.pop()
            valid = pilaid.pop()
            operator = popper.pop()
            if tipo_id == "float" and tipo_res == "int":
                valor = float(valor)
                #dir = Memory.GetDir(valor,"float")
            elif tipo_id == "int" and tipo_res == "float":
                print("error de semantica 1")
                sys.exit()
            #if(valid >= 7000) :
            #    cuad = Cuadrupl(valid, operator, None, id2, len(pilacuadruplos))
            #    pilacuadruplos.append(cuad)
            #    return av
            else:
                #print("dasdas",id2,valor,valid,av)
                cuad = Cuadrupl(id2, operator, None, valid, len(pilacuadruplos))
                pilacuadruplos.append(cuad)
                return valor
            #varsTable.update(valid,valor)
            #print(id, varsTable.getAttributes(id))

#Resuelve cuadruplos de suma y resta de dos id ademas de checar su semantica
def resolverterm():
    global contador
    tam = len(popper)
    if tam > 0:
        if popper[tam-1] == '+' or popper[tam-1] == '-':
            val_der = pilaVal.pop()
            id_der = pilaid.pop()
            tipo_der = pilaTipos.pop()
            val_izq = pilaVal.pop()
            id_izq = pilaid.pop()
            tipo_izq = pilaTipos.pop()
            operator = popper.pop()
            #print(operator)
            #print (tipo_der,tipo_izq,str(type(id_der)),str(type(id_izq)))
            tipo_resultado = semantic.getReturnType(tipo_der,tipo_izq,operator)
            if(tipo_resultado != "err"):
                if(operator == '+'):
                    resultado = val_izq + val_der
                    dir = Memory.global_memroy.insert_temporal(resultado,tipo_resultado)
                else:
                    resultado = val_izq - val_der
                    dir = Memory.global_memroy.insert_temporal(resultado,tipo_resultado)
                pilaVal.append(resultado)
                pilaid.append(dir)
                tip = crearTipo(resultado)
                #pilaTipos.append(tip)
                cuad = Cuadrupl(id_izq, operator, id_der, dir, len(pilacuadruplos))
                pilacuadruplos.append(cuad)
                #print("Antes")
                #print("OPE",popper)
                #print("VAL",pilaVal)
                #print("DIR",pilaid)
                #print("TIPO",pilaTipos)
            else:
                print("error de semantica 2")
                sys.exit()

#Resuelve cuadruplos de multiplicación y división de dos id ademas de checar su semantica
def resolverfact():
    global contador
    tam = len(popper)
    if tam > 0:
        if popper[tam-1] == '*' or popper[tam-1] == '/':
            val_der = pilaVal.pop()
            id_der = pilaid.pop()
            tipo_der = pilaTipos.pop()
            val_izq = pilaVal.pop()
            id_izq = pilaid.pop()
            tipo_izq = pilaTipos.pop()
            operator = popper.pop()
            tipo_resultado = semantic.getReturnType(tipo_der,tipo_izq,operator)
            if(tipo_resultado != "err"):
                if(operator == '*'):
                    resultado = val_izq * val_der
                    dir = Memory.global_memroy.insert_temporal(resultado,tipo_resultado)
                else:
                    resultado = val_izq / val_der
                    dir = Memory.global_memroy.insert_temporal(resultado,tipo_resultado)
                pilaVal.append(resultado)
                pilaid.append(dir)
                tip = crearTipo(resultado)
                cuad = Cuadrupl(id_izq, operator, id_der, dir, len(pilacuadruplos))
                pilacuadruplos.append(cuad)
                #imprimircuadruplo(val_izq, operator, val_der, resultado)
            else:
                print("error de semantica 3")
                sys.exit()

#Resuelve cuadruplos de relación de dos id ademas de checar su semantica y devolver un booleano
def resolverRel():
    global contador
    tam = len(popper)
    if tam > 0:
        if (popper[tam-1] == '<' or popper[tam-1] == '<=' or popper[tam-1] == '>' or popper[tam-1] == '>=' or popper[tam-1] == '==' or popper[tam-1] == '!='):
            val_der = pilaVal.pop()
            tipo_der = pilaTipos.pop()
            id_der = pilaid.pop()
            val_izq = pilaVal.pop()
            tipo_izq = pilaTipos.pop()
            id_izq = pilaid.pop()
            operator = popper.pop()
            #print (tipo_izq,tipo_der)
            tipo_resultado = semantic.getReturnType(tipo_der,tipo_izq,operator)
            #print("tip",tipo_resultado)
            if (tipo_resultado != "err"):
                if(operator == '<'):
                    resultado = val_izq < val_der
                    dir = Memory.global_memroy.insert_temporal(resultado,tipo_resultado)
                elif(operator == '<='):
                    resultado = val_izq <= val_der
                    dir = Memory.global_memroy.insert_temporal(resultado,tipo_resultado)
                elif(operator == '>'):
                    resultado = val_izq > val_der
                    dir = Memory.global_memroy.insert_temporal(resultado,tipo_resultado)
                elif(operator == '>='):
                    resultado = val_izq >= val_der
                    dir = Memory.global_memroy.insert_temporal(resultado,tipo_resultado)
                elif(operator == '=='):
                    resultado = val_izq == val_der
                    dir = Memory.global_memroy.insert_temporal(resultado,tipo_resultado)
                elif(operator == '!='):
                    resultado = val_izq != val_der
                    dir = Memory.global_memroy.insert_temporal(resultado,tipo_resultado)
                cuad = Cuadrupl(id_izq, operator, id_der, dir, len(pilacuadruplos))
                #imprimircuadruplo(val_izq, operator, val_der, resultado)
                pilacuadruplos.append(cuad)
                pilaid.append(dir)
                pilaVal.append(resultado)
                tip = crearTipo(resultado)
            else:
                print("error de semantica 4")
                sys.exit()

#Funcion que resuelve cuadruplos logicos
def ResolverLog():
    global contador
    tam = len(popper)
    if tam > 0:
        if (popper[tam-1] == "&&" or popper[tam-1] == "||"):
            val_der = pilaVal.pop()
            tipo_der = pilaTipos.pop()
            id_der = pilaid.pop()
            val_izq = pilaVal.pop()
            tipo_izq = pilaTipos.pop()
            id_izq = pilaid.pop()
            operator = popper.pop()
            tipo_resultado = semantic.getReturnType(tipo_der,tipo_izq,operator)
            if(tipo_resultado != 'error'):
                if (operator=="||"):
                    resultado = val_izq or val_der
                    dir = Memory.global_memroy.insert_temporal(resultado,tipo_resultado)
                else:
                    resultado = val_izq and val_der
                    dir = Memory.global_memroy.insert_temporal(resultado,tipo_resultado)
            cuad = Cuadrupl(id_izq, operator, id_der, dir, len(pilacuadruplos))
            pilacuadruplos.append(cuad)
            pilaid.append(dir)
            pilaVal.append(resultado)
            tip = crearTipo(resultado)

#Funcion que resuelve cuadruplos de condiciones
def ResolverCond():
    global contador
    tipo = pilaTipos.pop()
    if (tipo != "bool"):
        print("error de typme-mismatch")
        sys.exit()
    else:
        resultado = pilaVal.pop()
        id = pilaid.pop()
        cuad = Cuadrupl(id, "GotoF", None, resultado, len(pilacuadruplos))
        pilacuadruplos.append(cuad)
        pilaSaltos.append(len(pilacuadruplos)-1)

#Funcion que resuelve cuadruplos de condiciones else
def ResElse():
    global contador
    cuad = Cuadrupl(None, "Goto", None, None, len(pilacuadruplos))
    false = pilaSaltos.pop()
    pilaSaltos.append(len(pilacuadruplos))
    pilacuadruplos.append(cuad)
    fill(false, len(pilacuadruplos))

#Funcion que llena los distintos saltos que hay
def fill(cuadr, salto):
    pilacuadruplos[cuadr].resultado = salto

#Funcion que finaliza el if
def finalif():
    end = pilaSaltos.pop()
    fill(end, len(pilacuadruplos))

#Funcion que crea el inicio del ciclo
def while1():
    pilaSaltos.append(len(pilacuadruplos))

#Funcion que crea el cuadruplo GotoF
def while2():
    tipo = pilaTipos.pop()
    if (tipo != "bool"):
        print("error de type-mismatch")
        sys.exit()
    else:
        id = pilaid.pop()
        resultado = pilaVal.pop()
        cuad = Cuadrupl(id, "GotoF", None, resultado, len(pilacuadruplos)-1)
        pilacuadruplos.append(cuad)
        pilaSaltos.append(len(pilacuadruplos)-1)

#Funcion que crea Goto y manda a fill el GotoF
def while3():
    end = pilaSaltos.pop()
    regresa = pilaSaltos.pop()
    cuad = Cuadrupl(None, "Goto", None, regresa, len(pilacuadruplos))
    pilacuadruplos.append(cuad)
    fill(end,len(pilacuadruplos))

#Modulos
#Cuadruplo que genera return
def generateReturn():
    tam = len(popper)
    if tam > 0:
        if popper[tam-1] == "return":
            operator = popper.pop()
            resultado = pilaid.pop()
            valor = pilaVal.pop()
            tipo = pilaTipos.pop()
            val = Memory.getValor(resultado)
            dir = Memory.global_memroy.insert_returns(valor,tipo)
            #print("YES",valor,resultado,dir,val)
            cuad = Cuadrupl("None",operator,None,resultado,len(pilacuadruplos))
            pilacuadruplos.append(cuad)
            #esto puede fallar
            varsTable.symbol_table[varsTable.func_id].returno = dir
            varsTable.symbol_table[varsTable.func_id].isReturn = True

#Inicializa Era
def generateEra(id):
    cuad = Cuadrupl(None, "ERA", None, id, len(pilacuadruplos))
    pilacuadruplos.append(cuad)

#Function que crea el cuadrupo param
def getparam():
    resultado = pilaid.pop()
    pilaTipos.pop()
    valor = pilaVal.pop()
    num = str(varsTable.param_cont)
    cuadr = Cuadrupl(resultado,"param",None,"param"+num,len(pilacuadruplos))
    pilacuadruplos.append(cuadr)
    return resultado

#Function que crea el cuadrupo gosub
def generategosub(funct):
    resultado = varsTable.symbol_table[funct].cuadno
    cuadr = Cuadrupl(funct,"GoSub",None,resultado,len(pilacuadruplos))
    pilacuadruplos.append(cuadr)

#Funcion que permite asignar a un valor el valor que regresa una funcion
def funcasign(id):
    tipo = varsTable.symbol_table[id].tipo
    tam = len(popper)
    if tam > 0:
        if (popper[tam-1] == "="):
            valor = pilaVal.pop()
            valid = pilaid.pop()
            tipo_res = pilaTipos.pop()
            operator = popper.pop()
            id2 = varsTable.symbol_table[id].returno
            tipo_id = Memory.GetTipo(id2)
            #print("sdsdsd",valor,id2,av,valid)
            if tipo_id == "float" and tipo_res == "int":
                valor = float(valor)
                #dir = Memory.GetDir(valor,"float")
            elif tipo_id == "int" and tipo_res == "float":
                print("error de semantica 1")
                sys.exit()
            cuad = Cuadrupl(id2, operator, None, valid, len(pilacuadruplos))
            pilacuadruplos.append(cuad)
            return valor
        else:
            print("falla")
            sys.exit()


#GotMain
def gotoMain():
    cuadr = Cuadrupl(None,"GoTo",None,None,len(pilacuadruplos))
    pilacuadruplos.append(cuadr)

#Cuadruplos de print
def printcuad():
    tam = len(popper)
    if tam > 0:
        if popper[tam-1] == "print":
            resultado = pilaid.pop()
            pilaTipos.pop()
            pilaVal.pop()
            operator = popper.pop()
            cuadr = Cuadrupl(None, operator, None, resultado, len(pilacuadruplos))
            pilacuadruplos.append(cuadr)

#Cuadruplos de read
def readid():
    tam = len(popper)
    if tam > 0:
        if popper[tam-1] == "read":
            resultado = pilaid.pop()
            pilaTipos.pop()
            pilaVal.pop()
            operator = popper.pop()
            cuadr = Cuadrupl(None, operator, None, resultado, len(pilacuadruplos))
            pilacuadruplos.append(cuadr)

#Cuadruplos de find / No se usa confundimos lo que se pedia
def generateFind(id):
    tam = len(popper)
    if tam > 0:
        if popper[-1] == "find":
            dirpos = pilaid.pop()
            pilaTipos.pop
            pos = pilaVal.pop()
            operator = popper.pop()
            if ( pos <  len(varsTable.symbol_table[varsTable.func_id].dict[id].dirs)):
                dirvec = varsTable.symbol_table[varsTable.func_id].dict[id].dirs[pos]
                cuadr = Cuadrupl(id, operator, dirpos, dirvec,len(pilacuadruplos))
                pilacuadruplos.append(cuadr)
            else:
                print("Se sale del rango del arreglo")
                sys.exit()

#Cuadruplos de sort / No se usa confundimos lo que se pedia
def generateSort(id):
    tam = len(popper)
    if tam > 0:
        if popper[-1] == "sort":
            #arraux.append(varsTable.symbol_table[varsTable.func_id].dict[id].dirs.pop())
            operator = popper.pop()
            #dirvec = varsTable.symbol_table[varsTable.func_id].dict[id].dirs[pos]
            cuadr = Cuadrupl(None, operator, None, id,len(pilacuadruplos))
            pilacuadruplos.append(cuadr)


def Verificartam():

    tam = len(popper)
    if tam > 0:
        if popper[-1] == "[":
            val_inside = pilaVal.pop()
            dir_inside = pilaid.pop()
            pilaTipos.pop()
            dir_outsie = pilaid.pop()
            val_outside = pilaVal.pop()
            tipo_resultado = pilaTipos.pop()
            leng = varsTable.symbol_table["global"].dict[vector_id].space
            #print(val_inside,dir_inside,val_outside,dir_outsie)
            if ( val_inside <= leng):
                #print(newDir)
                cuadr = Cuadrupl(dir_inside, "VER", 1, leng,len(pilacuadruplos))
                pilacuadruplos.append(cuadr)
                valt = dir_inside + 1
                t = Memory.global_memroy.insert_temporal(valt,"int")
                cuadr = Cuadrupl(dir_inside,'+',1,t,len(pilacuadruplos))
                pilacuadruplos.append(cuadr)
                dirnew = Memory.global_memroy.insert_temporal(0,"int")
                Memory.UpdateTemp(dir_inside, dirnew, 'int')
                cuadr = Cuadrupl(t,'+',dir_outsie,dirnew,len(pilacuadruplos))
                pilacuadruplos.append(cuadr)
                pilaid.append('('+str(dirnew)+')')
                pilaVal.append(0)
                pilaTipos.append(tipo_resultado)
                #print(resultado_dir,resultado,)
                #print("Despues")
                #print("OPE",popper)
                #print("VAL",pilaVal)
                #print("DIR",pilaid)
                #print("TIPO",pilaTipos)
            else:
                print("Estas fuera del rango del vector")
                sys.exit()
