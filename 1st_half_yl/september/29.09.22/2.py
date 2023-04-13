changes = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
           "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
           "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
           "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
           "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
           "б": "b", "ю": "ju", "ё": "jo"}
with open('cyrillic.txt', 'r', encoding="utf8") as f:
    data = f.read()
final_text = []
for i in data:
    if i.lower() in changes.keys():
        if i.isupper():
            final_text.append(changes[i.lower()].capitalize())
        else:
            final_text.append(changes[i.lower()])
    else:
        final_text.append(i)
with open('transliteration.txt', 'w', encoding="utf8") as f1:
    f1.write(''.join(final_text))
