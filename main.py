from openai import OpenAI

client = OpenAI(api_key="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")

   # paste your key heresk-proj-MqeQszMCG-HfomcCNvRLT5_O6V-cJsbltA5bJSqkY8O7GBGU_wIdQZXdmMxjd7A-vH6PQo-BnIT3BlbkFJOGNQJ5YYzZgWwxC7Bepw_qOkOZj1fNNZXpQAIWathWxAIL-WeOOBHc6VST90L6qQNzJwzMwJQA

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Explain AI to a 10-year-old with emojis"}]
)

print(response.choices[0].message.content)
