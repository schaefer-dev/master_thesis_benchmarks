import sys

with open(sys.argv[1], 'r') as old_file:
    new_file = open(sys.argv[1] + "_web","w+")
    old_filedata = old_file.read()

    new_filedata = old_filedata.replace('¬', '!')
    new_filedata = new_filedata.replace('⊤', 'true')
    new_filedata = new_filedata.replace('∨', '||')
    new_filedata = new_filedata.replace('∧', '&&')

    new_file.write(new_filedata)

    new_file.close()
