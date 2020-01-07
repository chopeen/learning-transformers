# https://huggingface.co/transformers/quickstart.html#bert-example
#
# Available pre-trained models: https://huggingface.co/transformers/pretrained_models.html

import logging
import tensorflow
from transformers import BertTokenizer


# OPTIONAL: if you want to have more information on what's happening under the hood, activate the logger as follows
logging.basicConfig(level=logging.INFO)

# Load pre-trained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Tokenize input
text = "[CLS] Who was Jim Henson ? [SEP] Jim Henson was a puppeteer [SEP]"
tokenized_text = tokenizer.tokenize(text)

print(tokenized_text)
