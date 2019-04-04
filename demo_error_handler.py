from pypinyin import lazy_pinyin

print(lazy_pinyin('你好☆☆，我是xxx'))
print(lazy_pinyin('你好☆☆，我是xxx', errors='ignore'))

print(lazy_pinyin('你好☆☆，我是xxx', errors=lambda item: ''.join(['※' if c == '☆' else c for c in item])))
