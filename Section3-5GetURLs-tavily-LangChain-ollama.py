from dotenv import load_dotenv
from tavily import TavilyClient
from langchain_community.tools.tavily_search import TavilySearchResults
import json
#from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
#from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (create_react_agent, AgentExecutor)
from langchain import hub
import os

def get_profile_url_tavily_c(name: str):  ## Generates Exception
    TAVILY_API_KEY=os.getenv('TAVILY_API_KEY')
    client = TavilyClient(api_key=TAVILY_API_KEY)
    response = client.search(f"{name}")
    res= response['results']
    with open("temp-TavilyClient.json", "w") as f:
        json.dump(res, f, indent=2)
    return res

def get_profile_url_tavily(name: str):
    """Searches for Linkedin or twitter Profile Page.  The score of a result is not provided by this function"""
    search = TavilySearchResults(include_raw_content=True)
    res = search.run(f"{name}")
    with open("temp-TavilySearchResults.json", "w") as f:
        json.dump(res, f, indent=2)
    return res

def lookup(name:str) -> str:
    llm = ChatOllama(model="llama3.2")  ## did not work
    #llm = ChatOllama(model="mistral") ## did not work
    template = """given the full name {name_of_person} I want you to get the link to their Linkedin profile page.
                          Your answer should contain only a URL"""

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google for linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need get the Linkedin Page URL",
        )
    ]
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )
    linked_profile_url = result["output"]
    print("result:",result)
    print("result[output]:",result["output"])
    print("linked_profile_url:",linked_profile_url)
    return linked_profile_url

    print(res)


if __name__ == "__main__":
    load_dotenv()
    lookup("Pathik Paul")