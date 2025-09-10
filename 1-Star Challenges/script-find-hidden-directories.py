from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Selenium Setup
options = Options()
options.add_argument("--headless")
service = Service(executable_path="/usr/local/bin/geckodriver")  # anpassen falls nötig
driver = webdriver.Firefox(service=service, options=options)

# Juice Shop URL
base_url = "http://127.0.0.1:3000/#"

# Wordlist laden
with open("dirs_wordlist.txt", "r") as file:
    paths = [line.strip() for line in file.readlines()]

# Ergebnisliste
found_paths = []

# Teste jede Pfad-Erweiterung
for path in paths:
    test_url = f"{base_url}/{path}"
    try:
        driver.get(test_url)
        time.sleep(1)  # ggf. anpassen, falls Ladezeiten höher sind
        source = driver.page_source

        # Beispiel: wenn sich der Seiteninhalt *deutlich* ändert (z. B. nicht mehr nur 404-Seite o.ä.)
        if "error" not in source.lower() and "404" not in source:
            print(f"[+] Mögliches Verzeichnis gefunden: /{path}")
            found_paths.append(f"/{path}")
        else:
            print(f"[-] Nicht gefunden: /{path}")
    except Exception as e:
        print(f"[!] Fehler bei /{path}: {e}")

driver.quit()

# Ergebnisse speichern
with open("found_dirs.txt", "w") as f:
    for path in found_paths:
        f.write(path + "\n")

print("\n✅ Verzeichnissuche abgeschlossen. Gefundene Pfade gespeichert in found_dirs.txt")
