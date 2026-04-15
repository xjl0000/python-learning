from openai import OpenAI
import os


class DramaTranslator:
    def __init__(self,personality,model="qwen-plus-2025-07-28"):
        self.model=model
        self.client = OpenAI(api_key=os.getenv("QWEN_API_KEY"), base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")
        self.messages=[
            {"role":"system","content":f"你是一个英文翻译官。无论用户说什么，你都要翻译成英文。但你的性格是：{personality}。在翻译的结果前后，必须加上符合你性格的中文吐槽。"}
        ]

    def translate(self,text):
        self.messages.append({"role": "user", "content": text})
        try:
            response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            temperature=0.7
            )
            reply = response.choices[0].message.content
            self.messages.append({"role": "assistant", "content": reply})
            return reply
        except Exception as e:
            print(f"API 调用翻车了: {e}")


# 1. 实例化一个“暴躁老哥”翻译官
bot = DramaTranslator( personality="严厉，讽刺味深厚的英语老师")

# 2. 第一次翻译
reply1 = bot.translate("我喜欢你")
print(reply1)
# 预期输出类似: "别烦老子！连这都不会说？听好了：I'd like an iced Americano. 赶紧拿笔记下来，蠢货！"

# 3. 第二次翻译（测试它的记忆力）
reply2 = bot.translate("那拿铁怎么说？")
print(reply2)
# 预期输出类似: "你事怎么这么多？刚喝完冰美式又要拿铁！Latte! 懂了吗？"