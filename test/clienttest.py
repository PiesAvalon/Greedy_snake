import socket

def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def start_client(server_ip):
    # 创建一个Socket对象
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接到服务器
    client_socket.connect((server_ip, 12345))
    print("已连接到服务器")

    try:
        while True:
            message = input("请输入要发送的消息（输入'exit'退出）: ")
            if message.lower() == 'exit':
                break
            
            # 发送数据
            client_socket.sendall(message.encode('utf-8'))

            # 接收回应
            response = client_socket.recv(1024)
            print(f"服务器回应: {response.decode('utf-8')}")
    finally:
        # 关闭连接
        client_socket.close()

if __name__ == "__main__":
    print(f"局域网 IP 地址: {get_local_ip()}")
    server_ip = input("请输入服务器IP地址: ")
    start_client(server_ip)