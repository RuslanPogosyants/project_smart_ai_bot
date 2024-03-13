from dependencies import gigachat_token
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

chat = GigaChat(credentials=gigachat_token, verify_ssl_certs=False)


def request_answer(promt: str) -> str:
    role = [SystemMessage(content='Ты ассистент-помощник')]
    messages = role
    messages.append(HumanMessage(content=promt))
    result = chat(messages)
    messages.append(result)
    return result.content



