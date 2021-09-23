# 사실 import 키워드는 __import__ 함수를 사용한다.

import itertools
print(itertools)

itertools = __import__('itertools')
print(itertools)

import itertools as it
print(it)

it = __import__('itertools')
print(it)

random = __import__('RANDOM'.lower())
print(random)