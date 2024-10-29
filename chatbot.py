import os
from langchain.agents import initialize_agent, AgentType
from langchain_community.llms import OpenAI
from langchain.tools import Tool
from langchain_community.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS  # Use FAISS instead of SimpleVectorStore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
# from decouple import config


# Set up OpenAI API key
# os.environ["OPENAI_API_KEY"] = "key"

# Initialize LLM
llm = OpenAI(api_key= "KEY")

# Load PDF and Split into Chunks for Retrieval
def load_pdf_as_knowledge_base(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    split_docs = text_splitter.split_documents(documents)
    return split_docs

# Store Chunks in Vector Store for RAG
def create_vector_store(documents):
    embeddings = OpenAIEmbeddings(api_key= "key")
    vector_store = FAISS.from_documents(documents, embedding=embeddings)  # Use FAISS here
    return vector_store

# Function for Retrieval (RAG)
def retrieve_from_pdf(query, vector_store):
    results = vector_store.similarity_search(query, k=3)  # Retrieve top 3 similar chunks
    return " ".join([result.page_content for result in results])

# Load the knowledge base and initialize vector store
pdf_path = "rag_langchain.pdf"
documents = load_pdf_as_knowledge_base(pdf_path)
vector_store = create_vector_store(documents)

# Define a tool for RAG Retrieval
rag_tool = Tool(
    name="RetrievePDFInfo",
    func=lambda query: retrieve_from_pdf(query, vector_store),
    description="Retrieves information from a PDF knowledge base."
)

# Define a tool for Appointment Booking
def book_appointment(user_query):
    # Extract information for appointment (mockup logic here)
    user_info = {
        "name": "Extracted Name",
        "email": "user@example.com",
        "time": "2024-10-31 10:00 AM"
    }
    return f"Booking appointment for {user_info['name']} at {user_info['time']}."

appointment_tool = Tool(
    name="BookAppointment",
    func=book_appointment,
    description="Books an appointment by extracting details like name, email, and time."
)

# Initialize Agent with Tools
agent = initialize_agent(
    tools=[rag_tool, appointment_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True
)

#Query
user_query = "I'd like to know how do i book an appointment."

response = agent.run(user_query)
print(response)
