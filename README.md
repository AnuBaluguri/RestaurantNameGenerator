# 🍽️ Restaurant Name & Menu Generator

This is a simple Generative AI app built using **LangChain**, **GROQ's LLaMA-3**, and **Streamlit**. It lets users select a cuisine and generates a creative restaurant name along with a menu of 10 items — all powered by LLM prompt chaining.

## 🔍 Overview

- Select a cuisine (Indian, Mexican, Italian, etc.)
- The app uses LangChain's `SequentialChain` to:
  1. Generate a restaurant name
  2. Generate 10 menu items for that restaurant
- Output is displayed in a clean Streamlit UI

## 💡 Features

- Prompt chaining using `LLMChain` and `SequentialChain`
- GROQ-powered LLaMA-3 as the LLM backend
- Lightweight, fast UI with Streamlit
- Prompt templates customized for focused LLM output

## 🛠️ Tech Stack

- Python
- LangChain
- langchain-groq
- Streamlit
- GROQ API + LLaMA 3 (8B)

## 📦 Installation

```bash
git clone https://github.com/your-username/langchain-restaurant-generator.git
cd langchain-restaurant-generator
pip install -r requirements.txt
```

## 🚀 Run the App

```bash
streamlit run main.py
```

## 📸 Demo

| Cuisine | Output |
|--------|--------|
| Indian | "The Saffron Leaf" <br> Menu: Paneer Tikka, Butter Naan, Chole Bhature... |
| Italian | "Trattoria Nova" <br> Menu: Margherita Pizza, Ravioli, Tiramisu... |

> Screenshots available in `/screenshots` folder.

## 🔐 API Setup

Set your **GROQ API Key** in a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Then load it in your Python code using `python-dotenv`:

```python
from dotenv import load_dotenv
load_dotenv()
```

Make sure to add `.env` to your `.gitignore`:
```
.env
```

## 📁 Folder Structure

```
├── main.py
├── langchain_helper.py
├── requirements.txt
├── README.md
└── screenshots/
```

## 🙌 Acknowledgments

- [LangChain](https://www.langchain.com/)
- [GROQ API](https://console.groq.com/)
- [Streamlit](https://streamlit.io/)

## 🧑‍💻 Author

Anu Baluguri  
[LinkedIn](https://www.linkedin.com/in/anu-baluguri-536a63231) | [GitHub](https://github.com/AnuBaluguri)
