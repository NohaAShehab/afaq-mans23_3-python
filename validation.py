

def validateNum(num):
    if isinstance(num, int) or isinstance(num, float):
        return True



def validaName(name:str):
    if isinstance(name, str) and name.isalpha():
        return True


# print(validateNum(10))
if __name__=='__main__':
    print(validateNum(10))