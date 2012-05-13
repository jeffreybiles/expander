__author__ = 'jefferton'

import ply.lex as lex

tokens = (
    'START',
    'BETWEEN',
    'END',
    'STRING',
    )

t_START = r'\{'
t_BETWEEN = r'\|'
t_END = r'\}'
t_STRING = r'[\w<>,\.\/\\:\=\"\?\!\[\]\'\@\(\)]+'

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
    'START': '<span class="expander"><span class="expandable">',
    'BETWEEN': '</span><span class="expansion">',
    'END': '</span></span>'
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

input1 = """<p>{Hi, I'm|{Greetings, my name is|Salutations, friend!  You may refer to me as}} Jeffrey Biles.

<p>I am interested in {web development,|designing interactive web applications and games using {the latest tools.|Ruby, Rails, Javascript/Coffeescript, jQuery, Canvas, and whatever else I need to get the job done.}  My other interests are}entrepreneurship, {education, and <a href="http://jeffreybiles.com/games/">game design</a>|education, and  <a href="http://jeffreybiles.com/games/">game design</a>.  These last two fields, when practiced well, have a {surprising amount in common|focus on challenging and increasing the skills of the learner/player.  Games do this very well for skills of limited use.  School does this very poorly for skills of slightly more use}.

<p>I {won some awards|{did well on standardized tests|scored in the top 1% of the GRE Math and Verbal, the top 14% of the computer science GRE, and had a GPA of 3.87. I }published <a href="http://pubs.acs.org/doi/abs/10.1021/jp2004166">some</a> <a href="http://pubs.acs.org/doi/abs/10.1021/ja106167d">papers</a>, and {won|beat out business majors to claim a cash prize in} a business plan competition. I am an Eagle Scout, a member of Phi Beta Kappa,} and

have {many virtues| the programmer's virtues of
{laziness|laziness (I started programming because the {lab I was working for|<a href="http://www.cchem.berkeley.edu/erwgrp/">the Williams group at UC Berkeley</a>} was doing way too much {busywork|pressing the same button, reading the same field, and manually entering the result in the same computer})} and
{impatience|impatience (I made the switch to programming because the pace of change was much faster, and the time required to do something useful was significantly lower)},
but {hopefully not hubris| {hopefully not hubris|only a little overconfidence} (I'd rather make a useful program than a perfect program, and I love learning more than being right)}.

<p>You should {hire me|{contact me| email me at bilesjeffrey@gmail.com} so that we can {get to know one another better|decide if we can work well together.  But before that, check out <a href="https://github.com/jeffreybiles">my github</a> and play some of <a href="http://jeffreybiles.com/games/">my games</a>}}.

    """

print make_web(input1) #== output1

#
#input2 = '-12x34'
#output2 = ['NUMBER', -12.0, 'IDENTIFIER', 'x', 'NUMBER', 34.0]
#print test_lexer(input2) == output2
