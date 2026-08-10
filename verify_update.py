import os
import datetime

def verify():
    # Verifica se il file script.js è stato modificato oggi
    file_path = "script.js"
    if not os.path.exists(file_path):
        print("ERRORE: script.js non trovato!")
        return False
    
    # Ottieni la data di ultima modifica
    mtime = os.path.getmtime(file_path)
    last_modified_date = datetime.datetime.fromtimestamp(mtime).date()
    today = datetime.date.today()
    
    with open(file_path, 'r') as f:
        content = f.read()
        
    # Verifica se la data di oggi è presente nel contenuto (formato script.js)
    today_str = today.strftime("%d %B %Y")
    
    if today_str in content:
        print(f"SUCCESSO: L'aggiornamento del {today_str} è presente nel blog.")
        return True
    else:
        print(f"FALLIMENTO: L'aggiornamento del {today_str} non è stato trovato.")
        return False

if __name__ == "__main__":
    if not verify():
        exit(1)
