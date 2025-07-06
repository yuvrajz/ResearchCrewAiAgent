from langchain_community.llms import HuggingFaceEndpoint
import os

api_key = os.getenv("OPENAI_API_KEY")

def load_mistral():
    return HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct",
        huggingfacehub_api_token=api_key,
        temperature=0.7,
        max_new_tokens=10
    )
