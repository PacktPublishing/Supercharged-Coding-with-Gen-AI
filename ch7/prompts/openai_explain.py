import inspect

from openai import OpenAI
from openai.types.chat import ChatCompletion

from ch7.src.manhattan import get_manhattan_distance

SURROUND = """you are provided with:
1. A Python function enclosed with {{{ FUNCTION }}}
2. Explanation points enclosed with {{ HEADERS }}}."""
SINGLE_TASK = "Your task is to explain the function using the explanation points."


POINTS = """1. Function’s purpose
2. Arguments and their types
3. Step-by-step data flow
4. Output and its types
5. Potential edge cases"""


def get_user_prompt(func: callable) -> str:
    return f"""
    FUNCTION: {{{{{{ {inspect.getsource(func)} }}}}}}
    
    POINTS: {{{{{{ {POINTS} }}}}}}

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


