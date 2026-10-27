
# Password Policy Validation Engine

import string

# Password policy rules
MIN_LENGTH = 8
PROHIBITED_SUBSTRINGS = ["password", "admin", "123456"]

def validate_password(password):
    errors = []

    # 1. Minimum length check
    if len(password) < MIN_LENGTH:
        errors.append("Password must contain at least 8 characters.")

    # 2. Uppercase letter check
    if not any(ch.isupper() for ch in password):
        errors.append("Password must contain an uppercase letter.")

    # 3. Lowercase letter check
    if not any(ch.islower() for ch in password):
        errors.append("Password must contain a lowercase letter.")

    # 4. Digit check
    if not any(ch.isdigit() for ch in password):
        errors.append("Password must contain a digit.")

    # 5. Special character check
    if not any(ch in string.punctuation for ch in password):
        errors.append("Password must contain a special character.")

    # 6. Repeated character check
    if any(password[i] == password[i + 1]
           for i in range(len(password) - 1)):
        errors.append("Password must not contain consecutive repeated characters.")

    # 7. Prohibited substring check (case-insensitive)
    lower_password = password.lower()

    for word in PROHIBITED_SUBSTRINGS:
        if word in lower_password:
            errors.append(
                f"Password must not contain the prohibited substring '{word}'."
            )

    # Display result
    if errors:
        print("\nPassword: ", password)
        print("Result: INVALID")
        print("Failed conditions:")
        for error in errors:
            print("-", error)
    else:
        print("\nPassword: ", password)
        print("Result: VALID")
        print("All password policy conditions are satisfied.")

# Sample passwords
sample_passwords = [
    "Abc@1234",
    "hello",
    "PASSWORD@123",
    "Admin@5678",
    "Abc@@1234",
    "Strong#9x"
]

print("===== PASSWORD POLICY VALIDATION =====")

for pwd in sample_passwords:
    validate_password(pwd)
