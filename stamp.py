import cv2, wget, re, datetime, os
from pathlib import Path
from pyunpack import Archive
from imwatermark import WatermarkEncoder, WatermarkDecoder

def mountDirectory():
    os.makedir('~/stamp_py/src')

def getImg(input):
    url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(url_regex,input)
    
    filename = '~/stamp_py/src/'
    filename += datetime.fromtimestamp(datetime.datetime.now().timestamp()).strftime("%d-%m-%Y_%H:%M:%S")
    filename += '.png'
    if url:
        with open(filename, 'r+b', encoding = 'utf-8') as currentImg:
           wget.download(url[0], currentImg)
           img = Path(filename).glob('*')

    # caso não seja uma url, e sim um caminho local de arquivo
    else:
        if re.search('.zip$'|'.rar$'|'.tar.gz$', filename):
            Archive(filename).extractall('~/stamp_py/src')
            dir = filename
            extension = 4
            if re.search('.tar.gz$', filename):
                extension = 7
            for i in range(len(filename), len(filename)-extension):
                dir = dir.replace(dir[i], "")
            img = Path(dir).glob('*')
            
        else:
            img = Path(filename).glob('*')
    
    return img


print("STAMP.IMG\n\nCarimbe as suas imagens com uma marca d'água invisível!\n")

entry = input("Digite o caminho da sua imagem ou pasta compactada, ou o link da sua imagem na internet: ")

mountDirectory()
getImg(entry)

