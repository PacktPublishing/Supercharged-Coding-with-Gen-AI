import openai
from openai import OpenAI

USER_PROMPT = """
user prompt here
"""
SYSTEM_PROMPT = "system prompt here"


def get_code_with_instructions(code: str) -> str:
    """
    Add a comment to the code for specific code completion instruction
    :param code: Python code as string
    :return: The code with additional instruction - "Complete this code"
    """

    return code + "your wrapping instructions here"


if __name__ == "__main__":
    client: OpenAI = OpenAI()

    completion: openai.ChatCompletion = (
        client.chat.completions.create())

    for i in range(2):
        output = completion.choices[i].message.content
        print(f"Output {i + 1}:")
        try:
            suggested_code = output.split("```")[1]
            print(suggested_code)
        except IndexError:
            print(output)
