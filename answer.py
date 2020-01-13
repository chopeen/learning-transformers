import wikipedia

from tabulate import tabulate
from transformers import pipeline


def main():
    questions_poznan = [
        'Where is Poznań located in Poland?',
        'What is Poznań best know for?',
        'What is the population of Poznań?',
        'How many people live in Poznań?',
        'What is the Poznań International Fair?',
        'What are the most renowned landmarks of Poznań?',
        'When did Stary Browar win competition organised by National Geographic Traveler?',
        'Who are Saint Peter and Paul of Tarsus?'
    ]
    questions_kinshasa = [
        'What is the population of Kinshasa?',
        'How many provinces does the DRC have?',
        'Where is Kinshasa situated in the DRC?',
        'Where is Kinshasa located in the DRC?',
        'When did the 14th Francophone Summit take place?',
        'What is the closest city to Kinshasa?',
        'What city is close to Kinshasa?',
        'What city is located near Kinshasa?',
        'What is the Francophone urban area that surpasses Paris in population?',
        'What Francophone urban area is larger than Paris?',
        'What are the largest urban areas in Africa?'
    ]
    questions_bevacizumab = [
        'When was Bevacizumab approved in the United States?',
        'What is the trade name of Bevacizumab?',
        'What trade name is Bevacizumab sold under?',
        'How much does a dose cost?',
        'How does Bevacizumab work?',
        'What are the common side effects of Bevacizumab?',
        'How is Bevacizumab given?',
        'How was Bevacizumab derived?',
        'Is Bevacizumab an antibody?',
        'What is a specialty drug?'
    ]

    print_answers('Poznan', questions_poznan)
    # print_answers('Kinshasa', questions_kinshasa)
    # print_answers('Bevacizumab', questions_bevacizumab)


def print_answers(wiki_article_title, questions):
    nlp = pipeline('question-answering')
    text = get_wikipedia_content(wiki_article_title)

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
