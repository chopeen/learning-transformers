from sentence_transformers import SentenceTransformer, util

'''
Source: https://www.sbert.net/docs/usage/semantic_textual_similarity.html
'''

MODEL_NAME = 'distilbert-base-nli-stsb-mean-tokens'
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
    model = SentenceTransformer(MODEL_NAME)

    embeddings1 = model.encode(SENTENCES1, convert_to_tensor=True)
    embeddings2 = model.encode(SENTENCES2, convert_to_tensor=True)

    cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)

    for s1, s2, cos in zip(SENTENCES1, SENTENCES2, cosine_scores):
        print(f'{s1} \t\t {s2} \t\t Score: {cos:.4f}')
