import sys

import varsTable as varsTable
import semantic_Cube as semantic
import execMemory as Memory

popper = []
pilaid = []
pilaTipos = []
pilaSaltos = []
ptemp = []
avail = []
pilacuadruplos = []
contador = 0
paramcontador = 0

class Cuadrupl:
    def __init__(self, left, operator, right, resultado, num):
        self.left = left
        self.operator = operator
        self.right = right
        self.resultado = resultado
        self.num = num

def imprimirtodocuadr():
    for i in range(len(pilacuadruplos)):
        imprimircuadruplo(pilacuadruplos[i].num,pilacuadruplos[i].left,pilacuadruplos[i].operator,pilacuadruplos[i].right,pilacuadruplos[i].resultado)

def imprimircuadruplo(num,left, operator, right, resultado):
    print (num,operator, left, right, resultado)

def pushID(id):
    global contador
    pilaid.append(varsTable.getAttributes(id))
    avail.append(varsTable.getValue(id))
    pilaTipos.append(varsTable.getTypeVar(id))
    contador = contador + 1
    #print (contador,str(pilaid)[1:-1])
    #print(contador,str(avail)[1:-1])

# Funcion que obtiene elipo de un cte

# Funcion que verifica si el CTE ya se encuentra en la memoria
def verificarValorCte(cte,tipo):
    if tipo == "int":
        if(cte in Memory.global_memroy.ints.values()):
            return True
        else:
            return False
    elif tipo == "float":
        if(cte in Memory.global_memroy.floats.values()):
            return True
        else:
            return False
    elif tipo == "bool":
        if(cte in Memory.global_memroy.bools.values()):
            return True
        else:
            return False
    elif tipo == "string":
        if(cte in Memory.global_memroy.strings.values()):
            return True
        else:
            return False
    else:
        print("falla")

def pushCTE(var):
    global contador
    if (var == 'true' or var == 'false'):
        pilaTipos.append("bool")
        avail.append(var)
        pilaid.append(var)
    else:
        if str(type(var)) == "<class 'float'>":
            if (verificarValorCte(var,"float")):
                dir = Memory.GetDir(var,"float")
                avail.append(var)
                pilaid.append(dir)
                crearTipo(var)
            else:
                dir = Memory.global_memroy.insert_const(var,"float")
                avail.append(var)
                pilaid.append(dir)
                crearTipo(var)
        elif str(type(var)) == "<class 'int'>":
            if (verificarValorCte(var,"int")):
                dir = Memory.GetDir(var,"int")
                avail.append(var)
                pilaid.append(dir)
                crearTipo(var)
            else:
                dir = Memory.global_memroy.insert_const(var,"int")
                valor = Memory.global_memroy.ints.get(var)
                avail.append(var)
                pilaid.append(dir)
                crearTipo(var)
        elif str(type(var)) == "<class 'bool'>":
            if (verificarValorCte(var,"bool")):
                dir = Memory.GetDir(var,"bool")
                avail.append(var)
                pilaid.append(dir)
                crearTipo(var)
            else:
                dir = Memory.global_memroy.insert_const(var,"bool")
                valor = Memory.global_memroy.bools.get(var)
                avail.append(var)
                pilaid.append(dir)
                crearTipo(var)
        elif str(type(var)) == "<class 'str'>":
            if (verificarValorCte(var,"string")):
                dir = Memory.GetDir(var,"string")
                avail.append(var)
                pilaid.append(dir)
                crearTipo(var)
            else:
                dir = Memory.global_memroy.insert_const(var,"string")
                valor = Memory.global_memroy.strings.get(var)
                avail.append(var)
                pilaid.append(dir)
                crearTipo(var)
        else:
            print("bye")
    #print (contador,str(pilaid)[1:-1])
    #print(contador,str(avail)[1:-1])

def crearTipo(var):
    tipo = str(type(var))
    tipo1 = varsTable.getTypeVar2(tipo)
    pilaTipos.append(tipo1)
    #print (str(pilaid)[1:-1])
    #print (str(pilaTipos)[1:-1])

def pushPoper(oper):
    popper.append(oper)

def resolverasignacion():
    global contador
    tam = len(popper)
    if tam > 0:
        if popper[tam-1] == '=':
            valor = avail.pop()
            #Sacar temporal final de resultado id
            id2 = pilaid.pop()
            avail.pop()
            tipo_res = pilaTipos.pop()
            tipo_id = pilaTipos.pop()
            valid = pilaid.pop()
            #print("id",valid,id2,valor)
            operator = popper.pop()
            if tipo_id == "float" and tipo_res == "int":
                valor = float(valor)
                #dir = Memory.GetDir(valor,"float")
            elif tipo_id == "int" and tipo_res == "float":
                print("error de semantica 1")
                sys.exit()
            #print (str(pilaid)[1:-1])
            #print("el id es ",valor, operator, "None", valid, len(pilacuadruplos))
            cuad = Cuadrupl(id2, operator, None, valid, len(pilacuadruplos))
            pilacuadruplos.append(cuad)
            #varsTable.update(valid,valor)
            #print(id, varsTable.getAttributes(id))
            return valor

