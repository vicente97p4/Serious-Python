# sys 모듈에 path 변수는 모듈 위치가 저장되어있는 경로 리스트이다.

import sys
print(sys.path)
sys.path.append('/foo/bar')
print('/foo/bar' in sys.path)