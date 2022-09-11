def mutate_string(string, position, character):
    x=position+1
    string=string[:position]+character+string[x:]
    return string
