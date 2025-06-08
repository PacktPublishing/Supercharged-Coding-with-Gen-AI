import re

import openai
from openai import OpenAI

USER_PROMPT = """
def print_fibonacci_sequence(n: int) -> None:
"""
SYSTEM_PROMPT = ("You will be provided with a Python function signature. Your task is to implement the function. Return "
                 "code only.")


def get_code_with_instructions(code: str) -> str:
    """
    Add a comment to the code for specific code completion instruction
    :param code: Python code as string
    :return: The code with additional instruction - "Complete this code"
    """

    return code + "\n# Complete this code"


if __name__ == "__main__":
    client: OpenAI = OpenAI()

    completion: openai.ChatCompletion = (
        client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=1,
            n=2,
            messages=[{"role": "system", "content": SYSTEM_PROMPT},
                      {"role": "system", "content": "Include docstring and typehints."},
                      {"role": "user", "content": get_code_with_instructions(USER_PROMPT)}],
        ))

    for i in range(2):
        output = completion.choices[i].message.content
        code_suggestion = re.sub(r"(.*?)```python(.*?)```(.*)", r"\2", output, flags=re.DOTALL).strip()
        print(f"Output {i + 1}:")
        print(code_suggestion)
