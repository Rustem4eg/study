import string


def prepare_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.replace('\n', ' ')
    text = text.lower()
    text = text.split()

    return text

def statistics(words):
    words_stat = {}

    for word in words:
        if word not in words_stat:
            words_stat[word] = 1
        else:
            words_stat[word] += 1
    return words_stat

filename = input('Введите название файла: ')
words = prepare_words(filename)
words_stat = statistics(words)

print(f"Кол-во слов: {len(words)}")
print(f"Кол-во уникальных слов: {len(words_stat)}")
print("Все использованные слова:")
for word, count in words_stat.items():
    print(f"{word} {count}")




