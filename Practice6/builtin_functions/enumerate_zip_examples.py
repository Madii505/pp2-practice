names = ["Ali", "Madi", "John"]
scores = [90, 85, 78]

for index, name in enumerate(names):
    print(index, name)

for name, score in zip(names, scores):
    print(name, score)

print(len(scores))
print(sum(scores))
print(min(scores))
print(max(scores))
print(sorted(scores))