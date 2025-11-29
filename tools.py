from langchain.tools import Tool
from faq_data import get_faq
import difflib
import string

def search_faq_tool(query:str):
    
    faq = get_faq()
    q = query.lower().translate(str.maketrans("", "", string.punctuation))

    questions = list(faq.keys())
    normalized = [
        s.lower().translate(str.maketrans("", "", string.punctuation))
        for s in questions
    ]

    match = difflib.get_close_matches(q, normalized, n=1, cutoff=0.4)

    if match:
        idx = normalized.index(match[0])
        matched_question = questions[idx]
        return faq[matched_question]
    return None

faq_tool = Tool(
    name="FAQ_Search",
    func=search_faq_tool,
    description="Use this tool to answer questions based on the buisness FAQ"
)