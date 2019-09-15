import socket # Import thư viện socket

host = "127.0.0.1" # Địa chỉ loopback, là máy hiện tại
port = 8019 # Port có socket api của server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Khởi tạo lớp socket
s.bind((host, port)) # Kết nối socket tới địa chỉ tại host và port
s.listen() # socket lắng nghe request

conn = None
while True: # Lặp mãi mãi
  if conn is None: # Kiểm tra hàm access có đang bị block hay không.
    conn, addr = s.accept() # Chờ và sẽ chấp nhận request từ client
  else:
    data = conn.recv(1024) # Nhận thông tin dưới dạng byte từ data buffer
    conn.sendall(data.decode().upper().encode()) # Trả ngược về cho client