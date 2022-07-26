import socket

target_host = "127.0.0.1"
target_port = 9997
data_to_send = b'AAABBBCCC'

def udp_client(host, port):
    # creade a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # send some data
    client.sendto(data_to_send, (host, port))

    # recieve some data
    data, addr = client.recvfrom(4096)

    print(data.decode())
    print(addr)
    client.close()

udp_client(target_host, target_port)
