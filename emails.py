def main():

    email_to_name = {}
    email = input("Email: ")
    while email != "":
        user_name = get_name_from_email(email)
        confirm_input = input(f"Is your name {user_name}? (Y/n) ")
        if confirm_input.upper() != "Y" and confirm_input != "":
            user_name = input("Name: ")
        email_to_name[email] = user_name
        email = input("Email: ")

    for email, user_name in email_to_name.items():
        print(f"{user_name} ({email})")


def get_name_from_email(email):
    special_word = email.split("@")[0]
    parts = special_word.split(".")
    user_name = " ".join(parts).title()

    return user_name