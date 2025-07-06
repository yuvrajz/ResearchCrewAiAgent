from langchain_community.llms import HuggingFaceHub

def load_mistral():
    return HuggingFaceHub(
        repo_id="google/flan-t5-base",
        model_kwargs={"temperature": 0.7, "max_new_tokens": 512}
    )
