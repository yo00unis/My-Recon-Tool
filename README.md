# 🕵️ Recon Automation Tool

A powerful reconnaissance toolkit for:\
✅ Subdomain Enumeration\
✅ Live Host Detection\
✅ Port Scanning\
✅ Web Crawling\
✅ Directory Fuzzing

---

## 🔧 Tools Overview

| Tool          | Type                  | Description                                  | Link                                                    |
| ------------- | --------------------- | -------------------------------------------- | ------------------------------------------------------- |
| `subfinder`   | Subdomain Enumeration | Fast passive subdomain discovery             | [GitHub](https://github.com/projectdiscovery/subfinder) |
| `sublist3r`   | Subdomain Enumeration | OSINT-based subdomain enumeration            | [GitHub](https://github.com/aboul3la/Sublist3r)         |
| `assetfinder` | Subdomain Enumeration | Find related domains/subdomains              | [GitHub](https://github.com/tomnomnom/assetfinder)      |
| `crt.sh`      | Subdomain Enumeration | Certificate Transparency log search          | [Website](https://crt.sh/)                              |
| `httpx`       | Live Host Detection   | Fast HTTP/HTTPS host verification            | [GitHub](https://github.com/projectdiscovery/httpx)     |
| `gowitness`   | Screenshots           | Capture screenshots of live hosts            | [GitHub](https://github.com/sensepost/gowitness)        |
| `nmap`        | Port Scanning         | Comprehensive network scanner                | [Official](https://nmap.org/)                           |
| `naabu`       | Port Scanning         | Fast port scanning tool                      | [GitHub](https://github.com/projectdiscovery/naabu)     |
| `katana`      | Web Crawling          | Advanced crawling/spidering                  | [GitHub](https://github.com/projectdiscovery/katana)    |
| `gau`         | Web Crawling          | Fetch known URLs from CommonCrawl/AlienVault | [GitHub](https://github.com/lc/gau)                     |
| `gospider`    | Web Crawling          | Fast web crawler                             | [GitHub](https://github.com/jaeles-project/gospider)    |
| `waybackurls` | Web Crawling          | Extract archived URLs                        | [GitHub](https://github.com/tomnomnom/waybackurls)      |
| `ffuf`        | Fuzzing               | Bruteforce directories/parameters/VHosts     | [GitHub](https://github.com/ffuf/ffuf)                  |

---

## 🏃 Running the Tool (CLI)

The tool is fully **CLI-driven**.

### **Basic Usage**

```bash
python tool.py -d example.com
```

### **Common Options**

| Flag                             | Description                                                      |
| -------------------------------- | ---------------------------------------------------------------- |
| `-d`, `--domain`                 | Target domain (required)                                         |
| `-rd`, `--result-dir`            | Directory to save results (default: `ReconResult`)               |
| `-se`, `--subdomain-enumeration` | Enable subdomain enumeration                                     |
| `-sh`, `--screenshots`           | Take screenshots of live hosts                                   |
| `-ps`, `--port-scan`             | Enable port scanning                                             |
| `-p`, `--ports`                  | Ports to scan (comma-separated, default: `443,80`)               |
| `-c`, `--crawling`               | Enable web crawling                                              |
| `-f`, `--fuzzing`                | Enable directory fuzzing                                         |
| `-fw`, `--fuzz-wordlist`         | Fuzzing wordlist file (default: `directory-list-2.3-medium.txt`) |
| `-t`, `--threads`                | Max number of threads (default: 15)                              |

---

### **Examples**

1. **Subdomain enumeration + crawling**

```bash
python tool.py -d hackerone.com -se -c
```

2. **Port scanning specific ports + fuzzing**

```bash
python tool.py -d example.com -ps -p 80,443 -f -fw my_wordlist.txt
```

3. **Full scan with 20 threads**

```bash
python tool.py -d example.com -se -sh -ps -c -f -t 20
```

---

### ✅ Notes

- All results are saved in the specified `--result-dir` folder (default: `ReconResult`).
- Boolean flags (`-se`, `-sh`, `-ps`, `-c`, `-f`) are optional. Include the flag to enable, omit to disable.
- The tool will automatically create the necessary folders and files inside the result directory.

