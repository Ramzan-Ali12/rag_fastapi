from app.utils.dependencies import get_vector_store
from app.core.config import settings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.output_parsers import StrOutputParser
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

class RAGService:
    def __init__(self):
        self.vector_store = get_vector_store()
        self.llm = ChatOpenAI(openai_api_key=settings.OPENAI_API_KEY, temperature=0)
    
    def query_data(self, query: str) -> str:
        retriever = self.vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})
        template = """
        Context: {context}
        Question: {question}
        Answer:
        """
        
        custom_rag_prompt = PromptTemplate(
            input_variables=["context", "question"],
            template=template,
        )

        retriever = {
            "context": (lambda docs: "\n\n".join([d.page_content for d in docs])),
            "question": query,
        }
        
        rag_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
            prompt_template=custom_rag_prompt,
            output_parser=StrOutputParser(),
        )
        
        return rag_chain.run({"question": query})
