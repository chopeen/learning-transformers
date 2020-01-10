import wikipedia

from tabulate import tabulate
from transformers import pipeline


def main():
    article_title = 'Poznan'

    nlp = pipeline('question-answering')
    text = get_wikipedia_content(article_title)
    questions = [
        'Where is Poznań located in Poland?',
        'What is Poznań best know for?',
        'What is the population of Poznań?',
        'How many people live in Poznań?',
        'What is the Poznań International Fair?',
        'What are the most renowned landmarks of Poznań?',
        'When did Stary Browar win competition organised by National Geographic Traveler?',
        'Who are Saint Peter and Paul of Tarsus?'
    ]

    answers = []
    for question in questions:
        answer = get_answer(nlp, text, question)
        answers.append((question, answer))

    print(tabulate(answers))


def get_answer(nlp, text, question):
    answer_object = nlp(context=text, question=question)
    # example object: {'score': 0.9962748423312462, 'start': 1001, 'end': 1009, 'answer': 'Avastin,'}
    answer_text = answer_object['answer']
    return answer_text


def get_wikipedia_content(article_title):
    page = wikipedia.page(article_title)
    return page.content


if __name__ == '__main__':
    main()
