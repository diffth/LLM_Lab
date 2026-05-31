from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()

model = ChatOpenAI(model="gpt-4.1-nano")

# 비스트림 방식으로 응답을 처리
message = HumanMessage(content="안녕? 나는 홍길동이야.")
response = model.invoke([message])
print(f"User: {message.content}")
print(f"AI: {response.content}")
print()

print("*" * 50)

# 스트림 방식으로 응답을 처리 
message = HumanMessage("내 이름이 뭐지?")
response = model.stream([message])
print(f"User: {message.content}")
print(f"AI: ", end="")
for chunk in response:
    print(chunk.content, end="|", flush=True)
