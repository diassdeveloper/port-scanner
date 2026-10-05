"""
Port Scanner — Verifica quais portas estão abertas em um determinado host.

Lê os hosts do arquivo targets.txt e escaneia as portas mais comuns.

Uso:
    python main.py
"""

import socket
from datetime import datetime

ARQUIVO_TARGETS = "targets.txt"
PORTAS_COMUNS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 5432, 8080, 8443]

def escanear_host(host):
    """Escaneia as portas comuns de um host e retorna as portas abertas."""
    portas_abertas = []
    for porta in PORTAS_COMUNS:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            resultado = sock.connect_ex((host, porta))
            if resultado == 0:
                portas_abertas.append(porta)
            sock.close()
        except socket.gaierror:
            print(f"Host não encontado:' {host}")
            break
        except socket.error:
            pass
    return portas_abertas

def main():
    """Lê os targets e escaneia as portas de cada host."""
    print(f"\n{'='*50}")
    print(f"  Port Scanner - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}\n")

    with open(ARQUIVO_TARGETS, "r") as f:
        hosts = [linha.strip() for linha in f if linha.strip() and not linha.strip().startswith("#")]

    for host in hosts:
        print(f"Escaneando host: {host}")
        portas = escanear_host(host)
        if portas:
            print(f"  Portas em {host}: {', '.join(map(str, portas))}\n")
        else:
            print(f"Nenhuma porta aberta encontrada em {host}.\n")
        print()

if __name__ == "__main__":
    main()