import sipfullproxy
from sipfullproxy import *

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log', level=logging.INFO,
                    datefmt='%Y/%m/%d %H:%M:%S')
logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
hostname = socket.gethostname()
logging.info(hostname)
ipaddress = socket.gethostbyname(hostname)
logging.info(ipaddress)
sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
server = socketserver.UDPServer((HOST, PORT), UDPHandler)
server.serve_forever()
