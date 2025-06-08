import openai
from openai import OpenAI


SURROUND = """You are provided with:
1. A Python function signature enclosed with {{{ FUNCTION }}}.
2. Example signatures enclosed with {{{ FUNCTION_i }}} followed by the corresponding implementation enclosed with {{{ CODE_i }}}.
"""
SINGLE_TASK = "Your task is to implement the function."

INPUT_1 = """def get_area(radius: float) -> float:"""

OUTPUT_1 = """def get_area(radius: float) -> float:
    area: float = np.pi * radius ** 2
    return area"""

INPUT_2 = """def get_arithmetic_mean(x1: float, x2: float) -> float:"""

OUTPUT_2 = """def get_arithmetic_mean(x1: float, x2: float) -> float:
    arithmetic_mean: float = (x1 + x2) / 2
    return arithmetic_mean"""

FEW_SHOTS = [
    (INPUT_1, OUTPUT_1),
    (INPUT_2, OUTPUT_2),
]


def get_user_prompt(signature: str, few_shots: list) -> str:
    prompt = ""
    for i, (input_, output_) in enumerate(few_shots):
        prompt += f"""  
    FUNCTION_{i + 1}:  {{{{{{ {input_} }}}}}}
    CODE_{i + 1}:       {{{{{{ {output_} }}}}}}"""

    prompt += f"""
    FUNCTION:          {{{{{{ {signature} }}}}}}
    CODE:
    """
    return prompt




if __name__ == "__main__":
    system_prompt = f"{SURROUND} {SINGLE_TASK}"
    user_prompt = get_user_prompt("def print_fibonacci_sequence(n: int) -> None:", FEW_SHOTS)

    client: OpenAI = OpenAI()

    completion: openai.ChatCompletion = (
        client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        ))

    print(completion.choices[0].message.content)
