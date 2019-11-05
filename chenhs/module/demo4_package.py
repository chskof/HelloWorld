"""
在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录。
目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包

最简单的情况，放一个空的 :file:__init__.py就可以了。
当然这个文件中也可以包含一些初始化代码或者为（将在后面介绍的） __all__变量赋值。
"""

"""
用户可以每次只导入一个包里面的特定模块，比如:

import sound.effects.echo
这将会导入子模块:sound.effects.echo。 他必须使用全名去访问:

sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
"""

"""
导入子模块的方法是:

from sound.effects import echo

这同样会导入子模块: echo，并且他不需要那些冗长的前缀，所以他可以这样使用:

echo.echofilter(input, output, delay=0.7, atten=4)
"""


"""
直接导入一个函数或者变量:

from sound.effects.echo import echofilter
同样的，这种方法会导入子模块: echo，并且可以直接使用他的 echofilter() 函数:

echofilter(input, output, delay=0.7, atten=4)

注意当使用 from package import item 这种形式的时候，对应的 item 既可以是包里面的子模块（子包），
或者包里面定义的其他名称，比如函数，类或者变量。

"""


"""
from package import *

导入语句遵循如下规则：如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，
那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。

如果 __all__ 真的没有定义，那么使用from sound.effects import *这种语法的时候，
就不会导入包 sound.effects 里的任何子模块


使用 from Package import specific_submodule 这种方法永远不会有错。事实上，这也是推荐的方法
"""