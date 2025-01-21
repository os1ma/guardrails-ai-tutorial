from guardrails import Guard, OnFailAction
from guardrails.hub import RegexMatch

guard = Guard().use(
    RegexMatch,
    regex=r"(?!\d{3}-\d{4}-\d{4}).*",
    on_fail=OnFailAction.EXCEPTION,
)

guard.validate("00-0000-0000")
print("Guardrail passes")

guard.validate("000-0000-0000")
# 例外が発生
