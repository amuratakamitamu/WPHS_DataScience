s = input("String")
ans = "Yes"
for i in range(1, 6):
    if s[i * 2 - 1] == '1':
        ans = "No"
        break
print(ans)
