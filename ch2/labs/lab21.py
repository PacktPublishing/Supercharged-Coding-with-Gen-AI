import openai
from openai import OpenAI

if __name__ == "__main__":
    client: OpenAI = OpenAI()

    completion: openai.ChatCompletion = (
        client.chat.completions.create(
            model="",  # Your model's name here
            messages=[]  # Your messages here
        ))

    print("your print here")
