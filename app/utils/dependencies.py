from core.config import settings
from langchain_openai import OpenAIEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch

def get_vector_store():
    """
    Returns a MongoDBAtlasVectorSearch object that uses the
    OpenAI embeddings.

    The object is created from a connection string, a database name,
    a collection name, and the name of the index.

    Note that the "disallowed_special" argument is set to an empty tuple
    to exclude any special characters from the embeddings.

    The function returns the vector store object.
    """
    return MongoDBAtlasVectorSearch.from_connection_string(
        settings.MONGODB_URI,
        "langchain_demo.chunked_data",
        OpenAIEmbeddings(disallowed_special=(), openai_api_key=settings.OPENAI_API_KEY),
        index_name="vector_index",
    )
