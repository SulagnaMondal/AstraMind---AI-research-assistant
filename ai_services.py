from transformers import pipeline

def summarize(text: str, model_name="facebook/bart-large-cnn"):
    summarizer = pipeline("summarization", model=model_name)
    return summarizer(text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']

def extract_code(text: str):
    # Simple code extraction (improve with custom logic)
    code_blocks = re.findall(r'```(?:python|bash)?\n(.*?)```', text, re.DOTALL)
    return "\n\n".join(code_blocks)