import os
from dotenv import load_dotenv
# from transformers import pipelines
from huggingface_hub import InferenceClient

load_dotenv()

def ner(text):
    client = InferenceClient(token=os.getenv("HUGGINGFACE_TOKEN"))
    result = client.token_classification(text=text, model="dslim/bert-base-NER")

    named_entities = []
    for entity in result:
        named_entities.append({
            "word": entity["word"],
            "type": entity["entity_group"],
            "score": round(entity["score"], 3)
        })

    return named_entities  # ✅ returning list of dicts

def sent(text):
    client = InferenceClient(token=os.getenv("HUGGINGFACE_TOKEN"))

    text_input = text

    result = client.text_classification(
        text_input,
        model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    )

    # result is a list of dictionaries like: [{'label': 'POSITIVE', 'score': 0.999}]

    # ✅ Extract the label with the highest score
    top_label = max(result, key=lambda x: x['score'])

    fin = f"\n🧠 Predicted Sentiment: {top_label['label']} --> {top_label['score']:.2f}"
    return fin
"""We can use the above code it will take some time and data to run at first but after that it will be faster and no internet will be required: 
from transformers import pipeline
text_input = str(input("Enter text for analysis : "))
classifier = pipeline("text-classification", model = "roberta-large-mnli")
classifier(text_input)
## [{'label': 'ENTAILMENT', 'score': 0.98}]

"""

  # Load the environment variables from .env

def summarize_text(text):
    client = InferenceClient(token=os.getenv("HUGGINGFACE_TOKEN"))


    result = client.summarization(
        text,
        model="sshleifer/distilbart-cnn-12-6",
    )

    return f"\n📄 Summary:\n {result.summary_text}"







"""
For summrization
We can use the above code it will take some time and data to run at first but after that it will be faster and no internet will be required:
from transformers import pipeline
text_in = str(input("Enter text for summarization : "))
classifier = pipeline("summarization")
classifier(text_in)

"""
