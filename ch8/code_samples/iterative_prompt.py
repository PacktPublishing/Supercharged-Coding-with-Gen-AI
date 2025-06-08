import traceback


def get_refined_output(old_user_code, error_details):
    ...


user_code = ...

for i in range(100):
    try:
        exec(user_code)
        print(f"successfully compiled:\n {user_code}")
        break

    except SyntaxError as se:
        user_code = get_refined_output(user_code, traceback.format_exc())
