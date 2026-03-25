#!/usr/bin/env python3
"""
AWS Account Signup Automation Script
Fixed and improved version with proper error handling and field mapping
Test email: nokibox476@icousd.com
"""

import time
import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc

def human_delay(min_sec=0.5, max_sec=1.5):
    """Simulate human-like delays"""
    time.sleep(random.uniform(min_sec, max_sec))

def slow_type(element, text):
    """Type text slowly to mimic human behavior"""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.12))

def setup_driver():
    """Setup undetected Chrome driver"""
    print("\n[INFO] Setting up Stealth Chrome Driver...")
    options = uc.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # Explicitly disable headless mode to show browser window
    options.headless = False
    driver = uc.Chrome(options=options, use_subprocess=True, headless=False)
    return driver

def main():
    driver = None
    try:
        print("\n" + "="*60)
        print("   AWS SIGNUP AUTOMATION - COMPLETE WORKFLOW")
        print("="*60 + "\n")

        driver = setup_driver()

        # --- PHASE 1: START SIGNUP PROCESS ---
        print("[PHASE 1] Navigating to AWS Free Tier page...")
        driver.get("https://aws.amazon.com/free/")
        human_delay(2, 3)

        # Click on Create Free Account or Signup button
        try:
            signup_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'signup') or contains(text(), 'Create') or contains(text(), 'Sign up')]"))
            )
            signup_button.click()
            print("[SUCCESS] Clicked signup button")
        except Exception as e:
            print(f"[ERROR] Could not find signup button: {e}")
            return

        # Wait for new tab/window and switch to it
        human_delay(2, 3)
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            print("[INFO] Switched to signup window")

        # --- PHASE 2: EMAIL AND ACCOUNT NAME ---
        print("\n[PHASE 2] Entering email and account name...")

        # Use the provided test email
        email = "gesal65229@hudisk.com"
        account_name = "TestAccount_" + str(random.randint(1000, 9999))

        print(f"[INFO] Using email: {email}")
        print(f"[INFO] Using account name: {account_name}")

        try:
            email_field = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.NAME, "emailAddress"))
            )
            slow_type(email_field, email)
            print("[SUCCESS] Email entered")

            name_field = driver.find_element(By.NAME, "accountName")
            slow_type(name_field, account_name)
            print("[SUCCESS] Account name entered")

            submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            submit_btn.click()
            print("[SUCCESS] Submitted email/account form")
            human_delay(2, 3)
        except Exception as e:
            print(f"[ERROR] Failed to enter email/account: {e}")
            return

        # --- PHASE 3: OTP VERIFICATION ---
        print("\n[PHASE 3] OTP Verification...")
        otp = input("\n>>> Enter the OTP you received: ").strip()

        try:
            otp_field = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.NAME, "otp"))
            )
            slow_type(otp_field, otp)
            print("[SUCCESS] OTP entered")

            verify_btn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='verify-email-submit-button']")
            verify_btn.click()
            print("[SUCCESS] OTP submitted")
            human_delay(2, 3)
        except Exception as e:
            print(f"[ERROR] Failed OTP verification: {e}")
            return

        # --- PHASE 4: PASSWORD CREATION ---
        print("\n[PHASE 4] Creating password...")

        # Generate a strong password
        password = "SoulCracks@90"
        print(f"[INFO] Using password: {password}")

        try:
            pwd_field = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            slow_type(pwd_field, password)
            print("[SUCCESS] Password entered")

            repwd_field = driver.find_element(By.NAME, "rePassword")
            slow_type(repwd_field, password)
            print("[SUCCESS] Password confirmed")

            pwd_submit_btn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='create-password-submit-button']")
            pwd_submit_btn.click()
            print("[SUCCESS] Password submitted")
            human_delay(3, 4)
        except Exception as e:
            print(f"[ERROR] Failed password creation: {e}")
            return

        # --- PHASE 5: PLAN SELECTION (if appears) ---
        print("\n[PHASE 5] Handling plan selection...")
        try:
            basic_plan_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-analytics*='Account_Plan_Selection_Trial'], button[data-analytics*='Basic']"))
            )
            basic_plan_btn.click()
            print("[SUCCESS] Selected Basic/Free plan")
            human_delay(2, 3)
        except TimeoutException:
            print("[INFO] Plan selection not required or already selected")

        # --- PHASE 6: CONTACT INFORMATION ---
        print("\n[PHASE 6] Filling contact information...")
        print("[INFO] This is the critical form with all required fields")

        # Sample contact details
        contact_info = {
            "full_name": "John Doe Smith",
            "phone": "(630) 966-8944",
            "country": "India",
            "address": "123 Main Street, Apartment 4B",
            "city": "Mumbai",
            "state": "Maharashtra",
            "postal_code": "400001"
        }

        print(f"[INFO] Contact Info:")
        for key, value in contact_info.items():
            print(f"  - {key}: {value}")

        try:
            # Wait for contact form to load
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, "address.fullName"))
            )
            print("[INFO] Contact form loaded")
            human_delay(1, 2)

            # 0. ACCOUNT TYPE - Select "Personal" radio button
            print("[PROCESS] Selecting account type: Personal...")
            try:
                # Try multiple selectors for account type
                personal_radio = None
                selectors = [
                    "input[value='Personal'][type='radio']",
                    "input[id='Personal']",
                    "//input[@type='radio' and contains(@value, 'Personal')]",
                    "//label[contains(text(), 'Personal')]//input[@type='radio']"
                ]

                for selector in selectors:
                    try:
                        if selector.startswith("//"):
                            personal_radio = driver.find_element(By.XPATH, selector)
                        else:
                            personal_radio = driver.find_element(By.CSS_SELECTOR, selector)
                        if personal_radio:
                            break
                    except:
                        continue

                if personal_radio:
                    driver.execute_script("arguments[0].scrollIntoView(true);", personal_radio)
                    human_delay(0.5, 1)
                    driver.execute_script("arguments[0].click();", personal_radio)
                    print("[SUCCESS] Account type selected: Personal")
                    human_delay(1, 2)
                else:
                    print("[INFO] Account type field not found or not required")
            except Exception as e:
                print(f"[INFO] Account type selection skipped: {e}")

            # 1. FULL NAME (address.fullName)
            print("[PROCESS] Entering full name...")
            fullname_field = driver.find_element(By.ID, "address.fullName")
            fullname_field.clear()
            slow_type(fullname_field, contact_info["full_name"])
            print(f"[SUCCESS] Full name entered: {contact_info['full_name']}")

            # 2. PHONE NUMBER (address.phoneNumber)
            print("[PROCESS] Entering phone number...")
            phone_field = driver.find_element(By.ID, "address.phoneNumber")
            phone_field.clear()
            slow_type(phone_field, contact_info["phone"])
            print(f"[SUCCESS] Phone number entered: {contact_info['phone']}")

            # 3. COUNTRY (address.country) - THIS IS THE FIXED PART
            print("[PROCESS] Selecting country...")
            try:
                country_trigger = driver.find_element(By.ID, "address.country")
                driver.execute_script("arguments[0].scrollIntoView(true);", country_trigger)
                human_delay(0.5, 1)

                # Click to open dropdown
                country_trigger.click()
                human_delay(1, 1.5)

                # Find the filter input within the dropdown and type
                print("[INFO] Looking for dropdown filter input...")
                try:
                    # Wait for the dropdown to open and find the filter input
                    filter_input = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "input[role='combobox'], input[aria-expanded='true']"))
                    )
                    print("[INFO] Found filter input, typing 'India'...")
                    filter_input.clear()
                    filter_input.send_keys("India")
                    human_delay(2, 3)  # Wait for options to filter
                except Exception as e:
                    print(f"[WARNING] Could not find filter input: {e}")
                    # Fallback: send keys to active element
                    actions = ActionChains(driver)
                    actions.send_keys("India").perform()
                    human_delay(2, 3)

                # FIXED: Wait for options to appear and find the EXACT match
                print("[INFO] Waiting for options to load...")

                # Try multiple selectors for dropdown options
                india_options = []
                selectors = [
                    "//div[@role='option' and contains(., 'India')]",
                    "//li[@role='option' and contains(., 'India')]",
                    "//div[contains(@class, 'option') and contains(., 'India')]",
                    "//*[@role='option']//span[contains(text(), 'India')]/..",
                    "//*[contains(@class, 'awsui_option') and contains(., 'India')]"
                ]

                for selector in selectors:
                    try:
                        WebDriverWait(driver, 3).until(
                            EC.presence_of_element_located((By.XPATH, selector))
                        )
                        india_options = driver.find_elements(By.XPATH, selector)
                        if len(india_options) > 0:
                            print(f"[INFO] Found {len(india_options)} options using selector: {selector}")
                            break
                    except:
                        continue

                if not india_options:
                    # Last resort: get all visible text elements
                    print("[INFO] Trying broader search for options...")
                    india_options = driver.find_elements(By.XPATH, "//*[contains(text(), 'India')]")

                print(f"[INFO] Total options found containing 'India': {len(india_options)}")

                # Find the exact "India" option (not "British Indian Ocean Territory")
                target_option = None
                for option in india_options:
                    option_text = option.text.strip()
                    print(f"[INFO] Checking option: '{option_text}'")

                    # Match EXACTLY "India" - not "Indian" or any other variant
                    if option_text == "India":
                        target_option = option
                        print(f"[SUCCESS] Found exact match: '{option_text}'")
                        break

                if not target_option:
                    # Try a more flexible approach - look for option that is exactly "India"
                    print("[INFO] Trying exact text match with XPath...")
                    try:
                        target_option = driver.find_element(By.XPATH,
                            "//*[@role='option'][normalize-space(text())='India'] | "
                            "//div[contains(@class, 'option')][normalize-space(.)='India'] | "
                            "//li[normalize-space(.)='India']"
                        )
                        print("[SUCCESS] Found India using exact text match")
                    except:
                        print("[ERROR] Could not find exact 'India' option")
                        raise Exception("Exact 'India' option not found")

                # Scroll to and click the target option
                driver.execute_script("arguments[0].scrollIntoView(true);", target_option)
                human_delay(0.5, 1)

                # Try regular click first
                try:
                    target_option.click()
                    print(f"[SUCCESS] Clicked on India option")
                except:
                    # Fallback to JavaScript click
                    driver.execute_script("arguments[0].click();", target_option)
                    print(f"[SUCCESS] Clicked on India option (JS)")

                print(f"[SUCCESS] Country selected: {contact_info['country']}")
                human_delay(1, 2)
            except Exception as e:
                print(f"[WARNING] Country selection issue: {e}")
                print("[INFO] Trying alternative method...")
                import traceback
                traceback.print_exc()
                try:
                    driver.execute_script("arguments[0].value='IN';", country_trigger)
                except:
                    pass

            # 4. ADDRESS LINE 1 (address.addressLine1)
            print("[PROCESS] Entering address...")
            address_field = driver.find_element(By.ID, "address.addressLine1")
            address_field.clear()
            slow_type(address_field, contact_info["address"])
            print(f"[SUCCESS] Address entered: {contact_info['address']}")

            # 5. CITY (address.city)
            print("[PROCESS] Entering city...")
            city_field = driver.find_element(By.ID, "address.city")
            city_field.clear()
            slow_type(city_field, contact_info["city"])
            print(f"[SUCCESS] City entered: {contact_info['city']}")

            # 6. STATE/REGION (address.state) - Can be dropdown or input
            print("[PROCESS] Entering state...")
            try:
                state_element = driver.find_element(By.ID, "address.state")

                # Check if it's a button (dropdown) or input field
                if state_element.tag_name == "button":
                    # It's a dropdown
                    driver.execute_script("arguments[0].scrollIntoView(true);", state_element)
                    human_delay(0.5, 1)
                    state_element.click()
                    human_delay(1, 1.5)

                    actions = ActionChains(driver)
                    actions.send_keys(contact_info["state"]).perform()
                    human_delay(1, 2)

                    state_option = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{contact_info['state']}')] | //li[contains(text(), '{contact_info['state']}')]"))
                    )
                    state_option.click()
                    print(f"[SUCCESS] State selected from dropdown: {contact_info['state']}")
                else:
                    # It's a text input
                    state_element.clear()
                    slow_type(state_element, contact_info["state"])
                    print(f"[SUCCESS] State entered: {contact_info['state']}")

                human_delay(1, 2)
            except Exception as e:
                print(f"[WARNING] State entry issue: {e}")
                print("[INFO] Trying alternative method...")
                try:
                    state_input = driver.find_element(By.NAME, "address.state")
                    state_input.clear()
                    state_input.send_keys(contact_info["state"])
                except:
                    pass

            # 7. POSTAL CODE (address.postalCode)
            print("[PROCESS] Entering postal code...")
            postal_field = driver.find_element(By.ID, "address.postalCode")
            postal_field.clear()
            slow_type(postal_field, contact_info["postal_code"])
            print(f"[SUCCESS] Postal code entered: {contact_info['postal_code']}")

            # 8. AGREEMENT CHECKBOX (agreement)
            print("[PROCESS] Checking agreement checkbox...")
            try:
                agreement_checkbox = driver.find_element(By.ID, "agreement")
                driver.execute_script("arguments[0].scrollIntoView(true);", agreement_checkbox)
                human_delay(0.5, 1)

                # Use JavaScript click to ensure it works
                driver.execute_script("arguments[0].click();", agreement_checkbox)
                print("[SUCCESS] Agreement checkbox checked")
                human_delay(1, 2)
            except Exception as e:
                print(f"[WARNING] Agreement checkbox issue: {e}")

            # 9. SUBMIT CONTACT INFORMATION
            print("[PROCESS] Submitting contact information...")
            try:
                submit_contact_btn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='contact-information-submit-button']")
                driver.execute_script("arguments[0].scrollIntoView(true);", submit_contact_btn)
                human_delay(1, 2)
                submit_contact_btn.click()
                print("[SUCCESS] Contact information submitted!")
                human_delay(3, 4)
            except Exception as e:
                print(f"[ERROR] Failed to submit contact form: {e}")
                print("[INFO] Trying to find submit button with alternative selectors...")
                try:
                    alt_submit = driver.find_element(By.XPATH, "//button[@type='submit' or contains(@class, 'submit') or contains(text(), 'Continue')]")
                    alt_submit.click()
                    print("[SUCCESS] Contact information submitted using alternative method!")
                except:
                    print("[ERROR] Could not find submit button")

        except Exception as e:
            print(f"[ERROR] Failed during contact information: {e}")
            import traceback
            traceback.print_exc()
            return

        # --- PHASE 7: UPI VERIFICATION (if available) ---
        print("\n[PHASE 7] Checking for UPI verification option...")
        try:
            # Wait for UPI input field to appear (if it exists)
            upi_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Enter your UPI ID'], input[id*='formField'][type='text']"))
            )

            print("[INFO] UPI verification option found!")

            # Ask user for UPI ID
            upi_id = input("\n>>> Enter your UPI ID (e.g., yourname@paytm): ").strip()

            if upi_id:
                print(f"[INFO] Using UPI ID: {upi_id}")

                # Scroll to UPI input and enter the UPI ID
                driver.execute_script("arguments[0].scrollIntoView(true);", upi_input)
                human_delay(0.5, 1)

                upi_input.clear()
                slow_type(upi_input, upi_id)
                print("[SUCCESS] UPI ID entered")
                human_delay(1, 2)

                # Find and click "Verify and continue" button
                print("[PROCESS] Looking for 'Verify and continue' button...")
                try:
                    # Try multiple selectors for the verify button
                    verify_button = None
                    selectors = [
                        "//span[contains(text(), 'Verify and continue')]/..",
                        "//button[contains(., 'Verify and continue')]",
                        "//span[contains(@class, 'awsui_content') and contains(text(), 'Verify and continue')]/../..",
                        "//button//span[contains(text(), 'step 3 of 5')]/.."
                    ]

                    for selector in selectors:
                        try:
                            verify_button = driver.find_element(By.XPATH, selector)
                            if verify_button:
                                break
                        except:
                            continue

                    if verify_button:
                        driver.execute_script("arguments[0].scrollIntoView(true);", verify_button)
                        human_delay(1, 1.5)

                        try:
                            verify_button.click()
                            print("[SUCCESS] Clicked 'Verify and continue' button")
                        except:
                            driver.execute_script("arguments[0].click();", verify_button)
                            print("[SUCCESS] Clicked 'Verify and continue' button (JS)")

                        # Wait 60 seconds for verification process
                        print("[INFO] Waiting 60 seconds for UPI verification process...")
                        time.sleep(60)

                        # Now click the final "Verify" button
                        print("[PROCESS] Looking for final 'Verify' button...")
                        try:
                            final_verify_button = None
                            verify_selectors = [
                                "button[data-testid='aws-payments-mfa-widget-pending-continue-button']",
                                "//button[@data-testid='aws-payments-mfa-widget-pending-continue-button']",
                                "//button[.//span[text()='Verify']]",
                                "//button[@type='submit']//span[text()='Verify']/..",
                                "//span[text()='Verify']/../.."
                            ]

                            for selector in verify_selectors:
                                try:
                                    if selector.startswith("//"):
                                        final_verify_button = driver.find_element(By.XPATH, selector)
                                    else:
                                        final_verify_button = driver.find_element(By.CSS_SELECTOR, selector)
                                    if final_verify_button:
                                        break
                                except:
                                    continue

                            if final_verify_button:
                                driver.execute_script("arguments[0].scrollIntoView(true);", final_verify_button)
                                human_delay(0.5, 1)

                                try:
                                    final_verify_button.click()
                                    print("[SUCCESS] Clicked final 'Verify' button")
                                except:
                                    driver.execute_script("arguments[0].click();", final_verify_button)
                                    print("[SUCCESS] Clicked final 'Verify' button (JS)")

                                human_delay(2, 3)
                            else:
                                print("[WARNING] Could not find final 'Verify' button")
                        except Exception as e:
                            print(f"[WARNING] Failed to click final verify button: {e}")

                    else:
                        print("[WARNING] Could not find 'Verify and continue' button")

                except Exception as e:
                    print(f"[ERROR] Failed to click verify button: {e}")
            else:
                print("[INFO] No UPI ID provided, skipping UPI verification")

        except TimeoutException:
            print("[INFO] UPI verification option not available or already completed")
        except Exception as e:
            print(f"[INFO] UPI verification step skipped: {e}")

        # --- PHASE 8: WAITING BEFORE KYC ---
        print("\n[PHASE 8] Waiting 2 minutes before KYC Identity Confirmation...")
        print("[INFO] Please wait for 120 seconds...")
        for i in range(120, 0, -10):
            print(f"[INFO] {i} seconds remaining...")
            time.sleep(10)
        print("[SUCCESS] Wait complete! Starting KYC phase...")
        
        # --- PHASE 9: KYC IDENTITY CONFIRMATION ---
        print("\n[PHASE 9] KYC Identity Confirmation Phase...")
        print("[INFO] Checking if we're already on the KYC page or need to navigate...")
        
        try:
            # Check current URL
            current_url = driver.current_url
            print(f"[INFO] Current URL: {current_url}")
            
            # If not on KYC page, try to navigate there
            if '#/kyc' not in current_url:
                print("[INFO] Navigating directly to KYC page...")
                # Try to find a button or link that goes to KYC, or construct the URL
                try:
                    # Extract the base URL and navigate to KYC
                    if 'portal.aws.amazon.com/billing/signup' in current_url:
                        kyc_url = "https://portal.aws.amazon.com/billing/signup?type=register#/kyc"
                        driver.get(kyc_url)
                        print(f"[INFO] Navigated to: {kyc_url}")
                        human_delay(3, 5)
                except Exception as e:
                    print(f"[WARNING] Could not navigate directly: {e}")
            
            # Wait for the KYC page to load - try multiple selectors
            print("[INFO] Waiting for KYC page elements to load...")
            kyc_page_loaded = False
            
            # Try different ways to detect the KYC page
            selectors_to_try = [
                (By.XPATH, "//button[contains(@id, 'formField') and @type='button']"),
                (By.NAME, "dateOfBirth"),
                (By.NAME, "documentId"),
                (By.XPATH, "//h1 | //h2"),
                (By.CSS_SELECTOR, "button.awsui_button-trigger_18eso_10252_161"),
                (By.XPATH, "//div[contains(@class, 'PageContent')]")
            ]
            
            for selector_type, selector_value in selectors_to_try:
                try:
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((selector_type, selector_value))
                    )
                    print(f"[SUCCESS] Found element using {selector_type}: {selector_value}")
                    kyc_page_loaded = True
                    break
                except TimeoutException:
                    print(f"[INFO] Selector not found: {selector_type} - {selector_value}")
                    continue
            
            if not kyc_page_loaded:
                print("[WARNING] Could not confirm KYC page loaded with standard selectors")
                print("[INFO] Waiting additional 10 seconds for page to fully render...")
                time.sleep(10)
            
            print("[SUCCESS] KYC Identity confirmation page ready")
            human_delay(2, 3)

            # STEP 1: Select "Personal use" from Primary purpose dropdown
            print("\n[STEP 1] Selecting 'Personal use' from primary purpose dropdown...")
            try:
                # Wait a bit for any dynamic content to load
                human_delay(2, 3)
                
                # Find form dropdown buttons (exclude header/language dropdowns)
                # Look for buttons within the main content area, not in header
                form_buttons = driver.find_elements(By.XPATH, 
                    "//div[contains(@class, 'PageContent') or contains(@class, 'content') or contains(@class, 'App_content')]//button[@type='button' and contains(@class, 'awsui_button-trigger')]"
                )
                
                # If that doesn't work, try excluding header explicitly
                if len(form_buttons) == 0:
                    all_buttons = driver.find_elements(By.XPATH, "//button[@type='button' and contains(@class, 'awsui_button-trigger')]")
                    # Filter out buttons in header
                    form_buttons = []
                    for btn in all_buttons:
                        btn_text = btn.text.strip()
                        # Skip language selector and other header buttons
                        if btn_text not in ['English', 'Language', 'Feedback', '']:
                            form_buttons.append(btn)
                
                print(f"[INFO] Found {len(form_buttons)} form dropdown buttons")
                
                if len(form_buttons) >= 1:
                    # Click the first button (Primary purpose)
                    purpose_button = form_buttons[0]
                    print(f"[INFO] Purpose button text: '{purpose_button.text}'")
                    print(f"[INFO] Purpose button placeholder: {purpose_button.get_attribute('aria-label')}")
                    
                    driver.execute_script("arguments[0].scrollIntoView(true);", purpose_button)
                    human_delay(0.5, 1)
                    
                    # Click to open dropdown
                    driver.execute_script("arguments[0].click();", purpose_button)
                    print("[INFO] Opened primary purpose dropdown")
                    human_delay(2, 3)  # Wait longer for dropdown to appear
                    
                    # Find and click "Personal use" option
                    personal_use_selectors = [
                        "//div[@role='option']//span[text()='Personal use']",
                        "//li[@role='option']//span[text()='Personal use']",
                        "//div[@role='option' and contains(., 'Personal use')]",
                        "//li[@role='option' and contains(., 'Personal use')]",
                        "//*[@role='option'][contains(text(), 'Personal use')]",
                        "//span[text()='Personal use']"
                    ]
                    
                    personal_use_option = None
                    for selector in personal_use_selectors:
                        try:
                            options = driver.find_elements(By.XPATH, selector)
                            if options:
                                print(f"[INFO] Found {len(options)} options matching: {selector}")
                                # Look for exact match
                                for opt in options:
                                    if 'Personal use' in opt.text:
                                        personal_use_option = opt
                                        print(f"[INFO] Selected option with text: '{opt.text}'")
                                        break
                            if personal_use_option:
                                break
                        except:
                            continue
                    
                    if personal_use_option:
                        driver.execute_script("arguments[0].scrollIntoView(true);", personal_use_option)
                        human_delay(0.5, 1)
                        driver.execute_script("arguments[0].click();", personal_use_option)
                        print("[SUCCESS] Selected 'Personal use'")
                        human_delay(1, 2)
                    else:
                        print("[WARNING] Could not find 'Personal use' option in dropdown")
                        print("[INFO] Trying to list all visible options...")
                        all_options = driver.find_elements(By.XPATH, "//*[@role='option']")
                        for i, opt in enumerate(all_options[:10]):  # Show first 10
                            print(f"  Option {i}: '{opt.text}'")
                else:
                    print("[WARNING] No form dropdown buttons found on page")
                
            except Exception as e:
                print(f"[ERROR] Failed to select personal use: {e}")
                import traceback
                traceback.print_exc()

            # STEP 2: Select "Individual" from Ownership type dropdown
            print("\n[STEP 2] Selecting 'Individual' from ownership type dropdown...")
            try:
                # Find all dropdown buttons again (in case page updated)
                all_buttons = driver.find_elements(By.XPATH, "//button[@type='button' and contains(@class, 'awsui_button-trigger')]")
                print(f"[INFO] Found {len(all_buttons)} dropdown buttons on page")
                
                if len(all_buttons) >= 2:
                    # Click the second button (Ownership type)
                    ownership_button = all_buttons[1]
                    print(f"[INFO] Button text: {ownership_button.text}")
                    
                    driver.execute_script("arguments[0].scrollIntoView(true);", ownership_button)
                    human_delay(0.5, 1)
                    
                    # Click to open dropdown
                    driver.execute_script("arguments[0].click();", ownership_button)
                    print("[INFO] Opened ownership type dropdown")
                    human_delay(1, 2)
                    
                    # Find and click "Individual" option
                    individual_selectors = [
                        "//div[@role='option' and contains(., 'Individual')]",
                        "//li[@role='option' and contains(., 'Individual')]",
                        "//span[contains(text(), 'Individual')]",
                        "//*[contains(@class, 'option') and normalize-space(.)='Individual']"
                    ]
                    
                    individual_option = None
                    for selector in individual_selectors:
                        try:
                            individual_option = WebDriverWait(driver, 5).until(
                                EC.element_to_be_clickable((By.XPATH, selector))
                            )
                            if individual_option:
                                print(f"[INFO] Found 'Individual' option using: {selector}")
                                break
                        except:
                            continue
                    
                    if individual_option:
                        driver.execute_script("arguments[0].scrollIntoView(true);", individual_option)
                        human_delay(0.5, 1)
                        driver.execute_script("arguments[0].click();", individual_option)
                        print("[SUCCESS] Selected 'Individual'")
                        human_delay(1, 2)
                    else:
                        print("[WARNING] Could not find 'Individual' option in dropdown")
                else:
                    print("[WARNING] Not enough dropdown buttons found (need at least 2)")
                
            except Exception as e:
                print(f"[ERROR] Failed to select individual: {e}")
                import traceback
                traceback.print_exc()

            # STEP 3: Ask for and enter Date of Birth
            print("\n[STEP 3] Entering date of birth...")
            dob = input("\n>>> Enter your Date of Birth (format: YYYY/MM/DD, e.g., 1990/01/15): ").strip()
            
            if not dob:
                dob = "1990/01/15"  # Default value
                print(f"[INFO] Using default DOB: {dob}")
            
            try:
                dob_field = driver.find_element(By.NAME, "dateOfBirth")
                driver.execute_script("arguments[0].scrollIntoView(true);", dob_field)
                human_delay(0.5, 1)
                
                dob_field.clear()
                slow_type(dob_field, dob)
                print(f"[SUCCESS] Date of birth entered: {dob}")
                human_delay(1, 2)
                
            except Exception as e:
                print(f"[ERROR] Failed to enter date of birth: {e}")
                import traceback
                traceback.print_exc()

            # STEP 4: Check "Contact" radio button
            print("\n[STEP 4] Selecting 'Contact' radio button...")
            try:
                # Find radio button with value="Contact"
                contact_radio = driver.find_element(By.XPATH, "//input[@type='radio' and @value='Contact']")
                
                driver.execute_script("arguments[0].scrollIntoView(true);", contact_radio)
                human_delay(0.5, 1)
                
                # Click using JavaScript
                driver.execute_script("arguments[0].click();", contact_radio)
                print("[SUCCESS] 'Contact' radio button selected")
                human_delay(1, 2)
                
            except Exception as e:
                print(f"[ERROR] Failed to select contact radio: {e}")
                import traceback
                traceback.print_exc()

            # STEP 5: Ask for and enter PAN card number
            print("\n[STEP 5] Entering PAN card number...")
            pan_number = input("\n>>> Enter your PAN Card Number (e.g., ABCDE1234F): ").strip()
            
            if not pan_number:
                pan_number = "ABCDE1234F"  # Default value
                print(f"[INFO] Using default PAN: {pan_number}")
            
            try:
                pan_field = driver.find_element(By.NAME, "documentId")
                driver.execute_script("arguments[0].scrollIntoView(true);", pan_field)
                human_delay(0.5, 1)
                
                pan_field.clear()
                slow_type(pan_field, pan_number)
                print(f"[SUCCESS] PAN card number entered: {pan_number}")
                human_delay(1, 2)
                
            except Exception as e:
                print(f"[ERROR] Failed to enter PAN number: {e}")
                import traceback
                traceback.print_exc()

            # STEP 6: Upload soul.png image
            print("\n[STEP 6] Uploading soul.png document...")
            try:
                # Check if soul.png exists in current directory
                image_path = os.path.abspath("soul.png")
                if not os.path.exists(image_path):
                    # Try /app directory
                    image_path = "/app/soul.png"
                    if not os.path.exists(image_path):
                        print(f"[WARNING] soul.png not found. Please ensure the file exists.")
                        print(f"[INFO] Looking in current directory and /app/")
                        image_path = input("\n>>> Enter full path to soul.png: ").strip()
                
                if os.path.exists(image_path):
                    print(f"[INFO] Found image at: {image_path}")
                    
                    # Find the file input element (usually hidden)
                    file_input = driver.find_element(By.XPATH, "//input[@type='file']")
                    
                    # Send the file path directly to the input element
                    file_input.send_keys(image_path)
                    print("[SUCCESS] soul.png uploaded")
                    human_delay(2, 3)
                else:
                    print(f"[ERROR] soul.png not found at {image_path}")
                
            except Exception as e:
                print(f"[ERROR] Failed to upload document: {e}")
                import traceback
                traceback.print_exc()

            # STEP 7: Check the agreement checkbox
            print("\n[STEP 7] Checking agreement checkbox...")
            try:
                # Find checkbox by type
                agreement_checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
                
                # Usually the last checkbox is the agreement
                if agreement_checkboxes:
                    agreement_checkbox = agreement_checkboxes[-1]
                    driver.execute_script("arguments[0].scrollIntoView(true);", agreement_checkbox)
                    human_delay(0.5, 1)
                    
                    driver.execute_script("arguments[0].click();", agreement_checkbox)
                    print("[SUCCESS] Agreement checkbox checked")
                    human_delay(1, 2)
                else:
                    print("[WARNING] Agreement checkbox not found")
                
            except Exception as e:
                print(f"[ERROR] Failed to check agreement: {e}")
                import traceback
                traceback.print_exc()

            # STEP 8: Click "Continue (step 4 of 5)" button
            print("\n[STEP 8] Clicking 'Continue (step 4 of 5)' button...")
            try:
                # Find the continue button
                continue_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Continue') and contains(text(), 'step 4 of 5')]/..")
                
                driver.execute_script("arguments[0].scrollIntoView(true);", continue_button)
                human_delay(1, 1.5)
                
                driver.execute_script("arguments[0].click();", continue_button)
                print("[SUCCESS] Clicked 'Continue (step 4 of 5)' button")
                human_delay(3, 4)
                
            except Exception as e:
                print(f"[ERROR] Failed to click continue button: {e}")
                print("[INFO] Trying alternative selectors...")
                try:
                    # Try finding by button with "Continue" text
                    alt_continue = driver.find_element(By.XPATH, "//button[contains(., 'Continue') or contains(., 'step 4')]")
                    driver.execute_script("arguments[0].click();", alt_continue)
                    print("[SUCCESS] Clicked continue button (alternative method)")
                except:
                    print("[ERROR] Could not find continue button")
                    import traceback
                    traceback.print_exc()

            print("\n[SUCCESS] KYC Identity confirmation phase completed!")
            print("[INFO] Please verify all fields are filled correctly in the browser")
            
        except Exception as e:
            print(f"[ERROR] Failed during KYC identity confirmation: {e}")
            print("\n[MANUAL FALLBACK] The script encountered an error during KYC phase.")
            print("[INFO] The browser window is still open. You can:")
            print("  1. Manually complete the remaining KYC fields")
            print("  2. The following fields need to be filled:")
            print("     - Primary purpose: Select 'Personal use'")
            print("     - Ownership type: Select 'Individual'")
            print("     - Date of birth: Enter in YYYY/MM/DD format")
            print("     - Document type: Select 'Contact'")
            print("     - PAN Card number: Enter your PAN")
            print("     - Upload: Upload soul.png file")
            print("     - Agreement: Check the checkbox")
            print("     - Continue: Click the continue button")
            print("\n[INFO] Browser will remain open for manual completion...")
            import traceback
            traceback.print_exc()

        # --- PHASE 10: COMPLETION ---
        print("\n" + "!"*60)
        print("   AUTOMATION PROCESS COMPLETE!")
        print("   All available steps have been processed")
        print("   Keep this browser open to continue or inspect")
        print("!"*60)

        # Keep browser open for user inspection
        input("\n>>> Press ENTER to close the browser...")
        print("[INFO] Closing browser...")

    except KeyboardInterrupt:
        print("\n[INFO] Process interrupted by user")
    except Exception as e:
        print(f"\n[CRITICAL ERROR] {str(e)}")
        import traceback
        traceback.print_exc()
    finally:
        if driver:
            try:
                driver.quit()
                print("[INFO] Browser closed successfully")
            except:
                pass

if __name__ == "__main__":
    print("\n" + "="*60)
    print("   AWS ACCOUNT SIGNUP AUTOMATION WITH KYC")
    print("   Email: nokibox476@icousd.com")
    print("   Ready to start? Press Ctrl+C to cancel")
    print("="*60)

    try:
        input("\n>>> Press ENTER to start the automation...")
        main()
    except KeyboardInterrupt:
        print("\n[INFO] Automation cancelled by user")
