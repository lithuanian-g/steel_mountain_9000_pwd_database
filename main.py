from secret import password

username = 'sunflower'

print(f"My credentials\n{username}:", end="")
for i in range(len(password)):
    print("*",end="")