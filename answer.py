"""
1. Running `pipeline(...)` for the first time may take time, because it downloads
   the pretrained models from S3.
2. They are cached in .cache/torch/transformers (even if TensorFlow is used).
3. I found no way to download them manually:
   - https://github.com/huggingface/transformers/issues/2323
   - https://github.com/huggingface/transformers/issues/2157
"""

from transformers import pipeline


nlp = pipeline('question-answering')

text = 'He lived in London and his name was Jack.'

answer = nlp(context=text, question='What was his name?')
print(answer)
