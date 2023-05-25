from secret import passwords

username = 'sunflower'

print(f"Steel Mountain 9000x Password Database")
for entry in passwords:
    for username, password in entry.items():
        print(f"{username}:",end="")
        for asterisk in range(len(password)):
            print(f"*", end="")
        print("")