def resolverterm():
    global contador
    tam = len(popper)
    if tam > 0:
        if popper[tam-1] == '+' or popper[tam-1] == '-':
            val_der = avail.pop()
            id_der = pilaid.pop()
            tipo_der = pilaTipos.pop()
            val_izq = avail.pop()
            id_izq = pilaid.pop()
            tipo_izq = pilaTipos.pop()
            operator = popper.pop()
            #print(operator)
            tipo_resultado = semantic.getReturnType(tipo_der,tipo_izq,operator)
            if(tipo_resultado != "err"):
                if(operator == '+'):
                    resultado = val_izq + val_der
                    dir = Memory.global_memroy.insert_temporal(resultado,tipo_resultado)
                else:
                    resultado = val_izq - val_der
                    dir = Memory.global_memroy.insert_temporal(resultado,tipo_resultado)
                avail.append(resultado)
                pilaid.append(dir)
                tip = crearTipo(resultado)
                #pilaTipos.append(tip)
                cuad = Cuadrupl(id_izq, operator, id_der, dir, len(pilacuadruplos))
                pilacuadruplos.append(cuad)
                #imprimircuadruplo(val_izq, operator, val_der, resultado)
            else:
                print("error de semantica 2")
                sys.exit()


def resolverfact():
    global contador
    tam = len(popper)
    if tam > 0:
        if popper[tam-1] == '*' or popper[tam-1] == '/':
            val_der = avail.pop()
            id_der = pilaid.pop()
            tipo_der = pilaTipos.pop()
            val_izq = avail.pop()
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
                avail.append(resultado)
                pilaid.append(dir)
                tip = crearTipo(resultado)
                cuad = Cuadrupl(id_izq, operator, id_der, dir, len(pilacuadruplos))
                pilacuadruplos.append(cuad)
                #imprimircuadruplo(val_izq, operator, val_der, resultado)
            else:
                print("error de semantica 3")
                sys.exit()

def resolverRel():
    global contador
    tam = len(popper)
    if tam > 0:
        if (popper[tam-1] == '<' or popper[tam-1] == '<=' or popper[tam-1] == '>' or popper[tam-1] == '>=' or popper[tam-1] == '==' or popper[tam-1] == '!='):
            val_der = avail.pop()
            tipo_der = pilaTipos.pop()
            id_der = pilaid.pop()
            val_izq = avail.pop()
            tipo_izq = pilaTipos.pop()
            id_izq = pilaid.pop()
            operator = popper.pop()
            tipo_resultado = semantic.getReturnType(tipo_der,tipo_izq,operator)
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
                pilaid.append(resultado)
                avail.append(resultado)
                tip = crearTipo(resultado)
            else:
                print("error de semantica 4")
                sys.exit()

#Condiciones
def ResolverCond():
    global contador
    tipo = pilaTipos.pop()
    if (tipo != "bool"):
        print("error de typme-mismatch")
        sys.exit()
    else:
        resultado = avail.pop()
        id = pilaid.pop()
        cuad = Cuadrupl("GotoF", None, None, resultado, len(pilacuadruplos))
        pilacuadruplos.append(cuad)
        pilaSaltos.append(len(pilacuadruplos)-1)

def ResElse():
    global contador
    cuad = Cuadrupl("Goto", None, None, None, len(pilacuadruplos))
    false = pilaSaltos.pop()
    pilaSaltos.append(len(pilacuadruplos))
    pilacuadruplos.append(cuad)
    fill(false, len(pilacuadruplos))

def fill(cuadr, salto):
    pilacuadruplos[cuadr].resultado = salto

def finalif():
    end = pilaSaltos.pop()
    fill(end, len(pilacuadruplos))

def while1():
    pilaSaltos.append(len(pilacuadruplos))

def while2():
    tipo = pilaTipos.pop()
    if (tipo != "bool"):
        print("error de type-mismatch")
        sys.exit()
    else:
        resultado = avail.pop()
        cuad = Cuadrupl("GotoF", None, None, resultado, len(pilacuadruplos)-1)
        pilacuadruplos.append(cuad)
        pilaSaltos.append(len(pilacuadruplos)-1)

def while3():
    end = pilaSaltos.pop()
    regresa = pilaSaltos.pop()
    cuad = Cuadrupl("Goto", None, None, regresa, len(pilacuadruplos))
    pilacuadruplos.append(cuad)
    fill(end,len(pilacuadruplos))

#Modulos
#Inicializa Era
def generateEra(id):
    global paramcontador
    cuad = Cuadrupl(None, "ERA", None, id, len(pilacuadruplos))
    pilacuadruplos.append(cuad)
    paramcontador = paramcontador + 1
