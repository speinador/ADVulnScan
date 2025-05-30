import subprocess

def scan_host(ip):
    print(f"[*] Escaneando {ip}...\n")

    checks = {
        "Zerologon (CVE-2020-1472)": f"nmap --script smb-vuln-zerologon -p 445 {ip}",
        "EternalBlue (CVE-2017-0144)": f"nmap --script smb-vuln-ms17-010 -p 445 {ip}",
        "NTLM Signing Disabled (NTLM Relay Check)": f"nmap --script smb2-security-mode -p 445 {ip}",
    }

    for name, command in checks.items():
        print(f"[+] Chequeando: {name}")
        try:
            result = subprocess.check_output(command, shell=True, text=True)
            print(result)
        except subprocess.CalledProcessError as e:
            print(f"[!] Error al ejecutar el escaneo: {e}")
        print("-" * 60)

if __name__ == "__main__":
    ip_objetivo = input("Ingresa la IP del controlador de dominio: ")
    scan_host(ip_objetivo)
