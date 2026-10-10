
from collections import Counter
import re

filename = input("Enter text file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read().lower()

    words = re.findall(r"\b\w+\b", text)

    print("Total words:", len(words))
    print("Word frequency:")

    for word, count in Counter(words).most_common():
        print(word, ":", count)

except FileNotFoundError:
    print("File not found. Please check the filename.")
  
