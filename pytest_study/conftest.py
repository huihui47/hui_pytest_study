#import pytest
#@pytest.fixture(autouse="true")
#def myfixture():
#    print("执行myfixture")
import pytest
@pytest.fixture(params=["参数1","参数2"])
def myfixture(request):
    print("执行myfixture，带参数%s"%request.param)