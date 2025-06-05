# 🧠 Text Summarizer App (Transformers + Gradio)

A powerful and user-friendly English text summarizer built using **Hugging Face Transformers** and **Gradio**. This app enables you to generate concise and accurate summaries from a variety of input sources.

## 🚀 Features

- 📝 **Plain Text Input**  
  Enter any English text manually and get an instant summary.

- 🌐 **Summarize from URL**  
  Extracts and summarizes content directly from news article URLs.

- 📄 **Upload PDF Documents**  
  Upload your PDF files and summarize their content effortlessly.

## 🧠 Model

This application uses the [`facebook/bart-large-cnn`](https://huggingface.co/facebook/bart-large-cnn) model — a state-of-the-art transformer model known for its accurate and fluent summarization capabilities.
## 💻 Tech Stack

| Technology            | Description                                      |
|-----------------------|--------------------------------------------------|
| Python                | Core programming language                        |
| Hugging Face Transformers | For pre-trained NLP models                    |
| Gradio                | Interactive UI for the web app                   |
| Newspaper3k           | For scraping article content from URLs           |
| PyMuPDF (`fitz`)      | For extracting text from uploaded PDFs           |

## 📦 Installation

Make sure you have **Python 3.8+** and **pip** installed. Then follow these steps:

```bash
git clone https://github.com/SudeepRD001/text-summarizer.git
cd text-summarizer
python -m venv venv
venv\Scripts\activate    # On MacOS: source venv/bin/activate 
pip install -r requirements.txt
```
## 🚀 Running the App Locally

To start the application, simply run:

```bash
python app.py
```
Gradio will automatically launch the app in your default web browser at:
http://127.0.0.1:7860

## 🖼️ Screenshots

### 🔹 Main Interface
![Main Interface](images/main_interface.png)

### 🔹 Summary Output Example
![Summary Output](images/summary_output.png)
