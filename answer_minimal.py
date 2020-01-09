from transformers import pipeline

nlp = pipeline('question-answering')

answer = nlp(
    context='Poznań is a city on the Warta River in west-central Poland, '
            'in the Greater Poland region and is the fifth-largest city in Poland.',
    question='Where is Poznań located?'
)

print(answer)
# {'score': 0.485927675308254, 'start': 39, 'end': 59, 'answer': 'west-central Poland,'}
