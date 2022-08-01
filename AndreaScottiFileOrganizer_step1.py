import os
import shutil
import csv

#Funzione che otthiene il path in cui è situato il file .py e aggiunge /files
def target_folder():
    file_path = os.path.join(os.getcwd(), "files")
    if os.path.exists(file_path) == False:
        #trovare modo di scrivere le cartelle presenti all' interno della cartella in caso in cui la cartella files non esista
        print("Nella cartella in cui si trova questo file non è presente alcuna cartella di nome 'files'! Questa è una lista delle cartelle presenti nel: " + str(os.path.dirname(os.getcwd())))
    else:
        return file_path

#Funzione che crea le cartelle docs, images e audio se non esistono e se esistono gia manda un messaggio
def folder():
    folder_names = sorted(["images","audio","docs"])
    for folders in folder_names:
        #Cotrolla se le cartlle con questi nomi già esistono
        try:
            if not os.path.exists(target_folder().join(folders)):
                os.mkdir(os.path.join(target_folder(), folders))
        except FileExistsError as e:
            print("Errore! La cartella: " + str(folders) + " eisite già. Errore: ", e)
    return folder_names

#funzione che crea se non è presente il file recap.csv
def csv_file_creation():
    if not os.path.exists(os.path.join(target_folder(), "recap.csv")):    
        #Non c'è bisogno di controllare se il file esiste gia siccome nel caso questo fosse il caso lo sovrascrirrebbe
        f = open("recap.csv", "w", newline="")
        f.close()
        
#Funzione che logga e sposta
def log_and_move(file,folder):
    k = open("recap.csv", "a", newline="")
    k_write = csv.writer(k)
    try:
        shutil.move(os.path.join(target_folder(), file), os.path.join(target_folder(), str(folder)))
        print(file,"type:" + str(folder),"size:" + str(os.path.getsize(os.path.join(target_folder(),(folder),(file)))),"B")
        #Strip(".")[0] non sembra funzionare 
        k_write.writerow([str(file).strip("."),folder,str(os.path.getsize(os.path.join(target_folder(),(folder),(file))))])
        k.close()
    except Exception as e:
        print("Errore! Esiste gia un file di nome: " +str(file) + " nella cartella: " + str(folder) + " Errore: " + str(e))
        k.close()

#Funzione finale con cicli for per iterare la funzione precedente
def file_to_folder(folder_name_list):
    csv_file_creation()
    f = open("recap.csv", "w", newline="")
    write = csv.writer(f)
    write.writerow(["Name","Type","Size(B)"])
    f.close()
    for file in os.listdir(target_folder()):
        for folder in folder_name_list:
            if os.path.isfile(os.path.join(target_folder(), file)):
                if folder == "images":    
                    if str(file).split(".")[-1] == "png" or str(file).split(".")[-1] == "jpeg" or str(file).split(".")[-1] == "jpg":
                        log_and_move(str(file),folder,)
                elif folder == "audio":    
                    if str(file).split(".")[-1] == "mp3":
                        log_and_move(str(file),folder,)
                elif folder == "docs":   
                    if str(file).split(".")[-1] == "txt" or str(file).split(".")[-1] == "odt":
                        log_and_move(str(file),folder,)
    try:
        shutil.move(os.path.join(os.getcwd(),"recap.csv"), target_folder())
    except Exception as e:
        print("Errore! Esiste gia un file di nome report.csv nella cartella files! Errore: " + str(e))

def main():
    file_to_folder(folder())

if __name__ == "__main__":
    main()

