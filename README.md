# Learning 🤗 Transformers

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

https://en.m.wikipedia.org/wiki/Bevacizumab?action=render

    ---------------------------------------------------  ---------------------------------------------------------------
    When was Bevacizumab approved in the United States?  this?)  (verify)Bevacizumab, sold under the trade name Avastin,
    What is the trade name of Bevacizumab?               Avastin,
    What trade name is Bevacizumab sold under?           Avastin,
    How much does a dose cost?                           11–50 days)IdentifiersCAS
    How does Bevacizumab work?                           a medication
    What are the common side effects of Bevacizumab?     (Risk not ruled out)
    How is Bevacizumab given?                            Pregnancycategory
    How was Bevacizumab derived?                         Avastin,
    Is Bevacizumab an antibody?                          US DailyMed: Bevacizumab US FDA: Bevacizumab
    What is a specialty drug?                            Avastin,
    ---------------------------------------------------  ---------------------------------------------------------------

https://en.m.wikipedia.org/wiki/Poznan?action=render

    --------------------------------------------------------  ---------------------------------------------------
    What is the population of Poznań?                         2018) • City536,438
    Where is Poznań located?                                  Poznań
    What is the main river of Poznań?                         Poznań
    What is the climate is Poznań?                            (CET) • Summer
    How many neighbourhoods are there in Poznań?              Poznań
    How many districts?                                       Poland.
    When did the first free local elections take place?       (200 ft)Population (31 December 2018) • City536,438
    What is the largest lake in Poznań?                       Poznań
    Is there a zoo in Poznań?                                 Poznań
    What is the abbreviation for Adam Mickiewicz University?  "Posnania"
    --------------------------------------------------------  ---------------------------------------------------
