import sys

vart = None

class Entry:
    def __init__(self, id, tipo, value = None):
        self.id = id
        self.tipo = tipo
        self.value = value
symbol_table = []

def look(valid):
    for i in range(len(symbol_table)):
        if valid == symbol_table[i].id:
            return 0
        else:
            return 1


def insert(tipo,id):
    existe = look(id)
    if existe != 0:
        valor2 = Entry(id,tipo)
        symbol_table.append(valor2)
        #show()
    else:
        print("Variable ya declarada")
        sys.exit()
    #show()

def show():
    for i in range(len(symbol_table)):
        print(symbol_table[i].id , " ", symbol_table[i].tipo ," ",symbol_table[i].value)

#Si encuentra = cambiar valor
def update(valid,valor):
    for i in range(len(symbol_table)):
        if valid == symbol_table[i].id:
            if (validar(symbol_table[i].tipo, valor) == True):
                symbol_table[i].value = valor
    #show()

def validar(tipo, valor):
    print(tipo, str(type(valor)))
    if str(type(valor)) == "<class 'float'>" and tipo == 'float':
        return True
    if str(type(valor)) == "<class 'int'>" and tipo == 'int':
        #print("valido")
        return True
    if str(type(valor)) == "<class 'str'>" and tipo == 'string':
        return True
    if str(type(valor)) == "<class 'bool'>" and tipo == 'bool':
        return True
    else:
        print("Error")


#for i in range(len(list_tok)):
#    if str(list_tok[i]).find("int") != -1:
#        print(str(list_tok[i]).find("int"))

#valor = Entry("Francisco","int",123)
#symbol_table.append(valor)x
#valor = Entry("Oscar","float",12.5)
#symbol_table.append(valor)
#valor = Entry("Tony","int",502)
#symbol_table.append(valor)
#valid = input("Da el id ")
#valtipo = input("Da el tipo ")
#insert(valtipo,valid)
#update("Tony",500)
#valid = input("Da el id ")
#valtipo = input("Da el tipo ")
#insert(valtipo,valid)
#show()
