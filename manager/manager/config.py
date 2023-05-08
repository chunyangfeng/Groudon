"""
Date: 2023/5/8 16:25

Author: Fengchunyang

Contact: 274387451@qq.com

Record:
    2023/5/8 Create file.

"""
import os
from pathlib import Path


ENV = os.environ.get("GROUDON_ENV", "development")


class BasicConfig:
    """通用配置文件基类"""
    # debug标记
    DEBUG = False

    # 允许访问的地址
    ALLOWED_HOSTS = ['*', ]

    # 数据库配置
    BACKEND_DB = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': f'{Path(__file__).resolve().parent.parent}/db.sqlite3',
    }


class ProdConfig(BasicConfig):
    """生产环境配置文件"""


class DevConfig(BasicConfig):
    """开发环境配置文件"""
    # debug标记
    DEBUG = True


class TestConfig(BasicConfig):
    """测试环境配置文件"""
    # debug标记
    DEBUG = True


config_mapping = {
    "development": DevConfig(),
    "product": ProdConfig(),
    "test": TestConfig(),
}

config = config_mapping.get(ENV)


if config is None:
    raise ValueError(f"环境参数配置有误，{ENV}不在可选范围内('development', 'test', 'product')")

print(f"当前加载环境为：{ENV}")

