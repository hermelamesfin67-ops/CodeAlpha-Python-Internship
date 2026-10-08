import re
with open("emails.txt", "r") as file:
    text = file.read(
    )
    emails = re.findall(r"\S+@\S+\.\S+", text)

    for email in emails:
        print(email)
with open("extracted_emails.txt", "w") as output_file:
    for email in emails:
        output_file.write(email + "\n")
