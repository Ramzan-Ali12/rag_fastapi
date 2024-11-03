# app/services/rag_services.py

from app.utils.dependencies import get_vector_store
from app.core.config import settings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.output_parsers import PydanticOutputParser
from app.schemas.rag import RAGQueryRequest, RAGResponse
from langchain_openai import ChatOpenAI
from typing import Any

class RAGService:
    def __init__(self):
        self.vector_store = get_vector_store()
        self.llm = ChatOpenAI(openai_api_key=settings.OPENAI_API_KEY, temperature=0)


    def query_data(self, request: RAGQueryRequest) -> RAGResponse:
        # Set up the retriever
        retriever = self.vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})
        print("reteriver running")
        # Define the custom prompt template
        template = """
        Context: {context}
        Question: {question}
        Answer:
        """
        
        custom_rag_prompt = PromptTemplate(
            input_variables=["context", "question"],
            template=template,
        )

        # Create the retrieval chain
        rag_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            prompt_template=custom_rag_prompt,
            output_parser=PydanticOutputParser(RAGResponse),
        )
        print("rag cahin builds")
        # Run the chain with the user's question from the request body
        result= rag_chain.run({"question": request.question})  # Access question from the request body
        print("result------>", result)

        # Inspect result to confirm structure
        if isinstance(result, dict) and "answer" in result:
            return RAGResponse(**result)  # Unpack dictionary to match model fields
        else:
            raise ValueError("Unexpected response format from RAG chain")
