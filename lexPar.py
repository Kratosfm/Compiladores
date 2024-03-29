import ply.yacc as yacc
import ply.lex as lex
import sys
import varsTable as varsTable
import cuadruplos as cuadruplos
import execMemory as Memoria
import VM as Virtual

success = True

reserved = {
    'program' : 'PROGRAM',
    'var' : 'VAR',
    'function' : 'FUNCTION',
    'if' : 'IF' ,
    'else' : 'ELSE',
    'int' : 'INT',
    'float' : 'FLOAT',
    'string' : 'STRING',
    'bool' : 'BOOL',
    'print' : 'PRINT',
    'vector' : 'VECTOR',
  	'while' : 'WHILE',
    'read' : 'READ',
    'void' : 'VOID',
    'main' : 'MAIN',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'return' : 'RETURN',
    'find' : 'FIND',
    'sort' : 'SORT'
}

# List of tokens
tokens = [
    'ID',
    'CTE_I',
    'CTE_F',
    'CTE_S',
    #'CTE_STRING',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUAL',
  	'SAME',
    "DIFFERENT",
    'LOWERTHAN',
    'MORETHAN',
    'LOWEREQ',
    'MOREEQ',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LKEY',
    'RKEY',
    'COMA',
    "SEMICOLON",
    'AND',
    'OR',
    "COLON",
]

# Arithmetic Operators
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'

# Comparison Operators
t_EQUAL = r'\='
t_SAME = r'\=='
t_DIFFERENT = r'\!='
t_LOWERTHAN = r'\<'
t_MORETHAN = r'\>'
t_MOREEQ = r'\>='
t_LOWEREQ = r'\<='

# Logic Operators
t_OR = r'\|='
t_AND = r'\&&'

# Symbols
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\['
t_RBRACE = r'\]'
t_LKEY = r'\{'
t_RKEY = r'\}'
t_COMA = r'\,'
t_SEMICOLON = r'\;'
t_COLON = r'\:'

# Constants
#t_CTE_I = r'[0-9]+'
#t_CTE_F = r'[0-9]+\.[0-9]+'
t_CTE_S = r'\"([^\\\n]|(\\.))*?\"'
#t_CTE_STRING = r'\[a-zA-Z][a-zA-Z0-9]*'

tokens = tokens + list(reserved.values())

def t_CTE_F(t):
    r'[+-]?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CTE_I(t):
    r'[+-]?\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

'''def t_CTE_STRING(t):
    r'\"([^\\\n]|(\\(.|\n)))*?\"'
    t.value = str(t.value)
    return t'''


# Caracteres ignorados
t_ignore = ' \t\n'

def t_error(t):
    global success
    success = False
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)
    #print("entre aqui")

# Construye el lexer
lexer = lex.lex()
archivo = "prueba2.txt"
fopen = open(archivo, 'r')
abrir = fopen.read()
lexer.input(abrir)

list_tok = []

while True:
    tok = lexer.token()
    if not tok:
        break
    #print(tok)
    list_tok.append(tok)

def p_program(p):
  '''
  	program : PROGRAM COLON gotomain global program2 finglobal program3 llenarmain MAIN main1 mainc finmain
        | PROGRAM COLON gotomain global program2 finglobal llenarmain MAIN main1 mainc finmain
        | PROGRAM COLON gotomain global finglobal program3 llenarmain MAIN main1 mainc finmain
        | PROGRAM COLON gotomain llenarmain MAIN main1 mainc finmain
  '''
  cuad = cuadruplos.Cuadrupl(None, None, None, "ENDPROGRAM", len(cuadruplos.pilacuadruplos))
  cuadruplos.pilacuadruplos.append(cuad)

def p_gotomain(p):
    "gotomain :"
    cuadruplos.gotoMain()

def p_program2(p):
  '''
  	program2 : crear program2
    	| crear
  '''

def p_program3(p):
  '''
  	program3 : function program3
    	| function
  '''

def p_llenarmain(p):
    "llenarmain :"
    cuadruplos.fill(0, len(cuadruplos.pilacuadruplos))

def p_crear(p):
  '''
  	crear : var
    	| vector
  '''

def p_global(p):
    "global :"
    varsTable.exist_GLOBAL = True
    varsTable.is_global = True
    varsTable.func_id = "global"
    varsTable.insert(None, "global")

def p_finglobal(p):
  "finglobal :"
  varsTable.is_global = False

def p_main1(p):
    "main1 :"
    varsTable.is_main = True
    varsTable.func_id = "main"
    varsTable.insert(None, "main")

def p_finmain(p):
    "finmain :"
    varsTable.is_main = False

