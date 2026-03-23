from langchain_aws import ChatBedrockConverse
from langchain_core.messages import HumanMessage, AIMessage

def demo_chatbot():
    return ChatBedrockConverse(
        credentials_profile_name='default',
        region_name="us-east-1",
        model="us.amazon.nova-pro-v1:0",
        temperature=0.1,
        max_tokens=1000
    )

# Global chat history
chat_history = []

def demo_memory():
    return chat_history  # only returns the list

def demo_conversation(input_text, memory):
    llm = demo_chatbot()

    # Build messages from history + new input
    messages = memory + [HumanMessage(content=input_text)]

    # Call the model
    response = llm.invoke(messages)

    # Save exchange to history
    memory.append(HumanMessage(content=input_text))
    memory.append(AIMessage(content=response.content))

    return response.content