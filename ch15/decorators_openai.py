from openai import OpenAI
from openai.types.chat import ChatCompletion

SURROUND = "You are provided with a partial Python script in {{{FIZZBUZZ_PRINTER}}}, where some of the code is missing."
SINGLE_TASK = "Implement the decorators with the missing implementation in the code."


def get_user_prompt(script_path: str) -> str:
    with open(script_path, 'r') as file:
        incomplete_code = file.read()

    return f"""
    FIZZBUZZ_PRINTER: {{{{{{ {incomplete_code} }}}}}}
    
    CODE: 
    """


if __name__ == '__main__':
    client: OpenAI = OpenAI()
    system_prompt = f"{SURROUND} {SINGLE_TASK}"
    user_prompt = get_user_prompt("ch15/fizzbuzz_printer_starter.py")
    completion: ChatCompletion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    output = completion.choices[0].message.content

    print(output)
