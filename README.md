# 🐨 Bookoala: A Book Recommendation AI

🐨 Bookoala is an LLM-based autonomous agent designed to help users find and select books based on their preferences.

## 📚 Table of Contents
- [Problem Statement](#-problem-statement)
- [Workflow](#-workflow)
- [Technology Stack](#️-technology-stack)
- [Getting Started](#-getting-started)
- [Usage](#️-usage)
- [Project Structure](#️-project-structure)
- [Design Decisions](#-design-decisions)
- [Demo Video](#-demo-video)
- [Future Improvements](#-future-improvements)

## 🎯 Problem Statement

Develop a simple LLM-based autonomous agent for book recommendations with the following workflow:

1. Allow users to find the top books in fiction or any genre.

## 🔄 Workflow

The agent follows these steps:

a. User asks the agent for the top 100 books in any genre.
b. Agent finds the top 10 books in the given genre from the 100 books.
c. Agent helps the user select 1 book from the top ten based on their preferences.
d. Agent concludes the workflow with a thank you message.
e. The agent is exposed via a REST API endpoint using Streamlit for easy testing.

## 🛠️ Technology Stack

- **LLM**: Ollama (llama3:instruct model)
- **Frontend**: Streamlit
- **Backend**: Python
- **Agent Framework**: Custom implementation
- **Dependency Management**: Poetry

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- Ollama installed and running locally
- Poetry for dependency management

### Installation

1. Clone the repository:

```bash
git clone https://github.com/swax10/bookoala.git
```
```bash
cd bookoala
```

2. Install dependencies using Poetry:

```bash
poetry install
```

3. Run the Streamlit app:

```bash
streamlit run main.py
```


## 🖥️ Usage

1. Open your web browser and go to `http://localhost:8501`.
2. You'll see the Bookoala interface with a chat input.
3. Start by asking for book recommendations in any genre.
4. Follow the agent's prompts to narrow down your selection.

## 🏗️ Project Structure

- `main.py`: The main Streamlit application
- `agents/bookoala.py`: The Bookoala agent implementation
- `models/`: Contains the Ollama and OpenAI model implementations
- `tools/`: Contains the tools used by the agent (e.g., book recommendation tool)
- `prompts/`: Contains prompt templates used by the agent
- `pyproject.toml`: Poetry configuration and dependency management

## 🤔 Design Decisions

1. **LLM Choice**: We chose to use Ollama with the llama3:instruct model for its balance of performance and accessibility. It can run locally, which is beneficial for privacy and cost considerations.

2. **Agent Architecture**: We implemented a custom agent architecture that allows for flexible tool use and easy extension. This approach was chosen over existing frameworks to have more control over the agent's behavior and to tailor it specifically to the book recommendation task.

3. **Streamlit Frontend**: Streamlit was selected for its simplicity in creating interactive web applications with Python. It allows for rapid prototyping and easy deployment, making it ideal for this demonstration project.

4. **Tool-based Approach**: The agent uses a tool-based approach, where different functionalities (like book searching) are encapsulated in separate tools. This modular design allows for easy addition of new capabilities in the future.

5. **Poetry for Dependency Management**: We chose Poetry for its robust dependency management and packaging capabilities, ensuring consistency across development environments and simplifying the deployment process.

## 🎥 Demo Video

Check out our demo video showcasing the Bookoala in action:

https://github.com/swax10/anaya/assets/110764543/c36721ad-7e36-4bc4-af19-123b5fda2e0d

## 🔮 Future Improvements

- Integrate with a larger book database for more comprehensive recommendations
- Implement user profiles to remember preferences across sessions
- Add more sophisticated natural language processing for better understanding of user requests
- Expand the agent's capabilities to include book summaries, author information, etc.