def p_var(p):
  '''
  	var : VAR tipo ID SEMICOLON
  '''
  #print("Meter var")
  if varsTable.is_global:
      varsTable.insertVarInFunc(varsTable.var_tipo,p[3], "global")
  elif varsTable.is_main:
      varsTable.insertVarInFunc(varsTable.var_tipo,p[3], "main")
  elif varsTable.is_local:
      varsTable.insertVarInFunc(varsTable.var_tipo, p[3], varsTable.func_id)
#      print("aqui yace una var main")''

def p_tipo(p):
  '''
  	tipo : INT
    	| FLOAT
        | STRING
        | BOOL
  '''
  varsTable.var_tipo = p[1]
  p[0] = p[1]

def p_vector(p):
  '''
  	vector : VECTOR initvector tipo ID LBRACE CTE_I RBRACE SEMICOLON
  '''
  varsTable.insertVarInFunc(p[3],p[4], "global",p[6])
  varsTable.symbol_table["global"].dict[p[4]].isVector = True
  varsTable.is_vector = False

def p_initvector(p):
    "initvector :"
    varsTable.is_vector = True

def p_function(p):
  '''
  	function : FUNCTION functype ID addInTable LPAREN funci RPAREN LKEY localvar bloq return1 RKEY
    | FUNCTION functype ID addInTable LPAREN funci RPAREN LKEY bloq return1 RKEY
    | FUNCTION pushvoid ID addInTable LPAREN funci RPAREN LKEY localvar bloq RKEY
    | FUNCTION pushvoid ID addInTable LPAREN funci RPAREN LKEY bloq RKEY
    | FUNCTION functype ID addInTable LPAREN RPAREN LKEY localvar RKEY
    | FUNCTION pushvoid ID addInTable LPAREN RPAREN LKEY localvar RKEY
    | FUNCTION functype ID addInTable LPAREN RPAREN LKEY localvar bloq return1 RKEY
    | FUNCTION pushvoid ID addInTable LPAREN RPAREN LKEY localvar bloq RKEY
    | FUNCTION pushvoid ID addInTable  LPAREN RPAREN LKEY bloq RKEY
    | FUNCTION functype ID addInTable LPAREN RPAREN LKEY bloq return1 RKEY
    | FUNCTION functype ID addInTable LPAREN RPAREN LKEY RKEY
  '''
  #  print("lala", len(varsTable.param_table[varsTable.func_id].dict))
  #varsTable.ImprimirParamsType()
  varsTable.is_local = False
  #varsTable.ImprimirLcalTable(varsTable.func_id)
  #Memoria.global_memroy.show()  #eliminar esta
  #varsTable.ImprimirLcalTable(p[3])
  Memoria.Reiniciar()
  Memoria.BorrarInts()
  Memoria.BorrarFloats()
  Memoria.BorrarBools()
  Memoria.BorrarStrings()

  varsTable.param_cont = 0
  #cuadruplos.CrearENDPROC()
  cuad = cuadruplos.Cuadrupl(None, "ENDPROC", None, None, len(cuadruplos.pilacuadruplos))
  cuadruplos.pilacuadruplos.append(cuad)

#Tipo de funciones
def p_functype(p):
  '''
  	functype : INT
    | FLOAT
    | STRING
    | BOOL
  '''
  varsTable.func_tipo = p[1]

def p_pushvoid(p):
  '''
  	pushvoid : VOID
  '''
  varsTable.func_tipo = p[1]

#añade la funcion a la varstable
def p_addInTable(p):
    '''
    addInTable :
    '''
    varsTable.is_local = True
    varsTable.func_id = p[-1]
    varsTable.insert(varsTable.func_tipo, varsTable.func_id)
    varsTable.InsertParam(varsTable.func_id)
    varsTable.symbol_table[varsTable.func_id].cuadno = len(cuadruplos.pilacuadruplos)
#Creacion de los parametros
def p_funci(p):
  '''
    funci : tipo ID sumparam
    | tipo ID sumparam COMA funci
  '''
  varsTable.insertVarInFunc(p[1],p[2],varsTable.func_id)
  varsTable.InsertTypParam(p[1])
  varsTable.symbol_table[varsTable.func_id].dict[p[2]].isParam = True
#Tipo de los parametros de funciones
def p_localvar(p):
     '''
     localvar : var
     | vector
     | var localvar
     | vector localvar
     '''

def p_sumparam(p):
     '''
     sumparam :
     '''
     varsTable.param_cont = varsTable.param_cont + 1
     varsTable.symbol_table[varsTable.func_id].paramno = varsTable.param_cont

def p_return1(p):
    '''
    return1 : RETURN pushop expres resreturn SEMICOLON
    | empty
    '''
    cuadruplos.generateReturn()

