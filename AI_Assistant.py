import openai

API_KEY = "sk-proj-ak5p4gTS0vD0RMAhbRuzT3BlbkFJflLPZoasxFPCwrGVl2uS"
openai.api_key = API_KEY

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()







