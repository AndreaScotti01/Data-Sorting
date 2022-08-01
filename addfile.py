from os import listdir
from os.path import isfile, join
import os
import shutil

def target_folder():
    file_path = os.path.join(os.getcwd(), "files")
    return file_path

def move(file_name,folder):
    if os.path.isdir(os.path.join(target_folder(),folder)):
        shutil.move(os.path.join(target_folder(),file_name), os.path.join(target_folder(),folder))
    else:
        print("Non esiste la cartella adeguata per questo file! " + str(folder))
        
def file_to_folder(file_name):
    folder_name_list = ["audio","images","docs"]
    if os.path.isfile(os.path.join(target_folder(), file_name)):
        for folder in folder_name_list:
            if folder == "images":    
                if str(file_name).split(".")[-1] == "png" or str(file_name).split(".")[-1] == "jpeg" or str(file_name).split(".")[-1] == "jpg":
                    move(file_name,folder)    
            elif folder == "audio":    
                if str(file_name).split(".")[-1] == "mp3":
                    move(file_name,folder)           
            elif folder == "docs":   
                if str(file_name).split(".")[-1] == "txt" or str(file_name).split(".")[-1] == "odt":        
                    move(file_name,folder)

def file_list():
    onlyfiles = [f for f in listdir(target_folder()) if isfile(join(target_folder(), f))]
    return onlyfiles

def take_input():
    index = False
    print("Questa è la lista dei file disponibili: " + str(file_list()))
    x = input("Che file desideri spostare nella cartella di competenza? ")
    while index == False: 
        for files in os.listdir(target_folder()):
            if not os.path.isdir(os.path.join(target_folder(),files)):
                if x == files:
                    return str(x)
        print("Questa è la lista dei file disponibili: " + str(file_list()))
        x = input("Il file da te inserito non è valido o non esiste questa è la lista dei file disponibili: ")
        
            
def main():
    file_to_folder(str(take_input()))

if __name__=="__main__":
    main()
    