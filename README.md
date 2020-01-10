# Learning 🤗 Transformers

Experiments inspired by [this tweet](https://twitter.com/jmcimula/status/1213623492807135234/photo/1).

## QA pipeline

### Notes

1. Running `pipeline(...)` for the first time may take time, because
   it automatically downloads from S3 the required pretrained models.
2. They are cached in `.cache/torch/transformers` (even if TensorFlow is
   used).
3. I found no way to download them explicitly like it is possible for NLTK
   or spaCy (discussed [here](https://github.com/huggingface/transformers/issues/2323)
   and [here](https://github.com/huggingface/transformers/issues/2157)), but you can
   view the contents of the [models.huggingface.co](https://s3.amazonaws.com/models.huggingface.co/)
   bucket.
4. Sometimes I had to start the pipeline multiple times before it finally
   managed to download all the files - either the connection timed out and
   the downloaded files were corrupted
   (`Unable to open file (truncated file: eof = 244962661, sblock->base_addr = 0, stored_eof = 265582824)`).
   - UPDATE: It must have been an issue with my home network or my ISP.
             Switching to mobile hotspot solved the problem immediately.

### Results

#### Poznan (text snippet vs. article)
                                                      | Snippet of text (5 paragraphs)                             | Full article from Wikipedia 
    --------------------------------------------------|------------------------------------------------------------|----------------------------------------------------
    Where is Poznań located in Poland?                | west-central Poland,                                       | west-central Poland,
    What is Poznań best know for?                     | renaissance Old Town and Ostrów Tumski Cathedral.          | renaissance Old Town and Ostrów Tumski Cathedral.
    What is the population of Poznań?                 | 538,633                                                    | 538,633
    How many people live in Poznań?                   | 1.1 million                                                | 1.1 million
    What is the Poznań International Fair?            | the biggest industrial fair in Poland                      | the biggest industrial fair in Poland
    What are the most renowned landmarks of Poznań?   | Poznań Town Hall,                                          | renaissance Old Town and Ostrów Tumski Cathedral.
    When did Stary Browar win competition organised   | 2012,                                                      | (2011
      by National Geographic Traveler?                |                                                            |
    Who are Saint Peter and Paul of Tarsus?           | Poznań is a city on the Warta River in west-central Poland,| Poznań

#### Poznan (simple questions)

It cannot handle _polar questions_ (yes-no), because the answers are always passages extracted from the text (no NLG).

    -------------------------------------------  -------------------------------------------------
    Is Poznań a city?                            a city on the Warta River in west-central Poland,
    Is Poznań the fifth-largest city in Poland?  fifth-largest city in Poland.
    What is the fifth-largest city in Poland?    Poznań
    What is Stary Browar?                        the Poznań's Art and Business Center
    -------------------------------------------  -------------------------------------------------

#### Kinshasa (text snippet vs. article)

                                                                           | Snippet of text (5 paragraphs) | Full article from Wikipedia 
    -----------------------------------------------------------------------|--------------------------------|-------------------------------
    What is the population of Kinshasa?                                    | 11 million.                    | 11 million. 
    How many provinces does the DRC have?                                  | 26                             | 26
    Where is Kinshasa situated in the DRC?                                 | alongside the Congo River.     | one of the DRC's 26 provinces.
    Where is Kinshasa located in the DRC?                                  | alongside the Congo River.     | one of the DRC's 26 provinces.
    When did the 14th Francophone Summit take place?                       | October 2012.                  | October 2012.Residents
    What is the closest city to Kinshasa?                                  | Brazzaville,                   | Brazzaville,
    What city is close to Kinshasa?                                        | Rome and Vatican City.         | Brazzaville,
    What city is located near Kinshasa?                                    | Léopoldville                   | Léopoldville      
    What is the Francophone urban area that surpasses Paris in population? | Kinshasa                       | Léopoldville      
    What Francophone urban area is larger than Paris?                      | Kinshasa                       | side.Kinshasa
    What are the largest urban areas in Africa?                            | Cairo and Lagos.               | Cairo and Lagos.      

NOTE: Answers with merged words (`October 2012.Residents` or `side.Kinshasa`) suggest
      that better text pre-processing could improve the results even more.
