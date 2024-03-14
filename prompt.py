from openai import OpenAI

client = OpenAI("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")

def get_completion(prompt, model="gpt-4"):
	messages=[{"role": "user", "content": prompt}]
	response = client.chat.completions.create(
	  model=model,
		messages=messages,
		temperature=0
	)
	return response.choices[0].message["content"]

def get_values_from_input(text):
	prompt = f"""
	Get the values of source and destination from the text delimited with triple backticks.
	```{text}```
	"""
	response = get_completion(prompt)
	return response