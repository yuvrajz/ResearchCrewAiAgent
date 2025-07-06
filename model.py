from langchain_community.llms import HuggingFaceHub

def load_mistral():
    return HuggingFaceHub(
        repo_id="mistralai/Mistral-7B-Instruct",
        model_kwargs={"temperature": 0.7, "max_new_tokens": 512}
    )
