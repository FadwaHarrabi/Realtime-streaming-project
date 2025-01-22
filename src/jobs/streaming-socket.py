import json
import socket
import time


def send_data_over_socket(file_path,host='127.0.0.1',port=9999,chunk_size=2):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(1)
    print(f"listening for connections on {host}:{port}")
    conn,addr=s.accept()
    print(f"connection from {addr}")

