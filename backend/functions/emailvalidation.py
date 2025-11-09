import re


def emailvalidation(email):
    pattern = r"[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Za-z]{2,}"
    if re.fullmatch(pattern, email, flags=re.IGNORECASE):
        return True
    else:
        return False