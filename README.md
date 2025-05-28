# 🛡️ Penetration Test Bericht – [Challenge-Name]

## 1. Ziel  
Kurze Beschreibung des Ziels dieser Challenge oder Schwachstelle.  
*z. B. Zugriff auf ein vertrauliches Dokument ohne Autorisierung.*

---

## 2. Scope (Testumfang)  
- **Zielsystem:** OWASP Juice Shop – lokal gehostet  
- **Testmethode:** Black-Box  
- **Testzeitraum:** [z. B. 28.05.2025]  
- **Tools:** [z. B. Firefox DevTools, Burp Suite, etc.]

---

## 3. Vorgehensweise  
Schritt-für-Schritt-Erklärung, wie du vorgegangen bist, z. B.:

1. Webseite aufgerufen  
2. Menüpunkt „Customer Feedback“ geöffnet  
3. Quelltext im Browser untersucht  
4. Nach PDF-Dateien gesucht  
5. Versteckten Link entdeckt  
6. Datei geöffnet  

---

## 4. Gefundene Schwachstelle(n)
Beschreibe technische Einzelheiten, z. B.:

- HTML-Snippet oder Pfad zur Datei
- Verwendete HTTP-Requests
- Manipulation von Parametern
- Screenshots (optional)
- Hinweise auf fehlende Zugriffskontrolle

---

## 5. Risikoanalyse / Auswirkung:
Was könnte ein echter Angreifer dadurch erreichen?  
*z. B. Zugriff auf interne Dokumente mit sensiblen Informationen.*

---

## 6. Empfehlung  
Wie könnte man die Schwachstelle vermeiden? Zum Beispiel:

- Zugriffsbeschränkung über Authentifizierung
- PDF-Links nicht im Quellcode verstecken
- Richtige Berechtigungen auf Serverebene

---

## 7. Fazit  
Was hast du aus der Challenge gelernt?  
*z. B. Der Entwickler hat vermutlich „Security by Obscurity“ verwendet, was kein echter Schutz ist.*

---

