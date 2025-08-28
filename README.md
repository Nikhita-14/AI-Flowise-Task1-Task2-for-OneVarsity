# AI Flowise Task1 Task2 for OneVarsity Internship

> Official submission for the AI/ML + Flowise Internship at OneVarsity  
> Includes Task 1 (AI Microservices with Flowise + LangChain) and Task 2 (Bonus: Custom Flowise Node Development)

---

## 📋 Contents

- [About](#about)  
- [Task 1: AI Microservices with Flowise + LangChain](#task-1-ai-microservices-with-flowise--langchain)  
- [Task 2: Custom Flowise Node Development (Bonus)](#task-2-custom-flowise-node-development-bonus)  
- [Setup & Installation](#setup--installation)  
- [Usage](#usage)  
- [API Endpoints](#api-endpoints)  
- [Environment Variables](#environment-variables)  
- [Technologies Used](#technologies-used)  
- [Contact](#contact)

---

## About

This repository contains the complete solution for the AI/ML + Flowise Internship assignments at OneVarsity.

- **Task 1:** Modular AI microservices built using Flowise and LangChain for Text Summarization, Q&A over documents, and Dynamic Learning Path suggestions.  
- **Task 2:** Bonus task involving creation of a custom Flowise node for keyword extraction and demonstration of its integration.

---

## Task 1: AI Microservices with Flowise + LangChain

- Developed REST APIs for:
  - **Text Summarization**  
  - **Q&A over Documents**  
  - **Dynamic Learning Path Suggestion**

- Backend built with **FastAPI (Python)**  
- Integrated with a local **LangFlow** server to handle AI workflows  
- Frontend (basic HTML/JS) included for testing and demo  
- Modular design allowing easy extension and reuse  
- Complete API documentation provided below

---

## Task 2: Custom Flowise Node Development (Bonus)

- Created a custom **keyword extraction** node using **TypeScript**  
- Node integrates seamlessly into Flowise visual workflows  
- Outputs comma-separated keywords from text input  
- Includes source code and sample flow export  
- Setup and usage instructions provided  

---

## Setup & Installation

### Prerequisites

- Python 3.8+  
- Node.js (for custom node development)  
- LangFlow server (local instance running)  
- Git  

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Nikhita-14/AI-Flowise-Task1-Task2-for-OneVarsity.git
   cd AI-Flowise-Task1-Task2-for-OneVarsity
  ```
2. Create and activate Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install Python dependencies:

```bash
pip install -r requirements.txt
```

4. Set environment variables (see below).

5. Run the FastAPI backend:
```bash
uvicorn main:app --reload
```
---
## Usage

Open your browser at http://localhost:8000
 to access the frontend demo.
---
Use the API endpoints via Postman or curl as documented below.

# API Endpoints
|    Endpoint   |	Method   |	Description                      |
|---------------|----------|-----------------------------------|
|/summarize     | POST     |    Summarize given text           |
|/qa            |	POST     |	Question answering over documents|
|/learning-path |	POST     |	Suggest dynamic learning path    |

See README.md in the /task1 folder for detailed request/response format.

# Environment Variables

Create a .env file in the project root based on .env.example with the following content:
```env
LANGFLOW_API_KEY=your_langflow_api_key  
LANGFLOW_API_URL=http://localhost:3333/api
```

Make sure your LangFlow server is running and accessible before calling the APIs.

Technologies Used
```bash
Python 3.8+

FastAPI

LangFlow / Flowise

TypeScript (for custom node)

Node.js

HTML / JavaScript (for basic frontend demo)
```
---
## Contact

For questions or feedback, feel free to reach out:

GitHub: https://github.com/Nikhita-14
---
Thank you for reviewing my submission!
---
