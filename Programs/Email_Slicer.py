"""
Slicing Username and Domain from an Email Address
"""

email = input("Enter an Email Address: ")

at_char_pos = email.find("@")

username = email[:at_char_pos]
domain = email[at_char_pos+1:]

print(f"\nUserName: {username}")
print(f"Domain: {domain}\n")