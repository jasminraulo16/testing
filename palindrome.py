text = input()
new = ''
for i in text:
    new = i + new

if text == new:
    print("palindrome")
else:
    print("not palindrome")


# Print the palindrome words

st = input("enter:")
sp = st.split()
for i in sp:
    new1 = ''
    for j in i:
        new1 = j + new1
        if new1 == i:
            print(new1)