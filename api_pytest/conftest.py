import os
import pytest,yaml
@pytest.fixture(scope="session")
def env(request):
    path1=request.config.rootdir
    config_path = os.path.join(path1, 'config','config.yaml')
    # config_path='D:/PycharmProjects/pythonProject/api_pytest/config/config.yaml'
    with open(config_path) as f:
        env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
    return env_config