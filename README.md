# OWASP Juice Shop – Educational Pentesting Project

## 📑 Table of Contents
1. [Project Description](#project-description)  
2. [Disclaimer](#disclaimer)  
3. [Challenges](#challenges)  
   - [SQL Injection](#1-sql-injection)  
   - [Review Manipulation (Broken Access Control)](#2-review-manipulation-broken-access-control)  
   - [Cross-Site Scripting (XSS)](#3-cross-site-scripting-xss)  
4. [Loom Videos](#loom-videos)  
5. [Security Risks](#security-risks)  

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

### 1. SQL Injection
- **Category:** Injection  
- **Description:** Logged in as another user by bypassing authentication with a crafted SQL query.  
- **Risk:** Allows attackers to access or modify sensitive data, compromise accounts, and potentially gain admin privileges.

### 2. Review Manipulation (Broken Access Control)
- **Category:** Broken Access Control  
- **Description:** While logged in as Jim, manipulated another user's review (Bender) and changed its content.  
- **Risk:** Attackers can tamper with user-generated content, undermine trust, and cause reputational damage.

### 3. Cross-Site Scripting (XSS)
- **Category:** XSS (Cross-Site Scripting)  
- **Description:** Injected malicious JavaScript into a product review that executes in other users’ browsers.  
- **Risk:** Can steal session tokens, hijack user accounts, perform unauthorized actions, or spread malware.

---

## 🎥 Loom Videos
- [SQL Injection – Video Walkthrough](<your-loom-link-here>)  
- [Review Manipulation – Video Walkthrough](<your-loom-link-here>)  
- [Cross-Site Scripting – Video Walkthrough](<your-loom-link-here>)  

---

## 🔒 Security Risks
The vulnerabilities exploited in these challenges represent **real-world risks**:  
- **Injection attacks** threaten confidentiality and integrity of databases.  
- **Broken Access Control** allows privilege escalation and unauthorized modifications.  
- **XSS** puts end-users at risk, enabling identity theft and phishing.  

Proper security testing and secure coding practices are essential to prevent such attacks.
