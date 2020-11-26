Projekt: EY Document semantic search

1.	Wymagania
  1.	Funkcjonalne
    * Aplikacja ma udostępniać prosty interfejs graficzny pozwalający podać szukaną frazę oraz stronę do prezentacji wyników wyszukiwania.
    *	Aplikacja ma znajdować i zwracać podobne znaczeniowo fragmenty tekstu oraz udostępniać ich źródło.
    *	Aplikacja ma pracować na danych dostarczonych z korpusu polskiej Wikipedii.
  1.	Niefunkcjonalne
    *	Aplikacja ma bazować na algorytmach uczenia maszynowego.
  1. Przypadki użycia
    *	Wyszukanie pasujących fraz.:
      * Użytkownik podaje szukaną frazę, a następnie klika przycisk „wyszukaj”.
      * System przeszukuje zakres dokumentów pod kątem znaczeniowo podobnych fragmentów
      * System przygotowuje wyniki końcowe (zestaw najlepiej dopasowanych fragmentów i ich źródeł) i je wyświetla
      * Użytkownik wybiera interesujący go fragment i przechodzi do źródła
1.	Architektura
 
1.	Scrum
  1.	Kamienie milowe
    *	Projekt modelu wyszukiwania i klasyfikacji
    *	Wytrenowanie modelu i jego przetestowanie
    *	Implementacja przetwarzania dokumentów z Wikipedii
    *	Integracja elementów systemu i dodanie prostego interfejsu użytkownika
  1.	Zadania
    *	Ustawienie architektury Azure do nauki i obsługi modelu
    *	Stworzenie modelu AI
    *	Zebranie danych testowych
    *	Nauczenie modelu
    *	Ustawienie architektury Azure do przetwarzania dokumentów z Wikipedii
    *	Stworzenie algorytmów przetwarzania dokumentów
    *	Postawienie App Service z interfejsem użytkownika
    *	Integracja komponentów 
  1.	Repozytorium
    * GitHub
  1.	Harmonogram realizacji kamieni milowych
    *	10.12.2020
    *	23.12.2020
    *	14.01.2021
    *	27.01.2021

