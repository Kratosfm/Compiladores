import cuadruplos as cuadruplos
import varsTable as varsTable
import execMemory as Memory
import sys

resbol = None

def programa():
    pos = GoToMain(0,cuadruplos.pilacuadruplos[0])
    while(cuadruplos.pilacuadruplos[pos].resultado != "ENDPROGRAM"):
        pos = Ejecucion(pos,cuadruplos.pilacuadruplos[pos])


def Ejecucion(num,cuadrup):
    if (cuadrup.operator == "="):
        newVal = Memory.getValor(cuadrup.left)
        Memory.updateVal(cuadrup.resultado,newVal)
        num = num + 1
        return num
    elif(cuadrup.operator == "+"):
        val_izq = Memory.getValor(cuadrup.left)
        val_der = Memory.getValor(cuadrup.right)
        newVal = (val_izq + val_der)
        Memory.updateVal(cuadrup.resultado,newVal)
        num = num + 1
        return num
    elif(cuadrup.operator == "-"):
        val_izq = Memory.getValor(cuadrup.left)
        val_der = Memory.getValor(cuadrup.right)
        newVal = (val_izq - val_der)
        Memory.updateVal(cuadrup.resultado,newVal)
        num = num + 1
        return num
    elif(cuadrup.operator == "/"):
        val_izq = Memory.getValor(cuadrup.left)
        val_der = Memory.getValor(cuadrup.right)
        newVal = (val_izq / val_der)
        Memory.updateVal(cuadrup.resultado,newVal)
        num = num + 1
        return num
    elif(cuadrup.operator == "*"):
        val_izq = Memory.getValor(cuadrup.left)
        val_der = Memory.getValor(cuadrup.right)
        newVal = (val_izq * val_der)
        Memory.updateVal(cuadrup.resultado,newVal)
        num = num + 1
        return num
    elif(cuadrup.operator == "print"):
        res = Memory.getValor(cuadrup.resultado)
        print(res)
        num = num + 1
        return num
    elif(cuadrup.operator == "<"):
        res = Memory.getValor(cuadrup.resultado)
        val_izq = Memory.getValor(cuadrup.left)
        val_der = Memory.getValor(cuadrup.right)
        newVal = (val_izq < val_der)
        Memory.updateVal(cuadrup.resultado,newVal)
        num = num + 1
        return num
    elif(cuadrup.operator == ">"):
        res = Memory.getValor(cuadrup.resultado)
        val_izq = Memory.getValor(cuadrup.left)
        val_der = Memory.getValor(cuadrup.right)
        newVal = (val_izq > val_der)
        Memory.updateVal(cuadrup.resultado,newVal)
        num = num + 1
        return num
    elif(cuadrup.operator == "<="):
        res = Memory.getValor(cuadrup.resultado)
        val_izq = Memory.getValor(cuadrup.left)
        val_der = Memory.getValor(cuadrup.right)
        newVal = (val_izq <= val_der)
        Memory.updateVal(cuadrup.resultado,newVal)
        num = num + 1
        return num
    elif(cuadrup.operator == ">="):
        res = Memory.getValor(cuadrup.resultado)
        val_izq = Memory.getValor(cuadrup.left)
        val_der = Memory.getValor(cuadrup.right)
        newVal = (val_izq >= val_der)
        Memory.updateVal(cuadrup.resultado,newVal)
        num = num + 1
        return num
    elif(cuadrup.operator == "!="):
        res = Memory.getValor(cuadrup.resultado)
        val_izq = Memory.getValor(cuadrup.left)
        val_der = Memory.getValor(cuadrup.right)
        newVal = (val_izq != val_der)
        Memory.updateVal(cuadrup.resultado,newVal)
        num = num + 1
        return num
    elif(cuadrup.operator == "=="):
        val_izq = Memory.getValor(cuadrup.left)
        val_der = Memory.getValor(cuadrup.right)
        newVal = (val_izq == val_der)
        Memory.updateVal(cuadrup.resultado,newVal)
        num = num + 1
        return num
    elif(cuadrup.operator == "GotoF"):
        if(Memory.getValor(cuadrup.left) == False):
            num = cuadrup.resultado
            return num
        else:
            num = num + 1
            return num
    elif(cuadrup.operator == "Goto"):
        num = cuadrup.resultado
        return num
    num = num + 1
    return num


def GoToMain (num,cuadrup):
    return cuadrup.resultado
