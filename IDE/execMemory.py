class Memory:

    def __init__(self):
        self.ints = {}
        self.floats = {}
        self.bools = {}
        self.strings = {}

    def insert(self, var, dir):
        if( str(type(var)) == "<class 'int'>" ):
            self.ints[dir] = var
        if( str(type(var)) == "<class 'float'>" ):
            self.floats[dir] = var
        if( str(type(var)) == "<class 'bool'>" ):
            self.bools[dir] = var
        if( str(type(var)) == "<class 'str'>" ):
            self.strings[dir] = var
        return

    def look(self, var, dir):
        if( str(type(var)) == "<class 'int'>" ):
            self.ints[dir] = var
        if( str(type(var)) == "<class 'float'>" ):
            self.floats[dir] = var
        if( str(type(var)) == "<class 'bool'>" ):
            self.bools[dir] = var
        if( str(type(var)) == "<class 'str'>" ):
            self.strings[dir] = var
        return

    def delete(self):
        self.ints = {}
        self.floats = {}
        self.bools = {}
        self.strings = {}
        return

    def show(self):
        print(self.ints, self.floats, self.bools,self.strings)

main_memory = Memory()
global_memroy = Memory()
local_memory = memory()

mmy = Memory()
integer = 1
floats = 4.5
bools = False
bools2 = True
strings = "ALV"
mmy.insert(integer, 10)
mmy.insert(floats, 20)
mmy.insert(bools, 30)
mmy.insert(bools2, 31)
mmy.insert(strings, 40)
mmy.show()
mmy.delete()
mmy.show()