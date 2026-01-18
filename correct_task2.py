import re

def count_valid_emails(emails):
    count = 0
    # Simple regex for basic email structure: something@something.something
    email_pattern = r"^[^@]+@[^@]+\.[^@]+$"

    for email in emails:
        if isinstance(email, str) and re.match(email_pattern, email):
            count += 1

    return count
