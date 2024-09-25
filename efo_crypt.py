
def encrypt(word,key):
    word=word.lower()
    abc = "abcçdefgğhiıjklmnoöpqrsştuüvyz"
    new_word = []
    for i in range(0,len(word)):
        if word[i] in abc:
            index=abc.index(word[i])
            new_index=abc[(index+key)%len(abc)]
            new_word.append(new_index)
    return "".join(new_word)
def decrypt(word,key):
    abc = "abcçdefgğhiıjklmnoöpqrsştuüvyz"
    new_word = []
    for i in range(len(word)):
        if word[i] in abc:
            index=abc.index(word[i])
            new_index=abc[(index-key)%len(abc)]
            new_word.append(new_index)
    return "".join(new_word)