def p_resreturn(p):
    '''
    resreturn :
    '''
    #print (str(cuadruplos.pilaid)[1:-1])
def p_mainc(p):
    '''
    mainc : LKEY RKEY
    | LKEY localvar bloq RKEY
    | LKEY localvar RKEY
    | LKEY bloq RKEY
    '''

def p_bloq(p):
    '''
  	 bloq : estat
         | estat bloq
    '''

def p_estat(p):
  '''
  	estat : asign
        | cond
        | escrit
        | ciclo
        | leer
        | fcallvoid
        | findvec
        | sorti

  '''

def p_asign(p):
  '''
    asign : ID pushid EQUAL pushop fcall SEMICOLON
        | ID pushid EQUAL pushop expres resolverasignacion SEMICOLON
        | asigvector EQUAL pushop expres resasignvec SEMICOLON
        | ID pushid EQUAL pushop resasignvec SEMICOLON
        | asigvector EQUAL pushop asigvector resasignvec SEMICOLON
  '''

def p_cond(p):
  '''
    cond : IF LPAREN expres RPAREN LKEY resif bloq RKEY finif
        | IF LPAREN expres RPAREN LKEY resif bloq RKEY ELSE LKEY reselse bloq RKEY finif
  '''

def p_escrit(p):
  '''
    escrit : PRINT pushop LPAREN escriti RPAREN SEMICOLON
  '''

def p_escriti(p):
  '''
  	escriti : expres escrit1
    	| expres escrit2 COMA escriti
  '''

def p_escrit1(p):
    '''
    escrit1 :
    '''
    cuadruplos.printcuad()

def p_escrit2(p):
    '''
    escrit2 :
    '''
    cuadruplos.printcuad()
    cuadruplos.pushPoper("print")

def p_ciclo(p):
  '''
    ciclo : WHILE while1 LPAREN expres RPAREN while2 LKEY bloq RKEY while3
  '''

def p_leer(p):
  '''
  	leer : READ pushop LPAREN ID pushid RPAREN readid SEMICOLON
  '''

def p_readid(p):
  '''
  	readid :
  '''
  cuadruplos.readid()

def p_expres(p):
  '''
  expres : exr
        | exr log expres reslog
  '''


def p_exr(p):
  '''
  	exr : ex
    	| ex rel exr resrel
  '''

def p_reslog(p):
    '''
    reslog :
    '''
    cuadruplos.ResolverLog()

def p_ex(p):
  '''
  	ex : term resterm
    	| term resterm PLUS pushop ex
    	| term resterm MINUS pushop ex
  '''

def p_term(p):
  '''
  	term : fact resfact
    	| fact resfact TIMES pushop term
        | fact resfact DIVIDE pushop term
  '''

def p_fact(p):
  '''
  	fact : LPAREN pushop expres RPAREN popop
        | var_cte
        | PLUS pushop var_cte
        | MINUS pushop var_cte
  '''

def p_rel(p):
  '''
  	rel : LOWERTHAN
    	| MORETHAN
        | LOWEREQ
        | MOREEQ
        | SAME
        | DIFFERENT
  '''
  #print(p[1])
  cuadruplos.pushPoper(p[1])

def p_log(p):
  '''
  	log : OR
        | AND
  '''
  cuadruplos.pushPoper(p[1])

def p_var_cte(p):
  '''
  	var_cte : ID pushid
        | CTE_I pushcte
        | CTE_F pushcte
        | CTE_S pushcte
        | TRUE pushcte
        | FALSE pushcte
        | asigvector
  '''

def p_findvec(p):
    '''findvec : FIND pushop LPAREN ID LBRACE ex RBRACE RPAREN SEMICOLON
    '''
    cuadruplos.generateFind(p[4])

def p_sorti(p):
    '''sorti : SORT pushop LPAREN ID LBRACE RBRACE RPAREN SEMICOLON
    '''
    cuadruplos.generateSort(p[4])

def p_asigvector(p):
    '''
    asigvector : ID pushid LBRACE pushop ex RBRACE verificatam popop
    '''
    #print("valores",cuadruplos.pilaVal)
    #print("operadores",cuadruplos.popper)
    #print("id",cuadruplos.pilaid)
    #print("tipos",cuadruplos.pilaTipos)

def p_verifictam(p):
    '''
    verificatam :
    '''
    cuadruplos.vector_id = p[-6]
    cuadruplos.Verificartam()

