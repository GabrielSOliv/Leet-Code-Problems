example = '(al)G(al)()()G'


def interpret(command: str) -> str:
   
    strOutput = command.replace('(al)', 'al').replace('()', 'o') 
        
    return strOutput


print(interpret(example))
