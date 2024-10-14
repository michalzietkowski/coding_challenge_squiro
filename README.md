# PiiDetector
PiiDetector is a project designed to mask and unmask data being transmitted to Large Language Models (LLM).
## Requirements
Before starting, ensure you have the following software installed:
- Python 3.11 or newer
- [Poetry](https://python-poetry.org/) for dependency management
## Installation and Running
To run the PiiDetector project, follow these steps:
1. **Install project dependencies with Poetry:**
 
```bash
   poetry install
```
   
2. **Install the NLP model for spaCy:**
 
```bash
   python -m spacy download en_core_web_sm
```
   
3. **Set up the API key for OpenAI communication:**
  Set the OPENAI_API_KEY environment variable to your API key to communicate with the OpenAI API. You can do this by running:
 
```bash
   export OPENAI_API_KEY=<your api key>
```
  Make sure to replace <your api key> with your actual API key.
4. **Run the application:**
  To start the project, execute:
 
```bash
   python app.py
```
   
## How It Works
1. **Masking:** As you input text, PiiDetector identifies potential personal data and replaces it with appropriate masks. This allows the text to be sent to LLMs without exposing sensitive information.
2. **Unmasking:** After receiving a response from LLM, the masked data can be restored to their original form based on the replacement map.