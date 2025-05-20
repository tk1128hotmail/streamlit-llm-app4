from dotenv import load_dotenv

load_dotenv()


from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

# 専門家の種類とシステムメッセージ
expert_dict = {
    "医療専門家": "You are a medical expert. Please answer in an easy-to-understand and professional manner.",
    "ITコンサルタント": "You are an experienced IT consultant. Please answer from a technical perspective in a clear way.",
    "法律アドバイザー": "You are a reliable legal advisor. Please answer carefully from a legal perspective."
}

def ask_llm(user_input: str, expert_type: str) -> str:
    """入力テキストと専門家タイプを受け取り、LLMからの回答を返す関数"""
    system_message = SystemMessage(content=expert_dict[expert_type])
    human_message = HumanMessage(content=user_input)
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    messages = [system_message, human_message]
    result = llm(messages)
    return result.content

# Webアプリの概要・操作説明
st.title("専門家AIチャットアプリ")
st.write(
    """
    このアプリは、選択した専門家になりきったAIがあなたの質問に回答します。  
    1. 下のラジオボタンで専門家の種類を選んでください。  
    2. 質問内容を入力し、「送信」ボタンを押してください。  
    3. AIが専門家として回答します。

    ---
    **使い方の例：**
    - 医療専門家を選び「健康診断で気をつけることは？」と入力
    - ITコンサルタントを選び「おすすめのクラウドサービスは？」と入力
    - 法律アドバイザーを選び「契約書で注意すべき点は？」と入力
    """
)

# 専門家選択
expert_type = st.radio("専門家の種類を選択してください", list(expert_dict.keys()))

# 入力フォーム
user_input = st.text_area("質問内容を入力してください")

if st.button("送信"):
    if user_input.strip():
        with st.spinner("AIが回答中..."):
            answer = ask_llm(user_input, expert_type)
        st.success("AIの回答:")
        st.write(answer)
    else:
        st.warning("質問内容を入力してください。")

