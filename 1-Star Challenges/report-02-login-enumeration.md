# 🛡️ Penetrationstest-Bericht – OWASP Juice Shop  
**Autor:** Ishak Ates 
**Datum:** 25.05.2025  
**Testobjekt:** OWASP Juice Shop (lokale Testumgebung)  
**Ziel:** Identifikation und Dokumentation der Schwachstelle in der Challenge „Zero Stars“  

---

## 1. Zusammenfassung (Executive Summary)

Im Rahmen dieses penetrationstests im OWASP Juice Shop wurde die Challenge „Zero Stars“ erfolgreich abgeschlossen. Ziel war es, das zentrale Feedback-Formular zur Website-Bewertung zu manipulieren, sodass ein Eintrag mit null Sternen akzeptiert wird. Diese Bewertung ist im regulären Webinterface nicht vorgesehen. Die Schwachstelle beruht auf fehlender serverseitiger Validierung.

---

## 2. Scope (Testumfang)

- **Zielsystem:** OWASP Juice Shop – lokal gehostet  
- **Testmethode:** Black-Box  
- **Testzeitraum:** 22.05.2025  
- **Tools:** DevTools (Browser), Burp Suite

---

## 3. Methodik

- Navigation über das Hauptmenü zu **„Customer Feedback“**  
- Ausfüllen des Formulars mit Kommentar und Sternebewertung (z. B. 1–5 Sterne)  
- Abfangen der HTTP-Anfrage im burpsuite Proxy  
- Manuelles Ersetzen des Werts `rating` mit `0` auf `apply Changes` klicken
- Absenden der manipulierten Anfrage
- Feedback mit 0 Sternen wurde erfolgreich gespeichert  

---

## 4. Gefundene Schwachstelle

### 4.1 Bewertung der Website mit 0 Sternen

- **Schweregrad:** Niedrig  
- **Beschreibung:**  
  Die Feedback-Funktion erlaubt es über manipulierte HTTP-Anfragen, eine Bewertung mit null Sternen abzugeben – obwohl das Interface nur 1 bis 5 Sterne zulässt. Das Backend validiert den Eingabewert nicht korrekt.  

- **Reproduktionsschritte:**  
  1. In der Webanwendung zum Menüpunkt „Customer Feedback“ navigieren  
  2. Beliebige Nachricht und Sternebewertung ausfüllen  
  3. Netzwerk-Request im Burbsuite-Tool abfangen  
  4. Wert `rating` auf `0` ändern  
  5. Anfrage absenden (apply changes)
  6. Feedback mit 0 Sternen erscheint unter „About Us“  

- **Auswirkung:**  
  Die Feedback-Funktion kann manipuliert werden, um Bewertungen außerhalb des vorgesehenen Spektrums abzugeben. Dies ist zwar funktional nicht kritisch, zeigt aber eine Lücke in der serverseitigen Validierung. In realen Systemen könnte dies z. B. Bewertungssysteme beeinflussen.

- **Empfehlung:**  
  Im Backend sollten alle Eingaben serverseitig auf Plausibilität geprüft werden (z. B. `rating` ∈ [1,5]). Eingaben außerhalb des erlaubten Bereichs müssen mit einem Fehler abgelehnt werden.

---

## 5. Fazit

Diese Challenge demonstriert die Wichtigkeit serverseitiger Eingabevalidierung. Frontend-Kontrollen sind leicht umgehbar. Auch scheinbar harmlose Eingaben wie Feedback-Ratings müssen auf Serverseite abgesichert sein, um Manipulationen zu vermeiden.

---

## 6. Anhang

{
    "captchaId":17,
    "captcha":"13",
    "comment":"Die Seite gefällt mir überhaupt nicht. (anonymous)",
    "rating":0
}