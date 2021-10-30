from enum import Enum

class Types(Enum):
      
    # Tipo de datos
    INT = "\\b(int)\\b.*"
    FLOAT = "\\b(float)\\b.*"
    STRING = "\\b(String)\\b.*"
    BOOLEAN = "\\b(Boolean)\\b.*"

    # Palabras reservadas
    RESERVED_WORD = "\\b(char|main|float|return|void|if|else|while)\\b.*"
    
    # A omitir
    SPACE = "( ).*"
    LINE_BREAK = "(\\n).*"
    COMENT_BLOCK = "(/\\*.*?\\*/).*"
    COMENT_LINE = "(//(.*?)[\r$]?\n).*"


    # Valores
    INT_VAL = "\\b(\\d{1,9})\\b.*"
    BOOLEAN_VAL = "\\b(true|false)\\b"
    FLOAT_VAL = "\\b(\\d{1,9}\\.\\d{1,16})\\b.*"
    
    # Id
    IDENTIFIER = "\\b([a-zA-Z]{1}[0-9a-zA-Z_]{0,31})\\b.*"
    CADENA_TEXTO = '\"(\\.|[^\\"])*\"'
    CARACTER = r"\'(\\.|[^\\'])*\'"
    APOSTROFE = "(').*"
    COMILLA = '(").*'

    # Simbolos
    OPENING_PARENTHESIS = "(\\().*"
    CLOSING_PARENTHESIS = "(\\)).*"
    OPENING_BRACKET = "(\\[).*"
    CLOSING_BRACKET = "(\\]).*"
    BLOCK_START = "(\\{).*"
    BLOCK_END = "(\\}).*"
    SEMICOLON = "(;).*"
    POINT = "(\\.).*"
    COMMA = "(,).*"

    # Operadores
    MULTIPLICATION = "(\\*).*"
    SUBTRACT = "(\\-{1}).*"
    NO_EQUAL = "(\\!=).*"
    ASIGNACION = "(=).*"
    DIVISION = "(/).*"
    SUM = "(\\+{1}).*"
    MODULO = "(%).*"
    EQUAL = "(==).*"
    MAYOR = "(>).*"
    MENOR = "(<).*"
    AND = "(&&).*"

    # end of file
    EOF = "(\$).*"

    # Error de sintaxis
    SYNTAX_ERROR = "(sfedr).*"
