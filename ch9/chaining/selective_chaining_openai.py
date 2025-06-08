import inspect
import re
from typing import Dict

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


def get_refactor_user_prompt(assistant_output: str) -> str:
    code: str = re.sub(r"(.*?)```python(.*?)```(.*)",
                       r"\2",
                       assistant_output,
                       flags=re.DOTALL).strip()
    user_prompt: str = f"""
    OLD: {{{{{{ {code} }}}}}}
    
    REFACTORED: 
    """
    return user_prompt


if __name__ == '__main__':
    client: OpenAI = OpenAI()

    prompt_1: str = f"{SURROUND} {SINGLE_TASK}"
    prompt_2: str = "You are provided with a Python code enclosed in {{{ FUNCTION }}}. Your task is to add type hints to all variables."
    prompt_3: str = "You are provided with a Python code enclosed in {{{ FUNCTION }}}. Your task is to include Google Style docstring."

    prompts: Dict[str, callable] = {
        prompt_1: get_user_prompt,
        prompt_2: get_refactor_user_prompt,
        prompt_3: get_refactor_user_prompt}

    next_input: str = get_average_return

    for prompt, func in prompts.items():
        completion: ChatCompletion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": func(next_input)},

            ], )
        next_input: str = completion.choices[0].message.content

    print(next_input)


