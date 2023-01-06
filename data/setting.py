import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
# print(hostname)
# print(ip)
import os , sys
# print(os.getpid())
# print (os.system("taskkill /pid 544")) # act as command propmt
# import sys
# print (sys.version) # ==> 3.10.7
a = os.path.exists("server.py") # ==> check file or folder in path [true , false]
a = os.path.getsize("G:\project\python\AQIHAT\data\server.py")
''' # if folder is not then create folder'''
# if not (os.path.isdir("hello")):
    # os.mkdir("h1llo")


def encode(data):
    encoded = (__import__('base64').b64encode(__import__('codecs').getencoder("utf-8")(data)[0]))
    ok1=("'"+encoded.decode()+"'")
    ok = f"exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')({ok1})[0]))"
    return ok
def decode(data):
    decoded = (__import__('base64').b64decode(__import__('codecs').getencoder("utf-8")(data)[0]).decode())
    # print(type(decoded)) = > str
    return decoded

with open ("Encode/client.py" , "r") as f:
    content = f.read() #=> String
    if content[0] == "b":
        print("Data_decoded")
        content = content[1:]
    content = decode(content)
    with open ("Encode/1cli.py", "w") as f:
        f.write(content)
        print("[DONE]")
    # print(content)
    words = ["<IP>" , "<PORT>"]
    for i in words:
        if i == "<IP>":
            w = "127.0.0.10"
        elif i == "<PORT>":
            w = "12345"
        a = content.replace(i,w)
        # print("[DONE]")
        content = a
    # print(content)
    data = encode(content)
    with open ("Encode/cli.py", "w") as f:
        f.write(data)
name1 = "abc.p1y"
if (name1[-3:] != ".py") :
    name1 += ".py"
print(name1)
    # print(f.read().decode())

# try:
#     with open ("Encode/cli.py" , "w") as f2:
#         content1 = decode(content)
#         f2.write(content1) 
# except Exception as e:
#     print(e)

# print(a)
# string slicing for command slicing
a = "down setup.exe"
b= a[0:4]
b = a[5:]
print(b)


