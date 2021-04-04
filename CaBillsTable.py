# -*- coding: utf-8 -*-


import PyPDF2
import os 
from os import listdir
from os.path import isfile, join
import pandas as pd
import re

mypath = "path\\with\\all\\cabify\\bills"
df=pd.DataFrame(columns=["ticket","fecha","precio_2"])
str(mypath).split(', ')
index=0
onlyfiles = [mypath + "\\" +f for f in listdir(mypath) if isfile(join(mypath, f))]
for i in onlyfiles:
    nombre_pdf = i.split("\\")[-1]
    with open(i, 'rb') as pdf_file:
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        page = read_pdf.getPage(0)
        pc = page.extractText()
        pdf_file.close()
    
        ticket= pc.splitlines()[3].split(" - ")[0]
        df.loc[index,['ticket']]=str(ticket) + " "
        fecha= pc.splitlines()[7].split(".")[0]
        df.loc[index,['fecha']]=str(fecha) + " "
        precio_2_regex= re.compile(r'["Total"]*["$"]+\d{3}[,]+\d{2}')
        precio_2 = precio_2_regex.search(pc).group(0)
        df.loc[index,['precio_2']]=str(precio_2) + " "

    index=index+1
    old_file = os.path.join(mypath, i)

    new_file = os.path.join(mypath, str(index) +"_" + nombre_pdf)
    os.rename(old_file, new_file)







