# OWASP Juice Shop – Educational Pentesting Project

## 📑 Table of Contents
1. [Project Description](#-project-description)  
2. [Disclaimer](#️-disclaimer)  
3. [Challenges](#️-challenges)  
   - [CAPTCHA Bypass](#1-captcha-bypass)  
   - [Cross-Site Scripting (XSS)](#2-cross-site-scripting-xss)  
   - [Forged Review (Broken Access Control)](#3-forged-review---review-manipulation-broken-access-control)  
4. [Security Risks](#-security-risks)  

---

## 📘 Project Description
This repository documents the solutions to several hacking challenges within the **OWASP Juice Shop**.  
The purpose of this project is **educational pentesting**: understanding common web vulnerabilities by exploiting them in a safe and legal environment.

---

## ⚠️ Disclaimer
This repository and its content are for **educational purposes only**.  
All demonstrated attacks were performed exclusively against the intentionally vulnerable application **OWASP Juice Shop**.  
Do not attempt to apply these techniques on any system without explicit authorization.

---

## 🕵️ Challenges

### 1. CAPTCHA Bypass
- **Category:** Improper Input Validation / Broken Anti-Automation 
- **Description:** Submitted more than 10 feedback entries within 20 seconds by bypassing the CAPTCHA validation (e.g., reusing a valid solution or disabling the check).
- **Risk:** Allows attackers to flood the system with automated requests, perform spam attacks, or degrade system availability. 
- **Report:** [CAPTCHA Bypass – Pentest Report](https://github.com/IshakAtes/owasp_juice_shop/blob/6763e339f70e03c7b93921a9c8998b3075146951/3-Star%20Challenges/report-01-CAPTCHA-Bypass.md)
- **Video:** [CAPTCHA Bypass – Video Walkthrough](https://go.screenpal.com/watch/cTQV6Anoexj)  

### 2. Cross-Site Scripting (XSS)
- **Category:** XSS (Cross-Site Scripting)  
- **Description:** Injected malicious JavaScript into a product review that executes in other users’ browsers.  
- **Risk:** Can steal session tokens, hijack user accounts, perform unauthorized actions, or spread malware.
- **Report:** [Cross-Site Scripting – Pentest Report](https://github.com/IshakAtes/owasp_juice_shop/blob/6763e339f70e03c7b93921a9c8998b3075146951/3-Star%20Challenges/report-02-ClientSide-XSS-Protection.md)
- **Video:** [Cross-Site Scripting – Video Walkthrough](https://go.screenpal.com/watch/cTQf6Hno25D)

### 3. Forged Review - Review Manipulation (Broken Access Control)
- **Category:** Broken Access Control  
- **Description:** While logged in as Jim, submitted a new product review but modified the `author` field so that it appeared under another user’s name.  
- **Risk:** Attackers can impersonate other users, damage reputations, and undermine trust in the integrity of user-generated content.
- **Report:** [Review Manipulation – Pentest Report](https://github.com/IshakAtes/owasp_juice_shop/blob/1e67f59cb8035f66174743965cb203810c37e6f7/3-Star%20Challenges/report-03-ForgedReview.md)
- **Video:** [Review Manipulation – Video Walkthrough](https://go.screenpal.com/watch/cTQerdnolNC)  
  

---

## 🔒 Security Risks
The vulnerabilities exploited in these challenges highlight **common real-world risks**:  
- **Improper Input Validation / Broken Anti-Automation** can be abused to flood applications with automated requests, enabling spam or denial-of-service scenarios.  
- **Cross-Site Scripting (XSS)** exposes end-users to identity theft, session hijacking, phishing, and malware injection.  
- **Broken Access Control** enables attackers to impersonate users, alter sensitive data, or undermine trust in application integrity.  

Applying secure coding practices, implementing proper access controls, and enforcing input validation are essential to mitigate these risks.
