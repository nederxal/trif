#!/usr/bin/python
#-*- coding: utf-8 -*-
# Script pour trier le dossier DL dans des dossier "A TRIER"
# pour ranger un peu tout le bordel plus "facilement"

import os
import sys
import logging

logging.basicConfig(filename="_TRI.txt", level=logging.INFO)

def folderCreation(name):
    try:
        os.mkdir(name)
        logging.info("Création du dossier %s", name)
    except FileExistsError as e:
        if e.errno != 17:
            logging.exception(e)
            raise

def main():
    dicTri={
    "IMAGES":[".jpg", ".jpeg", ".bpm", ".png"],
    "VIDEOS":[".avi", ".mkv", "mp4"],
    "EXEC":[".exe", ".sh", ".msi"],
    "DOCUMENTS":[".docx", ".xlsx", ".pptx", ".doc", ".xls", ".ppt", ".pdf", ".PDF"],
    "TEXTE":[".txt"],
    "DIVERS":[".iso", ".cue", ".zip", ".rar", ".7z", ".gz"]
    }
    download = os.path.join(os.environ['HOMEPATH'],'Downloads')
    tri = os.path.join(os.environ['HOMEPATH'],'A_TRIER')
    notSorted = []
    
    folderCreation(tri)

    for rep in dicTri.keys():
        folderCreation(os.path.join(tri,rep))

    with os.scandir(download) as it:
        for ent in it:
            if not ent.name.startswith('.') \
               and ent.is_file():
                    name_,ext_=os.path.splitext(ent.name)
                    for folder,extens in dicTri.items():
                        if ext_ in extens:
                            try:
                                os.replace(ent.path,
                                            os.path.join(tri,folder,ent.name))
                                logging.info("%s a été déplacé dans %s", 
                                            ent.name, 
                                            folder)
                            except PermissionError as e:
                                logging.error("Impossible de bouger %s, erreur %s", ent.name, e)
            elif not ent.name.startswith('.') and ent.is_dir():
                notSorted.append("DOSSIER : "+ent.name)
            else:
                notSorted.append(ent.name)

    logging.info("Les choses suivantes ne sont pas triées : ")
    logging.info('\r'.join(notSorted))

if __name__ == '__main__':
    main()
    sys.exit(0)
