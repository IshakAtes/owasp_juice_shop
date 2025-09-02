# 🛡️ Penetration Test Bericht – [Challenge-Name]

## 1. Objective
The objective of this test was to demonstrate how a review can be submitted on behalf of another user by forging the request, thereby bypassing proper authentication and authorization mechanisms.

---

## 2. Scope
- **Target System:** OWASP Juice Shop – locally hosted 
- **Test Methodology:** Black-Box  
- **Test Period:** 02.09.2025
- **Tools:** Firefox DevTools, Burp Suite

---

## 3. Methodology
1. Logged in as Jim (or another user) by submitting the following payload in the email field and providing any value in the password field to satisfy client-side validation.
``` bash
' OR email = 'jim@juice-sh.op' -- 
```
2. Opened a product review and submitted a rating.
3. Enabled request interception and submitted the review.
4. Examined the request body and identified the `author` field. Modified the value to another name.
5. Forwarded the manipulated request.
6. Confirmed that the review appeared in the shop under Bender’s name, although it was originally submitted by Jim.


---

## 4. Identified Vulnerability(ies)
- Type: Broken Access Control / Insecure Direct Object Reference (IDOR)
- Description: The server relies on client-provided data (author parameter) to identify the review’s owner. Since this field is not validated server-side, attackers can impersonate other users by forging requests.


---

## 5. Risk Analysis / Impact
What could a real attacker achieve through this vulnerability?
e.g., Access to internal documents containing sensitive information.
**Technical Impact:**
- Attackers can impersonate other users when posting reviews.
- Reviews lose integrity since they no longer represent real user feedback.
- Could be extended to other sensitive fields if similar parameter trust exists.

**Business Impact:**
- Reputation damage: fake reviews harm trust in the platform.
- Potential legal issues if forged reviews are considered fraudulent manipulation.
- Users may lose confidence in the authenticity of ratings and comments.

---

## 6. Recommendation  
- Enforce server-side validation of the review’s author based on the authenticated session, not on client-provided parameters.
- Ignore or sanitize the author parameter in incoming requests.
- Implement proper access control checks ensuring that users can only submit reviews under their own account.
- Consider adding logging and monitoring to detect unusual patterns of forged reviews.

---

## 7. Conclusion
This challenge illustrates the importance of not trusting client-side data. Allowing users to define critical identifiers (such as the review’s author) enables impersonation attacks and undermines trust in the system. Proper server-side validation and strict access controls are required to prevent such vulnerabilities.

