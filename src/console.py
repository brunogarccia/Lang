import core

def error(msg):
    if(core.debug):
        out(msg)
        
def out(msg):
    print(msg)
