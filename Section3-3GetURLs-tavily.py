#Ref https://docs.tavily.com/docs/python-sdk/tavily-search/api-reference
# Needs  TAVILY_API_KEY
# pipenv install tavily-python  ## Your dependencies could not be resolved. You likely have a mismatch in your sub-dependencies

from dotenv import load_dotenv
from tavily import TavilyClient
import json
import os
load_dotenv()
TAVILY_API_KEY=os.getenv('TAVILY_API_KEY')
client = TavilyClient(api_key=TAVILY_API_KEY)
response = client.search("Pathik Paul")
print(type(response),"response:",response)
with open("pathik-tavily-response.json", "w") as f:
    json.dump(response, f, indent=2)
