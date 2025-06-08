import inspect

from openai import OpenAI
from openai.types.chat import ChatCompletion

from ch10.app import get_euclidean_distance

SURROUND = """You are provided with:
1. A Python function implementation enclosed with {{{ FUNCTION }}}
2. Lines to be refactored enclosed with {{{ OLD }}}
3. A library to be used in the new code enclosed with {{{ LIBRARY }}}."""
SINGLE_TASK = "Your task is to return a new implementation for the old lines using the specified library."

LINES = """dist_2 = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        dist_2 += (a[i][j] - b[i][j]) ** 2
"""


def get_user_prompt(func: callable, library: str, lines: str) -> str:
    return f"""
    FUNCTION: {{{{{{ {inspect.getsource(func)} }}}}}}
    
    LINES: {{{{{{ {lines} }}}}}}
    
    LIBRARY: {{{{{{ {library} }}}}}}

    REFACTORED:
    """


if __name__ == "__main__":
    client: OpenAI = OpenAI()

    system_prompt = f"{SURROUND} {SINGLE_TASK}"
    user_prompt = get_user_prompt(get_euclidean_distance, "NumPy", LINES)

    completion: ChatCompletion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    print("Explanation:", completion.choices[0].message.content)


