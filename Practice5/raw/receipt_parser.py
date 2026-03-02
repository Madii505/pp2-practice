import re

f = open("raw.txt", "r", encoding="utf-8")
text = f.read()
f.close()

prices = re.findall(r"\d[\d ]*,\d{2}", text)
names = re.findall(r"\d+\.\n(.+)", text)
date = re.search(r"\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}", text)
payment = re.search(r"Банковская карта", text)

print("Date and time:", date.group())
print("Payment:", payment.group())

print("\nProducts:")
for i in range(len(names)):
    print(names[i], "-", prices[i])

total = re.search(r"ИТОГО:\n([\d ]*,\d{2})", text)
print("\nTotal:", total.group(1))