s = input()
t = input()
ans = 0
for i in range(len(s)):
    if s[i:].startswith(t):
        ans += 1
print(ans)
