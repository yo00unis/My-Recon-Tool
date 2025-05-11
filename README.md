# 🕵️ Recon Automation Tool

A powerful reconnaissance toolkit for:  
✅ Subdomain Enumeration  
✅ Live Host Detection  
✅ Port Scanning  
✅ Web Crawling  
✅ Directory Fuzzing  

---

## 🔧 Tools Used

### 1. **Subdomain Enumeration**
- [`crt.sh`](https://crt.sh/) - Certificate Transparency log search (via browser or API) 
- [`subfinder`](https://github.com/projectdiscovery/subfinder) - Fast passive subdomain discovery  
- [`sublist3r`](https://github.com/aboul3la/Sublist3r) - OSINT-based subdomain enumeration  
- [`assetfinder`](https://github.com/tomnomnom/assetfinder) - Find domains/subdomains related to a target  
- [`amass`](https://github.com/OWASP/Amass) - In-depth DNS mapping and network topology   
- [`Chaos`](https://github.com/projectdiscovery/chaos-client) - Official API for Project Discovery's Chaos dataset 

### 2. **Live Host Detection**
- [`httpx`](https://github.com/projectdiscovery/httpx) - Fast HTTP/HTTPS host verification  

### 3. **Port Scanning**
- [`nmap`](https://nmap.org/) - Comprehensive network scanning  
- [`masscan`](https://github.com/robertdavidgraham/masscan) - Ultra-fast port scanner  

### 4. **Web Crawling**
- [`katana`](https://github.com/projectdiscovery/katana) - Advanced crawling/spidering  
- [`gau`](https://github.com/lc/gau) - Fetch known URLs from AlienVault/CommonCrawl  
- [`gospider`](https://github.com/jaeles-project/gospider) - Fast web crawler  
- [`waybackurls`](https://github.com/tomnomnom/waybackurls) - Extract archived URLs  

### 5. **Fuzzing**
- [`ffuf`](https://github.com/ffuf/ffuf) - Bruteforce directories/parameters/VHosts  

---
## 🛠️ Installation

### **1. Prerequisite Tools**
Install these dependencies first:

```bash
# Subdomain Enumeration
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install github.com/OWASP/Amass/v3/cmd/amass@latest
pip install Sublist3r
go install github.com/tomnomnom/assetfinder@latest
go install github.com/projectdiscovery/chaos-client/cmd/chaos@latest

# Live Hosts
go install github.com/projectdiscovery/httpx/cmd/httpx@latest

# Port Scanning
#### **Nmap Installation**
- **Linux Users**: 
sudo apt install nmap masscan 
- **Windows Users**:  
  📥 [Download Nmap for Windows](https://nmap.org/download.html) (Official installer)  
  ```powershell
  # After installation, add to PATH:
  [Environment]::SetEnvironmentVariable("PATH", "$env:PATH;C:\Program Files (x86)\Nmap", "User")

## 🚀 Masscan Installation

### **Linux/macOS (Recommended)**
```bash
# Install dependencies (Debian/Ubuntu)
sudo apt update && sudo apt install -y git make gcc

# Clone and compile
git clone https://github.com/robertdavidgraham/masscan.git
cd masscan
make -j

# Install system-wide
sudo cp bin/masscan /usr/local/bin/

# Crawling
go install github.com/projectdiscovery/katana/cmd/katana@latest
go install github.com/lc/gau/v2/cmd/gau@latest
go install github.com/jaeles-project/gospider@latest
go install github.com/tomnomnom/waybackurls@latest

# Fuzzing
go install github.com/ffuf/ffuf@latest
---
## 🐍 Python Environment Setup

### **1. Create Virtual Environment**
```bash
# Linux/macOS
python3 -m venv .venv
source .venv/bin/activate  # Activate

# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\activate

pip install -r requirements.txt

### 🏃 Running the Tool

### **Windows**
```cmd
cd src
python .\main.py
### **Linux/macOS**
```bash
# Navigate to source and run with python3
cd src/ && python3 main.py