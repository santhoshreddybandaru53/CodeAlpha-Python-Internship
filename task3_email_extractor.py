import re

# Create a sample input file to test
file = open("emails.txt", "w")
file.write("Contact alice@example.com or bob@gmail.com for help.\n")
file.write("You can also reach charlie@yahoo.com and dave@company.org\n")
file.write("Invalid: notanemail, @nodomain.com\n")
file.close()

# Read the file
file = open("emails.txt", "r")
text = file.read()
file.close()

# Find all emails
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

print("Emails found:")
for email in emails:
    print(email)

# Save to output file
output = open("found_emails.txt", "w")
for email in emails:
    output.write(email + "\n")
output.close()

print("Saved to found_emails.txt")
