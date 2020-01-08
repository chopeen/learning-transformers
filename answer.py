import requests
from bs4 import BeautifulSoup
from transformers import pipeline


def main():
    url = r'https://en.m.wikipedia.org/wiki/Bevacizumab?action=render'

    nlp = pipeline('question-answering')
    text = get_text(url)

    questions = [
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

    for question in questions:
        answer = get_answer(nlp, text, question)
        print(f'{question} - {answer}')


def get_answer(nlp, text, question):
    return nlp(context=text, question=question)


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
