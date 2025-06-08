from openai import OpenAI
from openai.types import FileObject
from openai.types.fine_tuning import FineTuningJob

model = "gpt-4o-mini-2024-07-18"

if __name__ == '__main__':
    client: OpenAI = OpenAI()

    upload_request: FileObject = client.files.create(
        file=open("fine_tuning.jsonl", "rb"),
        purpose="fine-tune"
    )

    file_id = upload_request.id



    job: FineTuningJob = client.fine_tuning.jobs.create(
        training_file=file_id,
        model=model,
        extra_body={"method": {"type": "dpo"}}

    )

    job_id = 'ftjob-9Hkt5dKWhZ828tW4bACWakLF'
    org_id = 'org-QPkfX4AuoZuy0swSm3205CbD'
    model_job = 'gpt-4o-2024-08-06'
    # client.fine_tuning.jobs.list(limit=10)

    completion = client.chat.completions.create(
        model='ft:gpt-4o-2024-08-06:pazpaz-the-coder::AsQxSdQL',
        messages=[
            {"role": "user", "content": "Write a Python function that finds the maximum value in a list."},
        ]
    )
