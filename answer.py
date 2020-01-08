import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from transformers import pipeline


def main():
    url = r'https://en.m.wikipedia.org/wiki/Poznan?action=render'

    nlp = pipeline('question-answering')
    text = get_text(url)

    questions = [
        'What is the population of Poznań?',
        'Where is Poznań located?',
        'What is the main river of Poznań?',
        'What is the climate is Poznań?',
        'How many neighbourhoods are there in Poznań?',
        'How many districts?',
        'When did the first free local elections take place?',
        'What is the largest lake in Poznań?',
        'Is there a zoo in Poznań?',
        'What is the abbreviation for Adam Mickiewicz University?'
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


def get_text(url):
    # TODO: find a way to make `requests` work with the TLS proxy
    # `verify=False` is a workaround for error:
    #   Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed:
    #   self signed certificate in certificate chain (_ssl.c:1076)
    file = requests.get(url, verify=False)

    raw_html = file.text
    clean_text = BeautifulSoup(raw_html, 'lxml').text

    return clean_text


if __name__ == '__main__':
    main()
