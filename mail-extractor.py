import re
import os
import sys

def extract_emails(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    email_addresses = []
    email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    detected_lines_count = 0
    total_lines = len(lines)
    
    for index, line in enumerate(lines):
        matches = email_regex.findall(line)
        if matches:
            detected_lines_count += 1
            for match in matches:
                email_addresses.append(match)

        # Print progress on the same line
        progress_message = f"Progress: {index + 1}/{total_lines} lines processed"
        sys.stdout.write('\r' + progress_message)
        sys.stdout.flush()

    print()  # Print newline after progress is complete
    print(f"\nNombre de lignes détectées : {detected_lines_count}")
    return email_addresses

def save_emails(email_addresses, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as file:
        for email in email_addresses:
            file.write(email + '\n')

def main():
    input_file = 'emails.txt'  # Change this to the path of your input file
    output_folder = 'Resultats'
    output_file = os.path.join(output_folder, 'emails.txt')

    print("Extraction des adresses e-mail en cours...")

    email_addresses = extract_emails(input_file)
    
    save_emails(email_addresses, output_file)
    
    print("Extraction terminée.")
    print(f"Les adresses e-mail ont été sauvegardées dans {output_file}")

    input("Appuyez sur Entrée pour fermer le programme...")

if __name__ == "__main__":
    main()
