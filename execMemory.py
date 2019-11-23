import pprint
import varsTable as varsTable

loc_int = 1000
loc_float = 1100
loc_string = 1200
loc_bools = 1300
global_int = 2000
global_float = 2100
global_string = 2200
global_bools = 2300
main_int = 3000
main_float = 3100
main_string = 3200
main_bools = 3300
cte_int = 4000
cte_float = 4100
cte_string = 4200
cte_bools = 4300
tm_int = 5000
tm_float = 5100
tm_string = 5200
tm_bools = 5300
tl_int = 6000
tl_float = 6100
tl_string = 6200
tl_bools = 6300

class Memory:

    def __init__(self):
        self.ints = {}
        self.floats = {}
        self.bools = {}
        self.strings = {}

    def insert_global(self, var, tipo, Space = None):
        global global_int
        global global_float
        global global_string
        global global_bools
        if( tipo == "int" and varsTable.is_vector == False):
            dir = global_int
            global_int = global_int + 1
            self.ints[dir] = var
            return dir
        elif( tipo == "float" and varsTable.is_vector == False):
            dir = global_float
            global_float = global_float + 1
            self.floats[dir] = var
            return dir
        elif( tipo == "bool" and varsTable.is_vector == False):
            dir = global_bools
            global_bools = global_bools + 1
            self.bools[dir] = var
            return dir
        elif( tipo == "string" and varsTable.is_vector == False):
            dir = global_string
            global_string = global_string + 1
            self.strings[dir] = var
            return dir
        elif( tipo == "int" and varsTable.is_vector == True):
            dir = global_int
            global_int = global_int + Space + 1
            self.ints[dir] = var
            return dir
        elif( tipo == "float" and varsTable.is_vector == True):
            dir = global_float
            global_float = global_float + Space + 1
            self.floats[dir] = var
            return dir
        elif( tipo == "bool" and varsTable.is_vector == True):
            dir = global_bools
            global_bools = global_bools + Space + 1
            self.bools[dir] = var
            return dir
        elif( tipo == "string" and varsTable.is_vector == True):
            dir = global_string
            global_string = global_string + Space + 1
            self.strings[dir] = var
            return dir

    def insert_main(self, var, tipo, Space = None):
        global main_int
        global main_float
        global main_bools
        global main_string
        if( tipo == "int" and varsTable.is_vector == False):
            dir = main_int
            main_int = main_int + 1
            self.ints[dir] = var
            return dir
        elif( tipo == "float" and varsTable.is_vector == False):
            dir = main_float
            main_float = main_float + 1
            self.floats[dir] = var
            return dir
        elif( tipo == "bool" and varsTable.is_vector == False):
            dir = main_bools
            main_bools = main_bools + 1
            self.bools[dir] = var
            return dir
        elif( tipo == "string" and varsTable.is_vector == False):
            dir = main_string
            main_string = main_string + 1
            self.strings[dir] = var
            return dir
        elif( tipo == "int" and varsTable.is_vector == True):
            dir = main_int
            main_int = main_int + Space + 1
            self.ints[dir] = var
            return dir
        elif( tipo == "float" and varsTable.is_vector == True):
            dir = main_float
            main_float = main_float + Space + 1
            self.floats[dir] = var
            return dir
        elif( tipo == "bool" and varsTable.is_vector == True):
            dir = main_bools
            main_bools = main_bools + Space + 1
            self.bools[dir] = var
            return dir
        elif( tipo == "string" and varsTable.is_vector == True):
            dir = main_string
            main_string = main_string + Space + 1
            self.strings[dir] = var
            return dir


    def insert_local(self, var, tipo, Space = None):
        global loc_int
        global loc_float
        global loc_bools
        global loc_string
        if( tipo == "int" and varsTable.is_vector == False):
            dir = loc_int
            loc_int = loc_int + 1
            self.ints[dir] = var
            return dir
        elif( tipo == "float" and varsTable.is_vector == False):
            dir = loc_float
            loc_float = loc_float + 1
            self.floats[dir] = var
            return dir
        elif( tipo == "bool" and varsTable.is_vector == False):
            dir = loc_bools
            loc_bools = loc_bools + 1
            self.bools[dir] = var
            return dir
        elif( tipo == "string" and varsTable.is_vector == False):
            dir = loc_string
            loc_string = loc_string + 1
            self.strings[dir] = var
            return dir
        elif( tipo == "int" and varsTable.is_vector == True):
            dir = loc_int
            loc_int = loc_int + Space + 1
            self.ints[dir] = var
            return dir
        elif( tipo == "float" and varsTable.is_vector == True):
            dir = loc_float
            loc_float = loc_float + Space + 1
            self.floats[dir] = var
            return dir
        elif( tipo == "bool" and varsTable.is_vector == True):
            dir = loc_bools
            loc_bools = loc_bools + Space + 1
            self.bools[dir] = var
            return dir
        elif( tipo == "string" and varsTable.is_vector == True):
            dir = loc_string
            loc_string = loc_string + Space + 1
            self.strings[dir] = var
            return dir

    def insert_const(self,var,tipo):
        global cte_int
        global cte_float
        global cte_string
        global cte_bools
        if( tipo == "int"):
            dir = cte_int
            cte_int = cte_int + 1
            self.ints[dir] = var
            return dir
        elif( tipo == "float" ):
            dir = cte_float
            cte_float = cte_float + 1
            self.floats[dir] = var
            return dir
        elif( tipo == "bool" ):
            dir = cte_bools
            cte_bools = cte_bools + 1
            self.bools[dir] = var
            return dir
        elif( tipo == "string" ):
            dir = cte_string
            cte_string = cte_string + 1
            self.strings[dir] = var
            return dir

    def insert_temporal(self,var,tipo):
        global tm_int
        global tm_float
        global tm_string
        global tm_bools
        global tl_int
        global tl_float
        global tl_string
        global tl_bools
        if( tipo == "int" and varsTable.func_id == "main"):
            dir = tm_int
            tm_int = tm_int + 1
            self.ints[dir] = var
            return dir
        elif( tipo == "float" and varsTable.func_id == "main"):
            dir = tm_float
            tm_float = tm_float + 1
            self.floats[dir] = var
            return dir
        elif( tipo == "bool" and varsTable.func_id == "main"):
            dir = tm_bools
            tm_bools = tm_bools + 1
            self.bools[dir] = var
            return dir
        elif( tipo == "string" and varsTable.func_id == "main"):
            dir = tm_books
            tm_books = tm_books + 1
            self.strings[dir] = var
            return dir
        elif( tipo == "int" and varsTable.func_id != "main"):
            dir = tl_int
            tl_int = tl_int + 1
            self.ints[dir] = var
            return dir
        elif( tipo == "float" and varsTable.func_id != "main"):
            dir = tl_float
            tl_float = tl_float + 1
            self.floats[dir] = var
            return dir
        elif( tipo == "bool" and varsTable.func_id != "main"):
            dir = tl_bools
            tl_bools = tl_bools + 1
            self.bools[dir] = var
            return dir
        elif( tipo == "string" and varsTable.func_id != "main"):
            dir = tl_string
            tl_string = tl_string + 1
            self.strings[dir] = var
            return dir

    def show(self):
        print("memoria int ",self.ints, " memoria float ",self.floats, " memoria bools ",self.bools," memoria string ",self.strings)


