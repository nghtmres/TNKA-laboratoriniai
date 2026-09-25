# Laboratory 1 — Editor's recommendation

**Name:** Nojus
**Date:** 2026-09-21

**Run instructions:**

`python prepare_data.py` — duomenų valymas ir atranka pradinei analizei.
`python modeling.py` — A, B ir C modelių mokymas, rezultatų palyginimas ir naujų antraščių analizė per gynimą.

**Package versions:** Python 3.11.9; pandas 3.0.5; scikit-learn 1.9.1.

**Parameters:** document sample seed = 42, initial analysis seed = 43, LDA seed = 42, `max_iter=15`, `learning_method="batch"`, `max_features=3000`, `min_df=2`, `lowercase=True`, English stop words.

## Initial analysis — separate checkpoint file

Pradinių įrašų skaičius buvo 50 000. Pašalinus aplink tekstą esančius tarpus ir tuščius įrašus liko 50 000 įrašų, o pašalinus tikslius dublikatus — 4 845 unikalios antraštės. Modeliavimui atsitiktinai atrinkta 1 500 antraščių naudojant `random_state=42`. Joms priskirti identifikatoriai H1–H1500. Iš šio korpuso pradinei analizei atsitiktinai atrinkta 20 antraščių naudojant `random_state=43`. Pradinės grupės, dviprasmiški atvejai ir dvi prognozuotos problemos pateiktos `initial-analysis.md` faile. 

## 1. Decisions and prediction

Pradinėje analizėje pastebėtos technologijų, sporto ir finansų temos bei įžymybių grupė. Todėl pasirinktos 4 temos kaip galimas plačių grupių skaičius. Palyginimui pasirinktos 6 temos, siekiant patikrinti, ar atsiskirtų siauresnės kryptys, pavyzdžiui, kibernetinis saugumas ir mašininis mokymasis.

Tikrintas vienas teksto paruošimo sprendimas — pasikartojančių šabloninių frazių pašalinimas. Prognozuota, kad modelis labiau remsis pagrindiniu antraštės turiniu, tačiau gali būti prarasta informacija apie rinkos reakciją, analitikų vertinimą ar susirūpinimą. C bandyme pašalintos frazės: „dėl rinkos reakcijos“, „po pranešimo“, „analitikų teigimu“, „as markets react“ ir „amid concerns“.

## 2. Three-run comparison

Tekstas paverstas žodžių dažnių matrica naudojant `CountVectorizer`. Naudota numatytoji tokenizacija: išskiriami bent dviejų simbolių žodžio simbolių junginiai, todėl žodyne gali likti ir skaičių. Visos raidės paverstos mažosiomis. Naudoti angliški stop žodžiai, nes didelė dalis antraščių parašyta angliškai. Lietuviški bendriniai žodžiai dėl to gali likti žodyne. Palikti bent dviejuose dokumentuose pasirodantys terminai (`min_df=2`), siekiant sumažinti retų terminų įtaką. Žodyno dydis apribotas iki 3 000 terminų. Gautos matricos dydis — 1 500 × 313. Dokumentų be išlikusių terminų buvo 0, todėl papildomai jų šalinti nereikėjo. LDA modeliai mokyti 15 iteracijų, naudojant `learning_method="batch"` ir `random_state=42`. Gauti kiekvienos temos svarbiausi žodžiai ir kiekvienos antraštės temų svoriai.

### A, B ir C palyginimas

| Bandymas | Temų skaičius | Teksto paruošimas | Pastovūs nustatymai / seed | Naudingumo ar problemų įrodymai |
| --- | ---: | --- | --- | --- |
| A | 4 | Originalus | Kaip nurodyta parametruose | Temos per plačios: kartu atsirado „Apple“, iPhone, infliacija ir akcijos. H254 ir H370 pateko į tą pačią temą. |
| B | 6 | Originalus | Tie patys kaip A | Atsirado siauresnių krypčių, tačiau 5 temos pavyzdžiai H254 ir H926 vis tiek sujungė centrinį banką su mašininiu mokymusi. |
| C | 6 | Pašalintos penkios šabloninės frazės | Tie patys kaip B | Žodynas sumažėjo nuo 313 iki 306 terminų, tuščių dokumentų buvo 0, tačiau aiškaus bendro temų pagerėjimo nenustatyta. |

