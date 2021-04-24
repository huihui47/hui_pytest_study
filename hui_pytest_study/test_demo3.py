import pytest
#获得多个参数化参数的所有组合，可以堆叠参数化装饰器
@pytest.mark.parametrize("a",[0,1])
@pytest.mark.parametrize("b",[2,3])
def test_foo(a,b):
    print("测试数据组合：a->%s,b->%s" %(a,b))