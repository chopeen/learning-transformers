import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from transformers import pipeline


def main():
    url = r'https://en.m.wikipedia.org/wiki/Kinshasa?action=render'

    nlp = pipeline('question-answering')
    text = get_text(url)

    questions = [
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
        'What are the largest urban areas in Africa?',
        'Is Kinshasa located in Africa?'
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
