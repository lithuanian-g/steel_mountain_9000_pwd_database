from secret import passwords

username = 'sunflower'

print("-" * 44)
print(f"--=Steel Mountain 9000x Password Database=--")
print("-" * 44)
for entry in passwords:
    for account, credentials in entry.items():
        for username, password in credentials.items():
            print(f"{account} - {username}:", end="")
            for asterisk in range(len(password)):
                print(f"*", end="")
            print("")
