text = input("enter:")
upper_case = text.upper()
lower_case = text.lower()
upper_count = 0
lower_count = 0
space_count = 0
for i in text:
    if i in upper_case:
        upper_count += 1
    if i in lower_case:
        lower_count += 1
    if i == " ":
        space_count += 1

print(upper_count)
print(lower_count)
print(space_count)