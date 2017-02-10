from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

import argparse
import pdf2txt
import os
import sys

rootdir = 'C:\Users\LuisPaulo\PycharmProjects\jiripo\data'

def pdfToText():
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filePath = os.path.join(subdir, file)

            # Remove non pdf files
            if(file[-3:] != "pdf"):
                os.remove(filePath)

            # The output file's name will begin with underscore and its extension is removed
            outputFileName = os.path.join(subdir, "_"+file).split('.pdf')[0];

            command = "python pdf2txt.py " + "-o " + outputFileName + " " + filePath
            os.system(command)

class Document:
    def __constructor__(self, cod):
        self.cod = cod

fname = "./data/2010/_2010.1.manha"
fp = file(fname, "r")

content = fp.read()

header = "Código\n\nS\n\nNum\n\nNome\n\nSexo\n\nData Nasc.\n\nNaturalidade\n\nTipo de Ensino\n\nSérie\n\nTurma\n\nTurno\n\nFiliação\n\nResidência\n\nAno\n\nData Elim.\n\nCausa Elim\n"

content.
print("ae");
