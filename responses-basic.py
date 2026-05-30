from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-5-nano",
    instructions="You are a helpful assistant.",		# 시스템 메시지 { "role": "system", "content": "..." } 
    input="홍길동전을 한 문장으로 요약해줘.",		# 사용자 메시지 { "role": "user", "content": "..." } 
)


print(response)
print(response.output_text)