global_memroy = Memory()

def Reiniciar():
    global loc_int
    global loc_float
    global loc_bools
    global loc_string
    global tl_int
    global tl_float
    global tl_string
    global tl_bools
    loc_int = 1000
    loc_float = 1100
    loc_string = 1200
    loc_bools = 1300
    tl_int = 6000
    tl_float = 6100
    tl_string = 6200
    tl_bools = 6300

def BorrarInts():
    arr = []
    for key in global_memroy.ints:
        if((key >= 1000 and key <= 1099) or (key >= 6000 and key <= 6099)):
            arr.append(key)
    for i in arr:
        val = arr.pop()
        del global_memroy.ints[val]

def BorrarFloats():
    arr = []
    for key in global_memroy.floats:
        if((key >= 1100 and key <= 1199) or (key >= 6100 and key <= 6199)):
            arr.append(key)
    for i in arr:
        val = arr.pop()
        del global_memroy.floats[val]

def BorrarBools():
    arr = []
    for key in global_memroy.bools:
        if((key >= 1300 and key <= 1399) or (key >= 6200 and key <= 6299)):
            arr.append(key)
    for i in arr:
        val = arr.pop()
        del global_memroy.bools[val]

def BorrarStrings():
    arr = []
    for key in global_memroy.strings:
        if((key >= 1200 and key <= 1299) or (key >= 6300 and key <= 6399)):
            arr.append(key)
    for i in arr:
        val = arr.pop()
        del global_memroy.strings[val]

