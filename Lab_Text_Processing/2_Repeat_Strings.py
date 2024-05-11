words = input().split()
result = ""

for word in words:
    result += word * len(word)

print(result)

'''2
result = [word * len(word) for word in words]
print(*result, sep="")
'''