import streamlit as st
from backend import app
from langchain_core.messages import HumanMessage
st.title("Ai Chatbot")
import uuid

#*******************************UTILITIES*********************************************
def generate_thread_id():
    return str(uuid.uuid4())

def new_chat():
    thread_id = generate_thread_id()
    st.session_state["thread_id"] = thread_id
    add_thread(thread_id)
    st.session_state["message_history"] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_thread']:
        st.session_state["chat_thread"].append(thread_id)

def load_chat(thread_id):
    CONFIG = {"configurable":{"thread_id": thread_id}}
    try:
        state = app.get_state(config=CONFIG)
        return state.values.get("message", [])
    except Exception as e:
        return []


        
#********************************Session State *********************************************
if "message_history" not in st.session_state:
    st.session_state.message_history = []
    
if "thread_id" not in st.session_state:
    st.session_state.thread_id = generate_thread_id()

if "chat_thread" not in st.session_state:
    st.session_state.chat_thread = []



add_thread(st.session_state["thread_id"])

#*******************************SLIDE BAR CONFIGURATION********************************

st.sidebar.title("AI Chatbot History")

if st.sidebar.button("New Chat"):
    new_chat()


for thread in st.session_state["chat_thread"][::-1]:
    if st.sidebar.button(thread, key=thread):
        st.session_state["thread_id"] = thread
        
        temp_messages = []
        for msg in load_chat(thread):
            if isinstance(msg, HumanMessage):
                role = "user"
            else:
                role = "assistant"
            temp_messages.append({"role": role, "content": msg.content})
        st.session_state["message_history"] = temp_messages
        


       



#******************************** MAIN CHAT INTERFACE ********************************
for message in st.session_state.message_history:
    with st.chat_message(message["role"]):
        st.text(message["content"])


user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state["message_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)

    
   
    with st.chat_message("assistant"):

        response = st.write_stream(message_chunks.content for message_chunks, metadata in app.stream({"message": [HumanMessage(content=user_input)]}, config={"configurable":{"thread_id": st.session_state["thread_id"]}}, stream_mode="messages")
        )
        st.session_state["message_history"].append({"role": "assistant", "content": response})
#******************************************************************************************





