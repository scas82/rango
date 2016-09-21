import re

txt = """
# skip me
192.168.1.2/2.2.2.2
255.244.12.3/24
"""

PATT = '(?P<ip>[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)' \
       '(\/(?P<mask1>[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) | ' \
       '(\/(?P<mask2>[1-9][0-9])))?'
ip_list = []

for l in txt.split('\n'):
    if re.match('^\s\t*$|^\s*\t*#', l): pass
    m = re.match(PATT, l)
    if m:
        ip_list += [m.groupdict()]

print(ip_list)

class SimoTest(object):
    """Simo DOC"""
    def __init__(self):
        self.__str__ = 'str'
        self.__doc__ = 'doc'
    def __doc__(self):
        return 'mystr'
    def __str__(self):
        return 'mystr'


s = SimoTest()

print(s)

class Test1(object):
    """Test class"""
    def __init__(self):
        pass
    def method1(self):
        pass
    def method2(self):
        pass

class Test3(object):
    """Test class"""
    def __init__(self):
        pass
    def method1(self):
        pass
    def method2(self):
        pass

class Test3(object):
    """Test class"""
    def __init__(self):
        pass
    def method1(self):
        pass
    def method2(self):
        pass

