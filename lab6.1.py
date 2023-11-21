try:
    Stroka = input(str('Введите слова через пробел: '))
    all_words = []
    one_word = ''
    for words in Stroka:
        if words == ' ':
            if one_word != '':
                all_words.append(one_word)
                one_word = ''
        else:
            one_word += words
    if one_word != '':
        all_words.append(one_word)
    len_first = all_words[0]
    num = 0
    for i in range(1, len(all_words)):
        if len(all_words[i]) > len(len_first):
            len_first = all_words[i]
            num = i
    print(all_words[num])
except IndexError:
    print("Введите хотя бы 1 символ!")