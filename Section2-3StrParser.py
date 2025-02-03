from langchain_ollama import ChatOllama
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

if __name__ == "__main__":
    userInput="Pizza"
    my_prompt_template = PromptTemplate(template="Please create a poem about {userInput}",input_variables=["userInput"])
    # llm = ChatOllama(model="llama3.2")
    llm = ChatOllama(model="mistral")
    chain = my_prompt_template | llm
    #chain = my_prompt_template | llm | StrOutputParser()
    res = chain.invoke(input={"userInput": userInput})

    print(res)
'''
## without StrOutputParser
C:\Users\pathi\.virtualenvs\ice_breaker-8_0o264F\Scripts\python.exe C:\work\udemy-langchain\ice_breaker\Section2-StrOutputParser.py 
    content="In the realm where flavors dance and twirl,\n\nA tale of delight I'm about to unfurl.\n\n..." 
    additional_kwargs={} 
    response_metadata={'model': 'mistral', 'created_at': '2025-01-31T13:10:34.2415204Z', 'done': True, 'done_reason': 'stop', 'total_duration': 43930001400, 'load_duration': 6507000, 'prompt_eval_count': 12, 'prompt_eval_duration': 171000000, 'eval_count': 257, 'eval_duration': 43751000000, 'message': Message(role='assistant', content='', images=None, tool_calls=None)} 
    id='run-1f272a8c-ac39-4ed4-8595-ab4d39752b9e-0' 
    usage_metadata={'input_tokens': 12, 'output_tokens': 257, 'total_tokens': 269}
##StrOutputParser
C:\Users\pathi\.virtualenvs\ice_breaker-8_0o264F\Scripts\python.exe C:\work\udemy-langchain\ice_breaker\Section2-StrOutputParser.py 
    In the realm where flavors intertwine,
    A symphony of tastes, a delight divine,
    :::
'''