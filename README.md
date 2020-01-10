# Learning 🤗 Transformers

Experiments inspired by [this tweet](https://twitter.com/jmcimula/status/1213623492807135234/photo/1).

## QA pipeline

### Notes

1. Running `pipeline(...)` for the first time may take time, because
   it downloads the pretrained models from S3.
2. They are cached in `.cache/torch/transformers` (even if TensorFlow is
   used).
3. I found no way to download them manually (like it is possible for NLTK
   or spaCy):
   - https://github.com/huggingface/transformers/issues/2323
   - https://github.com/huggingface/transformers/issues/2157

### Results

#### Poznan (text snippet vs. article)
                                                      | Snippet of text (5 paragraphs)                             | Full article from Wikipedia 
    --------------------------------------------------|------------------------------------------------------------|----------------------------------------------------
    Where is Poznań located in Poland?                | west-central Poland,                                       | Poznań
    What is Poznań best know for?                     | renaissance Old Town and Ostrów Tumski Cathedral.          | (disambiguation).
    What is the population of Poznań?                 | 538,633                                                    | 2018) • City536,438
    How many people live in Poznań?                   | 1.1 million                                                | (200 ft)Population (31 December 2018) • City536,438
    What is the Poznań International Fair?            | the biggest industrial fair in Poland                      | Poznań Town Hall,
    What are the most renowned landmarks of Poznań?   | Poznań Town Hall,                                          | Poznań Town Hall,
    When did Stary Browar win competition organised   | 2012,                                                      | (200 ft)Population (31 December 2018) • City536,438
      by National Geographic Traveler?                |                                                            |
    Who are Saint Peter and Paul of Tarsus?           | Poznań is a city on the Warta River in west-central Poland,|  Poland.

#### Poznan (simple questions)

It cannot handle _polar questions_ (yes-no), because the answers are always passages extracted from the text (no NLG).

    -------------------------------------------  -------------------------------------------------
    Is Poznań a city?                            a city on the Warta River in west-central Poland,
    Is Poznań the fifth-largest city in Poland?  fifth-largest city in Poland.
    What is the fifth-largest city in Poland?    Poznań
    What is Stary Browar?                        the Poznań's Art and Business Center
    -------------------------------------------  -------------------------------------------------

#### Kinshasa (Wikipedia article)

https://en.m.wikipedia.org/wiki/Kinshasa?action=render

    ----------------------------------------------------------------------  -----------------------------------------------------------------
    What is the population of Kinshasa?                                     KinshasaVille de KinshasaCapitalKinshasa
    How many provinces does the DRC have?                                   FlagSealNickname(s): Kin la belle(English: Kin the beautiful)DRC,
    Where is Kinshasa situated in the DRC?                                  city-province of KinshasaKinshasaDRC,
    Where is Kinshasa located in the DRC?                                   city-province of KinshasaKinshasaDRC,
    When did the 14th Francophone Summit take place?                        KinshasaVille de KinshasaCapitalKinshasa
    What is the closest city to Kinshasa?                                   Leopoldville.
    What city is close to Kinshasa?                                         Leopoldville.
    What city is located near Kinshasa?                                     Leopoldville.
    What is the Francophone urban area that surpasses Paris in population?  "Léopoldville"
    What Francophone urban area is larger than Paris?                       Leopoldville.
    What are the largest urban areas in Africa?                             Democratic Republic of the CongoKinshasaKinshasa
    Is Kinshasa located in Africa?                                          Democratic Republic of the CongoKinshasaKinshasa (Africa)Show
    ----------------------------------------------------------------------  -----------------------------------------------------------------

#### Kinshasa (text snippet)

    ----------------------------------------------------------------------  ---------------------------------------------
    What is the population of Kinshasa?                                     11 million.
    How many provinces does the DRC have?                                   26
    Where is Kinshasa situated in the DRC?                                  alongside the Congo River.
    Where is Kinshasa located in the DRC?                                   alongside the Congo River.
    When did the 14th Francophone Summit take place?                        October 2012.
    What is the closest city to Kinshasa?                                   Brazzaville,
    What city is close to Kinshasa?                                         Rome and Vatican City.
    What city is located near Kinshasa?                                     Léopoldville
    What is the Francophone urban area that surpasses Paris in population?  Kinshasa
    What Francophone urban area is larger than Paris?                       Kinshasa
    What are the largest urban areas in Africa?                             Cairo and Lagos.
    Is Kinshasa located in Africa?                                          Kinshasa is Africa's third-largest urban area
    ----------------------------------------------------------------------  ---------------------------------------------
