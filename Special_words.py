voroodi_raw = input('')
voroodi_raw += 'x'
voroodi_raw_list = voroodi_raw.split('.')
voroodi_made = []
for i in voroodi_raw_list:
    list_i = i.split()
    list_i.remove(list_i[0])
    list_i = ['zero'] +list_i # Can be anything, just for don't missing the position of deleted word!
    voroodi_made.append(' '.join(list_i))
voroodi = ' '.join(voroodi_made)
list_voroodi = voroodi.split()
dict_words = {}
list_words_with_positions = []
list_khorooji = []
count = 1
for words in list_voroodi:
    list_words_with_positions.append(str(count).split() + words.split())
    count += 1
for item in list_words_with_positions:
    if str(item[1]) != str(item[1]).lower():
        list_khorooji.append(item)
for word in list_khorooji:
    word_eslahi = str(word[1])
    word_dorost = str(word[0])
    if word_eslahi.endswith(','):
        word_eslahi = word_eslahi.replace(',', '')
        word = word_dorost.split() + word_eslahi.split()
    print(word[0]+':'+word[1])
if list_khorooji == []:
    print('None')