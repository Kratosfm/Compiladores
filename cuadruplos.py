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
    pilaid.append(id)
    avail.append(varsTable.getAttributes(id))
    pilaTipos.append(varsTable.getTypeVar(id))
    contador = contador + 1
    #print (contador,str(pilaid)[1:-1])
    #print(contador,str(avail)[1:-1])

def pushCTE(var):
    global contador
    if (var == 'true' or var == 'false'):
        pilaTipos.append("bool")
        avail.append(var)
        pilaid.append(var)
    else:
        avail.append(var)
        pilaid.append(var)
        crearTipo(var)
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
            pilaid.pop()
            avail.pop()
            tipo_res = pilaTipos.pop()
            tipo_id = pilaTipos.pop()
            valid = pilaid.pop()
            operator = popper.pop()
            if tipo_id == "float" and tipo_res == "int":
                valor = float(valor)
            elif tipo_id == "int" and tipo_res == "float":
                print("error de semantica")
                sys.exit()
            #print (str(pilaid)[1:-1])
            #print("el id es ",valor, operator, "None", valid, len(pilacuadruplos))
            cuad = Cuadrupl(valor, operator, None, valid, len(pilacuadruplos))
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
                else:
                    resultado = val_izq - val_der
                avail.append(resultado)
                pilaid.append(resultado)
                tip = crearTipo(resultado)
                #pilaTipos.append(tip)
                cuad = Cuadrupl(id_izq, operator, id_der, resultado, len(pilacuadruplos))
                pilacuadruplos.append(cuad)
                #imprimircuadruplo(val_izq, operator, val_der, resultado)
            else:
                print("error de semantica")
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
                else:
                    resultado = val_izq / val_der
                avail.append(resultado)
                pilaid.append(resultado)
                tip = crearTipo(resultado)
                cuad = Cuadrupl(id_izq, operator, id_der, resultado, len(pilacuadruplos))
                pilacuadruplos.append(cuad)
                #imprimircuadruplo(val_izq, operator, val_der, resultado)
            else:
                print("error de semantica")
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
                elif(operator == '<='):
                    resultado = val_izq <= val_der
                elif(operator == '>'):
                    resultado = val_izq > val_der
                elif(operator == '>='):
                    resultado = val_izq >= val_der
                elif(operator == '=='):
                    resultado = val_izq == val_der
                elif(operator == '!='):
                    resultado = val_izq != val_der
                cuad = Cuadrupl(id_izq, operator, id_der, resultado, len(pilacuadruplos))
                #imprimircuadruplo(val_izq, operator, val_der, resultado)
                pilacuadruplos.append(cuad)
                pilaid.append(resultado)
                avail.append(resultado)
                tip = crearTipo(resultado)
            else:
                print("error de semantica")
                sys.exit()

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
