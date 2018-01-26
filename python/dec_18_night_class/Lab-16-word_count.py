def word_count():

    with open('Rules_and_Examples_of_Perspective_proper_for_Painters_and_Architects.txt', 'r', encoding='UTF-8') as f:
        text = f.read()
        text = text.lower()

        text_list = text.split()

        word_count1 = {}

        for word in text_list:
            if word not in word_count1:
                word_count1[word] = 1
            else:
                word_count1[word] += 1

        for word, times in word_count1.items():
            print('"{}" seen {} times.'.format(word, times))


word_count()
