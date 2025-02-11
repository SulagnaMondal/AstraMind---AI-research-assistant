from langchain.vectorstores import AstraDB
from langchain.embeddings import HuggingFaceEmbeddings

def get_vector_store():
    embeddings = HuggingFaceEmbeddings(model_name="all-mpnet-base-v2")
    
    return AstraDB(
        embedding=embeddings,
        collection_name="research_papers",
        api_endpoint="",
        token=""
    )