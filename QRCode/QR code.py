
import pyqrcode
import png
from pyqrcode import QRCode

site="https://www.google.com"
url_qr=pyqrcode.create(site)
url_qr.png('Anish.png',scale=6)
