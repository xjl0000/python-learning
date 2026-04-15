def build_api_config(model_name,**kwargs):
    base_config={
        "temperature":0.7,
        "max_tokens":100,
        "stream":False,
        "model":model_name
    }
    base_config.update(kwargs)
    return base_config

# 测试 1：只传必传参数
config1 = build_api_config("gpt-3.5")
print(config1)
# 预期输出: {'temperature': 0.7, 'max_tokens': 100, 'stream': False, 'model': 'gpt-3.5'}

# 测试 2：覆盖默认值 + 增加新参数
config2 = build_api_config("gpt-4", temperature=0.9, top_p=1.0)
print(config2)
# 预期输出: {'temperature': 0.9, 'max_tokens': 100, 'stream': False, 'model': 'gpt-4', 'top_p': 1.0}