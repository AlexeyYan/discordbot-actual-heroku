import requests
from urllib.parse import urlsplit

import qrcode


def Curs():
    r = requests.get('http://www.nbrb.by/API/ExRates/Rates?Periodicity=0')# NBRB Api
    r = r.json()
    USD = r[4]['Cur_OfficialRate']
    EUR = r[5]['Cur_OfficialRate']
    RUB = r[16]['Cur_OfficialRate']
    UAH = r[2]['Cur_OfficialRate']
    return f'Курс доллара: {USD}\nКурс евро: {EUR}\nКурс рубля(100): {RUB}\nКурс гривны(100): {UAH}'


def Curs_All():
    r = requests.get('http://www.nbrb.by/API/ExRates/Rates?Periodicity=0')# NBRB Api
    curses = "***Курсы валют на сегодня:***\n"
    for curs in r.json():
        curses += curs['Cur_Name']+f'({str(curs["Cur_Scale"])}): __*{str(curs["Cur_OfficialRate"])}*__\n'
    return curs


def createQRCode(value):
    qr = qrcode.QRCode(version=1, box_size=12, border=2)
    qr.add_data(value)
    qr.make(fit=True)
    x = qr.make_image()
    image_file = open('qr.jpg', 'wb')
    x.save(image_file, 'JPEG')
    image_file.close()
