from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from tools import faq_tool

load_dotenv()

class ChatbotResponse(BaseModel):
    response: str
    tools_used: list[str]

    def to_dict(self):
        return {
            "response": self.response,
            "tools_used": self.tools_used
        }

llm = ChatOpenAI(model="gpt-4o-mini")

parser = PydanticOutputParser(pydantic_object=ChatbotResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system", 
            """
            You are my helpful assistant in my portfolio website that will answer questions about me and my services. 
            Answer the user query in a natural, human-like friendly way, no complicated english, just make it clear and understandable and use necessary tools.
            If the question is unrelated, politely guide the user back to relevant topics.
            Wrap the output in this format and provide no other text\n{format_instructions}
            """
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}")
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [faq_tool]


memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

def invoke_agent(query: str):

    memory = ConversationBufferMemory(
        memory_key="chat_history", 
        return_messages=True
    )

    agent = create_tool_calling_agent(
        llm=llm,
        prompt=prompt,
        tools=tools
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True
    )

    raw_response = agent_executor.invoke({"query": query}) 

    try:
        structured_response = parser.parse(raw_response.get("output"))
        return structured_response.to_dict()
    except Exception as e:
        return {
            "error": str(e),
            "raw_response": raw_response
        }





