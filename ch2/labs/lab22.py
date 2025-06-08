import openai
from openai import OpenAI

if __name__ == "__main__":
    client: OpenAI = OpenAI()
    completion: openai.ChatCompletion = (
        client.chat.completions.create(
        ))

    print("Completion Tokens: ")
    print("Output: ")
