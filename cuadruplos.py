import sys

import varsTable as varsTable
import semantic_Cube as semantic

popper = []
pilaid = []
pilaTipos = []
pilaSaltos = []
ptemp = []
avail = []

class Cuadrupl:
    def __init__(self, left, operator, right, resultado):
        self.id = left
        self.tipo = operator
        self.dict = right
        self.dict = resultado

def imprimircuadruplo(left, operator, right, resultado):
    print (operator, left, right, resultado)

def pushID(id):
    pilaid.append(id)
    avail.append(varsTable.getAttributes(id))
    pilaTipos.append(varsTable.getTypeVar(id))
    #print (str(pilaid)[1:-1])
    #print (str(pilaTipos)[1:-1])

def pushCTE(var):
    avail.append(var)
    pilaid.append(var)
    crearTipo(var)
    #pilaid.pop()

def crearTipo(var):
    tipo = str(type(var))
    tipo1 = varsTable.getTypeVar2(tipo)
    pilaTipos.append(tipo1)
    #print (str(pilaid)[1:-1])
    #print (str(pilaTipos)[1:-1])

def pushPoper(oper):
    popper.append(oper)

def resolverasignacion():
    tam = len(popper)
    if tam > 0:
        if popper[tam-1] == '=':
            valor = avail.pop()
            #Sacar temporal final de resultado id
            pilaid.pop()
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
            Cuadrupl(valor, operator, None, valid)
            imprimircuadruplo(valor, operator, None, valid)
            #varsTable.update(valid,valor)
            #print(id, varsTable.getAttributes(id))
            return valor

def resolverterm():
    tam = len(popper)
    if tam > 0:
        if popper[tam-1] == '+' or popper[tam-1] == '-':
            val_der = avail.pop()
            pilaid.pop()
            tipo_der = pilaTipos.pop()
            val_izq = avail.pop()
            pilaid.pop()
            tipo_izq = pilaTipos.pop()
            operator = popper.pop()
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
                imprimircuadruplo(val_izq, operator, val_der, resultado)
            else:
                print("error de semantica")
                sys.exit()

def resolverfact():
    tam = len(popper)
    if tam > 0:
        if popper[tam-1] == '*' or popper[tam-1] == '/':
            val_der = avail.pop()
            pilaid.pop()
            tipo_der = pilaTipos.pop()
            val_izq = avail.pop()
            pilaid.pop()
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
                imprimircuadruplo(val_izq, operator, val_der, resultado)
            else:
                print("error de semantica")
                sys.exit()

def resolverlog():
    tam = len(popper)
    if tam > 0:
        if (popper[tam-1] == '<' or popper[tam-1] == '<=' or popper[tam-1] == '>' or popper[tam-1] == '>=' or popper[tam-1] == '==' or popper[tam-1] == '!='):
            val_der = avail.pop()
            val_izq = avail.pop()
            operator = popper.pop
