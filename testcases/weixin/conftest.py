# author:小莉
import pytest

#读取数据
def read_data():
    return ['fangfang', 'zhouzhou', 'yanyang']

@pytest.fixture(scope="function",params=read_data(),ids=['ff','yy','zz'],name="kwkwkwkw")
def execute_sql(request):
    print("weixin下的固件")
    #固定写法 param没有s
    yield request.param
    print("weixin下的固件")