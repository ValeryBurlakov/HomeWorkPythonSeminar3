import re # регулярные выражения используются для поиска фрагмента текста и сопоставления символов

english_letters = {
     "A, E, I, O, U, L, N, S, T, R": 1,
     "D, G": 2,
     "B, C, M, P": 3,
     "F, H, V, W, Y": 4,
     "K": 5,
     "J, X": 8,
     "Q, Z": 10
}

russian_letters = {
     "А, В, Е, И, Н, О, Р, С, Т": 1,
     "Д, К, Л, М, П, У": 2,
     "Б, Г, Ё, Ь, Я": 3,
     "Й, Ы": 4,
     "Ж, З, Х, Ц, Ч": 5,
     "Ш, Э, Ю": 8,
     "Ф, Щ, Ъ": 10
}

def English(text):
    return bool(re.search('[A-Z]', text)) # true если английское слово, если есть строчные и заглавные: [a-zA-Z]

inpt =  input("Введите ваше слово: ").upper()

if English(inpt): # True
    def search_letters(i):
        for key in english_letters:
            if i in key:
                return english_letters.get(key)
    print(f"ваше слово дало очков: {sum(map(search_letters, inpt))}")
else: # False
    def search_letters(i):
        for key in russian_letters:
            if i in key:
                return russian_letters.get(key)
    print(f"ваше слово дало очков: {sum(map(search_letters, inpt))}")