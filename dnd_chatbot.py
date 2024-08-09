import os
from dotenv import load_dotenv

from image_generation_tool import image_generation_tool
from text_summarization_tool import extract_info_from_session_transcript
from langchain_openai import AzureChatOpenAI
from langgraph.prebuilt import create_react_agent
import chainlit as cl


@cl.on_chat_start
async def on_chat_start():
    model = AzureChatOpenAI(
        azure_deployment=os.environ.get("AZURE_GP4O_MINI_DEPLOYMENT"),  # or your deployment
        api_version=os.environ.get("AZURE_OPENAI_API_VERSION"),  # or your api version
    )

    tools = [image_generation_tool, extract_info_from_session_transcript]

    agent_executor = create_react_agent(model, tools)
    cl.user_session.set("chain", agent_executor)

@cl.on_message
async def on_message(message: cl.Message):
    chain = cl.user_session.get("chain")  # type: LLMChain

    resp = chain.invoke({"messages": [{"role": "user", "content": message.content}]})
   
    # print(resp)
   
    await cl.Message(content=resp["messages"][-1].content).send()