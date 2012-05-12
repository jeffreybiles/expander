__author__ = 'jefferton'

import ply.lex as lex

tokens = (
    'START',
    'BETWEEN',
    'END',
    'STRING',
    )

t_START = r'\('
t_BETWEEN = r'\|'
t_END = r'\)'
t_STRING = r'\w+'

t_ignore = '\t\v\r' # whitespace

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
    print "JavaScript Lexer: Illegal character " + t.value[0]
    t.lexer.skip(1)

# We have included two test cases to help you debug your lexer. You will
# probably want to write some of your own.

lexer = lex.lex()

translation = {
    'START': '<div class="expander"><div class="expandable">',
    'BETWEEN': '</div><div class="expansion">',
    'END': '</div></div>'
}

def test_lexer(input_string):
    lexer.input(input_string)
    result = [ ]
    while True:
        tok = lexer.token()
        if not tok: break
        result = result + [tok.type,tok.value]
    return result

def make_web(input_string):
    lexer.input(input_string)
    result = ''
    while True:
        tok = lexer.token()
        if not tok: break
        if tok.type == 'STRING':
            result += tok.value
            result += ' '
        else:
            result += translation[tok.type]
    return result
input1 = 'hello (friend|dear friend)'
print make_web(input1) #== output1

#
#input2 = '-12x34'
#output2 = ['NUMBER', -12.0, 'IDENTIFIER', 'x', 'NUMBER', 34.0]
#print test_lexer(input2) == output2