### Konkretūs C bandymo pavyzdžiai

C bandyme iš H370 ir H254 antraščių pašalinta frazė „dėl rinkos reakcijos“. Iš naujo apmokius modelį su visame korpuse pašalintomis penkiomis pasirinktomis frazėmis, H370 didžiausias temos svoris padidėjo nuo 0,718 iki 0,916. Priskirtos C modelio temos žodžiai „treneris“, „gynybos“, „taktiką“ ir „rungtynių“ atitiko antraštės turinį, tačiau toje pačioje temoje liko ir saugumo spragų žodžių. H254 didžiausias temos svoris sumažėjo nuo 0,936 iki 0,916, o priskirtoje temoje finansiniai žodžiai vis dar maišėsi su sporto žodžiais. Šie pokyčiai vertinami kaip viso C bandymo rezultatas, o ne kaip įrodytas vienos frazės poveikis.

Iš H1189 pašalinus „analitikų teigimu“, buvo prarasta informacija, kam priskiriamas teiginys. Didžiausias temos svoris sumažėjo nuo 0,924 iki 0,907. Priskirtos C modelio temos svarbiausi žodžiai nebuvo aiškiai susiję su antraštės mašininio mokymosi turiniu.

B ir C bandymuose naudoti tie patys 1 500 dokumentų, 6 temos, `random_state=42`, `max_iter=15`, `learning_method="batch"` ir vienodi vektorizavimo nustatymai. Pakeistas tik sprendimas dėl penkių pasirinktų šabloninių frazių šalinimo. Žodynas sudarytas iš naujo, todėl jo dydis galėjo pasikeisti. Bendras temų aiškumo pagerėjimas nebuvo pakankamai pagrįstas rezultatais. Todėl paliktas originalus B modelio teksto paruošimas. Poveikiui įvertinti palygintos H254 ir H370 antraštės, kuriose buvo ta pati frazė „dėl rinkos reakcijos“, nors jų turinys skirtingas: centrinio banko sprendimas ir trenerio taktika. Taip pat nagrinėta H1189 antraštė, iš kurios pašalinta frazė „analitikų teigimu“, siekiant įvertinti informacijos apie teiginio šaltinį praradimą.

## 3. Final model and failure analysis
### Palyginimas su pradine analize

| Antraštė| Pradinis vertinimas | B modelio rezultatas | Sutapimo arba nesutapimo paaiškinimas 
| --- | --- | --- | --- |
| H736: „78 Kaip pagreitinti kompiuterį paprastais triukais“ | tech | 5 tema, svoris 0,881 | Dalinis sutapimas: temos žodžiai „kompiuterį“, „triukais“ ir mašininio mokymosi terminai siejasi su technologijomis. Tačiau temai taip pat priskiriamos finansų antraštės, todėl tai nėra aiški technologijų grupė.|
| H696: „31 Atviro kodo bibliotekos pagreitina mašininio mokymosi procesus“ | tech| 3 tema, svoris 0,907 | Dalinis sutapimas: svarbiausi žodžiai „bibliotekos“, „mokymosi“, „mašininio“ ir „atviro“ atitinka turinį. Vis dėlto tema maišoma su clickbait žodžiais „trick“, „forever“ ir „life“.|
| H1413: „19 Ji padarė X — kas nutiks toliau, pribloškia“ | celebrity | 3 tema, svoris 0,896 | Pradinis įžymybių priskyrimas nepakankamai pagrįstas, nes neįvardytas nei asmuo, nei įvykis. Modelio temoje yra clickbait požymių, tačiau ji taip pat apima mašininį mokymąsi. Nei pradinis vertinimas, nei modelio rezultatas nesuteikia patikimos naujienos turinio kategorijos.|

Pradinis vertinimas naudotas kaip palyginimo pagrindas, o ne kaip teisingų klasių rinkinys. 

### Trys nesėkmių atvejai

