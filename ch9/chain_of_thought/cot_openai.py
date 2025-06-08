import inspect

from openai import OpenAI
from openai.types.chat import ChatCompletion

from ch9.chain_of_thought.get_average_return import get_average_return

SURROUND = "You are provided with a Python function enclosed with {{{ FUNCTION }}} that calls functions that should be completed."
SINGLE_TASK = "Your task is to implement the missing function."


def get_user_prompt(func: callable) -> str:
    return f""" 
    FUNCTION: {{{{{{ {inspect.getsource(func)} }}}}}} 

   CODE: 
    """


if __name__ == '__main__':
    client: OpenAI = OpenAI()
    system_prompt = f"{SURROUND} {SINGLE_TASK}"
    user_prompt = get_user_prompt(get_average_return)
    completion: ChatCompletion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    output = completion.choices[0].message.content
    print(output)
