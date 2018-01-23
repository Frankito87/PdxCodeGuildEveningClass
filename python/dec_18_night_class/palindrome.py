def palindrome():
    word = input("What word do you want to check: ")
    print('word: {}'.format(word))
    word_cleaned = word.replace(' ', '')
    print('word_cleaned: {}'.format(word_cleaned))
    word_reverse = ''.join(reversed(word_cleaned))
    print('word_reverse: {}'.format(word_reverse))
    if word_cleaned == word_reverse:
        return True

    else:
        return False
print(palindrome())
