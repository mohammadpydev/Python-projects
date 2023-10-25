import re

# Sample text containing email addresses
text = """
Here are some email addresses:
john.doe@example.com
jane.smith@test.net
support@company.org
5555555488888888888
wwwwwwwwwwwwwwwwwww
hamedhamedhamedhamed
"""

# Define a regular expression pattern for matching email addresses
email_pattern = r'\b[\w.-]+@[\w.-]+\.\w+\b'

# Use re.findall to find all email addresses in the text
email_addresses = re.findall(email_pattern, text)

# Count the number of email addresses found
email_count = len(email_addresses)

# Print the email addresses and count
print("Email Addresses:")
for email in email_addresses:
    print(email)

print(f"\nTotal Email Count: {email_count}")
