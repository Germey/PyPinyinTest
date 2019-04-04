最近碰到了一个问题，项目中很多文件都是接手过来的中文命名的一些素材，结果在部署的时候文件名全都乱码了，导致项目无法正常运行。

后来请教了一位大佬怎么解决文件名乱码的问题，他说这个需要正面解决吗？不需要，把文件名全部改掉，文件名永远不要用中文，永远不要。

我想他这么说的话，一定也是凭经验得出来的。

这里也友情提示大家，项目里面文件永远不要用中文，永远不要！

好，那不用中文用啥？平时来看，一般我们都会用英文来命名，一般也不会出现中文，比如 resource, controller, result, view, spider 等等，所以绝大多数情况下，是不会出现什么问题的。但是也有个别的情况，比如一些素材、资源文件可能的中文命名的，那么这时候该咋办呢？

首先像，因为是中文资源文件，我们要改成非中文命名的，无非两种，一种是英文，一种是拼音。

如果改英文，当然可以翻译、我们想翻译的话，逐个人工翻译成本太高，机器翻译的话，翻译完可能有些文不对题了，而且我们自己也不知道一些奇怪的资源英语应该叫什么，所以到时候真的找起来都找不到了。

所以第二种解决方案，那就是拼音了。中文转拼音，很自然，而且一个字就对应一串拼音，而且也非常容易从拼音看懂是什么意思，所以这确实是一个不错的方案。

那么问题就来了，怎样把一批中文文件转拼音命名呢？下面就让我们来了解 Python 的一个库 PyPinyin 吧！

## 概述

Python 中提供了汉字转拼音的库，名字叫做 PyPinyin，可以用于汉字注音、排序、检索等等场合，是基于 hotto/pinyin 这个库开发的，一些站点链接如下：

* GitHub: <https://github.com/mozillazg/python-pinyin>
* 文档：<https://pypinyin.readthedocs.io/zh_CN/master/>
* PyPi：<https://pypi.org/project/pypinyin/>

它有这么几个特性：

- 根据词组智能匹配最正确的拼音。
- 支持多音字。
- 简单的繁体支持, 注音支持。
- 支持多种不同拼音/注音风格。

是不是等不及了呢？那就让我们来了解一下它的用法吧！

## 安装

首先就是这个库的安装了，通过 pip 安装即可：

```
pip3 install pypinyin
```

安装完成之后导入一下这个库，如果不报错，那就说明安装成功了。

```
>>> import pypinyin
```

好，接下来我们看下它的具体功能。

## 基本拼音

首先我们进行一下基本的拼音转换，方法非常简单，直接调用 pinyin 方法即可：

```python
from pypinyin import pinyin
print(pinyin('中心'))
```

运行结果：

```python
[['zhōng'], ['xīn']]
```

可以看到结果会是一个二维的列表，每个元素都另外成了一个列表，其中包含了每个字的读音。

那么如果这个词是多音字咋办呢？比如 "朝阳"，它有两个读音，我们拿来试下：

```python
from pypinyin import pinyin
print(pinyin('朝阳'))
```

运行结果：

```python
[['zhāo'], ['yáng']]
```

好吧，它只给出来了一个读音，但是如果我们想要另外一种读音咋办呢？

其实很简单，只需添加 heteronym 参数并设置为 True 就好了，我们试下：

```python
from pypinyin import pinyin
print(pinyin('朝阳', heteronym=True))
```

运行结果：

```python
[['zhāo', 'cháo'], ['yáng']]
```

OK 了，这下子就显示出来了两个读音了，而且我们也明白了结果为什么是一个二维列表，因为里面的一维的结果可能是多个，比如多音字的情况就是这样。

但这个多少解析起来有点麻烦，很多情况下我们是不需要管多音字的，我们只是用它来转换一下名字而已，而处理上面的二维数组又比较麻烦。

所以有没有一个方法直接给我们一个一维列表呢？有！

我们可以使用 lazy_pinyin 这个方法来生成，尝试一下：

```python
from pypinyin import pinyin
print(pinyin('聪明的小兔子'))
```

运行结果：

```python
['cong', 'ming', 'de', 'xiao', 'tu', 'zi']
```

这时候观察到得到的是一个列表，并且不再包含音调了。

这里我们就有一个疑问了，为啥 pinyin 方法返回的结果默认是带音调的，而 lazy_pinyin 是不带的，这里面就涉及到一个风格转换的问题了。

## 风格转换

我们可以对结果进行一些风格转换，比如不带声调风格、标准声调风格、声调在拼音之后、声调在韵母之后、注音风格等等，比如我们想要声调放在拼音后面，可以这么来实现：

```python
from pypinyin import lazy_pinyin, Style

style = Style.TONE3
print(lazy_pinyin('聪明的小兔子', style=style))
```

运行结果：

