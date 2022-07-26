import socket

target_host = "0.0.0.0"
target_port = 9998
example_host = 'www.google.com'
example_port = 80
example_send = b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n'

def tcp_client(target, port, data_to_send):
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the client 
    client.connect((target, port))

    # send some data
    client.send(data_to_send)

    # recieve some data
    response = client.recv(4096)

    print(response.decode())

    client.close()


tcp_client(example_host, example_port, example_send)