def p_fcall(p):
  '''
  	fcall : ID existfunc LPAREN startera fcall1 RPAREN
        | ID existfunc LPAREN startera RPAREN
  '''
  varsTable.param_cont = 0
  cuadruplos.generategosub(p[1])
  cuadruplos.funcasign(p[1])
  varsTable.UpdateParam()
  varsTable.arrparam.clear()
  varsTable.fun_name = None

def p_fcallvoid(p):
    '''
    fcallvoid : ID existfunc LPAREN startera fcall1 RPAREN SEMICOLON
    | ID existfunc LPAREN startera RPAREN SEMICOLON
    '''
    varsTable.param_cont = 0
    cuadruplos.generategosub(p[1])
    varsTable.UpdateParam()
    varsTable.arrparam.clear()
    varsTable.fun_name = None

#Funcion que llama a CheckExistIdFunc para verificar que exista la funcion en la tabla
def p_existfunc(p):
    '''existfunc :'''
    existe = varsTable.CheckExistIdFunc(p[-1])
    if(existe == True):
        varsTable.fun_name = p[-1]
    else:
        print("funcion no declarada")
        sys.exit()
#Funcion que manda a llamar funcion para crear el cuadruplo de era
def p_startera(p):
    '''startera :'''
    cuadruplos.generateEra(p[-3])

def p_fcall1(p):
  '''
  	fcall1 : expres generateparam
        | expres generateparam COMA fcall1
  '''
  if varsTable.param_cont == varsTable.param_table[varsTable.fun_name].num:
      print("")
  else:
      print("Num de var no coinciden")
      sys.exit()

def p_generateparam(p):
    "generateparam :"
    #Paso 4 de Module Call
    varsTable.param_cont = varsTable.param_cont + 1
    val = cuadruplos.getparam()
    varsTable.arrparam.append(val)

def p_empty(p):
    '''
    empty :
    '''
    pass

def p_error(p):
    global success
    success = False
    print("Error de sintaxis en '%s'" % p.value)
    sys.exit()

def p_pushcte(p):
    "pushcte :"
    cuadruplos.pushCTE(p[-1])

def p_pushid(p):
    "pushid :"
    cuadruplos.pushID(p[-1])

def p_pushop(p):
    "pushop :"
    cuadruplos.pushPoper(p[-1])

def p_popop(p):
    "popop :"
    cuadruplos.popper.pop()

def p_resolverasignacion(p):
    "resolverasignacion :"
    res = cuadruplos.resolverasignacion()
    if(res == 'true'):
        resb = bool(res)
        varsTable.update(p[-5],resb)
    elif(res == 'false'):
        resb = bool()
        varsTable.update(p[-5],resb)
    else:
        varsTable.update(p[-5],res)

def p_resasignvec(p):
    "resasignvec :"
    cuadruplos.resolverasignacion()
    #name = p[-7]
    #pos = cuadruplos.pos_vect
    #print(res)
    #print ("dirrr", name,res,pos,dir)
    #if(res == 'true'):
    #    resb = bool(res)
    #    varsTable.update(dir,resb)
    #elif(res == 'false'):
    #    resb = bool()
    #    varsTable.update(dir,resb)
    #else:
    #    #print("RES",res)
    #    #varsTable.update(dir,res)
    #    Memoria.updateVal(dir,res)
    #    cuadruplos.pos_vect = 0


def p_resfact(p):
    "resfact :"
    cuadruplos.resolverfact()

def p_resterm(p):
    "resterm :"
    cuadruplos.resolverterm()

def p_resrel(p):
    "resrel :"
    cuadruplos.resolverRel()

def p_resif(p):
    "resif :"
    cuadruplos.ResolverCond()

def p_reselse(p):
    "reselse :"
    cuadruplos.ResElse()

def p_finif(p):
    "finif :"
    cuadruplos.finalif()

def p_while1(p):
    "while1 :"
    cuadruplos.while1()

def p_while2(p):
    "while2 :"
    cuadruplos.while2()

def p_while3(p):
    "while3 :"
    cuadruplos.while3()

parser = yacc.yacc()

archivo = "pruebas90.txt"
f = open(archivo, 'r')
s = f.read()

parser.parse(s)
print("")
if success == True:
    print("Archivo aprobado")
    #sys.exit()
else:
    print("Archivo no aprobado")
    #sys.exit()
cuadruplos.imprimirtodocuadr()
#print("memoria global ")
#Memoria.global_memroy.show()
varsTable.show();
print("")
print("VM")
#posicion = Virtual.GoToMain(0,cuadruplos.pilacuadruplos[0])
#Virtual.Ejecucion(posicion,cuadruplos.pilacuadruplos[posicion])
Virtual.programa()
#print("")
#print("Vars Table")
#varsTable.show();
#print("")
#print("Memoriac")
#Memoria.global_memroy.show()
