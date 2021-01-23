# AzureProject

## Wybór modelu do tworzenia reprezentacji wektorowych

W pierwszej kolejności zajeliśmy się szukaniem obiecujących pre-trenowanych modeli, które potencjalnie mogą tworzyć jak njbardziej trafne embedingi w języku polskim. W tym celu po wstępnych analizach zdecydowaliśmy sie przyjrzeć trzem:
* BERT
* ROBERT
* Doc2Vec

Są to modele których pretrenowanych wersji szukaliśmy starając się dopasować heurystycznie model, który na postawie korpusu polskiej wikipedi miał dopasować jej fragment do zadanego zapytania. W późniejszym czasie po przygotowaniu odpowiednich danych przeprowadziliśmy rónież ewluacje na zbiorach testowych. W wyniku heurystyki stwierdziliśmy, że Doc2Vec nie za dobrze się sprawuje. ROBERTA i BERTA wyskazywały się podobna sprwnością więc poddaliśmy pre-trenowane modele z biblioteki sentence_transformers ewaluacji.
//// TU TRZEBA DAĆ WYNIKI 
W rezultacie najlepszym okazał się model 'paraphrase-xlm-r-multilingual-v1'. Bazuje on na SBERT(Sentence-BERT), która jest modyfikacją BERT pod kątem szybkości znajdowania par najbardziej podobnych zdań. Jak mówią autorzy modelu zredukowali czas szukania pary z 65h(BERT) do 5s(SBERT) przy zachowaniu takiej samej skuteczności. Ten model przyjeliśmy więc jako bazowy aby w kolejnych krokach dostosować go do języka polskiego.

## Znalezienie i przygotowanie danych do douczania modelu

## Badanie wpływu uczenia na rezultaty modelu
 
