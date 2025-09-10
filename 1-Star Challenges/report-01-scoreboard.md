# 🛡️ Penetrationstest-Bericht – OWASP Juice Shop

**Autor:** Ishak Ates 
**Datum:** 22.05.2025  
**Testobjekt:** OWASP Juice Shop (lokale Testumgebung)  
**Ziel:** Identifikation und Dokumentation von Sicherheitslücken zu Schulungszwecken

---

## 1. Zusammenfassung (Executive Summary)

**Kurzfassung für nicht-technische Leser:**

Im Rahmen dieses Tests wurde eine versteckte Funktionalität in der Webanwendung OWASP Juice Shop aufgedeckt – das sogenannte Score Board, welches alle vorhandenen Challenges listet. Diese Funktion war nicht direkt über die Hauptnavigation erreichbar, konnte aber durch gezielte URL-Manipulation entdeckt werden. 

---

## 2. Scope (Testumfang)

- **Zielsystem:** OWASP Juice Shop – lokal gehostet  
- **Testzeitraum:** [22.05.2025 / 3std]  
- **Testmethode:** Black-Box-Ansatz (nur Nutzerrechte, keine Code-Einsicht)  
- **Verwendete Tools:**  
  - Browser DevTools
  - Burp Suite  

---

## 3. Methodik

Kurze Beschreibung des Vorgehens:

- Nutzung des Juice Shop Interfaces zur Exploration  
- Analyse der Client-Server-Kommunikation (z. B. mit DevTools und BurpSuite)  

---

## 4. Gefundene Schwachstellen

### 4.1 Account Enumeration beim Login

**Beschreibung:**  
Die Seite mit dem Score Board ist zwar nicht direkt über das Menü erreichbar, aber öffentlich über eine bekannte URL zugänglich. Dadurch kann ein Benutzer alle Challenges sehen, was bei echten Anwendungen zu ungewolltem Informationsleck führen könnte.

**Reproduktionsschritte:**

1. Öffne die Startseite
2. Navigiere zu: `http://localhost:3000/#/score-board`
3. Die Seite mit dem Score Board erscheint

**Auswirkung:**  
In produktiven Umgebungen könnte ein ähnliches Verhalten dazu führen, dass interne Funktionen versehentlich öffentlich zugänglich sind.

**Empfehlung:**  
Versteckte Seiten sollten nicht nur durch das Fehlen von Navigationselementen „geschützt“ werden, sondern durch echte Zugriffskontrollen (z. B. Authentifizierung, Rollenprüfung). In produktiven Systemen sollte Security by Obscurity niemals als alleinige Maßnahme verwendet werden.

---

## 5. Fazit

Die erste Challenge des Juice Shops demonstriert anschaulich, wie leicht versteckte Funktionen gefunden werden können – insbesondere wenn URLs vorhersehbar sind oder der Code Hinweise enthält. Die Übung sensibilisiert für das Thema „versteckte Informationen“ und betont die Wichtigkeit echter Zugriffskontrollen.


