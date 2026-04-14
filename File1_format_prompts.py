def format_prompts(prompts, prefix="请翻译："):
    if not prompts:
        return [], 0
    new_prompts = [prefix + p for p in prompts]
    return new_prompts, len(prompts)

# 正确姿势：使用字典和 **kwargs 魔法
params = {"prefix": "请优化："}
print(format_prompts(["代码"], **params))
# 输出: (['请优化：代码'], 1)