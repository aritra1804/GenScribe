# GenScribe

**GenScribe** is a AI article generator that uses LLaMA 3.2 to produce polished, Medium-style articles in seconds. Choose a category, subtopic, tone, and target length—enter your idea, hit “Generate,” and download your finished draft as a TXT file or save it locally.



## 🚀 Features

- **One-click article generation** using a local Ollama server running LLaMA 3.2  
- **Customizable** category (Tech, Health, Finance, Lifestyle, Education) and subtopic  
- **Tone selection**: Formal, Casual, Informative, Persuasive  
- **Length presets**: Short (~300 words), Medium (~600 words), Long (~1000+ words)  
- **Session history**: Review and re-run past prompts  
- **Download** your article as a `.txt` or save it into `articles/`  



## 🔧 Prerequisites

- **Python 3.7+**  
- Access to `llama3.2` model 



## ⚙️ Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/aritra1804/GenScribe.git
   cd GenScribe
2. **Create & activate a virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```
4. Install Python dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```


## 🏃 Usage
1. Start the app

```bash
streamlit run app.py
```
2. Open your browser
Navigate to http://localhost:8501

3. Generate

- Select Category → Subtopic

- Choose Tone and Length

- Enter your Article prompt or idea

- Click Generate Article

4. Review & Download

- View your draft in the app

- Click Download as TXT to get a .txt file

- Or click Save to Local File to save under articles/
---
