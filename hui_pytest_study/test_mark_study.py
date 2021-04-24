#Mark标签
#方法：在测试用例/测试类前加上：@pytest.mark.标记名
import pytest
class Test_Demo4():
    @pytest.mark.demo
    def test_demo(self):
        a=5
        b=-1
        assert a!=b
        print("这是打标签为demo的用例")
    @pytest.mark.smoke
    def test_two(self):
        a=2
        b=-1
        assert a!=b
        print("这是打标签为smoke的用例")
    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    @pytest.mark.demo
    def test_add_02(self):
        b=2
        assert 0==b #注意这个用例会失败
        print("这是打标签为smoke和add的用例")
