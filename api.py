from huggingface_hub import InferenceClient
from transformers import pipeline

def sent(text):
    client = InferenceClient(
        token="",  # your token
    )

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
def ner(text):
    # Load once globally (efficient for repeated calls)
    classifier = pipeline("ner", model="dslim/bert-base-NER", grouped_entities=True)
    result = classifier(text)
    named_entities = []

    for entity in result:
        group = entity['entity_group']
        word = entity['word']
        score = entity['score']
        named_entities.append({
            "word": word,
            "type": group,
            "score": round(score, 3)
        })

    return named_entities


"""
For summrization
We can use the above code it will take some time and data to run at first but after that it will be faster and no internet will be required:
from transformers import pipeline
text_in = str(input("Enter text for summarization : "))
classifier = pipeline("summarization")
classifier(text_in)
"""
