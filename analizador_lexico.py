import ply.lex as lex

resultado_lexema = []

palabra_reservada = (
    # Variables Reservadas
    'INCLUDE',
    'CADENA',
    'RETURN',
    'VOID',
    'INT',
    'IF',
    'ELSE',
    'WHILE',
    'FOR',
    'DO',
    'SWITCH',
    'CASE'
)
tokens = palabra_reservada + (
    'IDENTIFICADOR',
    'ENTERO',
    'ASIGNAR',
    'MASIGUAL',
    'MENORIGUAL',
    'PORIGUAL',
    'ENTREIGUAL',

    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POTENCIA',
    'MODULO',

    'DECREMENTO',
    'INCREMENTO',

    'AND',
    'OR',
    'NOT',
    'MENORQUE',
    'MENOR_O_IGUAL',
    'MAYORQUE',
    'MAYOR_O_IGUAL',
    'IGUAL',
    'DIFERENTE_DE',

    'NUMERAL',
    'PARENTESIS_ABRE',
    'PARENTESIS_CIERRA',
    'CORCHETE_ABRE',
    'CORCHETE_CIERRA',
    'LLAVE_ABRE',
    'LLAVE_CIERRA',
    'PUNTO_COMA',
    'COMA',
    'DOS_PUNTOS',
    'COMILLA_DOBLE',
    'COMILLA_SIMPLE',
    'PUNTO'

)

# Operadores Aritmeticos
t_SUMA = r'\+'
t_RESTA = r'-'
t_DECREMENTO = r'\-\-'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'

# Asignacion
t_ASIGNAR = r'='
t_MASIGUAL = r'\+='
t_MENORIGUAL = r'-='
t_PORIGUAL = r'\*='
t_ENTREIGUAL = r'/='

# Operadores Logicos
t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'

# Operadores Relacionales
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_MAYOR_O_IGUAL = r'>='
t_MENOR_O_IGUAL = r'<='
t_IGUAL = r'=='
t_DIFERENTE_DE = r'!='

# Simbolos Especiales
t_PUNTO_COMA = ';'
t_COMA = r','
t_PARENTESIS_ABRE = r'\('
t_PARENTESIS_CIERRA = r'\)'
t_CORCHETE_ABRE = r'\['
t_CORCHETE_CIERRA = r'\]'
t_LLAVE_ABRE = r'{'
t_LLAVE_CIERRA = r'}'
t_COMILLA_DOBLE = r'"'
t_COMILLA_SIMPLE = r'\''
t_PUNTO = r'\.'
t_DOS_PUNTOS = r'\:'
t_NUMERAL = r'\#'


def t_INCLUDE(t):
    r'\#include\s+<\w+(\.\w)?>'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_IF(t):
    r'if\(\w+(\[\w+\])?\s+?(==|!=|<|>|<=|>=)\s+?\w+(\[\w+\])?\)'
    return t

def t_RETURN(t):
   r'return'
   return t

def t_VOID(t):
   r'void'
   return t

def t_WHILE(t):
    r'while'
    return t

def t_FOR(t):
    r'for'
    return t

def t_DO(t):
    r'do'
    return t

def t_SWITCH(t):
    r'switch'
    return t

def t_CASE(t):
    r'case'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t

def t_CADENA(t):
   r'\"?(\w+ \ *\w*\d* \ *)\"?'
   return t

def t_INCREMENTO(t):
    r'\+\+'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    print("Comentario de multiple linea")

def t_comments_ONELine(t):
     r'\/\/(.)*\n'
     t.lexer.lineno += 1
     print("Comentario de una linea")
t_ignore =' \t'

def t_error( t):
    global resultado_lexema
    estado = "** Error, Token no valido en la Linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value),
                                                                      str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)

# Prueba de ingreso
def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        
        estado = "Linea {:4}   Tipo {:16}      Valor {:16}   Posicion {:4}".format(str(tok.lineno),str(tok.type) ,str(tok.value), str(tok.lexpos) )
        resultado_lexema.append(estado)
    return resultado_lexema

analizador = lex.lex()

