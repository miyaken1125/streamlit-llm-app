from dotenv import load_dotenv

load_dotenv()
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def run_expert_llm(input_text: str, selected_value: str) -> str:
    """
    入力テキストとラジオボタンの選択値（A or B）を受け取り、
    LLM に渡すシステムプロンプトを切り替えて、回答を返す関数。
    """
    
    # 選択値に応じてシステムメッセージを変更
    if selected_value == "A":
        system_prompt = "あなたは健康の専門家です。根拠に基づき、安全な健康アドバイスを提供してください。"
    elif selected_value == "B":
        system_prompt = "あなたは金融の専門家です。リスクに配慮し、安全で実用的な金融アドバイスを提供してください。"
    else:
        system_prompt = "あなたは丁寧なアシスタントです。"

    # LLM 呼び出し
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": input_text}
        ],
        temperature=0.5
    )

    # 回答テキストだけ返す
    return response.choices[0].message.content


# -------------------------
# 使い方（例）
# -------------------------
user_input = "最近太り気味です。どうしたらいいですか？"
radio_value = "A"  # ← ラジオボタンで選択された値が入る想定（A or B）

result = run_expert_llm(user_input, radio_value)
print(result)
