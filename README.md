# RWA - projekt

## Upute za instalaciju
1. Kloniraj repozitorij
2. Kreiraj virtualnu okolinu
3. Aktiviraj virtualnu okolinu naredbom `venv\Scripts\activate`
4. Instaliraj potrebne stvari pomoću requirements.txt datoteke naredbom `pip install -r requirements.txt`
5. Pokreni naredbom `python app.py`
6. U web browseru upiši `localhost:5000`

## Nakon instalacije
1. Pod "First time API" prvo treba stvoriti bazu podataka pod `/db-init`
2. Nakon toga dodajte prvog admina pod `/add-first-admin`
3. Sada se ulogirajte s tim adminom, autorizirajte token i moći ćete pristupiti ostatku API-a

## Sadržaj web aplikacije
- Admin i User login
- Admin može brisati i izlistavati sve Usere
- Admin može pregledavati i brisati sve upite (pojedinačno i zajedno)
- User može izlistavati svoje upite 
- Uz to može pregledavati svoje podatke i uređivati ih