import cuadruplos as cuadruplos
import varsTable as varsTable
import execMemory as Memory
import sys

resbol = None
cont_param = 0
func_id = None
val_return = None
#arreglo que almacena las direcciones de los parametros
arrparam = []
#arreglo que almacena los tipos de los parametros
arrparam2 =[]
last_pos = 0


def programa():
    pos = GoToMain(0,cuadruplos.pilacuadruplos[0])
    while(cuadruplos.pilacuadruplos[pos].resultado != "ENDPROGRAM"):
        pos = Ejecucion(pos,cuadruplos.pilacuadruplos[pos])
    print ("YOLE",Memory.global_memroy.ints[7000],Memory.global_memroy.ints[7001],Memory.global_memroy.ints[7002])


def Ejecucion(num,cuadrup):
    global cont_param
    global last_pos
    global func_id
    if (cuadrup.operator == "="):
        if (func_id != None):
            if(varsTable.symbol_table[func_id].isReturn == True):
                newVal = Memory.getValor(cuadrup.left)
                Memory.updateVal(cuadrup.resultado,newVal)
                #print("Se recibe dir en funcion", cuadrup.left, "con valor",Memory.getValor(cuadrup.left),"en", cuadrup.resultado, "con", Memory.getValor(cuadrup.resultado),"en",func_id)
        else:
            newVal = Memory.getValor(cuadrup.left)
            Memory.updateVal(cuadrup.resultado,newVal)
            #print("Se recibe dir", cuadrup.left, "con valor",Memory.getValor(cuadrup.left),"en", cuadrup.resultado, "con", Memory.getValor(cuadrup.resultado),"en",func_id)
            num = num + 1
            return num

    elif(cuadrup.operator == "+"):
        val_izq = Memory.getValor(cuadrup.left)
        val_der = Memory.getValor(cuadrup.right)
        newVal = (val_izq + val_der)
        #sprint(val_izq,val_der)
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

    elif(cuadrup.operator == "GoSub"):
        num = cuadrup.resultado
        last_pos = cuadrup.num + 1
        return num

    elif(cuadrup.operator == "ENDPROC"):
        num = last_pos
        cont_param = 0
        arrparam.clear()
        arrparam2.clear()
        return num

    elif(cuadrup.operator == "ERA"):
        func_id = cuadrup.resultado
        for i in varsTable.symbol_table[func_id].dict :
            if (varsTable.symbol_table[func_id].dict[i].isParam == True):
                arrparam.append(varsTable.symbol_table[func_id].dict[i].value)
                arrparam2.append(varsTable.symbol_table[func_id].dict[i].tipo)
        cont_param = len(arrparam)
        num = num + 1
        return num

    elif(cuadrup.operator == "param"):
        val_izq = Memory.getValor(cuadrup.left)
        tipo = varsTable.getTypeVar2(str(type(val_izq)))
        if (tipo == arrparam2[cont_param-1]):
            Memory.updateVal(arrparam[cont_param-1],val_izq)
            cont_param = cont_param - 1
        else:
            print("No concuerdan los datos se esperaba un",arrparam2[cont_param-1], "y se recibio un",tipo)
            sys.exit()

    elif(cuadrup.operator == "return"):
        newVal = Memory.getValor(cuadrup.resultado)
        tipo = Memory.GetTipo(cuadrup.resultado)
        Memory.updateVal(cuadrup.resultado,newVal)
        dirRet = varsTable.symbol_table[func_id].returno
        #print("Semental",newVal,cuadrup.resultado,tipo)
        if (tipo == "int"):
            Memory.global_memroy.ints[dirRet] = newVal
            Memory.updateVal(dirRet,newVal)
        elif (tipo == "float"):
            Memory.global_memroy.ints[dirRet] = newVal
            Memory.updateVal(dirRet,newVal)
        elif (tipo == "string"):
            Memory.global_memroy.ints[dirRet] = newVal
            Memory.updateVal(dirRet,newVal)
        elif (tipo == "bool"):
            Memory.global_memroy.ints[dirRet] = newVal
            Memory.updateVal(dirRet,newVal)
        num = num + 1
        return num
    num = num + 1
    return num

#def Funciones (num,cuadrup,func_id):


def GoToMain (num,cuadrup):
    return cuadrup.resultado
