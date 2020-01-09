import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from transformers import pipeline


def main():
    url = r'https://en.m.wikipedia.org/wiki/Kinshasa?action=render'

    nlp = pipeline('question-answering')
    #text = get_text(url)
    text = '''
    Kinshasa, formerly Léopoldville (Dutch: Leopoldstad), is the capital and the largest city of the 
    Democratic Republic of the Congo. The city is situated alongside the Congo River.
    
    Once a site of fishing and trading villages, Kinshasa is now a megacity with an estimated 
    population of more than 11 million. It faces Brazzaville, the capital of the neighbouring 
    Republic of the Congo, which can be seen in the distance across the wide Congo River, making 
    them the world's second-closest pair of capital cities after Rome and Vatican City. The city 
    of Kinshasa is also one of the DRC's 26 provinces. Because the administrative boundaries of 
    the city-province cover a vast area, over 90 percent of the city-province's land is rural in 
    nature, and the urban area occupies a small but expanding section on the western side.
    
    Kinshasa is Africa's third-largest urban area after Cairo and Lagos. It is also the world's 
    largest Francophone urban area (surpassing Paris in population), with French being the 
    language of government, schools, newspapers, public services, and high-end commerce in the 
    city, while Lingala is used as a lingua franca in the street. Kinshasa hosted the 14th 
    Francophonie Summit in October 2012.
    '''

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
