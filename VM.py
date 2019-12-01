import cuadruplos as cuadruplos
import varsTable as varsTable
import execMemory as Memory
from ast import literal_eval
import operator
import sys

arr_vec = []
resbol = None
cont_param = 0
func_id = None
val_return = None
isArray = False
cont_vect = 0
pos = 0
#arreglo que almacena las direcciones de los parametros
arrparam = []
#arreglo que almacena los tipos de los parametros
arrparam2 =[]
last_pos = []

#Funcion que inicializa la lectura de la virtual machine con el cuadruplo de GotoMain
def programa():
    pos = GoToMain(0,cuadruplos.pilacuadruplos[0])
    while(cuadruplos.pilacuadruplos[pos].resultado != "ENDPROGRAM"):
        pos = Ejecucion(pos,cuadruplos.pilacuadruplos[pos])
    Memory.Reiniciar()
    Memory.BorrarInts()
    Memory.BorrarBools()
    Memory.BorrarFloats()
    Memory.BorrarStrings()
    #No se porque no se elimina el 1000
    #Memory.global_memroy.ints.pop(1000)

#El if gigante que dependiendo el operador del cuadruplo empezara a hacer las acciones necesarias.
def Ejecucion(num,cuadrup):
    global pos
    global cont_param
    global last_pos
    global func_id
    global isArray
    global cont_vect
    if (cuadrup.operator == "="):
        if (func_id != None):
            if(varsTable.symbol_table[func_id].isReturn == True):
                newVal = Memory.getValor(cuadrup.left)
                Memory.updateVal(cuadrup.resultado,newVal)
            else:
                newVal = Memory.getValor(cuadrup.left)
                tipo1 = Memory.GetTipo(cuadrup.resultado)
                tipo2 = Memory.GetTipo(cuadrup.left)
                if(tipo1 == tipo2):
                    Memory.updateVal(cuadrup.resultado,newVal)
                    num = num + 1
                    return num
                else:
                        print("error de tipos")
                        sys.exit()
        else:
            #print("print",cuadrup.left,cuadrup.resultado)
            left = isdirect(cuadrup.left)
            valleft = Memory.getValor(left)
            resdir = isdirect(cuadrup.resultado)
            #Memory.updateVal()
            #print("print",resdir)
            Memory.updateVal(resdir,valleft)
        num = num + 1
        return num

    elif(cuadrup.operator == "+"):
        left = isdirect(cuadrup.left)
        right = isdirect(cuadrup.right)
        if cuadrup.right == 1:
            isArray = True
        if isArray:
            val_izq = Memory.getValor(left)
            val_der = Memory.getValor(right)
            newVal = (val_izq + right)
            cont_vect = cont_vect + 1
        #    print(cuadrup.operator,cuadrup.left,cuadrup.right,cuadrup.resultado)
        else:
            val_izq = Memory.getValor(left)
            val_der = Memory.getValor(right)
            newVal = (val_izq + val_der)
            #print ("suma",  val_izq,left,val_der,right,newVal,cuadrup.resultado)
        Memory.updateVal(cuadrup.resultado,newVal)
        if cont_vect >= 2:
            isArray = False
        num = num + 1
        return num

    elif(cuadrup.operator == "-"):
        val_izq = isdirect(cuadrup.left)
        val_der = isdirect(cuadrup.right)

        val_izq = Memory.getValor(val_izq)
        val_der = Memory.getValor(val_der)
        newVal = (val_izq - val_der)
        Memory.updateVal(cuadrup.resultado,newVal)
        num = num + 1
        return num

    elif(cuadrup.operator == "/"):
        val_izq = isdirect(cuadrup.left)
        val_der = isdirect(cuadrup.right)

        val_izq = Memory.getValor(val_izq)
        val_der = Memory.getValor(val_der)
        newVal = (val_izq / val_der)
        Memory.updateVal(cuadrup.resultado,newVal)
        num = num + 1
        return num

    elif(cuadrup.operator == "*"):
        val_izq = isdirect(cuadrup.left)
        val_der = isdirect(cuadrup.right)

        val_izq = Memory.getValor(val_izq)
        val_der = Memory.getValor(val_der)
        newVal = (val_izq * val_der)
        Memory.updateVal(cuadrup.resultado,newVal)
        num = num + 1
        return num

    elif(cuadrup.operator == "print"):
        #sprint(cuadrup.operator,cuadrup.left,cuadrup.right,cuadrup.resultado)
        res = isdirect(cuadrup.resultado)
        valres = Memory.getValor(res)
        print(valres)
        num = num + 1
        return num

    elif(cuadrup.operator == "read"):
        newVal = input()
        tipo = str(get_type(newVal))
        if (tipo == "<class 'int'>"):
            tipo = "int"
            newVal = int(newVal)
        elif (tipo == "<class 'float'>"):
            tipo = "float"
            newVal = float(newVal)
        elif (newVal == 'true' or newVal == 'false'):
            tipo = "bool"
            newVal = bool(newVal)
        else:
            tipo = "string"
        Memory.updateVal(cuadrup.resultado,newVal)
        num = num + 1
        return num

    elif(cuadrup.operator == "find"):
        res = Memory.getValor(cuadrup.resultado)
        print(res)
        num = num + 1
        return num

    elif(cuadrup.operator == "sort"):
        acomodar(cuadrup.resultado)
        #res = Memory.getValor(cuadrup.resultado)
        #print("El valor del arreglo en la posicion es", res)
        num = num + 1
        return num

    elif(cuadrup.operator == "<"):
        res = isdirect(cuadrup.resultado)
        val_izq = isdirect(cuadrup.left)
        val_der = isdirect(cuadrup.right)

        res = Memory.getValor(res)
        val_izq = Memory.getValor(val_izq)
        val_der = Memory.getValor(val_der)
        newVal = (val_izq < val_der)
        Memory.updateVal(cuadrup.resultado,newVal)
        num = num + 1
        return num

    elif(cuadrup.operator == ">"):
        res = isdirect(cuadrup.resultado)
        val_izq = isdirect(cuadrup.left)
        val_der = isdirect(cuadrup.right)

        res = Memory.getValor(res)
        val_izq = Memory.getValor(val_izq)
        val_der = Memory.getValor(val_der)
        newVal = (val_izq > val_der)
        Memory.updateVal(cuadrup.resultado,newVal)
        num = num + 1
        return num

    elif(cuadrup.operator == "<="):
        #Memory.global_memroy.show()
        res = isdirect(cuadrup.resultado)
        val_izq = isdirect(cuadrup.left)
        val_der = isdirect(cuadrup.right)

        res = Memory.getValor(res)
        val_izq = Memory.getValor(val_izq)
        val_der = Memory.getValor(val_der)
        newVal = (val_izq <= val_der)
        Memory.updateVal(cuadrup.resultado,newVal)
        num = num + 1
        return num

    elif(cuadrup.operator == ">="):
        res = isdirect(cuadrup.resultado)
        val_izq = isdirect(cuadrup.left)
        val_der = isdirect(cuadrup.right)

        res = Memory.getValor(res)
        val_izq = Memory.getValor(val_izq)
        val_der = Memory.getValor(val_der)
        newVal = (val_izq >= val_der)
        Memory.updateVal(cuadrup.resultado,newVal)
        num = num + 1
        return num

    elif(cuadrup.operator == "!="):
        res = isdirect(cuadrup.resultado)
        val_izq = isdirect(cuadrup.left)
        val_der = isdirect(cuadrup.right)

        res = Memory.getValor(res)
        val_izq = Memory.getValor(val_izq)
        val_der = Memory.getValor(val_der)
        newVal = (val_izq != val_der)
        Memory.updateVal(cuadrup.resultado,newVal)
        num = num + 1
        return num

    elif(cuadrup.operator == "=="):
        res = isdirect(cuadrup.resultado)
        val_izq = isdirect(cuadrup.left)
        val_der = isdirect(cuadrup.right)

        res = Memory.getValor(res)
        val_izq = Memory.getValor(val_izq)
        val_der = Memory.getValor(val_der)
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
        last_pos.append(cuadrup.num + 1)
        return num

    elif(cuadrup.operator == "ENDPROC"):
        num = last_pos.pop()
        #Memory.global_memroy.show()
        Memory.BorrarInts()
        Memory.BorrarBools()
        Memory.BorrarFloats()
        Memory.BorrarStrings()
        Memory.Reiniciar()
        #Memory.global_memroy.show()
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

    elif(cuadrup.operator == "VER"):
        #print(cuadrup.operator,cuadrup.left,cuadrup.right,cuadrup.resultado)
        left = isdirect(cuadrup.left)
        val_left = Memory.getValor(left)
        val_der = cuadrup.right
        val_res = cuadrup.resultado
        #print ("entre", cuadrup.left,val_left, val_der, val_res)
        if( val_left >= val_der and val_left <= val_res ):
            pos = cuadrup.left + cuadrup.resultado
            cont_vect = 0
        else:
            print("Valores fuera de rango")
            sys.exit()
    num = num + 1
    return num

