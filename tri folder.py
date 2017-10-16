#!/usr/bin/python
#-*- coding: utf-8 -*-
# Script pour trier le dossier DL dans des dossier "A TRIER"
# pour ranger un peu tout le bordel plus "facilement"

import os
import sys
import re

images = "jpg|jpeg|bpm|png"
videos = "avi|mkv|mp4"
exe = "exe|sh|ksh|msi"
docs = "docx|xlsx|pptx|doc|xls|ppt|pdf"
texte = "txt"
divers = "iso|cue|zip|rar|7z"

download = os.environ['HOME']+'/Downloads'
tri = os.environ['HOME']+"/A_TRIER/"
repTri = ['IMAGES', 'VIDEOS', 'EXECUTABLES', 'DOCUMENTS', 'TEXTE', 'DIVERS']
notSorted = []

if not os.path.isdir(tri):
    try:
        os.mkdir(os.environ['HOME']+'/A_TRIER')
    except OSError as e:
        print (e)
        raise

for rep in repTri:
    if not os.path.isdir(tri+rep):
        try:
            os.mkdir(os.environ['HOME']+"/A_TRIER/"+rep)
        except OSError as e:
           print (e)
           raise

with os.scandir(download) as it:
    for ent in it:
        if not ent.name.startswith('.') \
           and not ent.name.endswith('ini')\
           and ent.is_file():
            if re.search(images, ent.name, re.IGNORECASE):
                os.replace(ent.path, tri+repTri[0]+"/"+ent.name)
            elif re.search(videos, ent.name, re.IGNORECASE):
                os.replace(ent.path, tri+repTri[1]+"/"+ent.name)
            elif re.search(exe, ent.name, re.IGNORECASE):
                os.replace(ent.path, tri+repTri[2]+"/"+ent.name)
            elif re.search(docs, ent.name, re.IGNORECASE):
                os.replace(ent.path, tri+repTri[3]+"/"+ent.name)
            elif re.search(texte, ent.name, re.IGNORECASE):
                os.replace(ent.path, tri+repTri[4]+"/"+ent.name)
            elif re.search(divers, ent.name, re.IGNORECASE):
                os.replace(ent.path, tri+repTri[5]+"/"+ent.name)
            else:
                notSorted.append(ent.name)
        elif not ent.name.startswith('.') and ent.is_dir():
            notSorted.append("DOSSIER : "+ent.name)

print("Les choses suivantes ne sont pas triées : \n")
print('\n'.join(notSorted))

sys.exit(0)

# avoir la taille
#info = os.stat(ent)
