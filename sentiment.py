from transformers import pipeline


nlp = pipeline('sentiment-analysis')

sent = nlp('We are very happy to include pipeline into the transformers repository.')
print(sent)