```python
['cong1', 'ming2', 'de', 'xiao3', 'tu4', 'zi']
```

可以看到运行结果每个拼音后面就多了一个声调，这就是其中的一个风格，叫做 TONE3，其实还有很多风格，下面是我从源码里面找出来的定义：

```python
#: 普通风格，不带声调。如： 中国 -> ``zhong guo``
NORMAL = 0
#: 标准声调风格，拼音声调在韵母第一个字母上（默认风格）。如： 中国 -> ``zhōng guó``
TONE = 1
#: 声调风格2，即拼音声调在各个韵母之后，用数字 [1-4] 进行表示。如： 中国 -> ``zho1ng guo2``
TONE2 = 2
#: 声调风格3，即拼音声调在各个拼音之后，用数字 [1-4] 进行表示。如： 中国 -> ``zhong1 guo2``
TONE3 = 8
#: 声母风格，只返回各个拼音的声母部分（注：有的拼音没有声母，详见 `#27`_）。如： 中国 -> ``zh g``
INITIALS = 3
#: 首字母风格，只返回拼音的首字母部分。如： 中国 -> ``z g``
FIRST_LETTER = 4
#: 韵母风格，只返回各个拼音的韵母部分，不带声调。如： 中国 -> ``ong uo``
FINALS = 5
#: 标准韵母风格，带声调，声调在韵母第一个字母上。如：中国 -> ``ōng uó``
FINALS_TONE = 6
#: 韵母风格2，带声调，声调在各个韵母之后，用数字 [1-4] 进行表示。如： 中国 -> ``o1ng uo2``
FINALS_TONE2 = 7
#: 韵母风格3，带声调，声调在各个拼音之后，用数字 [1-4] 进行表示。如： 中国 -> ``ong1 uo2``
FINALS_TONE3 = 9
#: 注音风格，带声调，阴平（第一声）不标。如： 中国 -> ``ㄓㄨㄥ ㄍㄨㄛˊ``
BOPOMOFO = 10
#: 注音风格，仅首字母。如： 中国 -> ``ㄓ ㄍ``
BOPOMOFO_FIRST = 11
#: 汉语拼音与俄语字母对照风格，声调在各个拼音之后，用数字 [1-4] 进行表示。如： 中国 -> ``чжун1 го2``
CYRILLIC = 12
#: 汉语拼音与俄语字母对照风格，仅首字母。如： 中国 -> ``ч г``
CYRILLIC_FIRST = 13
```

有了这些，我们就可以轻松地实现风格转换了。

好，再回到原来的问题，为什么 pinyin 的方法默认带声调，而 lazy_pinyin 方法不带声调，答案就是：它们二者使用的默认风格不同，我们看下它的函数定义就知道了：

pinyin 方法的定义如下：

```python
def pinyin(hans, style=Style.TONE, heteronym=False, errors='default', strict=True)
```

lazy_pinyin 方法的定义如下：

```python
def lazy_pinyin(hans, style=Style.NORMAL, errors='default', strict=True)
```

这下懂了吧，因为 pinyin 方法默认使用了 TONE 的风格，而 lazy_pinyin 方法默认使用了 NORMAL 的风格，所以就导致二者返回风格不同了。

好了，有了这两个函数的定义，我们再来研究下其他的参数，比如定义里面的 errors 和 strict 参数又怎么用呢？

## 错误处理

在这里我们先做一个测试，比如我们传入无法转拼音的字，比如：

```python
from pypinyin import lazy_pinyin
print(lazy_pinyin('你好☆☆，我是xxx'))
```

其中包含了星号两个，还有标点一个，另外还包含了一个 xxx 英文字符，结果会是什么呢？

```python
['ni', 'hao', '☆☆，', 'wo', 'shi', 'xxx']
```

可以看到结果中星号和英文字符都作为一个整体并原模原样返回了。

那么这种特殊字符可以单独进行处理吗？当然可以，这里就用到刚才提到的 errors 参数了。

errors 参数是有几种模式的：

*  default：默认行为，不处理，原木原样返回
* ignore：忽略字符，直接抛掉
* replace：直接替换为去掉 `\u` 的 unicode 编码
* callable 对象：当传入一个可调用的对象的时候，则可以自定义处理方式。

下面是 errors 这个参数的源码实现逻辑：

```python
def _handle_nopinyin_char(chars, errors='default'):
    """处理没有拼音的字符"""
    if callable_check(errors):
        return errors(chars)

    if errors == 'default':
        return chars
    elif errors == 'ignore':
        return None
    elif errors == 'replace':
        if len(chars) > 1:
            return ''.join(text_type('%x' % ord(x)) for x in chars)
        else:
            return text_type('%x' % ord(chars))
