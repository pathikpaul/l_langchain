from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
#from langchain_ollama import ChatOllama
from langchain.prompts.prompt import PromptTemplate

if __name__ == "__main__":
    load_dotenv()
    userInput="Pizza"
    my_prompt_template = PromptTemplate(template="Please create a poem about {userInput}",input_variables=["userInput"])
    # llm = ChatOllama(model="llama3.2")
    #llm = ChatOllama(model="mistral")
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    chain = my_prompt_template | llm
    res = chain.invoke(input={"userInput": userInput})

    print(res)
