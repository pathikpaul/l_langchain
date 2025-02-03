from dotenv import load_dotenv
import os
import requests
import json
from langchain_ollama import ChatOllama
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    if mock:
        '''
        response = requests.get(
            'https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/78233eb934aa9850b689471a604465b188e761a0/eden-marco.json', timeout=10)
        #print(type(response), "response:", response)
        #print(type(response.status_code), "response.status_code:", response.status_code)
        #print(type(response.json()), "response.json():", response.json())
        data = response.json()
        '''
        with open('pathik.linkedin.json', 'r') as file:
            content = file.read()
        data = json.loads(content)
        #print(type(data), "data:", data)
    else:
        ## Needs PROXYCURL_API_KEY
        headers = {'Authorization': 'Bearer ' + os.environ.get('PROXYCURL_API_KEY')}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        params = {'linkedin_profile_url': linkedin_profile_url}
        response = requests.get(api_endpoint, params=params, headers=headers, timeout=10)
        data = response.json()
        #print(type(data), "data:", data)
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications","profile_pic_url"]
    }
    return data


if __name__ == "__main__":
    load_dotenv()
    information = scrape_linkedin_profile(linkedin_profile_url='https://www.linkedin.com/in/pathikpaul/',mock=True)
    print("information:",information)
    #information = scrape_linkedin_profile(linkedin_profile_url='https://www.linkedin.com/in/pathikpaul/',mock=False)
    my_query = """
    given the information {detailed_info_of_person} about a person I want you to summarize and provide:
    1. A short summary
    2. two interesting facts about them
    """
    my_prompt_template = PromptTemplate(template=my_query,input_variables=["detailed_info_of_person"])
    #llm = ChatOllama(model="llama3.2")
    llm = ChatOllama(model="mistral")
    #chain = my_prompt_template | llm
    chain = my_prompt_template | llm | StrOutputParser()
    res = chain.invoke(input={"detailed_info_of_person": information})

    print(res)
