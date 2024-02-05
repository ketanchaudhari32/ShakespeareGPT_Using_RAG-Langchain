# Import necessary modules from Flask and other dependencies
from flask import Flask, request, jsonify
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from query_data import query_data

# Initialize Flask application
app = Flask(__name__)

# Path to the Chroma directory where embeddings are stored
CHROMA_PATH = "chroma"

# Template for generating prompts for the chat model
PROMPT_TEMPLATE = """
Answer the question based only on the following context:
{context}

---

Answer the question based on the above context: {question}
"""

# Define a route for handling chat API requests
@app.route("/api/chat", methods=["POST"])
def chat():
    # Extract query text from the incoming JSON data
    data = request.get_json()
    query_text = data["query_text"]

    # Query external data source for additional information
    query_data(query_text)

    # Initialize embedding function and Chroma vector store
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Perform similarity search on the vector store
    results = db.similarity_search_with_relevance_scores(query_text, k=3)

    # Check if a relevant result is found
    if len(results) == 0 or results[0][1] < 0.7:
        formatted_response = {
            "response": "Unable to find response",
            "sources": ''
        }
    else:
        # Generate context text from the top matching documents
        context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])

        # Create a chat prompt using the defined template
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text, question=query_text)

        # Initialize the ChatOpenAI model for generating responses
        model = ChatOpenAI()
        response_text = model.predict(prompt)

        # Extract sources from the matched documents
        sources = [doc.metadata.get("source", None) for doc, _score in results]

        # Format the response for API output
        formatted_response = {
            "response": response_text,
            "sources": sources
        }

    # Return the formatted response as JSON
    return jsonify(formatted_response)
