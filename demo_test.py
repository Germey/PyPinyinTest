from pypinyin import lazy_pinyin,Style
Passage=str(input('输入中文:'))
style=Style.TONE
print(lazy_pinyin(Passage,style=style,errors='ignore'))
