from langchain_ollama import ChatOllama
from langchain.prompts.prompt import PromptTemplate

if __name__ == "__main__":
    userInput="Pizza"
    my_prompt_template = PromptTemplate(template="Please create a poem about {userInput}",input_variables=["userInput"])
    # llm = ChatOllama(model="llama3.2")
    llm = ChatOllama(model="mistral")
    chain = my_prompt_template | llm
    res = chain.invoke(input={"userInput": userInput})

    print(res)
