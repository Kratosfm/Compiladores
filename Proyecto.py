import ply.yacc as yacc
import ply.lex as lex
import sys
import symbol_table as symbol_table

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
}

# List of tokens
tokens = [
    'ID',
    'CTE_I',
    'CTE_F',
  	'CTE_B',
    'CTE_S',
    'CTE_STRING',
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
#t_CTE_STRING = r'\"([^\\\n]|(\\.))*?\"'
t_CTE_STRING = r'\[a-zA-Z][a-zA-Z0-9]*'

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

# def p_program(p):
#    '''program : PROGRAM ID COLON crear bloque
#               | PROGRAM ID COLON bloque'''

def p_program(p):
  '''
  	program : PROGRAM ID COLON program2 bloq
    	| PROGRAM ID COLON bloq
        | PROGRAM ID COLON
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
  symbol_table.insert(symbol_table.vart,p[3])

def p_tipo(p):
  '''
  	tipo : INT
    	| FLOAT
        | STRING
        | BOOL
  '''
  symbol_table.vart = p[1]

def p_vector(p):
  '''
  	vector : VECTOR ID LBRACE CTE_I RBRACE SEMICOLON
  '''

def p_func(p):
  '''
  	func : FUNCTION functype ID LPAREN funci RPAREN bloq
    | FUNCTION functype ID LPAREN funci RPAREN bloq RETURN expres
  '''

def p_functype(p):
  '''
  	functype : tipo
    | VOID
  '''

def p_funci(p):
  '''
    funci : tipo ID
    | tipo ID COMA funci
  '''

def p_bloq(p):
  '''
  	bloq : LKEY bloqi RKEY
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
    asign : ID EQUAL expres SEMICOLON
        | ID LBRACE exr RBRACE EQUAL expres SEMICOLON
  '''
  symbol_table.update(p[1],symbol_table.vart)

def p_cond(p):
  '''
    cond : IF LPAREN expres RPAREN bloq
        | IF LPAREN expres RPAREN bloq ELSE bloq
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
    ciclo : WHILE LPAREN expres RPAREN bloq
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
    	| ex rel exr
  '''

def p_ex(p):
  '''
  	ex : term
    	| term PLUS ex
    	| term MINUS ex
  '''

def p_term(p):
  '''
  	term : fact
    	| fact TIMES term
        | fact DIVIDE term
  '''

def p_fact(p):
  '''
  	fact : LPAREN expres RPAREN
        | fact1
  '''

def p_fact1(p):
  '''
  	fact1 : PLUS var_cte
        | MINUS var_cte
        | var_cte
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

def p_log(p):
  '''
  	log : OR
        | AND
  '''

def p_var_cte(p):
  '''
  	var_cte : ID
        | CTE_I
        | CTE_F
        | CTE_B
        | CTE_S
        | fcall
        | vcall
  '''
  symbol_table.vart = p[1]

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

def p_error(p):
    global success
    success = False
    print("Error de sintaxis en '%s'" % p.value)
    sys.exit()

parser = yacc.yacc()

archivo = "prueba.txt"
f = open(archivo, 'r')
s = f.read()

parser.parse(s)

if success == True:
    print("Archivo aprobado12")
    #sys.exit()
else:
    print("Archivo no aprobado")
    #sys.exit()
