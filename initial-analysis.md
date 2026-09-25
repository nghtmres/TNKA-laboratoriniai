# Laboratory 1 — Pradinė antraščių analizė

**Vardas: Nojus**  
**Data: 2026-09-11**  

## 1. Duomenų paruošimas

- Pradinių įrašų skaičius: **50 000**.
- Po tuščių įrašų pašalinimo liko **50 000** įrašų.
- Pašalinus tikslius dublikatus liko **4 845** unikalios antraštės.
- Modeliavimui atsitiktinai pasirinkta **1 500** antraščių, naudojant `random seed = 42`.
- Iš šio rinkinio pradinei analizei atsitiktinai pasirinkta **20** antraščių, naudojant `random seed = 43`.

## 2. Antraščių analizė

| ID | Antraštė | Mano siūloma tema arba temos | Dviprasmiškumas ir jo priežastis |
| --- | --- | --- | --- |
| H736 | 78 Kaip pagreitinti kompiuterį paprastais triukais | tech | nėra |
| H468 | 34 Central bank cuts rates, markets rally on dovish guidance | neaišku | nesuprantu finansinių terminų |
| H1327 | 43 Žvaigždė pasirašė daugiametę sutartį su klubu | celebrity | nėra |
| H535 | 47 How to speed up your computer with simple tweaks | tech | nėra |
| H436 | 2 Perėjimų gandai: jaunas puolėjas gali kainuoti rekordą | sports/celebrity | Gali būti sports, nes minimas puolėjas, arba celebrity, nes kalbama apie žaidėjo gandus |
| H696 | 31 Atviro kodo bibliotekos pagreitina mašininio mokymosi procesus | tech | nėra |
| H378 | 30 Didelė saugumo spraga paveikė milijonus vartotojų | tech | nėra |
| H951 | 75 Investors hedge inflation risk using index-linked bonds in a surprise move | finance/tech | Gali būti finance, nes minimi investuojantieji, arba tech, nes kalbama apie naujus nenuspėtus būdus |
| H811 | Investors hedge inflation risk using index-linked bonds in a surprise move (Kaunas) | finance | nėra |
| H1448 | 94 Central bank cuts rates, markets rally on dovish guidance (Paris) | neaišku | nesuprantu finansinių terminų |
| H643 | 22 Major security breach affects millions of users worldwide | tech | nėra |
| H1062 | Transfer rumors suggest a record deal for the young striker — analysts say | neaišku | nesuprantu terminų |
| H443 | Messi scores a stunning goal in the Champions League match amid concerns (London) | sports | nėra |
| H789 | 62 Top 7 secrets companies don't want you to know | tech | nėra |
| H68 | 36 Atviro kodo bibliotekos pagreitina mašininio mokymosi procesus | tech | nėra |
| H1169 | 30 Major security breach affects millions of users worldwide | tech | nėra |
| H1413 | 19 Ji padarė X — kas nutiks toliau, pribloškia | celebrity | nėra |
| H1482 | 40 Analysts predict record profits for the banking sector | finance | nėra |
| H1455 | 61 Ji padarė X — kas nutiks toliau, pribloškia | celebrity | nėra |
| H1204 | 81 Atviro kodo bibliotekos pagreitina mašininio mokymosi procesus | tech | nėra |

## 3. Pastebėtos temų grupės

Peržiūrėjęs 20 antraščių pastebėjau šias pagrindines grupes:

- Tech
- Sports
- Finance

## 4. Prognozuojamos temų modelio problemos

### 4.1. Pirma problema

Manau, kad modelis gali klysti atpažįstant temas tarp gandų sklidimo / puolėjo / sporto šakos. Tai matyti antraštėje H436, nes sakinys labai platus ir tema visiškai neaiški.

### 4.2. Antra problema

Manau, kad modelis gali klysti atpažįstant cybersecurity / programą, kuri buvo „breachinta“ / pačius naudotojus. Tai matyti antraštėje H1169, nes nepaminima security breach vieta ar pasekmės.
