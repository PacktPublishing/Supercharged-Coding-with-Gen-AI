import inspect

SURROUND = ""
SINGLE_TASK = ""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def get_user_prompt(func: callable) -> str:
    ...


if __name__ == "__main__":
    from openai import OpenAI
    from openai.types.chat import ChatCompletion

    client: OpenAI = OpenAI()

    completion: ChatCompletion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[],
    )
    print("Docstring:", completion.choices[0].message.content)
