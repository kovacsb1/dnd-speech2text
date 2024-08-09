import json
import os
from langchain.tools import tool
from langchain.pydantic_v1 import BaseModel, Field
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

def __generate_image(prompt):
    client = AzureOpenAI(
        api_version=os.environ.get("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )

    return client.images.generate(
        model="dalle3",
        prompt=prompt,
        n=1
    )

class ImagegenInput(BaseModel):
    image_description: str = Field(description="describe image to be generated")

@tool("image_generation_tool", args_schema=ImagegenInput)
def image_generation_tool(image_description: str):
    """This tool generates an image based on the passed text. Before using it, you may need to extract information from the transcript"""
    print("Imagen prompt: ", image_description)
    result = __generate_image(image_description)
    return json.loads(result.model_dump_json())['data'][0]['url']  # Assuming the response contains a URL to the generated image

