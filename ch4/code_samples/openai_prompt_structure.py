SURROUND = "Your context here"
SINGLE_TASK = "Your task here"


def get_user_prompt(*args, **kwargs) -> str:
    """" Your Data here """
    ...


system_prompt = f"{SURROUND} {SINGLE_TASK}"
user_prompt = get_user_prompt(...)

messages = [
    {"role": "system", "content": f"{SURROUND} {SINGLE_TASK}"},
    {"role": "user", "content": user_prompt},
]