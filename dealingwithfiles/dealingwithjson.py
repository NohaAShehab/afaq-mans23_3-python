import  json


def readjson():
    try:
        fileobj = open('users.json', 'r')
    except Exception as e:
        return  False
    else:
        print(fileobj)
        data = fileobj.read()  # json in string
        res= json.loads(data)  # return string into list of dicts
        print(res)

        return res

data= readjson()
print(data)



# open json object to the file


# def writeTojson():
#
#     obj = {"name":"noha", 'id':10}
#
#     try:
#         fileobj = open('users.json', 'a')
#     except Exception as e:
#         print(e)
#         return False
#     else:
#         # convert dict to string
#         data_to_write = json.dumps(obj)
#         print(data_to_write, type(data_to_write))
#         fileobj.write(data_to_write)
#         fileobj.close()
#
# writeTojson()



def writeTojson():
    old_data = readjson()

    obj = {"name":"noha", 'id':10}
    old_data.append(obj)
    print(old_data)
    # return

    try:
        fileobj = open('users.json', 'w')
    except Exception as e:
        print(e)
        return False
    else:
        # convert dict to string
        data_to_write = json.dumps(old_data, indent=2)
        print(data_to_write, type(data_to_write))
        fileobj.write(data_to_write)
        fileobj.close()

writeTojson()
