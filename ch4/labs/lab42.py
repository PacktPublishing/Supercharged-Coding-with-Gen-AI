import inspect

from openai import OpenAI
from openai.types.chat import ChatCompletion

SURROUND = "Your context here"
SINGLE_TASK = "Your task here"


def get_user_prompt(func: callable, change: str) -> str:
    ...


def get_estimated_user_costs(prompts_data):
    costs = {}

    for entry in prompts_data:
        user = entry["user"]
        prompt = entry["prompt"]
        estimated_tokens = len(prompt) / 4  # 4 is the average number of tokens per character
        cost = estimated_tokens * 0.0001  # 0.0001 is the cost per token

        if user not in costs:
            costs[user] = cost
        else:
            costs[user] += cost

    return costs


if __name__ == "__main__":
    client: OpenAI = OpenAI()

    changes = ["your requested changes here"]

    for c in changes:
        user_prompt = get_user_prompt(get_estimated_user_costs, c)

        completion: ChatCompletion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=["Your messages here"],
            temperature=0.2,
        )

        print(f"Change: {c}")
        print(completion.choices[0].message.content)
