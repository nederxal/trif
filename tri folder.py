#!/usr/bin/python
#-*- coding: utf-8 -*-
# Script pour trier le dossier DL dans des dossier "A TRIER"
# pour ranger un peu tout le bordel plus "facilement"

import os
import sys
import re

dicTri={\
    "IMAGES":"jpg|jpeg|bpm|png",\
    "VIDEOS":"avi|mkv|mp4",\
    "EXEC":"exe|sh|ksh|msi",\
    "DOCUMENTS":"docx|xlsx|pptx|doc|xls|ppt|pdf",\
    "TEXTE":"txt",\
    "DIVERS":"iso|cue|zip|rar|7z"
    }

download = os.path.join(os.environ['HOME'],'Downloads')
tri = os.path.join(os.environ['HOME'],'A_TRIER')

notSorted = []

if not os.path.isdir(tri):
    try:
        os.mkdir(os.path.join(os.environ['HOME'],'A_TRIER'))
    except FileExistsError as e:
            if e.errno != 17:
                print(e)
                raise

for rep in dicTri.keys():
    if not os.path.isdir(tri+rep):
        try:
            os.mkdir(os.path.join(tri,rep))
        except FileExistsError as e:
            if e.errno != 17:
                print(e)
                raise

with os.scandir(download) as it:
    for ent in it:
        if not ent.name.startswith('.') \
           and not ent.name.endswith('ini')\
           and ent.is_file():
                for folder,extens in dicTri.items():
                    if re.search(extens, ent.name, re.IGNORECASE):
                        os.replace(ent.path, os.path.join(tri,folder,ent.name))
        elif not ent.name.startswith('.') and ent.is_dir():
            notSorted.append("DOSSIER : "+ent.name)
        else:
            notSorted.append(ent.name)

print("Les choses suivantes ne sont pas triées : \n")
print('\n'.join(notSorted))

sys.exit(0)

# avoir la taille
#info = os.stat(ent)
