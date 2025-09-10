"""
🔐 Mini Security Project: Password Manager
Features:
1. Register new users
2. Login authentication
3. OTP system (Random module)
4. Password strength checker
5. Store data in memory (dict)
"""

import random

# ---- Global Constant ----
SECURITY_LEVEL = 8  # minimum password length

# ---- Global Variable ----
users = {}  # store username:password


def password_strength(password):
    """Check strength of password (returns True if strong)"""
    if len(password) < SECURITY_LEVEL:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    return True


def register(username, password):
    """Register a new user if password strong"""
    if not password_strength(password):
        print("❌ Weak password! Use min length 8, 1 uppercase, 1 digit.")
        return False
    users[username] = password
    print("✅ User registered successfully!")
    return True


def login(username, password):
    """Login system with OTP"""
    if username not in users:
        print("❌ No such user!")
        return False

    if users[username] == password:
        # OTP system
        otp = random.randint(1000, 9999)
        print("📩 OTP sent:", otp)  # simulate sending
        user_otp = int(input("Enter OTP: "))
        if user_otp == otp:
            print("✅ Login Successful!")
            return True
        else:
            print("❌ Wrong OTP!")
            return False
    else:
        print("❌ Incorrect password!")
        return False


def show_menu():
    """Main menu for security app"""
    while True:
        print("\n---- SECURITY APP ----")
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            u = input("Enter username: ")
            p = input("Enter password: ")
            register(u, p)

        elif choice == "2":
            u = input("Enter username: ")
            p = input("Enter password: ")
            login(u, p)

        elif choice == "3":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice!")


# Run app
show_menu()