| Antraštės ID ir tekstas| B modelio rezultatas | Kodėl rezultatas netinka redaktoriui | Galimas sprendimas arba neaiškumas |
| --- | --- | --- | --- |
| H436: „2 Perėjimų gandai: jaunas puolėjas gali kainuoti rekordą“ | 4 tema, svoris 0,896. Tarp svarbiausių temos žodžių: `gadget`, `buy`, `spraga`, `saugumo`. | Sporto antraštė priskirta mišriai temai, kurios svarbiausi žodžiai siejasi su įrenginiais ir saugumo spragomis. Tokia grupė nepadeda redaktoriui atskirti sporto naujienų. | Galima būtų tikrinti žodžių junginių, pavyzdžiui, „jaunas puolėjas“, naudojimą. |
| H1482: „40 Analysts predict record profits for the banking sector“ | 6 tema, svoris 0,895. Tarp svarbiausių temos žodžių: `analysts`, `york`, `coach`, `tactics`, `messi`.| Antraštė apie bankų pelną priskirta temai su sporto ir kitais žodžiais. Aiški finansų naujienų grupė nesudaryta.| Galima papildomai tirti bendrinių žodžių ir vietovardžių įtaką. Iš šio rezultato negalima nustatyti, kuris žodis nulėmė priskyrimą. |
| H1413: „19 Ji padarė X — kas nutiks toliau, pribloškia“ | 3 tema, svoris 0,896. Tarp svarbiausių temos žodžių: `trick`, `life`, `forever`, `mašininio`, `mokymosi`.| Antraštėje neįvardytas nei asmuo, nei įvykis, todėl tikroji naujienos tema neaiški. Priskirta tema taip pat maišo clickbait ir mašininį mokymąsi. | Reikalingas straipsnio tekstas arba redaktoriaus vertinimas. Galima atpažinti clickbait stilių, tačiau vien iš antraštės patikimai nustatyti turinio temos negalima. |

Nustatytos bent dvi skirtingos problemos: nesusijusių turinio sričių sujungimas į mišrias temas ir informacijos trūkumas pačioje antraštėje. Visais trimis atvejais didžiausias temos svoris yra apie 0,90, tačiau tai negarantuoja redaktoriui naudingo priskyrimo.


## 4. Recommendation

Galutiniam vertinimui pasirinktas B modelis: 6 temos su originaliu teksto paruošimu. Priimtas kompromisas — galimybė išskirti siauresnes kryptis, nors temos išlieka persidengiančios ir mišrios. C bandymas neparodė pakankamai aiškios naudos, kuri pagrįstų pasirinktų frazių pašalinimą. B modelio temų pavadinimai, svarbiausi žodžiai ir po dvi reprezentatyvias antraštes pateikti A priede. 

### Rekomendacija redaktoriui

Modelio nerekomenduojama naudoti savarankiškam antraščių paskirstymui. Jį būtų galima išbandyti kaip pagalbinį grupavimo įrankį, tačiau redaktoriaus patikra būtų reikalinga mišrioms temoms ir neinformatyvioms antraštėms. Didelis temos svoris nėra prasmingo priskyrimo garantija. Šis mokomasis rinkinys turi trumpų, pasikartojančių, šabloninių ir skirtingų kalbų antraščių. Todėl rezultatai neįrodo, kad modelis taip pat veiktų su naujomis realiomis naujienomis.

## 5. Sources and AI use

Naudotos dėstytojo pateiktos Laboratory 1 gairės ir `scikit-learn` dokumentacija apie `CountVectorizer` bei `LatentDirichletAllocation`. Išorinis kodas į projektą nekopijuotas.

Kodo paaiškinimams, ataskaitos struktūrai ir kalbos redagavimui naudoti ChatGPT ir Gemini. Rezultatai patikrinti vietiškai paleidus `prepare_data.py` ir `modeling.py`; ataskaitoje pateikti skaičiai, temos ir svoriai sutikrinti su programos išvestimi.

Vienas AI pasiūlymas buvo per daug kategoriškas: H370 svorio padidėjimas C modelyje buvo laikytas aiškiu pagerėjimu. Tai pataisyta, nes H254 ir H370 jau buvo skirtingose B modelio temose, o C bandyme vienu metu pašalintos penkios frazės ir modelis mokytas iš naujo. Todėl vien iš šio pokyčio negalima spręsti apie vienos frazės poveikį. Pradinė 20 antraščių interpretacija atlikta be AI pagalbos.

