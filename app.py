import streamlit as st
import ollama
from utils import categories, build_prompt, save_markdown
from datetime import datetime

# Page config
st.set_page_config(page_title="GenScribe", layout="centered")
st.title("📝 GenScribe: AI Article Generator")
st.write("Generate a Medium-quality article with LLaMA 3.2 (via Ollama).")

# --- User Inputs ---
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

# --- Generate Article ---
if st.button("Generate Article"):
    if not user_prompt.strip():
        st.warning("Please enter a prompt or idea.")
    else:
        # Map length label to target word count
        target_words = {
            "Short": 300,
            "Medium": 600,
            "Long": 1000
        }[length_choice.split()[0]]

        # Build and send prompt to LLaMA 3.2
        prompt = build_prompt(category, subtopic, user_prompt, tone, target_words)
        with st.spinner("Generating article..."):
            try:
                resp = ollama.chat(
                    model="llama3.2",
                    messages=[{"role": "user", "content": prompt}]
                )
                st.session_state.article_text = resp["message"]["content"]
            except Exception as e:
                st.error(f"Generation error: {e}")

# --- Display & Export ---
if "article_text" in st.session_state:
    article = st.session_state.article_text

    st.subheader("📰 Generated Article")
    st.write(article)

    # Download as Markdown
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = f"article_{ts}.md"
    st.download_button(
        label="Download as Markdown",
        data=article,
        file_name=fname,
        mime="text/markdown"
    )

    # Save to local file system
    if st.button("Save to Local File"):
        path = save_markdown(article)
        st.success(f"Article saved to `{path}`")
