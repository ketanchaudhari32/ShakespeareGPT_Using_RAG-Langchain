# Import necessary modules
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
import os
import shutil

# Define paths for Chroma database and data directory
CHROMA_PATH = "chroma"
DATA_PATH = "data"

# Main function to generate the data store
def main():
    generate_data_store()

# Function to generate the data store by loading, splitting, and saving to Chroma
def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)

# Function to load documents from the specified data directory
def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents

# Function to split the text of documents into chunks using RecursiveCharacterTextSplitter
def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    
    # Print information about the splitting process
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")
    
    # Print content and metadata of a specific chunk for verification
    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

    return chunks

# Function to save the chunks to Chroma vector store
def save_to_chroma(chunks: list[Document]):
    # Clear out the existing database directory if it exists
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # Create a new Chroma vector store from the chunks using OpenAIEmbeddings
    db = Chroma.from_documents(
        chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH
    )
    
    # Persist the vector store to disk
    db.persist()
    
    # Print information about the saving process
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

# Entry point to execute the main function when the script is run
if __name__ == "__main__":
    main()