#def Funciones (num,cuadrup,func_id):

#Funcion que devuelve el numero donde empieza el main
def GoToMain (num,cuadrup):
    return cuadrup.resultado

#funcion que acomoda los valores dentro de un vector / esta mal, sentimos eso nos enteramos ayer que no era asi
def acomodar(id):
    arraux = {}
    arrfin = []
    i = 0
    x = 0
    tam = len(varsTable.symbol_table["main"].dict[id].dirs)
    while ( i < tam):
        dir = varsTable.symbol_table["main"].dict[id].dirs[i]
        val = Memory.getValor(dir)
        arraux[dir] = val
        i = i + 1
    varsTable.symbol_table["main"].dict[id].dirs.clear()
    for key, value in sorted(arraux.items(), key=lambda item: item[1]):
        arrfin.append(key)
        #imprime bonito el sort
        #print("%s: %s" % (key, value))
    while ( x < tam):
        varsTable.symbol_table["main"].dict[id].dirs.append(arrfin.pop(0))
        x = x + 1
    print(varsTable.symbol_table["main"].dict[id].dirs)
    #arraux.append(varsTable.symbol_table["main"].dict[id].dirs.pop())

#funcion que regresa el valor de los input con la funcion literal_eval
def get_type(newVal):
    try:
        return type(literal_eval(newVal))
    except (ValueError, SyntaxError):
        # A string, so return str
        return str

def isdirect(operator):
    operator = str(operator)
    if operator[0] == '(':
        newOp = operator[1:len(operator)-1]
        newOp = int(newOp)
        dir = Memory.getValor(newOp)
        return dir
    else:
        return int(operator)
