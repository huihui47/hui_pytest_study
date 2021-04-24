#参数化
import pytest
def add_function(a,b):
    return a+b
@pytest.mark.parametrize("a,b,expected",   #“参数名”
                         [(3,5,8),          #列表数据，每个元素与参数名一一对应，如：a——(3,5,8)
                          (-1,-2,-3),
                          (100,200,300),
                          ])
def test_add(a,b,expected):
    assert add_function(a,b) == expected