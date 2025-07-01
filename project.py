def find_substrings(s):
    substrings = []
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(s[i:j])
    return substrings

text = "abc"
result = find_substrings(text)
print("All substrings:")
for sub in result:
    print(sub)
