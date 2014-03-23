import console, exception

dict_variables = {}

def set_var(var_name, value=None):
    
    #tipagem dinamica, um int pode virar string por exemplo
    #cria ou seta a váriavel

    if(isinstance(var_name, str)):
       dict_variables[var_name] = value
    else:
        console.error(exception.declare_var_invalid_type)

def get_var(var_name):
    
    if(isinstance(var_name, str)):
        if(var_name in dict_variables):
            return dict_variables[var_name]
        else:
            console.error(exception.get_var_not_exists)
    else:
        console.error(exception.declare_var_invalid_type)

    return None

def del_var(var_name):

    if(isinstance(var_name, str)):
        if(var_name in dict_variables):
            del dict_variables[var_name]
        else:
            console.error(exception.get_var_not_exists)
    else:
        console.error(exception.declare_var_invalid_type)
