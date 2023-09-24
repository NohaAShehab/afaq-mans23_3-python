'log messages '

'''w: write mode --> open file for writing= starting from the beginning of the file  
if file doesn't will try to create it ---> linux 
remove old content
'''

try:
    filobject= open('mycv.txt', 'w') #TextIOWrapper
except Exception as e:
    print(e)
    exit()
else:
    print(filobject)
    filobject.write('Nice to meet you \n')
    filobject.write('abc')
    filobject.writelines(['ddd\n', 'mmm\n', 'sss\n', 'iti'])

    filobject.close()
