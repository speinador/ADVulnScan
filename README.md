# Active Directory Vulnerability Scanner (ADVulnScan)

Este proyecto es un escáner básico de vulnerabilidades comunes en controladores de dominio de Active Directory, utilizando `nmap` y scripts NSE.

## 🚨 Vulnerabilidades detectadas

- **Zerologon** (CVE-2020-1472)
- **EternalBlue** (CVE-2017-0144)
- **NTLM Relay (firma deshabilitada)**

## ⚙️ Requisitos

- Python 3
- Nmap instalado y accesible desde la terminal
- Privilegios de red suficientes para escanear puertos SMB (445)

## ▶️ Uso

```bash
python ADVulnScan.py
```

Luego ingresa la IP del controlador de dominio.

### 🔧 Cómo instalar `smb-vuln-zerologon.nse` si no está incluido en Nmap

1. Descarga el script desde:
   [https://github.com/dirkjanm/CVE-2020-1472/blob/master/nmap/smb-vuln-zerologon.nse](https://github.com/dirkjanm/CVE-2020-1472/blob/master/nmap/smb-vuln-zerologon.nse)

2. Copia el archivo a tu directorio de scripts de Nmap. Ejemplo en Linux:

```bash
sudo cp smb-vuln-zerologon.nse /usr/share/nmap/scripts/
sudo nmap --script-updatedb
```

En Windows, copia el archivo al directorio `scripts` dentro de la carpeta donde instalaste Nmap (por ejemplo, `C:\Program Files (x86)\Nmap\scripts`).

## 📄 Licencia

MIT License
