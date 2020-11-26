Projekt: EY Document semantic search

1.	Wymagania
1.1.	Funkcjonalne
a)	Aplikacja ma udostępniać prosty interfejs graficzny pozwalający podać szukaną frazę oraz stronę do prezentacji wyników wyszukiwania.
b)	Aplikacja ma znajdować i zwracać podobne znaczeniowo fragmenty tekstu oraz udostępniać ich źródło.
c)	Aplikacja ma pracować na danych dostarczonych z korpusu polskiej Wikipedii.
1.2.	Niefunkcjonalne
a)	Aplikacja ma bazować na algorytmach uczenia maszynowego.
1.3.	Przypadki użycia
a)	Wyszukanie pasujących fraz.:
•	Użytkownik podaje szukaną frazę, a następnie klika przycisk „wyszukaj”.
•	System przeszukuje zakres dokumentów pod kątem znaczeniowo podobnych fragmentów
•	System przygotowuje wyniki końcowe (zestaw najlepiej dopasowanych fragmentów i ich źródeł) i je wyświetla
•	Użytkownik wybiera interesujący go fragment i przechodzi do źródła
2.	Architektura
 
3.	Scrum
3.1.	Kamienie milowe
a)	Projekt modelu wyszukiwania i klasyfikacji
b)	Wytrenowanie modelu i jego przetestowanie
c)	Implementacja przetwarzania dokumentów z Wikipedii
d)	Integracja elementów systemu i dodanie prostego interfejsu użytkownika
3.2.	Zadania
a)	Ustawienie architektury Azure do nauki i obsługi modelu
b)	Stworzenie modelu AI
c)	Zebranie danych testowych
d)	Nauczenie modelu
e)	Ustawienie architektury Azure do przetwarzania dokumentów z Wikipedii
f)	Stworzenie algorytmów przetwarzania dokumentów
g)	Postawienie App Service z interfejsem użytkownika
h)	Integracja komponentów 
3.3.	Repozytorium
GitHub
3.4.	Harmonogram realizacji kamieni milowych
a)	10.12.2020
b)	23.12.2020
c)	14.01.2021
d)	27.01.2021

