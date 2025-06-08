from openai import OpenAI
from openai.types.chat import ChatCompletion


SURROUND = "You will be given a code snippet enclosed with {{{ CODE }}}."
SINGLE_TASK = "Your task is to identify the programming language of the provided code snippet."


def get_user_prompt(code_source: str) -> str:
    return f"""
    CODE: {{{{{{ {code_source} }}}}}}
    
    PROGRAMMING LANGUAGE:
    """


def get_programming_language(openai_client: OpenAI, code_text: str) -> str:
    system_prompt = f"{SURROUND} {SINGLE_TASK}"
    user_prompt = get_user_prompt(code_text)
    completion: ChatCompletion = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return completion.choices[0].message.content



if __name__ == "__main__":
    sources = {
        "COBOL": """
         PERFORM VARYING WS-NUMBER FROM 1 BY 1 UNTIL WS-NUMBER > 100
             MOVE SPACES TO WS-OUTPUT
    """,
        "Python": """
    def fizz_buzz(n):
        for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
        """,
        "Java": """
    public class FizzBuzz {
        public static void main(String[] args) {
            for (int i = 1; i <= 100; i++) {
    """,
    }

    client: OpenAI = OpenAI()

    for lang, source in sources.items():
        print(f"Actual Language: {lang}")
        print("identified Language:", get_programming_language(client, source))
