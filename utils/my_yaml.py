# Description: YAML文件处理

import yaml


# 读取Yaml文件方法
def read_yaml(yaml_path) -> dict:
    with open(yaml_path, encoding="utf-8", mode="r") as f:
        result = yaml.load(stream=f, Loader=yaml.FullLoader)
        return result


# 写入YAML文件的方法
def write_yaml(yaml_path, data):
    with open(yaml_path, encoding="utf-8", mode="w") as f:
        yaml.dump(data, stream=f, allow_unicode=True)