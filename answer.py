import requests

from transformers import pipeline


def main():
    url = r'https://en.m.wikipedia.org/wiki/Bevacizumab'
    text = get_text(url)
    print(text)

    exit(1)

    nlp = pipeline('question-answering')

    text = 'He lived in London and his name was Jack.'

    answer = nlp(context=text, question='What was his name?')
    print(answer)


def get_text(url):
    # `verify=False` is a workaround for error:
    #   Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed:
    #   self signed certificate in certificate chain (_ssl.c:1076)
    file = requests.get(url, verify=False)
    text = file.text
    return text


if __name__ == '__main__':
    main()
