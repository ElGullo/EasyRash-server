from easyrash import app
import secrets
import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler('easyrash.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)    
app.logger.addHandler(handler)

app.run(host='localhost', port=10000, debug=True, threaded=True)
