import pytest
import yaml
def add_function(a,b):
    return a+b
#参数数据从文件读取
# @pytest.mark.parametrize("a,b,expected",   #“参数名”
#                         yaml.safe_load(open("./data.yml"))["datas"]     #列表数据，每个元素与参数名一一对应，如：a——(3,5,8)
#                         ,ids=yaml.safe_load(open("./data.yml"))["myid"]
#                        )
#读取文件步骤可以抽离出来，为单独的函数
def get_datas():
    with open("./data.yml") as f:
        datas=yaml.safe_load(f)
        print(datas)
        add_datas=datas["datas"]
        add_ids=datas["myid"]
        return [add_datas,add_ids]
@pytest.mark.parametrize("a,b,expected",
                         get_datas()[0],
                         ids=get_datas()[1])
def test_add(a,b,expected):
    assert add_function(a,b) == expected