# Ref: https://goatreview.com/format-chatgpt-results-with-pydantic-langchain-2/
from langchain_ollama import ChatOllama
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

class CryptoCurrencySummary(BaseModel):
    name: str
    high: float
    low: float

class Summary(BaseModel):
    date: str = Field(description="date of yesterday with the format YYYY-MM-DD")
    crypto_currencies: List[CryptoCurrencySummary] = Field(description="list of 10 best cryptocurrencies summary of yesterday")

parser = PydanticOutputParser(pydantic_object=Summary)

if __name__ == "__main__":
    prompt_template = """
            You're an expert about cryptocurrency.
            Your role is to extract yesterday's high and low about the 10 best cryptocurrencies.
            The date format should be in the format YYYY-MM-DD
            
            {format_instructions}
        """
    my_prompt_template = PromptTemplate(
        template=prompt_template,
        input_variables=[],
        partial_variables={"format_instructions": parser.get_format_instructions()}    )
    # llm = ChatOllama(model="llama3.2")
    llm = ChatOllama(model="mistral")
    chain = my_prompt_template | llm
    #res = chain.invoke(input={"userInput": userInput})
    res = chain.invoke(input={})
    result = parser.parse(res.content)
    print(type(res),"res:",res)
    print(type(result), "result:",result)
'''
<class 'langchain_core.messages.ai.AIMessage'> res: content=' Here is the formatted JSON instance for yesterday\'s high and low of the 10 best cryptocurrencies. Note that I can\'t provide real-time data as I\'m an AI model, but I will create a hypothetical example based on the provided schema:\n\n```json\n{\n  "date": "2023-03-29",\n  "crypto_currencies": [\n    {\n      "name": "Bitcoin",\n      "high": 28567.41,\n      "low": 27783.31\n    },\n    {\n      "name": "Ethereum",\n      "high": 1950.81,\n      "low": 1868.24\n    },\n    {\n      "name": "Binance Coin",\n      "high": 327.52,\n      "low": 311.43\n    },\n    {\n      "name": "Cardano",\n      "high": 0.9862,\n      "low": 0.8748\n    },\n    {\n      "name": "Ripple",\n      "high": 1.08,\n      "low": 1.01\n    },\n    {\n      "name": "Solana",\n      "high": 92.34,\n      "low": 85.76\n    },\n    {\n      "name": "Polkadot",\n      "high": 18.70,\n      "low": 17.13\n    },\n    {\n      "name": "Terra",\n      "high": 79.65,\n      "low": 72.44\n    },\n    {\n      "name": "Avalanche",\n      "high": 60.11,\n      "low": 54.83\n    },\n    {\n      "name": "Uniswap",\n      "high": 9.78,\n      "low": 8.95\n    }\n  ]\n}\n```' additional_kwargs={} response_metadata={'model': 'mistral', 'created_at': '2025-01-31T15:45:08.1564441Z', 'done': True, 'done_reason': 'stop', 'total_duration': 114269357800, 'load_duration': 2284245500, 'prompt_eval_count': 398, 'prompt_eval_duration': 21465000000, 'eval_count': 502, 'eval_duration': 90518000000, 'message': Message(role='assistant', content='', images=None, tool_calls=None)} id='run-fbed063a-948a-45d7-82b4-f295f1db6f6d-0' usage_metadata={'input_tokens': 398, 'output_tokens': 502, 'total_tokens': 900}
<class '__main__.Summary'>                     result: date='2023-03-29' crypto_currencies=[CryptoCurrencySummary(name='Bitcoin', high=28567.41, low=27783.31), CryptoCurrencySummary(name='Ethereum', high=1950.81, low=1868.24), CryptoCurrencySummary(name='Binance Coin', high=327.52, low=311.43), CryptoCurrencySummary(name='Cardano', high=0.9862, low=0.8748), CryptoCurrencySummary(name='Ripple', high=1.08, low=1.01), CryptoCurrencySummary(name='Solana', high=92.34, low=85.76), CryptoCurrencySummary(name='Polkadot', high=18.7, low=17.13), CryptoCurrencySummary(name='Terra', high=79.65, low=72.44), CryptoCurrencySummary(name='Avalanche', high=60.11, low=54.83), CryptoCurrencySummary(name='Uniswap', high=9.78, low=8.95)]
'''