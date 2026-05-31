from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableBranch, RunnablePassthrough

# 모델 초기화
openai_model = ChatOpenAI(model="gpt-5-nano", temperature=0.7)
claude_model = ChatAnthropic(model="claude-haiku-4-5-20251001")

# 프롬프트 템플릿 정의
template = ChatPromptTemplate.from_messages([
    ("system", "당신은 유용한 AI 서비스입니다. 사용자의 질문에 친절하게 답변해 주세요."),
    ("human", "{question}")
])

# 각 모델에 대한 독립적인 체인을 정의 
openai_chain = template | openai_model
claude_chain = template | claude_model

# RunnableBranch를 사용해서 조건부 라우팅을 설정 
branch = RunnableBranch(
    (lambda x: x.get("question").startswith("클로드"), claude_chain),
    openai_chain
)

# 최종 체인 구성
final_chain = {"question": RunnablePassthrough()} | branch


while True:
    user_input = input("질문: ")
    if user_input == "exit":
        break

    response = final_chain.invoke(user_input)
    print("답변:", response.content)
