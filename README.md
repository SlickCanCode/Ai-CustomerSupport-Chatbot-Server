# Ai-CustomerSupport Chatbot Server

A Flask-based chatbot server that connects to OpenAI's GPT API using LangChain for intelligent buisness conversational capabilities.

---

## Features

- **Customer Support:** Reduces manual labour and replies to buisness faq's within seconds
- **Intelligent Chat:** Handles context-aware conversations with GPT.
- **LangChain Integration:** Makes managing conversation flows and chains easy.
- **Flask API:** Simple REST endpoints to send and receive chat messages.
- **Extensible:** Easily integrate into your web or mobile applications.

---

## Tech Stack

- Python 3.x
- Flask
- LangChain
- OpenAI GPT API

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```
2. Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Setup Api Key

```bash
OPENAI_API_KEY= your_API_key
```


## Usage

1. Start the Flask server:
   
```bash
python main.py
```

2.Send POST requests to the /chatbot endpoint with JSON:

```bash
{
  "message": "Hello!"
}
```

3. Receive Chatbot Response:

```bash
{
  "response": "Hi there! How can I help you today?"
}
```


## Notes

1. Demo Only: This is a demonstration project. Users will need their own OpenAI API keys to run.
2. There's an additional "Contact Me" endpoint you can use to create a contact me form that sends message to your email.
   You will need the following environmental variables:
   ```bash
   EMAIL_ADDRESS= your_email_address
   EMAIL_PASSWORD= your_password
   SMTP_SERVER = e.g smtp.gmail.com
   SMTP_PORT = e.g g402
   ``` 

