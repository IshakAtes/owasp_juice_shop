# 🛡️ Penetration Test Report – CAPTCHA Bypass

## 1. Objective
The objective of this penetration test in OWASP Juice Shop was to bypass the CAPTCHA verification and submit multiple feedbacks automatically within a short period of time.

---

## 2. Scope
- **Target System:** OWASP Juice Shop – locally hosted
- **Test Methodology:** Black-Box
- **Test Date:** 2025-08-26
- **Tools:** Firefox DevTools, Burp Suite

---

## 3. Methodology
1. Opened a terminal using `Ctrl` + `Alt` + `T` and started Burp Suite.
2. In the Proxy tab, selected the option Open Browser.
3. Navigated to the Customer Feedback page in OWASP Juice Shop: `http://127.0.0.1:3000/#/contact`.
4. Entered a comment and rating, solved the CAPTCHA, but did not yet submit the form.
5. Activated `Intercept on` in Burp Suite and then clicked the `Submit` button in Juice Shop.
6. Burp Suite intercepted the request. Using `Forward`, navigated step by step until the `POST`request was visible. The request looked as follows:
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
The request was then forwarded to Intruder using Right-click `Send to Intruder`.

7. In the Intruder tab, parameters (e.g., comment or rating) were marked and added as variables using the `Add §` button. In the Payloads tab, a list of multiple comments/ratings was manually added.

8. After adding more than ten payloads, the attack was launched with `Start attack`. The individual requests were sent to the server:
``` bash
Statuscode 401 → Request denied.

Statuscode 201 → Request successful.
```
For successful requests, the feedbacks were stored.

9. The proxy was then set to `Intercept off` again so that all further requests could be processed in the background.

10. OWASP Juice Shop confirmed successful completion of the challenge with the message:
`You successfully solved a challenge: CAPTCHA Bypass (Submit 10 or more customer feedbacks within 20 seconds.)`

---

## 4. Identified Vulnerability
- Broken CAPTCHA Validation:
The CAPTCHA is generated client-side and not properly validated on the backend. The API accepts feedback requests even with incorrect or empty CAPTCHA values, allowing automated submission of multiple feedbacks within seconds.

---

## 5. Risk Analysis / Impact
- Enables automated and mass feedback (spam) attacks.
- Database can be flooded with fake ratings, manipulating the reputation of products or the shop.

---

## 6. Recommendation
- Implement server-side CAPTCHA validation (not only client-side).
- Strictly validate requests on the server and block invalid inputs.
- Use rate limiting and spam filters to prevent abuse by bots.

---

## 7. Conclusion
This challenge demonstrates that relying solely on client-side CAPTCHA validation is insecure.
An attacker can bypass the CAPTCHA with minimal effort and send automated requests.
It underlines the importance of always implementing security controls on the server side.


