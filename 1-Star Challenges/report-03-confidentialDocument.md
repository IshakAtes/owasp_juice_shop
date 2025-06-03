# Penetrationstest-Bericht: "Confidential Document"

**Autor:** Ishak Ates  
**Datum:** 28.05.2025  
**Testobjekt:** OWASP Juice Shop (lokale Testumgebung)  
**Ziel:** Identifikation und Zugriff auf ein vertrauliches Dokument („Confidential Document“)  

---

## 1. Zusammenfassung

In diesem Pentest wurde durch einfache URL-Manipulation ein vertrauliches Dokument in einem öffentlich zugänglichen Verzeichnis entdeckt. Das Problem liegt in der ungeschützten Bereitstellung sensibler Dateien, die nur durch „Security by Obscurity“ versteckt wurden. Die Schwachstelle zeigt, wie wichtig es ist, sensible Pfade zusätzlich durch Zugriffskontrollen abzusichern.

---

## 2. Scope (Testumfang)

- **Zielsystem:** OWASP Juice Shop – lokal gehostet  
- **Testmethode:** Black-Box  
- **Testzeitraum:** 28.05.2025  
- **Tools:** Browser (DevTools, manuelle URL-Manipulation)

---

## 3. Vorgehensweise

1. Navigiert zur Seite **„About Us“** im Hauptmenü.
2. Im Textbereich wurde ein Link entdeckt mit dem Hinweis:  
   _„Check out our boring terms of use if you are interested in such lame stuff.“_
3. Nach dem Klick auf diesen Link wurde der Browser weitergeleitet auf:  
   `http://127.0.0.1:3000/ftp/legal.md`
4. Die URL ließ vermuten, dass sich die Datei in einem zugänglichen Ordner befindet.
5. Durch Entfernen von `legal.md` wurde die neue URL `http://127.0.0.1:3000/ftp` geöffnet.
6. Dort war ein **öffentlich sichtbares Verzeichnislisting** verfügbar, mit mehreren Dateien wie:
   - `.kdbx`
   - `.yml`
   - `.md`
7. Eine dieser Markdown-Dateien enthielt das gesuchte **vertrauliche Dokument**.
8. Die Aufgabe war mit dem Zugriff auf dieses Dokument erfolgreich abgeschlossen.

---

## 4. Gefundene Schwachstelle(n)

- **Directory Listing aktiviert:**  
  Das Verzeichnis `/ftp` war öffentlich zugänglich und listete alle darin enthaltenen Dateien auf. Dadurch konnte ein Benutzer direkt sehen, welche Dateien vorhanden sind, ohne spezifische Links zu kennen.

- **Keine Zugriffsbeschränkung:**  
  Die angezeigten Dateien, darunter auch solche mit sensiblen Informationen, konnten ohne Anmeldung oder Autorisierung aufgerufen werden. Es gab keine Zugriffskontrolle.

- **Security by Obscurity:**  
  Der Schutz des vertraulichen Dokuments beruhte allein darauf, dass der Pfad nicht direkt verlinkt oder leicht auffindbar war. Dies ist keine wirksame Sicherheitsmaßnahme, da neugierige Nutzer oder Angreifer durch einfache Manipulation der URL Zugriff erhalten können.

---

## 5. Risikoanalyse / Auswirkung:

- **Vertraulichkeit:** Hoch gefährdet – vertrauliche Dateien offen einsehbar  
- **Integrität:** Ungefährdet (nur Lesezugriff)  
- **Verfügbarkeit:** Nicht betroffen  

---

## 6. Empfehlung(en)

- **Directory Listing deaktivieren**, z. B. durch entsprechende Webserver-Konfiguration (z. B. Apache/Nginx `Options -Indexes`)
- **Verzeichnisse mit sensiblen Dateien schützen**, z. B. durch Authentifizierung oder Sperrung via `.htaccess`, ACL oder Firewall
- **Keine sensiblen Dateien im Webroot ablegen**, sondern außerhalb des öffentlich zugänglichen Pfades
- **Security by Obscurity vermeiden** – URLs dürfen nie die einzige Schutzmaßnahme sein

---

## 7. Fazit

Diese Aufgabe zeigt, wie durch einfache URL-Manipulation und Neugier auf offen liegende Verzeichnisse zugegriffen werden kann. Ein realer Angreifer könnte damit auf kritische Daten stoßen. Solche Fehler passieren oft unbeabsichtigt – umso wichtiger sind regelmäßige Sicherheitstests, saubere Serverkonfiguration und ein Bewusstsein für mögliche Angriffsvektoren.
