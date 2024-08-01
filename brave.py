import os
import subprocess

def abrir_brave():
    # Procurar o executável do Brave Browser
    brave_executable = None
    possible_paths = [
        r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe',
        r'C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'
    ]

    for path in possible_paths:
        if os.path.exists(path):
            brave_executable = path
            break
    
    if brave_executable:
        try:
            subprocess.Popen([brave_executable])
        except Exception as e:
            print(f"Erro ao abrir Brave Browser: {e}")
    else:
        print("Brave Browser não encontrado.")

# Exemplo de uso:
if __name__ == "__main__":
    abrir_brave()