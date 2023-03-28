import openai
import streamlit as st
import os

# OpenAI APIキーの設定
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("No OpenAI API Key found in environment variables.")
openai.api_key = OPENAI_API_KEY

# Streamlitアプリ
st.title("ChatGPTを使ったチャットアプリ")

def main():
    system_text = st.text_area("AIアシスタントの設定", value="あなたはアシスタントAIです。")
    user_text = st.text_area("質問文", value="うどんの茹で方教えて",)
    is_generate_clicked = st.button("文章生成")

    if is_generate_clicked and user_text:
        message = [{"role": "system", "content": system_text}, {"role": "user", "content": user_text}]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=message,
            max_tokens=2000,
            temperature=0,
            stream=True
        )

        partial_words = "" 
        answer = st.empty()

        for chunk in response:
            if chunk and "delta" in chunk["choices"][0] and "content" in chunk["choices"][0]["delta"]:
                partial_words += chunk["choices"][0]["delta"]["content"]
                answer.write(partial_words)

if __name__ == "__main__":
    main()
