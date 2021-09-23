# 사용자 지정 불러오기를 사용해서 불러오기 방법을 확장할 수 있다. 여기서는 .hy 확장자 파일을 불러온다.
# 메타 경로 파인더

# 메타 경로 파인더 객체는 로더 객체를 반환하는 find_module(fullname, path=None) 메서드를 호출해야 한다.
import os
import sys


# .hy 파일을 찾아서 이 로더에 전달해주면 파일을 컴파일 하고, 등록하고, 일부 속성을 설정한 다음 파이썬 인터프리터로 반환한다.
class MetaLoader(object):
    def __init__(self, path):
        self.path = path

    def is_package(self, fullname):
        dirpath = '/'.join(fullname.split('.'))
        for pth in sys.path:
            pth = os.path.abspath(pth)
            composed_path = f'{pth}/{dirpath}/__init__.hy'
            if os.path.exists(composed_path):
                return True    
        return False

    def load_module(self, fullname):
        if fullname in sys.modules:
            return sys.modules[fullname]
        if not self.path:
            return

        sys.modules[fullname] = None
        
        # import_file_to_module 함수는 현재 구현되지 않았다. 기능은 .hy 소스파일을 읽고, 파이썬 코드로 컴파일하고, 파이썬 모듈 객체를 반환한다.
        mod = import_file_to_module(fullname, self.path) 

        ispkg = self.is_package(fullname)

        # 속성 설정
        mod.__file__ = self.path
        mod.__loader__ = self
        mod.__name__ = fullname

        if ispkg:
            mod.__path__ = []
            mod.__package__ = fullname
        else:
            mod.__package__ = fullname.rpartition('.')[0]

        sys.modules[fullname] = mod # 파일 등록
        return mod



class MetaImporter(object):
    def find_on_path(self, fullname):
        fls = ['%s/__init__.hy', '%s.hy']
        dirpath = '/'.join(fullname.split('.'))

        for pth in sys.path:
            pth = os.path.abspath(pth)
            for fp in fls:
                composed_path = fp % (f'{pth}/{dirpath}')
                if os.path.exists(composed_path):
                    return composed_path

    def find_module(self, fullname, path=None):
        path = self.find_on_path(fullname)
        
        if path:
            return MetaLoader(path)

sys.meta_path.append(MetaImporter())