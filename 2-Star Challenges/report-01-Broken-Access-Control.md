# Penetration Test Bericht – Access the administration section of the store

## 1. Ziel  
Ziel dieses Pentests im OWASP Juice Shop war es, unautorisierten Zugang zum Adminbereich zu erlangen – also Adminrechte zu bekommen.

---

## 2. Scope (Testumfang)  
- **Zielsystem:** OWASP Juice Shop – lokal gehostet  
- **Testmethode:** Black-Box  
- **Testzeitraum:** 17.07.2025 
- **Tools:** DevTools

---

## 3. Vorgehensweise  
1. Zum Login Bereich vom Owasp Juice Shop Navigieren. In unserm Fall: `http://127.0.0.1:3000/#/login`.
2. Im E-Mail Feld folgenden String eingeben:
``` bash
'OR 1=1 --
```
3. Im Passwort Feld beliebigen Wert eingeben, damit die Validierung, das absenden nicht blockiert.
4. Nach dem Klick auf "Login" erfolgte der direkte Zugriff – man war als Admin eingeloggt.

---

## 4. Gefundene Schwachstelle(n)
- Login als Admin ohne gültige Zugangsdaten
- Zugriff auf alle Benutzerkonten, inklusive der Möglichkeit, sie zu deaktivieren oder zu löschen

---

## 5. Risikoanalyse / Auswirkung:
- Da die eingabe im Suchfeld ungefilter ausgeführt wird kann Fremdcode ohne probleme hinzugegeben werden.
- Die Website kann nach belieben manipuliert werden - Vollständige Kontrolle
- Zugriff auf sensible Daten wie Bankverbindungen, persönliche Infos, Bestellhistorien
- Geldtransfers könnten durchgeführt oder Konten kompromittiert werden
- Daten können gestohlen, verkauft oder manipuliert werden
- Potenziell Nachladen von Schadcode oder Umleitungen auf Phishingseiten

---

## 6. Empfehlung  
- Prepared Statements verwenden: Eingaben dürfen nie direkt in SQL-Queries landen.
- Input-Validierung & Sanitizing: Sowohl client- als auch serverseitig müssen Eingaben validiert werden.
- Fehlermeldungen beschränken: Keine technischen Details preisgeben, die Angreifern helfen könnten.
- Zugriffsrechte trennen: Adminfunktionen nur über sichere, authentifizierte Kanäle anbieten.
- Security Testing automatisieren: Z. B. durch CI/CD-Pipelines mit automatischen Sicherheitsscans.

---

## 7. Fazit  
Der Test zeigt, wie gefährlich es wird, wenn Eingaben nicht richtig geprüft und abgesichert werden – sowohl im Frontend als auch im Backend. Mit einer einfachen SQL-Injection konnte ich Adminzugriff bekommen und hätte damit das komplette System übernehmen können – inklusive Benutzerdaten, Bankinformationen und Rechteverwaltung. Solche Lücken sind kritisch und sollten in produktiven Umgebungen unbedingt verhindert werden.

---

