import ply.yacc as yacc
import ply.lex as lex
import sys
import varsTable as varsTable
import cuadruplos as cuadruplos

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
}

# List of tokens
tokens = [
    'ID',
    'CTE_I',
    'CTE_F',
  	'CTE_B',
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
  	"RETURN"
]

# Arithmetic Operators
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'

# Comparison Operators
t_EQUAL = r'\='
t_SAME = r'\=='
t_DIFFERENT = r'\[!=]'
t_LOWERTHAN = r'\<'
t_MORETHAN = r'\>'
t_MOREEQ = r'\[>=]'
t_LOWEREQ = r'\[<=]'

# Logic Operators
t_OR = r'\[|=]'
t_AND = r'\[&&]'

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
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CTE_I(t):
    r'\d+'
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
archivo = "prueba.txt"
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
  	program : PROGRAM COLON program2 MAIN mainc
    	| PROGRAM COLON bloq
        | PROGRAM COLON
  '''

def p_program2(p):
  '''
  	program2 : crear program2
    	| crear
  '''

def p_crear(p):
  '''
  	crear : var
    	| vector
        | func
  '''

def p_var(p):
  '''
  	var : VAR tipo ID SEMICOLON
  '''
  varsTable.var_id = p[3]
  if(varsTable.is_local):
      varsTable.insertVarInFunc(varsTable.var_tipo, varsTable.var_id)
  else:
      varsTable.insert(varsTable.var_tipo, varsTable.var_id)

def p_tipo(p):
  '''
  	tipo : INT
    	| FLOAT
        | STRING
        | BOOL
  '''
  varsTable.var_tipo = p[1]

def p_vector(p):
  '''
  	vector : VECTOR ID LBRACE CTE_I RBRACE SEMICOLON
  '''
  varsTable.var_id = p[1]
  varsTable.var_space = p[4]

def p_func(p):
  '''
  	func : FUNCTION functype ID addInTable LPAREN funci RPAREN localvar bloq return
    | FUNCTION functype ID addInTable LPAREN funci RPAREN bloq return
  '''
  varsTable.func_id = p[3]
  varsTable.is_local = False


def p_functype(p):
  '''
  	functype : INT
    | FLOAT
    | STRING
    | BOOL
    | VOID
  '''
  varsTable.func_tipo = p[1]

def p_addInTable(p):
    '''
    addInTable :
    '''
    varsTable.is_local = True
    varsTable.func_id = p[-1]
    varsTable.insert(varsTable.func_tipo, varsTable.func_id)


def p_funci(p):
  '''
    funci : tipo ID
    | tipo ID COMA funci
    | empty
  '''


def p_localvar(p):
     '''
     localvar : var
     | vector
     | var localvar
     | vector localvar
     '''

def p_return(p):
    '''
    return : RETURN expres
    | empty
    '''

def p_mainc(p):
    '''
    mainc : LKEY bloq RKEY
    | LKEY mainc2 bloq RKEY
    '''
    varsTable.is_main = True



def p_mainc2(p):
    '''
    mainc2 : var
    | var mainc2
    '''

def p_bloq(p):
    '''
  	 bloq : bloqi
    '''

def p_bloqi(p):
  '''
  	bloqi : estat
        | estat bloqi
  '''

def p_estat(p):
  '''
  	estat : asign
        | cond
        | escrit
        | ciclo
        | leer
  '''

def p_asign(p):
  '''
    asign : ID pushid EQUAL pushop expres resolverasignacion SEMICOLON
        | ID pushid LBRACE exr RBRACE EQUAL pushop expres SEMICOLON
  '''

def p_cond(p):
  '''
    cond : IF LPAREN expres RPAREN LKEY bloq RKEY
        | IF LPAREN expres RPAREN LKEY bloq RKEY ELSE LKEY bloq RKEY
  '''

def p_escrit(p):
  '''
    escrit : PRINT LPAREN escriti RPAREN SEMICOLON
  '''

def p_escriti(p):
  '''
  	escriti : expres
    	| expres COMA escriti
  '''

def p_ciclo(p):
  '''
    ciclo : WHILE LPAREN expres RPAREN LKEY bloq RKEY
  '''

def p_leer(p):
  '''
  	leer : READ LPAREN ID RPAREN SEMICOLON
  '''

def p_expres(p):
  '''
  expres : exr
        | exr log expres
  '''

def p_exr(p):
  '''
  	exr : ex
    	| ex reslog rel exr
  '''

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
  	fact : LPAREN pushop expres RPAREN pushop
        | var_cte
        | PLUS var_cte
        | MINUS var_cte
  '''

def p_rel(p):
  '''
  	rel : LOWERTHAN pushop
    	| MORETHAN pushop
        | LOWEREQ pushop
        | MOREEQ pushop
        | SAME pushop
        | DIFFERENT pushop
  '''

def p_log(p):
  '''
  	log : OR
        | AND
  '''

def p_var_cte(p):
  '''
  	var_cte : ID pushid
        | CTE_I pushcte
        | CTE_F pushcte
        | CTE_B pushcte
        | CTE_S pushcte
        | fcall
        | vcall
  '''

def p_fcall(p):
  '''
  	fcall : ID LPAREN fcall1 RPAREN
        | ID LPAREN RPAREN
  '''

def p_fcall1(p):
  '''
  	fcall1 : expres
        | expres COMA fcall1
  '''

def p_vcall(p):
  '''
  	vcall : ID LBRACE expres RBRACE
  '''

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

def p_resolverasignacion(p):
    "resolverasignacion :"
    res = cuadruplos.resolverasignacion()
    varsTable.update(p[-5],res)

def p_resfact(p):
    "resfact :"
    cuadruplos.resolverfact()

def p_resterm(p):
    "resterm :"
    cuadruplos.resolverterm()

def p_reslog(p):
    "reslog :"
    cuadruplos.resolverlog()


parser = yacc.yacc()

archivo = "prueba.txt"
f = open(archivo, 'r')
s = f.read()

parser.parse(s)

if success == True:
    print("Archivo aprobado")
    #sys.exit()
else:
    print("Archivo no aprobado")
    #sys.exit()
print

varsTable.show();
