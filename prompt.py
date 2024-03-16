import json
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_TOKEN"))


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model, messages=messages, temperature=0
    )
    return response.choices[0].message.content


def get_values_from_input(text):
    prompt = f"""
	Your task is to extrct amount, source currency and destination currency from the text delimited with triple backticks in a json object format as specified in the below example.
	If you are not able to extract any of these values then return 'Invalid query' error in the 
	json object format as specified in the example below.
	
	Few examples:
	If input text is "3000 inr to usd", 
	then output response should be {{"amount": 3000, "source_currency": "inr", "destination_currency": "usd"}}
	
	If input text is "3000 inr to",
	then output response should be {{"error": "Invalid query"}}
	```{text}```
	"""
    response = get_completion(prompt)
    return json.loads(response)
