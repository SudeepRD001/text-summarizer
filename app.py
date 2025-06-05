# ✅ Install dependencies including the new lxml_html_clean
#pip install -q transformers gradio newspaper3k PyMuPDF lxml_html_clean

import gradio as gr
from transformers import pipeline
from newspaper import Article
import fitz  # PyMuPDF

# Load summarization pipeline
try:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
except Exception as e:
    raise RuntimeError(f"❌ Failed to load summarization model: {str(e)}")

# Helper Functions
def extract_text_from_url(url):
    try:
        if not url.startswith("http"):
            return "❌ Invalid URL format. Please include http or https."
        article = Article(url)
        article.download()
        article.parse()
        if not article.text.strip():
            return "❌ No text found in the article."
        return article.text
    except Exception as e:
        return f"❌ Error extracting from URL: {str(e)}"

def extract_text_from_pdf(file):
    try:
        if not file.name.endswith(".pdf"):
            return "❌ Invalid file format. Only PDFs are supported."
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        if not text.strip():
            return "❌ No text found in PDF."
        return text
    except Exception as e:
        return f"❌ Error reading PDF: {str(e)}"

# Main summarization logic
def summarize_input(text, url, file, word_length):
    source = "Textbox"

    try:
        if file is not None:
            text = extract_text_from_pdf(file)
            source = "PDF"
        elif url and url.strip():
            text = extract_text_from_url(url)
            source = "URL"
    except Exception as e:
        return f"❌ Failed to extract input: {str(e)}"

    if not text or "❌" in text:
        return text  # return the error message directly

    if len(text.strip()) < 30:
        return (
            f"⚠️ Please provide at least 30 characters of valid content.\n\n"
            f"📝 Current Input Length: {len(text.strip())} characters."
        )

    # Estimate token length from word count (approx. 1 word ≈ 1.3 tokens)
    estimated_max = min(int(word_length * 1.3), 1024)
    estimated_min = max(int(word_length * 0.5), 20)

    try:
        summary_result = summarizer(
            text,
            max_length=estimated_max,
            min_length=estimated_min,
            do_sample=False
        )
        summary = summary_result[0]['summary_text']
    except Exception as e:
        return f"❌ Summarization failed: {str(e)}"

    return (
        f"✅ **Source**: {source}\n"
        f"🧾 **Input Length**: {len(text.strip())} characters\n"
        f"📏 **Target Summary Length**: {word_length} words "
        f"(≈ {estimated_min}-{estimated_max} tokens)\n\n"
        f"### 🧠 Summary:\n{summary}"
    )

# Build UI
with gr.Blocks() as demo:
    gr.Markdown("## 🧠 English Text Summarizer (Text / URL / PDF)")

    with gr.Row():
        text_input = gr.Textbox(label="📄 Paste Text (Optional)", lines=10, placeholder="Type or paste up to 5000 characters...")
        url_input = gr.Textbox(label="🔗 URL (Optional)", placeholder="https://example.com/article")
        file_input = gr.File(label="📎 Upload PDF (Optional)", file_types=[".pdf"])

    word_slider = gr.Slider(
        minimum=30,
        maximum=790,
        value=80,
        step=10,
        label="📝 Desired Summary Length (Words)",
        info="Max supported summary length ≈ 790 words (1024 tokens)."
    )

    summarize_button = gr.Button("🚀 Summarize")
    output = gr.Markdown(elem_id="summary-output")

    summarize_button.click(
        fn=summarize_input,
        inputs=[text_input, url_input, file_input, word_slider],
        outputs=output
    )

demo.launch()

