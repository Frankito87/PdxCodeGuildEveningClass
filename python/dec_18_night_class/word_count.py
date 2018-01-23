
with open('Rules_and_Examples_of_Perspective_proper_for_Painters_and_Architects.txt', 'r', encoding='UTF-8') as f:
    text = f.read()
    text = text.lower()

    text_list = text.split()

    word_count = {}

    for word in text_list:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    for word, times in word_count.items():
        print('"{}" seen {} times.'.format(word, times))
