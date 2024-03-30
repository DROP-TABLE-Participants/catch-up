import openai
import os

from dotenv import load_dotenv

load_dotenv()

openai.api_key = "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"


def name_serializer(name: str) -> str:
    completion = openai.chat.completions.create(
        model="gpt-4-0613",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant skilled in text parsing."
            },
            {
                "role": "user",
                "content": f"Given a user-friendly product name, please provide me with the specific product or category it belongs to. You should include only the exact name of the product. For example, if the product name is 'Apple iPhone 12 Pro Max 256GB', the extracted product would be 'iPhone 12 Pro Max' or if the prompt is 'Gaming Mouse Hama Urage Reaper 500', the extracted product would be 'Hama Urage Reaper 500'. Feel free to include any relevant details or examples to assist in the extraction process. Another example is 'Apple MacBook Air 13' 2020, Space Grey, 13.3', WQXGA, Apple M1 8C (3.2GHz, 16M), 7 ядра GPU Apple M1, 8 GB, 256 GB SSD - MGN63ZE/A'. It should be 'MacBook Air 13' 2020'. \n\nInput: \"{name}\"\nOutput:"
            }
        ]
    )

    return completion.choices[0].message.content
