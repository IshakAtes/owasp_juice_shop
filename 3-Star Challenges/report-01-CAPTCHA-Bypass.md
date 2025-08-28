# 🛡️ Penetration Test Bericht – CAPTCHA Bypass

## 1. Ziel  
Ziel dieses Pentests im OWASP Juice Shop war es, die CAPTCHA-Überprüfung zu umgehen und innerhalb kurzer Zeit mehrere Feedbacks automatisiert abzusenden.

---

## 2. Scope (Testumfang)  
- **Zielsystem:** OWASP Juice Shop – lokal gehostet  
- **Testmethode:** Black-Box  
- **Testzeitraum:** 26.08.2025
- **Tools:** Firefox DevTools, Burp Suite

---

## 3. Vorgehensweise  
1. Ein Terminal mit der Tastenkombination `Strg` + `Alt` + `T` geöffnet und Burp Suite gestartet.
2. Im Menüpunkt Proxy die Option Open Browser ausgewählt.
3. Zur Seite Customer Feedback im OWASP Juice Shop navigiert `http://127.0.0.1:3000/#/contact`.
4. Einen Kommentar und ein Rating eingegeben sowie das Ergebnis des CAPTCHA gelöst, jedoch das Formular noch nicht abgesendet.
5. Im Burp Suite-Tool `Intercept on` aktiviert und anschließend im Juice Shop das Feedback über den Button `Submit` abgeschickt.
6. Burp Suite fing den Request ab. Schrittweise mit `Forward` navigiert, bis der `POST`-Request sichtbar war. Der Request sah beispielhaft folgendermaßen aus:
``` bash
POST /api/Feedbacks/ HTTP/1.1
Host: 127.0.0.1:3000
Content-Length: 75
sec-ch-ua-platform: "Linux"
Accept-Language: en-US,en;q=0.9
Accept: application/json, text/plain, */*
sec-ch-ua: "Not.A/Brand";v="99", "Chromium";v="136"
Content-Type: application/json
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36
Origin: http://127.0.0.1:3000
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://127.0.0.1:3000/
Accept-Encoding: gzip, deflate, br
Cookie: language=en; welcomebanner_status=dismiss; cookieconsent_status=dismiss
Connection: keep-alive

{
    "captchaId":1,
    "captcha":"2",
    "comment":"asfasdfa (anonymous)",
    "rating":"2"
}
```
Der Request wurde anschließend mit Rechte mausklick `Send to Intruder` weitergeleitet.

7. Im Reiter Intruder wurden die Parameter (z. B. comment oder rating) markiert und über den Button `Add §` als Variablen definiert. Anschließend wurde im Tab Payloads eine Liste mit mehreren Kommentaren bzw. Ratings manuell hinzugefügt.

8. Nach dem Einfügen von mehr als zehn Payloads wurde der Angriff über `Start attack` gestartet. Die einzelnen Requests wurden an den Server geschickt.
``` bash
Statuscode 401 → Anfrage abgelehnt.

Statuscode 201 → Anfrage erfolgreich.
```
Bei erfolgreichen Anfragen wurden die Feedbacks gespeichert.

9. Danach wurde der Proxy erneut auf `Intercept off` gesetzt, sodass alle weiteren Requests im Hintergrund verarbeitet werden konnten.

10. Der OWASP Juice Shop bestätigte die erfolgreiche Durchführung der Challenge durch die Einblendung der Meldung:
`You successfully solved a challenge: CAPTCHA Bypass (Submit 10 or more customer feedbacks within 20 seconds.)`

---

## 4. Gefundene Schwachstelle(n)
- Fehlerhafte CAPTCHA-Prüfung:
Das CAPTCHA wird clientseitig generiert und im Backend nicht zuverlässig validiert. Die API akzeptiert Feedback-Requests auch mit falschen oder leeren CAPTCHA-Werten. Dadurch ist ein automatisiertes Absenden mehrerer Feedbacks innerhalb kürzester Zeit möglich.

---

## 5. Risikoanalyse / Auswirkung:
- automatisiert und massenhaft Feedback (Spam) Angriff möglich.
- die Datenbank mit falschen Bewertungen füllen und so die Reputation von Produkten oder des Shops manipulieren.

---

## 6. Empfehlung  
- CAPTCHA-Prüfung serverseitig implementieren (nicht nur clientseitig).
- Requests serverseitig validieren und ungültige Eingaben konsequent blockieren.
- Rate Limiting und Spam-Filter einsetzen, um Missbrauch durch Bots zu verhindern.

---

## 7. Fazit  
Die Challenge zeigt, dass CAPTCHA-Validierung ausschließlich auf Client-Seite unsicher ist.
Ein Angreifer kann mit minimalem Aufwand das CAPTCHA umgehen und automatisierte Anfragen absenden.
Dies unterstreicht, dass Sicherheitskontrollen unbedingt auch serverseitig angewendet werden sollten.

---