def Imprimirlocales():
    for i in local_memory:
        local_memory[i].show()

def GetDir(val,tipo):
    if tipo == "int":
        for i,y in global_memroy.ints.items():
            if (y == val and i >= 4000 and i < 4100):
                return i
    elif tipo == "float":
        for i,y in global_memroy.floats.items():
            if (y == val and i >= 4100 and i < 4200):
                return i
    elif tipo == "string":
        for i,y in global_memroy.strings.items():
            if (y == val and i >= 4200 and i < 4300):
                return i
    elif tipo == "bool":
        for i,y in global_memroy.bools.items():
            if (y == val and i >= 4300 and i < 4300):
                return i
    else:
        print("No existe")

def getValor(dir):
    if((dir >= 1000 and dir < 1100) or (dir >= 2000 and dir < 2100 ) or (dir >= 3000 and dir < 3100) or (dir >= 4000 and dir < 4100) or (dir >= 5000 and dir < 5100) or (dir >= 6000 and dir < 6100)):
        valor = global_memroy.ints[dir]
        return valor
    elif((dir >= 1100 and dir < 1200) or (dir >= 2100 and dir < 2200 ) or (dir >= 3100 and dir < 3200) or (dir >= 4100 and dir < 4200) or (dir >= 5100 and dir < 5200) or (dir >= 6100 and dir < 6200)):
        valor = global_memroy.floats[dir]
        return valor
    elif((dir >= 1200 and dir < 1300) or (dir >= 2200 and dir < 2300 ) or (dir >= 3200 and dir < 3300) or (dir >= 4200 and dir < 4300) or (dir >= 5200 and dir < 5300) or (dir >= 6200 and dir < 6300)):
        valor = global_memroy.strings[dir]
        return valor
    elif((dir >= 1300 and dir < 1400) or (dir >= 2300 and dir < 2400 ) or (dir >= 3300 and dir < 3400) or (dir >= 4300 and dir < 4400) or (dir >= 5300 and dir < 5400) or (dir >= 6300 and dir < 6400)):
        valor = global_memroy.bools[dir]
        return valor

def updateVal(dir,valor):
    if((dir >= 1000 and dir < 1100) or (dir >= 2000 and dir < 2100 ) or (dir >= 3000 and dir < 3100) or (dir >= 4000 and dir < 4100) or (dir >= 5000 and dir < 5100) or (dir >= 6000 and dir < 6100)):
        global_memroy.ints[dir] = valor
        #print(dir,global_memroy.ints[dir])

    elif((dir >= 1100 and dir < 1200) or (dir >= 2100 and dir < 2200 ) or (dir >= 3100 and dir < 3200) or (dir >= 4100 and dir < 4200) or (dir >= 5100 and dir < 5200) or (dir >= 6100 and dir < 6200)):
        global_memroy.floats[dir] = valor
        #print(dir,global_memroy.floats[dir])

    elif((dir >= 1200 and dir < 1300) or (dir >= 2200 and dir < 2300 ) or (dir >= 3200 and dir < 3300) or (dir >= 4200 and dir < 4300) or (dir >= 5200 and dir < 5300) or (dir >= 6200 and dir < 6300)):
        global_memroy.strings[dir] = valor
        #print(dir,global_memroy.strings[dir])

    elif((dir >= 1300 and dir < 1400) or (dir >= 2300 and dir < 2400 ) or (dir >= 3300 and dir < 3400) or (dir >= 4300 and dir < 4400) or (dir >= 5300 and dir < 5400) or (dir >= 6300 and dir < 6400)):
        global_memroy.bools[dir] = valor
        #print(dir,global_memroy.bools[dir])
