import socket,logging
import threading
 
logging.basicConfig(level = logging.DEBUG)
 
BUF_SIZE=1024
s = None
 
def createsocket():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('localhost',8180))
    s.listen(5)
    return s
 
def process(connection,address):
    logging.debug("server is processing")
    while 1:
        data = connection.recv(BUF_SIZE)
        if not data:
            break
        logging.debug("server sends data")
        connection.send("server to client info: "+data)
    connection.close()
 
s = createsocket()
 
while 1:
    logging.debug("server waitting ...")
    connection,address = s.accept()
    t = threading.Thread(target=process,args=(connection,address))
    t.start()
s.close()
