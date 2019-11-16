import sys

import varsTable as varsTable
import semantic_Cube as semantic

popper = []
pilaid = []
pilaTipos = []
pilaSaltos = []
ptemp = []
avail = []
pilacuadruplos = []

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

def imprimircuadruplo(left, operator, right, resultado):
    print (operator, left, right, resultado)

def pushID(id):
    pilaid.append(id)
    avail.append(varsTable.getAttributes(id))
    pilaTipos.append(varsTable.getTypeVar(id))
    #print (str(pilaid)[1:-1])
    #print (str(pilaTipos)[1:-1])

def pushCTE(var):
    if (var == 'true' or var == 'false'):
        pilaTipos.append("bool")
        avail.append(var)
        pilaid.append(var)
    else:
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
            cuad = Cuadrupl(valor, operator, None, valid, len(pilacuadruplos))
            pilacuadruplos.append(cuad)
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
            print(operator)
            tipo_resultado = semantic.getReturnType(tipo_der,tipo_izq,operator)
            print(tipo_resultado)
            if(tipo_resultado != "err"):
                if(operator == '+'):
                    resultado = val_izq + val_der
                else:
                    resultado = val_izq - val_der
                avail.append(resultado)
                pilaid.append(resultado)
                tip = crearTipo(resultado)
                #pilaTipos.append(tip)
                cuad = Cuadrupl(val_izq, operator, val_der, resultado, len(pilacuadruplos))
                pilacuadruplos.append(cuad)
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
            print(operator)
            tipo_resultado = semantic.getReturnType(tipo_der,tipo_izq,operator)
            if(tipo_resultado != "err"):
                if(operator == '*'):
                    resultado = val_izq * val_der
                else:
                    resultado = val_izq / val_der
                avail.append(resultado)
                pilaid.append(resultado)
                tip = crearTipo(resultado)
                cuad = Cuadrupl(val_izq, operator, val_der, resultado, len(pilacuadruplos))
                pilacuadruplos.append(cuad)
                imprimircuadruplo(val_izq, operator, val_der, resultado)
            else:
                print("error de semantica")
                sys.exit()

def resolverRel():
    tam = len(popper)
    if tam > 0:
        if (popper[tam-1] == '<' or popper[tam-1] == '<=' or popper[tam-1] == '>' or popper[tam-1] == '>=' or popper[tam-1] == '==' or popper[tam-1] == '!='):
            val_der = avail.pop()
            tipo_der = pilaTipos.pop()
            pilaid.pop()
            val_izq = avail.pop()
            tipo_izq = pilaTipos.pop()
            pilaid.pop()
            operator = popper.pop
            print(val_izq,val_der,operator)
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
                cuad = Cuadrupl(val_izq, operator, val_der, resultado, len(pilacuadruplos))
                imprimircuadruplo(val_izq, operator, val_der, resultado)
                pilacuadruplos.append(cuad)
                pilaid.append(resultado)
                avail.append(resultado)
                tip = crearTipo(resultado)
            else:
                print("error de semantica")
                sys.exit()
