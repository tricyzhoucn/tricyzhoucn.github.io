"""
Tricy 数字分身 - Streamlit 对话界面
基于本地 Markdown 知识库 + NVIDIA NIM 大模型
"""

import streamlit as st
import re
import os
from datetime import datetime

AVATAR_NAME = "Tricy"
KB_DIR = "../../source/about"

# ============== 配置加载 ==============
API_URL = os.getenv("NVDA_API_URL")
API_KEY = os.getenv("NVDA_API_KEY")
MODEL = os.getenv("NVDA_MODEL")


# ============== 知识库加载 ==============
@st.cache_data(ttl=3600)
def load_knowledge_base() -> str:
    """加载知识库所有内容（缓存1小时）"""
    import os

    content_parts = []
    try:
        for filename in os.listdir(KB_DIR):
            if filename.endswith('.md'):
                filepath = os.path.join(KB_DIR, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content_parts.append(f"【{filename}】\n{f.read()}")
    except Exception:
        pass

    return "\n\n---\n\n".join(content_parts) if content_parts else ""

def build_system_prompt() -> str:
    """构建系统提示"""
    kb_content = load_knowledge_base()

    if kb_content:
        kb_section = f"""

【知识库内容】
{kb_content}

当用户问到 Tricy 的技术、项目、经验、笔记等相关内容时，请优先基于上述知识库内容回答。"""
    else:
        kb_section = ""

    return f"""你是 Tricy 的数字分身。Tricy 是一位全栈开发者，技术热情高。

你的职责：
1. 基于知识库内容回答用户问题
2. 如果知识库中没有相关信息，诚实说明并尝试基于你的知识回答
3. 保持友好、专业的语气，像 Tricy 本人在交流
4. 回答要简洁有条理{kb_section}"""


# ============== 大模型对话 ==============
def chat_with_llm(user_input: str):
    """使用 NVIDIA NIM API 调用大模型，流式返回"""
    import requests
    import json

    messages = [{"role": "system", "content": build_system_prompt()}]
    print(messages)
    for msg in st.session_state.messages[-10:]:
        if msg["role"] in ["user", "assistant"]:
            messages.append({"role": msg["role"], "content": msg["content"]})

    messages.append({"role": "user", "content": user_input})

    payload = {
        "model": MODEL,
        "messages": messages,
        "max_tokens": 2048,
        "temperature": 1.0,
        "top_p": 1.0,
        "stream": True,
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "text/event-stream"
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, stream=True, timeout=120)
        response.raise_for_status()

        for line in response.iter_lines():
            if line:
                line = line.decode('utf-8')
                if line.startswith("data: "):
                    data = line[6:]
                    if data == "[DONE]":
                        break
                    try:
                        chunk = json.loads(data)
                        choices = chunk.get("choices")
                        if choices and len(choices) > 0:
                            delta = choices[0].get("delta", {})
                            if delta.get("content"):
                                yield delta["content"]
                    except (json.JSONDecodeError, IndexError, TypeError):
                        continue

    except requests.exceptions.RequestException as e:
        yield f"请求错误: {str(e)}"


# ============== Streamlit UI ==============
def main():
    st.set_page_config(
        page_title=f"{AVATAR_NAME} - 数字分身",
        page_icon="🤖",
        layout="centered"
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "initialized" not in st.session_state:
        st.session_state.messages.append({
            "role": "assistant",
            "content": f"""你好！我是 {AVATAR_NAME} 的数字分身 👋

我可以帮你回答关于 Tricy 的各种问题，基于他的个人知识库和大模型能力。

有什么想问的吗？""",
            "timestamp": datetime.now()
        })
        st.session_state.initialized = True

    st.title(f"🤖 {AVATAR_NAME} 的数字分身")

    # 聊天历史
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            with st.chat_message("user", avatar="👤"):
                st.markdown(msg["content"])
        else:
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(msg["content"])

    # 用户输入
    if prompt := st.chat_input("输入你的问题..."):
        st.session_state.messages.append({
            "role": "user",
            "content": prompt,
            "timestamp": datetime.now()
        })

        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)

        with st.chat_message("assistant", avatar="🤖"):
            response = st.write_stream(chat_with_llm(prompt))

        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "timestamp": datetime.now()
        })


if __name__ == "__main__":
    main()
