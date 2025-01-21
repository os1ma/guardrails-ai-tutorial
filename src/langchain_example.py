from dotenv import load_dotenv
from guardrails import Guard, OnFailAction
from guardrails.hub import RegexMatch
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv(override=True)

guard = Guard().use(
    RegexMatch,
    regex=r"(?!\d{3}-\d{4}-\d{4}).*",
    on_fail=OnFailAction.EXCEPTION,
)

prompt = ChatPromptTemplate.from_template("Answer this question {question}")
model = ChatOpenAI(model="gpt-4o-mini")
output_parser = StrOutputParser()

chain = prompt | model | guard.to_runnable() | output_parser

result = chain.invoke(
    {"question": "適当な電話番号を生成してください"},
)
print(result)
