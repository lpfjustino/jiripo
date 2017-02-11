#!-*- coding: utf8 -*-

import os
import codecs
import mammoth
import re

import time

import enum
import resub

rootdir = 'C:\\Users\\LuisPaulo\\PycharmProjects\\jiripo\\data'

Fields = enum.Enum('codigo', 's', 'num', 'nome', 'sexo', 'datanasc', 'naturalidade', 'tipoensino', 'serie', 'turma',
                   'turno', 'filiacao', 'residencia', 'ano', 'dataelim', 'causaelim')

Fields = enum.Enum('codigo', 's', 'num', 'nome', 'sexo', 'datanasc', 'naturalidade', 'tipoensino', 'serie', 'turma',
                   'turno', 'filiacao', 'residencia', 'ano', 'dataelim', 'causaelim', 'resto', 'lixo', 'fudeu', 'hiiii', 'holy', 'erois')

def docx_to_html(fpath, opath):
    print(fpath)
    with open(fpath, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html = result.value  # The generated HTML

        html = process_file(html)

        out = open(opath, "w")
        out.write(html)

def process_file(html):
    header = '<table><tr><td><p>Código</p></td><td><p>S</p></td><td><p>Num</p></td><td><p>Nome</p></td><td><p>Sexo</p></td><td><p>Data Nasc.</p></td><td><p>Naturalidade</p></td><td colspan="2"><p>Tipo de Ensino</p></td><td colspan="2"><p>Série</p></td><td><p>Turma</p></td><td><p>Turno</p></td></tr><tr><td colspan="4"><p>Filiação</p></td><td colspan="3"><p>Residência</p></td><td><p>Ano</p></td><td colspan="2"><p>Data Elim.</p></td><td colspan="3"><p>Causa Elim</p></td></tr></table>'
    separator = '</p><p>'
    separator2 = '<p>'
    separator3 = '</p>'

    html = html.encode('utf-8').replace(header, "").replace(separator, "\t").replace(separator2, "").replace(separator3, "")
    html = re.sub(r'(\d{6})', r'\n\1', html)

    # Junta filiação
    html = re.sub(r'\t(Mãe)', r' \1', html)

    # Trata cidades vazias
    pattern = r'(\d{2}/\d{2}/\d{4})\t(ER)'
    html = re.sub(pattern, r'\1\t-\t\2', html)

    #OLD pattern = r'(\t)((\w| |\.|\,)*)( )*(,)( )*((\w|\d|\/| )*)( *- *((\w|\d| )*))?(\.)( |\t)*((\w| )*)'
    #OLD html = resub.re_sub(pattern, r'\1\2\4\5\6\7\9\12 \14', html)
    pattern = r'(\t)((\w| |\.|\,)*)( |\t)*(,)( |\t)*((\w|\d|\/| )*)(( |\t)*- *((\w|\d| )*))?(\t)?(\.)((\w| )*)'
    #html = resub.re_sub(pattern, r'\1\2\5\6\7\12 \14\15', html)

    # Trata sobrenomes em endereços
    pattern = r'((Pai: )((\w| )*)?(Mãe: )((\w| )*)?)(\t)((\w| )*)((\t)(((\w| |\.|\,)*)( )*(,)( )*((\w|\d|\/)*)( *- *((\w|\d| )*))?(\.)( |\t)*((\w| )*)))'
    #html = resub.re_sub(pattern, r'\1 \9\11', html)

    # Trata naturalidade em tipoensino
    pattern = r'((\d{2}\/\d{2}\/\d{4})(\t)((\w| )*))(\t)((\w| )*)\tER'
    html = re.sub(pattern, r'\1 \7', html)

    # Remove pais com hífem
    pattern = r'((Pai: )(.)*)(\t(-)*)(\t)'
    html = re.sub(pattern, r'\1\6', html)


    return html

def convert():
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filePath = os.path.join(subdir, file)

            # Remove pdf files
            if (file[-3:] == "pdf"):
                os.remove(filePath)
                continue

            # The output file's name will begin with underscore and its extension is removed
            outputFileName = os.path.join(subdir, "_" + file).split('.docx')[0];

            if(file[-4:] == "docx"):
                docx_to_html(filePath, outputFileName)


def my_parse():
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            print file
            filePath = os.path.join(subdir, file)

            # Remove pdf files
            if (file[-4:] == "docx"):
                continue

            curr_file = codecs.open(filePath, "r", 'utf-8')
            # Skip 1st line
            curr_file.readline()
            for line in curr_file:
                #line = curr_file.readline()
                #print(line)
                fields = re.split(r'\t', line)
                i = 0
                if(len(fields) > 17):
                    print (len(fields))
                    for field in fields:
                        print Fields[i], " - ", field
                        i += 1
            time.sleep(3)


class Aluno:
    def __constructor__(self, codigo, s, num, nome, sexo, datanasc, naturalidade, tipoensino, serie, turma, turno,
                        filiacao, residencia, ano, dataelim, causaelim):
        self.codigo = codigo
        self.s = s
        self.num = num
        self.nome = nome
        self.sexo = sexo
        self.datanasc = datanasc
        self.naturalidade = naturalidade
        self.tipoensino = tipoensino
        self.serie = serie
        self.turma = turma
        self.turno = turno
        self.filiacao = filiacao
        self.residencia = residencia
        self.ano = ano
        self.dataelim = dataelim
        self.causaelim = causaelim


    #print html

convert()
my_parse()
print("ae");
