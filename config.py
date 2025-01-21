from guardrails import Guard
from guardrails.hub import GibberishText

guard = Guard()
guard.name = "gibberish_guard"
guard.use(GibberishText(on_fail="exception"))  # TODO: Add parameters.
