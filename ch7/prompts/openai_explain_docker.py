from openai import OpenAI
from openai.types.chat import ChatCompletion

SURROUND = """you are provided with:
1. A Dockerfile enclosed with {{{ DOCKERFILE }}}
2. A line from the file enclosed with {{ LINE }}}."""
SINGLE_TASK = "Your task is to explain the purpose of the line."


def get_user_prompt(path: str, line: str) -> str:
    with open(path, 'r') as file:
        dockerfile_content = file.read()

    return f"""
    DOCKERFILE: {{{{{{ {dockerfile_content} }}}}}}
    
    LINE: {{{{{{ {line} }}}}}}

    EXPLANATION:
    """


if __name__ == "__main__":
    client: OpenAI = OpenAI()

    system_prompt = f"{SURROUND} {SINGLE_TASK}"
    user_prompt = get_user_prompt('../../ch7/Dockerfile', 'EXPOSE 5000')

    completion: ChatCompletion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    print("Explanation:", completion.choices[0].message.content)


