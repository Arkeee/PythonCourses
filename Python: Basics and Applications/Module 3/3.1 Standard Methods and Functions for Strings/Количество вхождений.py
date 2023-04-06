"""
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa
"""

s = input()
t = input()
ans = 0
for i in range(len(s)):
    if s[i:].startswith(t):
        ans += 1
print(ans)
