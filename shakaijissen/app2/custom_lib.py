import pandas as pd
import json
import openai

# OpenAI APIキーの設定
openai.api_key = "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" # 安全な方法でキーを管理してください

def generate_advice(expenses_summary):
    """
    収支データを元に節約アドバイスを生成するAI機能
    """
    prompt = f"Based on the following expense summary, provide advice on how to save money: {expenses_summary}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # 使用するモデル（davinciが最も強力）
        prompt=prompt,
        max_tokens=150,  # 生成するテキストの長さ
        temperature=0.7  # 創造的な回答を得るためのパラメータ
    )
    
    return response.choices[0].text.strip()

def load_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def load_budget(budget_path):
    return pd.read_csv(budget_path)

def save_budget(budget_path, data):
    data.to_csv(budget_path, index=False)

def add_transaction(budget_data, date, category, amount):
    new_entry = {"date": date, "category": category, "amount": amount}
    return budget_data.append(new_entry, ignore_index=True)

