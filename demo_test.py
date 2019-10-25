from pypinyin import lazy_pinyin,Style
Passage=input('输入中文:')
Passage=str(Passage)
style=Style.TONE
print(lazy_pinyin(Passage,style=style,errors='ignore'))
