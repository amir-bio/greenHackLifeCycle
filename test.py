# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 13:27:24 2018

@author: huika
"""
from pyzbar.pyzbar import ZBarSymbol

decode(Image.open('pyzbar/tests/qrcode.png'), symbols=[ZBarSymbol.QRCODE])
[Decoded(data=b'Thalassiodracon', type='QRCODE')]

# If we look for just code128, the qrcodes in the image will not be detected
decode(Image.open('pyzbar/tests/qrcode.png'), symbols=[ZBarSymbol.CODE128])