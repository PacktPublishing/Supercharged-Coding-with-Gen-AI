import inspect

SURROUND = "You will be provided with a Python function enclosed with {{{ Function }}}."
SINGLE_TASK = "Your task is to generate Google Style docstring for it."


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def get_user_prompt(func: callable) -> str:
    return f"""
    FUNCTION: {{{{{{ {inspect.getsource(func)} }}}}}}

    GOOGLE STYLE DOCSTRING:
    """


if __name__ == "__main__":
    from openai import OpenAI
    from openai.types.chat import ChatCompletion

    client: OpenAI = OpenAI()

    system_prompt =  f"{SURROUND} {SINGLE_TASK}"
    user_prompt = get_user_prompt(Singleton.__call__)

    completion: ChatCompletion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    print("Docstring:", completion.choices[0].message.content)


