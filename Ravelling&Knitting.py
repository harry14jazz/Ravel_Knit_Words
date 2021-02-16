def ravel(word):
    word_process = word.title()
    new_word = ''
    for index in range(len(word)+1):
        for index_char in range(index):
            new_word += word[index_char]
    return new_word

def knit(word):
    first_char = word[0]
    word2 = word.split(first_char)
    maxlen = len(word2) - 1
    almost_full_word = word2[maxlen]
    new_word = first_char+almost_full_word
    
    return new_word


print(ravel('Purwadhika'))
print(ravel('Digital'))
print(ravel('Coding'))
print(ravel('School'))
print('')
print('='*100)
print('')
print(knit('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
print(knit('DDiDigDigiDigitDigitaDigital'))
print(knit('CCoCodCodiCodinCoding'))
print(knit('SScSchSchoSchooSchool'))

