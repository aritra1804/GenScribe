import os
from datetime import datetime

# --- Category definitions ---
categories = {
    "Tech":        ["AI", "Startups", "Acquisitions", "Cybersecurity", "Gadgets"],
    "Health":      ["Nutrition", "Mental Health", "Fitness", "Medical Research"],
    "Finance":     ["Personal Finance", "Stock Market", "Cryptocurrency", "Fintech"],
    "Lifestyle":   ["Travel", "Food & Dining", "Home Improvement", "Hobbies"],
    "Education":   ["EdTech", "Online Learning", "Higher Education", "Study Tips"]
}

def build_prompt(category: str, subtopic: str, user_prompt: str, tone: str, target_words: int) -> str:
    """
    Construct an instruction prompt for LLaMA 3.2 based on user inputs.
    """
    return (
        f"Write a {tone.lower()} article in the {category} category "
        f"(subtopic: {subtopic}) about {user_prompt}. "
        f"The article should be around {target_words} words, with a clear introduction "
        "and conclusion. Ensure the writing is well-structured and polished, suitable "
        "for publishing on Medium."
    )

def save_markdown(content: str, directory: str = "articles", prefix: str = "article") -> str:
    """
    Save content to a Markdown file under `directory/`, returning the file path.
    """
    os.makedirs(directory, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prefix}_{ts}.md"
    filepath = os.path.join(directory, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath
