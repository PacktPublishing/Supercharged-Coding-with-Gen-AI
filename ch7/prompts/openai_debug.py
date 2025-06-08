import inspect

from openai import OpenAI
from openai.types.chat import ChatCompletion

from ch7.src.manhattan import get_manhattan_distance

SURROUND = """you are provided with:
1. A Python function enclosed with {{{ FUNCTION }}}
2. Arguments requirements enclosed with {{ REQUIREMENTS }}}."""
SINGLE_TASK = "Your task is to call the function with the data requirements."

REQUIREMENTS = """
1. 5 rows
2. 3 columns
3. floats and integers in cells
"""


def get_user_prompt(func: callable) -> str:
    return f"""
    FUNCTION: {{{{{{ {inspect.getsource(func)} }}}}}}

    REQUIREMENTS: {{{{{{ {REQUIREMENTS} }}}}}}

    EXPLANATION:
    """


if __name__ == "__main__":
    client: OpenAI = OpenAI()

    system_prompt = f"{SURROUND} {SINGLE_TASK}"
    user_prompt = get_user_prompt(get_manhattan_distance)

    completion: ChatCompletion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    print("Explanation:", completion.choices[0].message.content)


