# Import necessary modules
import argparse
from dataclasses import dataclass
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Define the path to the Chroma vector store
CHROMA_PATH = "chroma"

# Define the template for generating prompts for the chat model
PROMPT_TEMPLATE = """
Answer the question based only on the following context:
{context}

---

Answer the question based on the above context: {question}
"""

# Function to query data based on the provided query text
def query_data(query_text):
    # Prepare the vector store
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the vector store for similarity with relevance scores
    results = db.similarity_search_with_relevance_scores(query_text, k=1)
    
    # Check if a relevant result is found
    if len(results) == 0 or results[0][1] < 0.7:
        # Return a message when no matching results are found
        return "Unable to find matching results."

    # Generate context text from the top matching document
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    
    # Create a chat prompt using the defined template
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    # Initialize the ChatOpenAI model for generating responses
    model = ChatOpenAI()
    response_text = model.predict(prompt)

    # Extract sources from the matched document
    sources = [doc.metadata.get("source", None) for doc, _score in results]

    # Format the response with the generated text and sources
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    
    # Return the formatted response
    return formatted_response

# Entry point to execute the script when run directly
if __name__ == "__main__":
    # Create a command-line interface
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    
    # Call the query_data function with the provided query text and print the result
    print(query_data(query_text))
