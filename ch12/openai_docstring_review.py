import inspect
from types import ModuleType
from typing import Dict

from openai import OpenAI
from openai.types.chat import ChatCompletion

import distances

SURROUND = """You are provided with:
1. A Python function implementation enclosed with {{{ FUNCTION }}}
2. A docstring for the function enclosed with {{{ DOCSTRING }}}."""
SINGLE_TASK = "Your task is determine if the docstring matches the implementation."


def extract_functions_info(module: ModuleType) -> Dict[str, Dict[str, str]]:
    functions_info: Dict[str, Dict[str, str]] = {}
    for name, obj in inspect.getmembers(module, inspect.isfunction):
        src: str = inspect.getsource(obj)
        doc: str = inspect.getdoc(obj) or ""
        functions_info[name] = {
            "source": src,
            "docstring": doc
        }
    return functions_info


def get_user_prompt(info: Dict[str, str]) -> str:
    return f"""
    FUNCTION: {{{{{{ {info.get("source")} }}}}}}

    DOCSTRING: {{{{{{ {info.get("docstring")} }}}}}}

    MATCHES:
    """


if __name__ == "__main__":
    client: OpenAI = OpenAI()

    system_prompt = f"{SURROUND} {SINGLE_TASK}"

    func_info: Dict[str, Dict[str, str]] = extract_functions_info(distances)
    for func, info in func_info.items():

        user_prompt = get_user_prompt(info)

        completion: ChatCompletion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        print("Function:", func)
        print("Docstring:", info.get("docstring"))
        print("Source:", info.get("source"))
        print("Matches:", completion.choices[0].message.content)
