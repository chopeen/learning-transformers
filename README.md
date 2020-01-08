# Learning 🤗 Transformers

## Notes for the QA pipeline

1. Running `pipeline(...)` for the first time may take time, because
   it downloads the pretrained models from S3.
2. They are cached in `.cache/torch/transformers` (even if TensorFlow is
   used).
3. I found no way to download them manually (like it is possible for NLTK
   or spaCy):
   - https://github.com/huggingface/transformers/issues/2323
   - https://github.com/huggingface/transformers/issues/2157
