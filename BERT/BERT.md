# BERT

1. Można BERTa wytrenować na dwóch taskach:

	1. Masked LM (MLM) - Before feeding word sequences into BERT, 15% of the words in each sequence are replaced
    with a [MASK] token. The model then attempts to predict the original value of the masked words,
    based on the context provided by the other, non-masked, words in the sequence.
	
   2. Next Sentence Prediction (NSP) - In the BERT training process, the model receives pairs of sentences as input
    and learns to predict if the second sentence in the pair is the subsequent sentence
    in the original document.
   
   Nie warto raczej BERTa trenować od początku bo wymaga to bardzo dużego datasetu, mocy obliczeniowej i czasu. Lepiej zrobić jakiś fine-tuning gotowego modelu.
   
2. [Biblioteka Transformers](https://huggingface.co/transformers)
    - Fajna biblioteka z przetrenowanymi transformerami, tokenizerami, można korzystając z niej dotrenować model na swoich danych - jest dużo notebooków i tutoriali. 

    - Testowałam stamtąd BERTa uśredniając jego hidden states w celu uzyskania embeddingów - wynik taki sobie, ale jakoś działało.
    
3. Sentence BERT

    - Używa sieci syjamskich, żeby robić lepsze, krótsze embeddingi.
    - Trenowany na parach zdań gdzie zdania są podobne, mają przeciwne znaczenia lub jedno wynika z drugiego.
    - Dataset w języku polskim zawierający 10 tysięcy par takich zdań:  [CDSCorpus](http://zil.ipipan.waw.pl/Scwad/CDSCorpus)

    - Można pobrać stamtąd 1000 par, ale można też napisać emaila i poprosić o cały dataset.
    - Można wykorzystać gotowy z biblioteki [sentence-transformers](https://github.com/UKPLab/sentence-transformers)
    - Testowałam stamtąd wielojęzycznego BERTa i wyniki są dosyć fajne.
    
4. [bert-as-service](https://bert-as-service.readthedocs.io/en/latest/)
   
    - Robi embeddingi zdań korzystając z BERTa.
    
    - Pozwala robić krótsze embeddingi (i może lepsze niż przez zwykłe uśrednianie, ale jeszcze nie testowałam).
    
5. Githuby z polskimi datasetami i modelami do NLP:

    - [awesome-nlp-polish](https://github.com/ksopyla/awesome-nlp-polish#models-and-embeddings)
    - [polish-nlp-resources](https://github.com/sdadas/polish-nlp-resources)

