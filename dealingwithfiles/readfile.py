'log messages '

'r: read mode --> open file for reading starting from the beginning of the file  '

try:
    filobject= open('names.txt', 'r') #TextIOWrapper
except Exception as e:
    print(e)
    exit()
else:
    print(filobject)
    data = filobject.read() # read file content into one string?
    print(data, type(dataa))
    filobject.seek(0)
    lines=  filobject.readlines()
    print(lines)
    filobject.close()
