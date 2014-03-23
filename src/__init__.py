import os.path, console, exception, interpreter, core

def main():

    try:
        file_name = input("Digite o nome do script: ")
    except:
        console.error(exception.file_not_exists)

    if(file_name != None):
        
        file_name = "../scripts/" + file_name
        
        if(os.path.isfile(file_name)):
            if(os.path.splitext(file_name)[1] == core.lang_extension):

                with open(file_name, "r") as file:
                    data = file.readlines()

                interpreter.interpret(data)

            else:
                console.error(exception.file_invalid_extension)
        else:
            console.error(exception.file_not_exists)
    else:
        console.error(exception.file_not_exists)    

if(__name__ == "__main__"):
    main()
