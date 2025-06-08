import openai
from openai import OpenAI


if __name__ == "__main__":
    client: OpenAI = OpenAI()

    completion: openai.ChatCompletion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "What is the FizzBuzz problem?"}]
    )

    print(completion.choices[0].message.content)
