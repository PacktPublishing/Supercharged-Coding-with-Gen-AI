import inspect

from openai import OpenAI
from openai.types.chat import ChatCompletion


SURROUND = "You are provided with a Python function signature enclosed with {{{ FUNCTION }}}."
SINGLE_TASK = "Your task is to implement the function."

SRC_CODE = """def get_geometric_mean(\n\tnet_returns: Dict[str, float],\n) -> float:"""


def get_user_prompt(src: str) -> str:
    return f""" 
    FUNCTION: {{{{{{ {src} }}}}}} 

   CODE: 
    """


if __name__ == '__main__':
    client: OpenAI = OpenAI()
    system_prompt = f"{SURROUND} {SINGLE_TASK}"
    user_prompt = get_user_prompt(SRC_CODE)
    completion: ChatCompletion = client.chat.completions.create(
        model="o3-mini-2025-01-31",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    output = completion.choices[0].message.content
    print(output)


