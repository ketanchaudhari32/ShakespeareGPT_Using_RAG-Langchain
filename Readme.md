# ShakespeareGPT Using RAG Langchain

## Dataset-used  
Project Gutenberg complete set of William Shakespeare

## Summary
The Shakespeare Bot project is a combination of a Flask-based backend and a front-end interface for interacting with a chatbot trained on Shakespearean texts. The backend utilizes OpenAI models, Chroma vector stores, and Flask for handling API requests. The front end, located in the `shakespeare_bot` folder, is a Flask application providing a user interface.

### Key Features
- **RAG Integration:** The chatbot incorporates the innovative Retrieval-Augmented Generation (RAG) approach, combining generative capabilities with the ability to retrieve information from a knowledge base.
  
- **Langchain Approach:** The Langchain approach is employed for effective text processing and understanding. It utilizes advanced techniques for document loading, text splitting, and vectorization, contributing to the chatbot's overall intelligence.

- **Chroma Vector Stores:** The backend utilizes Chroma vector stores for storing and retrieving document embeddings. This enhances the efficiency of similarity searches and ensures relevant information is readily available during user queries.

- **Flask-based Backend:** The backend is implemented using Flask, a powerful web framework, to handle API requests efficiently. The backend facilitates communication between the front end, the RAG model, and the Chroma vector stores.

- **User-Friendly Front End:** The front-end interface, located in the `shakespeare_bot` folder, is designed using Flask, providing users with an intuitive platform to interact with the chatbot. Users can easily input queries and receive responses based on the rich context of Shakespearean texts.


## Dataset-used  
Project Gutenberg complete set of William Shakespeare

## Folder Structure

Certainly! I've added information about installing React libraries from package.json and steps to run both the front end and back end in the README:

markdown
Copy code
# Shakespeare Bot Project

## Summary
The Shakespeare Bot project is a combination of a Flask-based backend and a front-end interface for interacting with a chatbot trained on Shakespearean texts. The backend utilizes OpenAI models, Chroma vector stores, and Flask for handling API requests. The front end, located in the `shakespeare_bot` folder, is a Flask application providing a user interface.

## Folder Structure
* back_end/    
    * create_database.py
    * query_data.py
    * base.py
* requirements.txt
* shakespeare_bot/ React front end source files

## Setup Environment

1. **Create Virtual Environment**:
   ```bash
   python -m venv venv
   ```
2. **Activate Virtual Environment**:
* On Windows:
   ```bash
    .\venv\Scripts\activate
    ```
* On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

3. **Install required Python libraries**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Initialize Database**:
* Navigate to the back_end folder:
    ```bash
    cd back_end/
    python create_database.py
    ```  

6. **Install Frontend Libraries**:
* Navigate to the ./shakespeare_bot folder:
    ```bash
    cd ./shakespeare_bot
    ```  
* Install required React libraries:
    ```bash
    npm install
    ```

## Run the Project
* Start Backend Server:
    ```bash
    flask run
    ``` 

* Start Frontend Server:

    * Navigate to the ./shakespeare_bot folder:
    * Run the React app:
    ```bash
    npm start
    ```

* Access the Application:

* Open a web browser and go to http://localhost:3000
* Interact with the Chatbot: Use the provided interface to enter queries and receive responses from the Shakespeare Bot.

## Important Note
Make sure to run ```create_database.py``` in the base folder to initialize the database before starting the project. This script is crucial for creating the necessary data store for the chatbot to function properly.

## Acknowledgment
This project is inspired by a tutorial from [pixegami/langchain-rag-tutorial](https://github.com/pixegami/langchain-rag-tutorial).