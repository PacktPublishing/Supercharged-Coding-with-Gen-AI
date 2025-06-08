import openai
from openai import OpenAI

if __name__ == "__main__":
    client: OpenAI = OpenAI()
    completion: openai.ChatCompletion = (
        client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0.2,
            max_tokens=100,
            n=1,
            messages=[{"role": "system", "content": "You are a hiring manager at a tech company."},
                      {"role": "user", "content": "What is the Two Sum problem?"}],
        ))

    print("Completion Tokens: ", completion.usage.completion_tokens)
    print("Output: ", completion.choices[0].message.content)
