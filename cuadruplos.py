import sys

import varsTable as varsTable
from semantic import resultType

popper = []
pilaid = []
pilaTipos = []
pilaSaltos = []
ptemp = []
avail = []

def imprimircuadruplo(left, operator, right, resultado):
    print (operator, left, right, resultado)

def pushID(id):
    pilaid.append(id)
    avail.append(varsTable.getAttributes(id))

def pushCTE(var):
    avail.append(var)
    pilaid.append("var")

def pushPoper(oper):
    popper.append(oper)

def poppilaid():
    pilaid.pop()
    avail.pop()

def popPoper():
    popper.pop()

def resolverasignacion():
    tam = len(popper)
    if tam > 0:
        if popper[tam-1] == '=':
            valor = avail.pop()
            valid = pilaid.pop()
            print ("se borra ", valid)
            operator = popper.pop()
            imprimircuadruplo(valor, operator, None, valid)
            #varsTable.update(valid,valor)
            #print(id, varsTable.getAttributes(id))
            return valor

def resolverterm():
    tam = len(popper)
    if tam > 0:
        if popper[tam-1] == '+' or popper[tam-1] == '-':
            val_der = avail.pop()
            imprimit = pilaid.pop()
            print ("se borra ", imprimit)
            val_izq = avail.pop()
            imprimit = pilaid.pop()
            print ("se borra ", imprimit)
            operator = popper.pop()
            #checar en la semantica si se puede. me falta meter los tipos en un arreglo
            if(operator == '+'):
                resultado = val_izq + val_der
            else:
                resultado = val_izq - val_der
            avail.append(resultado)
            imprimircuadruplo(val_izq, operator, val_der, resultado)

def resolverfact():
    tam = len(popper)
    if tam > 0:
        if popper[tam-1] == '*' or popper[tam-1] == '/':
            val_der = avail.pop()
            val_izq = avail.pop()
            operator = popper.pop()
            #checar en la semantica si se puede. me falta meter los tipos en un arreglo
            if(operator == '*'):
                resultado = val_izq * val_der
            else:
                resultado = val_izq / val_der
            avail.append(resultado)
            imprimircuadruplo(val_izq, operator, val_der, resultado)

def resolverlog():
    tam = len(popper)
    if tam > 0:
        if (popper[tam-1] == '<' or popper[tam-1] == '<=' or popper[tam-1] == '>' or popper[tam-1] == '>=' or popper[tam-1] == '==' or popper[tam-1] == '!='):
            val_der = avail.pop()
            val_izq = avail.pop()
            operator = popper.pop
