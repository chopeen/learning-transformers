import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from transformers import pipeline


def main():
    url = r'https://en.m.wikipedia.org/wiki/Poznan?action=render'

    nlp = pipeline('question-answering')
    text = get_text(url)
    # text = '''q
    # Poznań is a city on the Warta River in west-central Poland, in the Greater Poland region
    # and is the fifth-largest city in Poland. It is best known for its renaissance Old Town and
    # Ostrów Tumski Cathedral. Today, Poznań is an important cultural and business centre and
    # one of Poland's most populous regions with many regional customs such as Saint John's Fair,
    # traditional Saint Martin's croissants and a local dialect.
    #
    # Poznań is among the oldest and largest cities in Poland. The city's population is 538,633
    # (2011 census), while the continuous conurbation with Poznań County and several other
    # communities is inhabited by almost 1.1 million people. The Larger Poznań Metropolitan
    # Area (PMA) is inhabited by 1.3–1.4 million people and extends to such satellite towns as
    # Nowy Tomyśl, Gniezno and Września, making it the fourth largest metropolitan
    # area in Poland. It is the historical capital of the Greater Poland region and is currently
    # the administrative capital of the province called Greater Poland Voivodeship.
    #
    # Poznań is a centre of trade, sports, education, technology and tourism. It is an important
    # academic site, with about 130,000 students and the Adam Mickiewicz University, the third
    # largest Polish university. Poznań is also the seat of the oldest Polish diocese, now being
    # one of the most populous archdioceses in the country. The city also hosts the Poznań
    # International Fair – the biggest industrial fair in Poland and one of the largest fairs in
    # Europe. The city's most renowned landmarks include Poznań Town Hall, the National Museum,
    # Grand Theatre, Fara Church, Poznań Cathedral and the Imperial Castle.
    #
    # In 2012, the Poznań's Art and Business Center "Stary Browar" won a competition organised by
    # National Geographic Traveler and was given the first prize as one of the seven "New Polish Wonders".
    #
    # The official patron saints of Poznań are Saint Peter and Paul of Tarsus, the patrons of
    # the cathedral. Martin of Tours – the patron of the main street Święty Marcin is also
    # regarded as one of the patron saints of the city.
    # '''

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
