import re
import os
import threading
import tkinter as tk
from tkinter import messagebox

def extract_lines_with_specific_emails(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    filtered_lines = []
    email_regex = (
        r'\b[A-Za-z0-9._%+-]+@('
        r'sfr\.fr|neuf\.fr|numericable\.fr|bbox\.fr|gmx\.fr|icloud\.com|'
        r'laposte\.net|gmail\.com|hotmail\.fr|outlook\.fr|'
        r'free\.fr|yahoo\.fr'
        r')\b'
    )  # Modifiez en mettant les domaines que vous souhaitez conserver

    for line in lines:
        if re.search(email_regex, line): 
            filtered_lines.append(line.strip())

    return filtered_lines

def save_filtered_lines(filtered_lines, output_file):
    # Créer le dossier "Resultats" s'il n'existe pas
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        for line in filtered_lines:
            file.write(line + '\n')

def start_extraction(input_file, output_file, root):
    filtered_lines = extract_lines_with_specific_emails(input_file)
    save_filtered_lines(filtered_lines, output_file)
    root.destroy()
    messagebox.showinfo("Terminé", "Les lignes correspondantes ont été extraites avec succès et sauvegardées dans " + output_file)

def main():
    input_file = 'emails.txt'
    output_file = os.path.join('Resultats', 'mails_filtre.txt')

    # Créer la fenêtre tkinter
    root = tk.Tk()
    root.title("Extraction en cours")

    # ouvre un label pour afficher le message
    label = tk.Label(root, text="L'extraction est en cours, veuillez patienter...")
    label.pack(padx=20, pady=20)

    # Utiliser un thread pour exécuter l'extraction afin de ne pas bloquer l'interface graphique
    extraction_thread = threading.Thread(target=start_extraction, args=(input_file, output_file, root))
    extraction_thread.start()

    # Lancer la boucle principale de tkinter
    root.mainloop()

if __name__ == "__main__":
    main()
