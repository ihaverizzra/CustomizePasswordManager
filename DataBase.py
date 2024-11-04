import os
import time
import winsound  # For sound on Windows
import getpass

# Function to announce the word "Database"
def announce_database():
    print("Database")
    winsound.Beep(1000, 500)  # Beep sound
    time.sleep(0.5)
    print("Database")  # Print again for clarity

# Function to shift letters
def shift_letters(word):
    shifted_word = ""
    for char in word:
        for _ in range(2):  # Shift twice
            shifted_word += chr(ord(char) + 1)  # Shift character
            time.sleep(0.1)  # Delay for effect
        shifted_word += " "  # Space between letters
    return shifted_word.strip()

# Main function
def main():
    passcode = "1234"
    secondary_password = "Ekul-2013"
    passwords = {
        "example@gmail.com": "password123",
        "user@example.com": "mypassword",
        "admin@site.com": "adminpass"
    }

    # Passcode input
    entered_passcode = getpass.getpass("Enter Passcode: ")
    if entered_passcode == passcode:
        print(shift_letters("Database"))
        announce_database()
        
        command = input("Type '/passwords' to access your passwords: ")
        if command == "/passwords":
            entered_secondary_password = getpass.getpass("Enter the secondary password: ")
            if entered_secondary_password == secondary_password:
                print("-----------------")
                print("    Passwords")
                print("-----------------")
                print("You have access to the following passwords:")
                for email, password in passwords.items():
                    print(f"{email}: {password}")
            else:
                print("Incorrect secondary password. Access denied.")
        else:
            print("Invalid command.")
    else:
        print("Incorrect passcode. Access denied.")

if __name__ == "__main__":
    main()