```

当处理没有拼音的字符的时候，errors 的不同参数会有不同的处理结果，更详细的逻辑可以翻看源码。

好了，下面我们来尝试一下，比如我们想将不能转拼音的字符去掉，则可以这么设置：

```python
from pypinyin import lazy_pinyin
print(lazy_pinyin('你好☆☆，我是xxx', errors='ignore'))
```

运行结果：

```python
['ni', 'hao', 'wo', 'shi']
```

如果我们想要自定义处理，比如把 `☆` 转化为  `※`，则可以这么设置：

```python
print(lazy_pinyin('你好☆☆，我是xxx', errors=lambda item: ''.join(['※' if c == '☆' else c for c in item])))
```

运行结果：

```python
['ni', 'hao', '※※，', 'wo', 'shi', 'xxx']
```

如上便是一些相关异常处理的操作，我们可以随心所欲地处理自己想处理的字符了。

## 严格模式

最后再看下 strict 模式，这个参数用于控制处理声母和韵母时是否严格遵循 [《汉语拼音方案》](http://www.moe.edu.cn/s78/A19/yxs_left/moe_810/s230/195802/t19580201_186000.html) 标准。

下面的一些说明来源于官方文档：

当 strict 参数为 True 时根据 [《汉语拼音方案》](http://www.moe.edu.cn/s78/A19/yxs_left/moe_810/s230/195802/t19580201_186000.html) 的如下规则处理声母、在韵母相关风格下还原正确的韵母：

- 21 个声母： `b p m f d t n l g k h j q x zh ch sh r z c s` （**y, w 不是声母**）
- i行的韵母，前面没有声母的时候，写成yi(衣)，ya(呀)，ye(耶)，yao(腰)，you(忧)，yan(烟)， yin(因)，yang(央)，ying(英)，yong(雍)。（**y 不是声母**）
- u行的韵母，前面没有声母的时候，写成wu(乌)，wa(蛙)，wo(窝)，wai(歪)，wei(威)，wan(弯)， wen(温)，wang(汪)，weng(翁)。（**w 不是声母**）
- ü行的韵母，前面没有声母的时候，写成yu(迂)，yue(约)，yuan(冤)，yun(晕)；ü上两点省略。 （**韵母相关风格下还原正确的韵母 ü**）
- ü行的韵跟声母j，q，x拼的时候，写成ju(居)，qu(区)，xu(虚)，ü上两点也省略； 但是跟声母n，l拼的时候，仍然写成nü(女)，lü(吕)。（**韵母相关风格下还原正确的韵母 ü**）
- iou，uei，uen前面加声母的时候，写成iu，ui，un。例如niu(牛)，gui(归)，lun(论)。 （**韵母相关风格下还原正确的韵母 iou，uei，uen**）

当 strict 为 False 时就是不遵守上面的规则来处理声母和韵母， 比如：`y`, `w` 会被当做声母，yu(迂) 的韵母就是一般认为的 `u` 等。

具体差异可以查看源码中 [tests/test_standard.py](https://github.com/mozillazg/python-pinyin/blob/master/tests/test_standard.py) 中的对比结果测试用例。

## 自定义拼音

如果对库返回的结果不满意，我们还可以自定义自己的拼音库，这里用到的方法就有 load_single_dict 和 load_phrases_dict 方法了。

比如刚才我们看到 "朝阳" 两个字的发音默认返回的是 zhao yang，我们想默认返回 chao yang，那可以这么做：

```python
from pypinyin import lazy_pinyin, load_phrases_dict

print(lazy_pinyin('朝阳'))
personalized_dict = {
    '朝阳': [['cháo'], ['yáng']]
}
load_phrases_dict(personalized_dict)
print(lazy_pinyin('朝阳'))
```

这里我们自定义了一个词典，然后使用 load_phrases_dict 方法设置了一下就可以了。

运行结果：

```python
['zhao', 'yang']
['chao', 'yang']
```

这样就可以完成自定义的设置了。

在一些项目里面我们可以自定义很多拼音库，然后加载就可以了。

另外我们还可以注册样式实现自定义，比如将某个拼音前面加上 Emoji 表情，样例：

```python
from pypinyin.style import register
from pypinyin import lazy_pinyin

@register('kiss')
def kiss(pinyin, **kwargs):
    if pinyin == 'me':
        return f'😘{pinyin}'
    return pinyin

print(lazy_pinyin('么么哒', style='kiss'))
```

运行结果：

```python
['😘me', '😘me', 'dá']
```

这里我们调用 register 方法注册了一个样式 style，然后转换的时候指定即可，通过观察运行结果我们可以发现，这样我们就可以将 me 字的拼音前面加上 😘 这个 Emoji 表情了。

以上就是 PyPinyin 这个库的基本用法，更多的用法建议大家看看源码或者看 API 文档：<https://pypinyin.readthedocs.io/zh_CN/master/api.html>。
