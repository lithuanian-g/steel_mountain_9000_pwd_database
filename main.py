from secret import passwords

username = 'sunflower'

print(f"--=Steel Mountain 9000x Password Database=--")
for entry in passwords:
    for account, credentials in entry.items():
        for username, password in credentials.items():
            print(f"{account} - {username}:", end="")
            for asterisk in range(len(password)):
                print(f"*", end="")
            print("")