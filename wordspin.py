def spin_words(sentence):
    length = 4
    for word in sentence.split():
        if len(word) > length :
            sentence = sentence.replace(word,word[::-1])
    return sentence