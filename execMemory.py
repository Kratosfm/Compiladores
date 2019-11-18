import pprint

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

class Memory:

    def __init__(self,name):
        self.name = name
        self.ints = {}
        self.floats = {}
        self.bools = {}
        self.strings = {}

    def insert(self, var,dir):
        if( str(type(var)) == "<class 'int'>" ):
            self.ints[dir] = var
        if( str(type(var)) == "<class 'float'>" ):
            self.floats[dir] = var
        if( str(type(var)) == "<class 'bool'>" ):
            self.bools[dir] = var
        if( str(type(var)) == "<class 'str'>" ):
            self.strings[dir] = var
        return

    def insert_global(self, var, tipo):
        global global_int
        global global_float
        global global_string
        global global_bools
        if( tipo == "int"):
            dir = global_int
            global_int = global_int + 1
            self.ints[dir] = var
            return dir
        if( tipo == "float" ):
            dir = global_float
            global_float = global_float + 1
            self.floats[dir] = var
            return dir
        if( tipo == "bool" ):
            dir = global_bools
            global_bools = global_bools + 1
            self.bools[dir] = var
            return dir
        if( tipo == "string" ):
            dir = global_string
            global_string = global_string + 1
            self.strings[dir] = var
            return dir

    def insert_main(self, var, tipo):
        global main_int
        global main_float
        global main_bools
        global main_string
        if( tipo == "int"):
            dir = main_int
            main_int = main_int + 1
            self.ints[dir] = var
            return dir
        if( tipo == "float" ):
            dir = main_float
            main_float = main_float + 1
            self.floats[dir] = var
            return dir
        if( tipo == "bool" ):
            dir = main_bools
            main_bools = main_bools + 1
            self.bools[dir] = var
            return dir
        if( tipo == "string" ):
            dir = main_string
            main_string = main_string + 1
            self.strings[dir] = var
            return dir

    def insert_local(self, var, tipo):
        global loc_int
        global loc_float
        global loc_bools
        global loc_string
        if( tipo == "int"):
            dir = loc_int
            loc_int = loc_int + 1
            self.ints[dir] = var
            return dir
        if( tipo == "float" ):
            dir = loc_float
            loc_float = loc_float + 1
            self.floats[dir] = var
            return dir
        if( tipo == "bool" ):
            dir = loc_bools
            loc_bools = loc_bools + 1
            self.bools[dir] = var
            return dir
        if( tipo == "string" ):
            dir = loc_string
            loc_string = loc_string + 1
            self.strings[dir] = var
            return dir

    def delete(self):
        self.ints = {}
        self.floats = {}
        self.bools = {}
        self.strings = {}
        return

    def show(self):
        print("memoria int ",self.ints, " memoria float ",self.floats, " memoria bools ",self.bools," memoria string ",self.strings)

main_memory = Memory("main")
global_memroy = Memory("global")
local_memory = {}
cte_memory = Memory("cte")

def Reiniciar():
    print("hola")
    global loc_int
    global loc_float
    global loc_bools
    global loc_string
    loc_int = 1000
    loc_float = 1100
    loc_string = 1200
    loc_bools = 1300

def Imprimirlocales():
    for i in local_memory:
        local_memory[i].show()
