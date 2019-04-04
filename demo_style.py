from pypinyin import lazy_pinyin, Style

style = Style.TONE3
print(lazy_pinyin('聪明的小兔子', style=style))