import streamlit as st
import ollama
from utils import categories, build_prompt, save_text
from datetime import datetime

# ―― Session‐state initialization ――
if "history" not in st.session_state:
    st.session_state.history = []

# ―― Page config & title ――
st.set_page_config(page_title="GenScribe", layout="centered")
st.title("📝 GenScribe: AI Article Generator")
st.write("Generate a polished Medium-style article with LLaMA 3.2 (via Ollama).")

# ―― Display previous sessions ――
if st.session_state.history:
    st.markdown("## 🕘 Previous Sessions")
    # Show newest first
    for i, chat in enumerate(reversed(st.session_state.history), start=1):
        with st.expander(f"Session {i}: \"{chat['user_prompt']}\"", expanded=False):
            st.markdown(f"**Category:** {chat['category']} › {chat['subtopic']}")
            st.markdown(f"**Tone:** {chat['tone']}  |  **Length:** {chat['length_choice']}")
            st.write(chat["response"])

# ―― User inputs ――
category = st.selectbox("Category:", list(categories.keys()))
subtopic = st.selectbox("Subtopic:", categories[category])
user_prompt = st.text_input(
    "Article prompt or idea:",
    placeholder="E.g. The impact of AI on future job markets"
)
tone = st.radio(
    "Tone:",
    ["Formal", "Casual", "Informative", "Persuasive"],
    horizontal=True
)
length_choice = st.selectbox(
    "Length:",
    ["Short (~300 words)", "Medium (~600 words)", "Long (~1000+ words)"]
)

# ―― Generate article ――
if st.button("Generate Article"):
    if not user_prompt.strip():
        st.warning("Please enter a prompt or idea.")
    else:
        # map length label → word count
        size_key = length_choice.split()[0]  # "Short"/"Medium"/"Long"
        target_words = {"Short": 300, "Medium": 600, "Long": 1000}[size_key]

        # build the instruction prompt
        prompt = build_prompt(category, subtopic, user_prompt, tone, target_words)

        with st.spinner("Generating article…"):
            try:
                # call local Ollama server
                resp = ollama.chat(
                    model="llama3.2",
                    messages=[{"role": "user", "content": prompt}]
                )
                article_text = resp["message"]["content"]
                st.session_state.article_text = article_text

                # record to history
                st.session_state.history.append({
                    "category": category,
                    "subtopic": subtopic,
                    "user_prompt": user_prompt,
                    "tone": tone,
                    "length_choice": length_choice,
                    "response": article_text
                })

            except Exception as e:
                st.error(f"Generation error: {e}")

# ―― Display & export the new article ――
if "article_text" in st.session_state:
    article = st.session_state.article_text

    st.markdown("## 📰 Generated Article")
    st.write(article)

    # Download as TXT
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = f"article_{ts}.txt"
    st.download_button(
        label="Download as TXT",
        data=article,
        file_name=fname,
        mime="text/plain"
    )

    # Save locally
    if st.button("Save to Local File"):
        path = save_text(article)
        st.success(f"Article saved to `{path}`")
