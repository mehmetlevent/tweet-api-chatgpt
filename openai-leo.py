import openai
import os
import random
import configparser

config = configparser.ConfigParser()
config.read("config.ini")


openai.api_key = config.get("OpenAI", "ApiKey")

promts = [
    "crypto para güvenlik açıkları ile ilgili twitterda kullanılabilecek formatta bir alıntı üret."
]

prompt = random.choice(promts)

model = "text-davinci-002"
temperature = 0.5

max_tokens = 50
response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
    n=1,
    stop = None
)
quote = response.choices[0].text
print(quote)