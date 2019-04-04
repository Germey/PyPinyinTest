from pypinyin import lazy_pinyin, load_phrases_dict

print(lazy_pinyin('朝阳'))
personalized_dict = {
    '朝阳': [['cháo'], ['yáng']]
}
load_phrases_dict(personalized_dict)
print(lazy_pinyin('朝阳'))