## A priedas. Galutinio B modelio temos

Kiekvienai temai pateikti 10 svarbiausių žodžių ir dvi antraštės, turinčios didžiausius tos temos svorius. Pavadinimai suteikti įvertinus žodžius ir antraštes. Didelis temos svoris negarantuoja prasmingos turinio grupės.

### 1 tema — „Apple“ ir finansų rinkos (mišri)

**Žodžiai:** amid, concerns, inflation, apple, iphone, new, stock, falls, market, ai.

**H148 | 0,951:** 90 „Apple“ pristatė naują iPhone su pažangia kamera ir DI funkcijomis dėl rinkos reakcijos (New York)
**H806 | 0,944:** 69 „Apple“ pristatė naują iPhone su pažangia kamera ir DI funkcijomis as markets react (Berlin)

Abu pavyzdžiai susiję su „Apple“, tačiau svarbiausiuose žodžiuose matomi ir finansų rinkų bei šabloninių frazių požymiai.

### 2 tema — Verslo pajamos, sportas ir clickbait (mišri)

**Žodžiai:** won, believe, po, earnings, segment, revenue, grows, expectations, cloud, beat.

**H1156 | 0,930:** 72 Treneris aiškino naują gynybos taktiką po rungtynių po pranešimo (Kaunas)
**H815 | 0,930:** Earnings beat expectations as revenue grows in cloud segment dėl rinkos reakcijos (Kaunas)

Reprezentatyvios antraštės apima trenerio taktiką ir įmonės pajamas, todėl vienos aiškios turinio temos nustatyti negalima.

### 3 tema — Mašininis mokymasis, saugumas ir clickbait (mišri)

**Žodžiai:** trick, life, forever, change, procesus, bibliotekos, mokymosi, mašininio, atviro, pagreitina.

**H11 | 0,930:** 54 Major security breach affects millions of users worldwide po pranešimo (Paris)
**H1189 | 0,924:** 40 Atviro kodo bibliotekos pagreitina mašininio mokymosi procesus analitikų teigimu

Mašininio mokymosi terminai maišomi su clickbait žodžiais, o tarp reprezentatyvių antraščių yra ir saugumo spragos atvejis.

### 4 tema — Įrenginiai ir saugumas su nesusijusiais pavyzdžiais (neaiški)

**Žodžiai:** 10, gadget, buy, reasons, 50, spraga, didelė, milijonus, saugumo, paveikė.

**H713 | 0,936:** 28 Perėjimų gandai: jaunas puolėjas gali kainuoti rekordą dėl rinkos reakcijos (Vilnius)
**H235 | 0,930:** 20 Start-up raises $50 million to scale its AI platform dėl rinkos reakcijos

Svarbiausi žodžiai siejasi su įrenginiais ir saugumu, tačiau pavyzdžiai apima futbolo perėjimus ir DI startuolio finansavimą. Tema pažymėta kaip neaiški.

### 5 tema — Atviras kodas, kompiuteriai ir finansai (mišri)

**Žodžiai:** markets, learning, libraries, accelerate, open, source, machine, workflows, triukais, kompiuterį.

**H254 | 0,936:** 32 Central bank cuts rates, markets rally on dovish guidance dėl rinkos reakcijos
**H926 | 0,930:** 78 Open-source libraries accelerate machine learning workflows analitikų teigimu (Madrid)

Žodžiuose ryški technologijų kryptis, tačiau vienas reprezentatyvus pavyzdys susijęs su centrinio banko sprendimu. Finansai ir technologijos nėra aiškiai atskirti.

### 6 tema — Sportas ir startuolių finansavimas (mišri)

**Žodžiai:** new, analysts, york, tactics, coach, game, explains, defensive, 50, messi.

**H1014 | 0,936:** Startuolis pritraukė 50 mln. USD DI platformos plėtrai analitikų teigimu (New York) 
**H1397 | 0,930:** 94 Startuolis pritraukė 50 mln. USD DI platformos plėtrai (New York)

Svarbiausiuose žodžiuose yra sporto terminų, tačiau abu reprezentatyvūs pavyzdžiai susiję su startuolio finansavimu. Taip pat matomas vietovardis „New York“, todėl tema neturi vienos aiškios turinio krypties.
