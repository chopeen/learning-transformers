import torch
from torch.tensor import Tensor
from transformers import AutoTokenizer, AutoModel
from transformers import pipeline
import numpy as np

# https://www.sbert.net/docs/usage/semantic_textual_similarity.html
MODEL_NAME = 'sentence-transformers/distilbert-base-nli-stsb-mean-tokens'
SENTENCES1 = [
    'The cat sits outside',
    'A man is playing guitar',
    'The new movie is awesome'
]
SENTENCES2 = [
    'The dog plays in the garden',
    'A woman watches TV',
    'The new movie is so great that you cannot imagine it'
]


def main():
    model = AutoModel.from_pretrained(MODEL_NAME)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    nlp = pipeline('feature-extraction', model=model, tokenizer=tokenizer, framework='pt')

    embeddings1 = nlp("What is this?")
    embeddings2 = nlp("What is that?")

    # embeddings1 = torch.stack(embeddings1)
    # embeddings2 = torch.stack(embeddings2)

    cosine_scores = pytorch_cos_sim(embeddings1, embeddings2)

    for s1, s2, cos in zip(SENTENCES1, SENTENCES2, cosine_scores):
        print(f'{s1} \t\t {s2} \t\t Score: {cos:.4f}')


# https://github.com/UKPLab/sentence-transformers/blob/3824a191ea812e33439098c47a71a951af4f0f36/sentence_transformers/util.py#L13
def pytorch_cos_sim(a: Tensor, b: Tensor):
    """
    Computes the cosine similarity cos_sim(a[i], b[j]) for all i and j.
    This function can be used as a faster replacement for 1-scipy.spatial.distance.cdist(a,b)
    :return: Matrix with res[i][j]  = cos_sim(a[i], b[j])
    """
    if not isinstance(a, torch.Tensor):
        a = torch.tensor(a)

    if not isinstance(b, torch.Tensor):
        b = torch.tensor(b)

    if len(a.shape) == 1:
        a = a.unsqueeze(0)

    if len(b.shape) == 1:
        b = b.unsqueeze(0)

    a_norm = a / a.norm(dim=1)[:, None]
    b_norm = b / b.norm(dim=1)[:, None]
    return torch.mm(a_norm, b_norm.transpose(0, 1))


if __name__ == '__main__':
    main()
