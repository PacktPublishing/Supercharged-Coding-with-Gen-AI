import inspect

from openai import OpenAI
from openai.types.chat import ChatCompletion


SURROUND = ("You will be provided with a Python function enclosed with {{{ CODE }}} and a desired code change enclosed "
            "with {{{ CHANGE }}}.")
SINGLE_TASK = "Your task is to return a new Python function with the required change."


def get_user_prompt(func: callable, change: str) -> str:
    return f"""
    CHANGE: {{{{{{ {change} }}}}}}
    
    CODE: {{{{{{ {inspect.getsource(func)} }}}}}}
    
    REFACTORED CODE:
    """


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

    changes = [
        "Replace dictionary key-value assignments with calls to dict.get()",
        "Convert hard-coded integers to global constants",
        "Replace dictionary key-value assignments with calls to dict.get() and convert hard-coded integers to global constants",
    ]

    for c in changes:
        user_prompt = get_user_prompt(get_estimated_user_costs, c)

        completion: ChatCompletion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"{SURROUND} {SINGLE_TASK}"},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.2,
        )

        print(f"Change: {c}")
        print(completion.choices[0].message.content)
