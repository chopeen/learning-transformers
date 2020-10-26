from sentence_transformers import SentenceTransformer, util

'''
Source: https://www.sbert.net/docs/usage/semantic_textual_similarity.html
'''

MODEL_NAME = 'distilbert-base-nli-stsb-mean-tokens'
SENTENCES = [
    'valve leaking',
    'valves leaking',
    'valve leakage',
    'water dripping',
    'reagent seeping from a broken valve',
    'worn rubber gasket'
]
BASE_SENTENCE = ['valve leaking'] * len(SENTENCES)


def main():
    model = SentenceTransformer(MODEL_NAME)

    embeddings1 = model.encode(BASE_SENTENCE, convert_to_tensor=True)
    embeddings2 = model.encode(SENTENCES, convert_to_tensor=True)

    cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)

    for i in range(len(BASE_SENTENCE)):
        print(f'Score: {cosine_scores[i][i]:.4f} \t {BASE_SENTENCE[i]} \t {SENTENCES[i]}')


if __name__ == '__main__':
    main()
