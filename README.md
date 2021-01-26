# AzureProject - Document semantic search (EY)

#### W ramach projektu zrealizowaliśmy:
* wybór pretrenowanego modelu do tworzenia vektorowych reprezentacji tekstu
* znalezienie i dostosowanie danych do nauki
* dotrenowanie modelu
* postwienie modelu w formie prostej aplikacji webowej

#### Funkcjonalność aplikacji:
* aplikacja przyjmuje na wejsciu fragment tekstu, następnie zwraca 10 najbanrdziej pasujących paragrafów z korpusu polskiej wikiedii
 
#### Diagram architektury:
* aplikacja jest postawiona jako AppService, a operacje na modelach dokonywane były w notebook'ach

![](/docs/OstatecznyAzureDiagram.png)

## Wybór modelu do tworzenia reprezentacji wektorowych

W pierwszej kolejności zajeliśmy się szukaniem obiecujących pre-trenowanych modeli, które potencjalnie mogą tworzyć jak njbardziej trafne embedingi w języku polskim. W tym celu po wstępnych analizach zdecydowaliśmy sie przyjrzeć trzem:
* BERT
* ROBERT
* Doc2Vec

Są to modele których pretrenowanych wersji szukaliśmy starając się dopasować heurystycznie model, który na postawie korpusu polskiej wikipedi miał dopasować jej fragment do zadanego zapytania. W późniejszym czasie po przygotowaniu odpowiednich danych przeprowadziliśmy rónież ewluacje na zbiorach testowych. W wyniku heurystyki stwierdziliśmy, że Doc2Vec nie za dobrze się sprawuje. ROBERTA i BERTA wyskazywały się podobna sprwnością więc poddaliśmy pre-trenowane modele z biblioteki sentence_transformers ewaluacji.

Wyniki ewaluacji surowych modeli zaprezentowane sa w pierwszym punkcjie dokumentu:
[Wyniki ewaluacji](models_training/Trening.md)

W rezultacie najlepszym okazał się model 'paraphrase-xlm-r-multilingual-v1'. Bazuje on na SBERT(Sentence-BERT), która jest modyfikacją BERT pod kątem szybkości znajdowania par najbardziej podobnych zdań. Jak mówią autorzy modelu zredukowali czas szukania pary z 65h(BERT) do 5s(SBERT) przy zachowaniu takiej samej skuteczności. Ten model przyjeliśmy więc jako bazowy aby w kolejnych krokach dostosować go do języka polskiego.

## Znalezienie i przygotowanie danych do douczania modelu
Przy douczaniu bazujemy na dwóch zbiorach:
#### a) Zbiór 10000 par zdań i etykietami opisującymi ich podobieństwo [LINK](http://zil.ipipan.waw.pl/Scwad/CDSCorpus?action=AttachFile&do=view&target=dataset_1000.csv)
Jest to zbiór stworzony przez The Linguistic Engineering (LE) Group is part of the Department of Artificial Intelligence at the Institute of Computer Science, Polish Academy of Sciences (IPI PAN). Dane te zastosowaliśmy bez dodatkowego przygotowania jedynie przeskalowalaiśmy podobieństwo z przedziału 0-5 na 0-1.
 
#### b) Zbiór pytań i powiązanych z nimi artykółów wikipedii [LINK](http://nlp.pwr.wroc.pl/en/tools-and-resources/resources/czy-wiesz-question-answering-dataset)
Jest to zbiór przygotowany przez zespół badawczy Instytutu Informatyki Politechniki Wrocławskiej w latach 2013-2014. Dane w nim zawarte po podpowiednim przygotowaniu pozwoliły poprawić nam nasz model.

Schemat przygotowania danych:
 - sprawdzenie i odrzucenie tcyh pytań, do których w aktualnej wikipedii nie ma odnośników
 - przy wykorzystaniu wstepnie wybranego modelu odszukanie najbardziej podobnych paragrafów, a następnie konkretnych zdań
 - heurystyczna weryfikacja wyników
 - zapisanie poprawnych par pytanie-odpowiedź w celu późniejszego trenwania modelu
 
## Badanie wpływu uczenia na rezultaty modelu
 
 [Wyniki trenowania - ewaluacja na zbiorach testowych](models_training/Trening.md) - trenowanie jest opisane od 2 punktu dokumentu
 
 [Wyniki testów heurystycznych - relaizacja 15 zapytań](models_tests/README.md) - plik pokazuje na jakiej pozycji znalazły się rzeczywiście blisko powiązane z danym pytaniem rezultaty
 
 W wyniku testów heurystycznych zobserwowaliśmy największa poprawę względem surowego modelu po douczeniu go na zbiorze *cds*, a nestępnie zbiorze *czywiesz*. Z racji, że nieu udało nam sie znaleźć cross-encodera dedykowanego językowi polskiemu wyniki uzyskane z jego wykorzystaniem w większości przypadków okazywały się gorsze, ale w niektórych scenariuszach był skuteczy. Możliwe jest, że bardziej staranne dobranie i douczenie cross-encodera mogłoby pozwolić na dodatkową poprawę wyników wyszukiwania. 
