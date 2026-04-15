import File2_APIConfig
from File2_APIConfig import build_api_config


class MiniAgent:
    def __init__(self,api_key,default_model="gpt-3.5"):
        self.api_key=api_key
        self.default_model=default_model
        self.history=[]
    def chat(self,prompt,**kwargs):
        self.history.append(prompt)
        API_request=build_api_config(self.default_model,**kwargs)
        #打印一段模拟请求的日志
        print("model",API_request["model"])
        print("len",len(self.history))
        print("config",API_request)
        #返回一个模拟的大模型回复字符串,f"模拟回复：已收到你的提示词
        return f"模拟回复：已收到你的提示词{prompt}"

    def get_history(self):
        return self.history


# 1. 实例化 Agent
agent = MiniAgent(api_key="sk-123456", default_model="gpt-4")

# 2. 第一次对话，使用默认配置
reply1 = agent.chat("你好，你是谁？")
# 预期打印: [请求发出] 模型: gpt-4 | 记忆数量: 1 | 配置: {'model': 'gpt-4'} (如果有其他 kwargs 也打印出来)
print(reply1)

# 3. 第二次对话，开启流式传输并调高温度
reply2 = agent.chat("给我讲个笑话", temperature=0.9, stream=True)
# 预期打印: [请求发出] 模型: gpt-4 | 记忆数量: 2 | 配置: {'model': 'gpt-4', 'temperature': 0.9, 'stream': True}
print(reply2)

# 4. 查看历史记忆
print("历史记忆:", agent.get_history())
# 预期输出: 历史记忆: ['你好，你是谁？', '给我讲个笑话']