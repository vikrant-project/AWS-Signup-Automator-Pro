
# ☁️ AWS Signup Automator Pro
> **High-end, stealth-based automation for AWS account creation and KYC verification.**

[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Engine-Selenium%20UC-orange)](https://github.com/ultrafunkamsterdam/undetected-chromedriver)
[![Status](https://img.shields.io/badge/Status-Advanced-success)](#)

---

## 🔍 What is this Code?
**AWS Signup Automator Pro** is a sophisticated automation suite designed to navigate the complex multi-stage signup process of Amazon Web Services (AWS). It utilizes `undetected-chromedriver` (UC) to bypass bot-detection algorithms and mimics human behavior through variable typing speeds and randomized delays.

The script handles everything from initial email registration to the critical **KYC (Know Your Customer) Identity Confirmation** phase.

---

## 🚀 Why Use It?
Setting up AWS accounts manually is a tedious, 10-step process prone to human error. This tool is essential for:
* **Efficiency:** Automates the repetitive data entry of contact info and address details.
* **Stealth:** Uses Advanced Selenium techniques to avoid being flagged as a "scraper" or "bot."
* **KYC Integration:** Specialized logic to handle the Indian AWS region (including PAN card and UPI verification steps).

---

## 💎 Importance
In modern cloud architecture, the ability to programmatically initialize account environments is highly valued.
1.  **Anti-Detection:** Uses `uc` to ensure the browser fingerprint looks like a real user.
2.  **Robust Error Handling:** Features a "Manual Fallback" mode—if a step fails, the browser stays open for you to finish, rather than crashing the whole process.
3.  **Complex Field Mapping:** Automatically handles tricky AWS UI elements like filtered country dropdowns and dynamic plan selections.

---

## ⚙️ How It Works
The automation follows a 10-Phase logic flow:



1.  **Stealth Initialization:** Launches a hardened Chrome instance.
2.  **Identity Setup:** Enters email and account name using `slow_type` logic.
3.  **Interactive OTP:** Pauses for the user to provide the verification code from their email.
4.  **Contact Synthesis:** Automatically maps a full "Personal" profile including address and phone.
5.  **Country Filtration:** Navigates the AWS-specific "combobox" to select the correct region (e.g., India) without triggering errors.
6.  **KYC Engine:** Handles the specific `#/kyc` portal, selecting "Personal use" and "Individual" ownership.
7.  **Document Injection:** Uploads the required `soul.png` identity document directly to the file input.

---

## 🛠️ Installation & Setup

### 1. Prerequisites
* **Python 3.9+**
* **Chrome Browser** installed on the system.
* **Identity Document:** You must have a file named `soul.png` in the script directory.

### 2. Clone & Install
```bash
git clone https://github.com/vikrant-project/AWS-Signup-Automator-Pro
cd AWS-Signup-Automator-Pro
pip install undetected-chromedriver selenium
```

### 3. Usage
```bash
python3 aws_signup_bot.py
```

---

## 🎨 High-End Features
* **Human-Mimicry:** Uses `ActionChains` and JavaScript injection to interact with elements that standard bots cannot "see."
* **Smart Delays:** Every action is buffered with `human_delay()` to prevent account flagging.
* **Visual Logging:** The console provides real-time, color-coded updates on every phase of the automation.

---

**Disclaimer:** This tool is for educational purposes and internal workflow automation only. Ensure you comply with the AWS Terms of Service when using automation.
