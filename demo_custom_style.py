from pypinyin.style import register
from pypinyin import lazy_pinyin


@register('kiss')
def kiss(pinyin, **kwargs):
    if pinyin == 'me':
        return f'😘{pinyin}'
    return pinyin


print(lazy_pinyin('么么哒', style='kiss'))
