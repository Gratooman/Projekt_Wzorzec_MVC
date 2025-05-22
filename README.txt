#Cyfrowa Biblioteka

Projekt aplikacji internetowej stworzonej w Django, umożliwiającej zarządzanie listą książek z poziomu przeglądarki. Użytkownik ma możliwość dodawania, edytowania, filtrowania oraz usuwania pozycji książkowych w wirtualnej bibliotece.

##Spis treści

- [Opis projektu](#opis-projektu)
- [Funkcjonalności](#funkcjonalności)
- [Wymagania](#wymagania)
- [Instalacja](#instalacja)
- [Uruchomienie](#uruchomienie)

##Opis projektu

Aplikacja wykonana w ramach projektu zaliczeniowego na studiach. Zbudowana w oparciu o wzorzec architektoniczny MVC, z użyciem Django i języka Python. Projekt nie wymaga logowania – każdy użytkownik ma dostęp do pełnej funkcjonalności aplikacji.

##Funkcjonalności

- Wyświetlanie listy książek
- Filtrowanie książek po statusie (przeczytana / nieprzeczytana)
- Filtrowanie po kategorii literackiej
- Sortowanie po tytule, autorze i roku
- Dodawanie książek (z walidacją pól)
- Edytowanie książek
- Usuwanie książek

## Wymagania

- Python 3.10 lub nowszy
- Pip (menedżer pakietów Pythona)
- System operacyjny Windows/Linux/macOS

## Instalacja

1.Klonowanie repozytorium:

git clone https://github.com/Gratooman/Projekt_Wzorzec_MVC.git
cd digital_library


2.Utworzenie środowiska wirtualnego:

python -m venv venv


3.Aktywacja środowiska:

- Windows:

venv\Scripts\activate

- Linux/macOS:

source venv/bin/activate


4.Instalacja Django:

pip install django


##Uruchomienie

1.Wykonanie migracji bazy danych:

python manage.py makemigrations
python manage.py migrate


2.Uruchomienie serwera:

python manage.py runserver


3.Otwórz przeglądarkę i wejdź na adres:

http://127.0.0.1:8000/
