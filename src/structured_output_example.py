"""
うまく動作しませんでした
"""

import openai
from dotenv import load_dotenv
from guardrails import Guard
from pydantic import BaseModel, Field

load_dotenv(override=True)


class Pet(BaseModel):
    pet_type: str = Field(description="Species of pet")
    name: str = Field(description="a unique pet name")


prompt = """
    What kind of pet should I get and what should I name it?

    ${gr.complete_json_suffix_v2}
"""
guard = Guard.for_pydantic(output_class=Pet, prompt=prompt)

raw_output, validated_output, *rest = guard(
    llm_api=openai.completions.create,
    engine="gpt-3.5-turbo-instruct",
)

print(validated_output)
