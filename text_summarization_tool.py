import json
import os
from langchain.tools import tool
from langchain.pydantic_v1 import BaseModel, Field
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv

load_dotenv()

class TranscriptSummarizationInput(BaseModel):
    query: str = Field(description="user query for which we need to fetch relevant information")

def __create_prompt(prompt: str):
    with open("transcript.txt") as f:
        transcript = f.read()

    prompt_template = f"""Extract all information from the transcript of a role playing session that could be relevant to answer the following user query:
    "{prompt}"
    
    Here is the transcript:
    {transcript}
    """

    return prompt_template

@tool("extract_info_from_session_transcript", args_schema=TranscriptSummarizationInput)
def extract_info_from_session_transcript(query):
    """Use this tool to extract information from the transcript of the role playing session that is relevant to the user query.
    Do not make up any information about the campaign, ask this tool instead!"""
  
    llm = AzureChatOpenAI(
        azure_deployment=os.environ.get("AZURE_GP4O_MINI_DEPLOYMENT"),  # or your deployment
        api_version=os.environ.get("AZURE_OPENAI_API_VERSION"),  # or your api version
    )

    summary_prompt = __create_prompt(query)
    resp = llm.invoke([("user", summary_prompt)])
    return resp.content

# resp = extract_info_from_session_transcript("Who is Clarota?")

# print(resp)

# print(extract_info_from_session_transcript.name)
# print(extract_info_from_session_transcript.description)
# print(extract_info_from_session_transcript.args)