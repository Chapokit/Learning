
msg = input("Enter a message: ")

out = ""
for i in range(0, len(msg), 2):
    out = out+msg[i]
    print(out)

out = ""
for i in range(1, len(msg), 2):
    out = out+msg[i]
    print(out)