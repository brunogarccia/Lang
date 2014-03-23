from pyparsing import Word, Regex, Literal, OneOrMore, ParseException
import console, exception, define, data

def lexical_analysis(data):   

    if(data != None):
        
        try:
           
            lines = []

            for line in data:              
               
                operator = Regex(r'(?<![\+\-\^\*/%])[\+\-]|[\^\*/%!]')
                function = Regex(r'[a-zA-Z_][a-zA-Z0-9_]*(?=([ \t]+)?\()')
                variable = Regex(r'[+-]?[a-zA-Z_][a-zA-Z0-9_]*(?!([ \t]+)?\()')
                number = Regex(r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?')
                lbrace = Word('(')
                rbrace = Word(')')               
                linebreak = Word('\n')
                skip = Word(' \t')
                assign = Literal('=')
                shift_left = Literal('<<=')
                shift_right = Literal('>>=')
                and_ = Literal('&=')
                or_ = Literal('|=')
                xor = Literal('^=')
              
                lexOnly = operator | function | variable | number | lbrace \
                   | rbrace | assign |  shift_left | shift_right \
                   |  and_ | or_ | xor

                lexAllOnly = OneOrMore(lexOnly)
                 
                lines.append(lexAllOnly.parseString(line))          
            
            return lines
        
        except ParseException as err:            
            console.error(err.line)
            console.error(" "*(err.column-1) + "^")
            console.error(err)
    else:
        console.error(exception.invalid_parameters)

def interpret_assign(line):

    if(line[1] == define.assign_operator):

        #apenas inteiros por enquanto
        
        value = int(line[2]) + int(line[4])

        data.set_var(line[0], value)

        print(data.get_var(line[0]))

def interpret(data):

    data = lexical_analysis(data)

    if(data != None):

        for line in data:

            interpret_assign(line)           

    
    


