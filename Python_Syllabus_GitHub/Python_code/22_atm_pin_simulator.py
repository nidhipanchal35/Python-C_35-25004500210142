"""Practical: 1.22 ATM PIN Simulator"""

correct_pin = "1234"  # Change this sample PIN if needed
attempts = 0
while attempts < 3:
    entered_pin = input("Enter your 4-digit PIN: ")
    if entered_pin == correct_pin:
        print("Access Granted")
        break
    attempts += 1
    print("Incorrect PIN. Attempts remaining:", 3 - attempts)
else:
    print("Card Blocked")
