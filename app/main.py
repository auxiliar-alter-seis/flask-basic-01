
import routes
from app import app


#### externally visible server
HOST = '0.0.0.0'
PORT = 7007


if __name__ == '__main__':
   app.run(host=HOST, port=PORT)