from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=[
        {
            "role": "user",
            "content": "'LLM'으로 삼행시(각 글자로 시작해야 함)를 작성해줘.",
        },
    ],
    #temperature=0
    temperature=1.2
)


print(completion.choices[0].message.content)
