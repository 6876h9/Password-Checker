import re

def strength(p):
    score = 0
    if len(p) >= 8: score += 1
    if len(p) >= 12: score += 1
    if re.search(r"[a-z]", p): score += 1
    if re.search(r"[A-Z]", p): score += 1
    if re.search(r"\d", p): score += 1
    if re.search(r"[^\w\s]", p): score += 1

    return ["Very Weak", "Weak", "Okay", "Good", "Strong", "Very Strong", "Excellent"][score]

pwd = input("Password: ")
print(strength(pwd))
