import re

def password_strength(password):
    # Initialize score
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Lowercase check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Number check
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Strength classification based on score
    strength = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Good",
        4: "Strong",
        5: "Very Strong"
    }

    result = {
        "score": score,
        "strength": strength[score],
        "feedback": feedback
    }

    return result

# Example usage
password = input("Enter a password to check its strength: ")
result = password_strength(password)
print(f"Password Score: {result['score']}/5")
print(f"Password Strength: {result['strength']}")
if result['feedback']:
    print("Feedback:")
    for item in result['feedback']:
        print(f"- {item}")