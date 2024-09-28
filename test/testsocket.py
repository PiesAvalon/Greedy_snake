import socket

def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def start_server():
    # 创建一个Socket对象 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定地址和端口
    server_socket.bind(('0.0.0.0', 12345))  # 监听所有可用的接口

    # 开始监听
    server_socket.listen(1)
    print("服务器启动，等待连接...")

    # 接受连接
    client_socket, addr = server_socket.accept()
    print(f"连接来自: {addr}")

    while True:
        # 接收数据
        data = client_socket.recv(1024)
        if not data:
            break  # 如果没有数据，退出循环
        print(f"接收到: {data.decode('utf-8')}")
        
        # 发送回应
        message = "成功接受"
        client_socket.sendall(message.encode('utf-8'))

    # 关闭连接
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    print(f"局域网 IP 地址: {get_local_ip()}")
    start_server()