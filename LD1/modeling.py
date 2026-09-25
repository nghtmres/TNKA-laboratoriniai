from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from prepare_data import corpus, initial_20

# Sukuriama atrinktų žodžių matrica
vectorizer = CountVectorizer(
    lowercase=True,
    stop_words="english",
    max_features=3000,
    min_df=2
)

document_term_matrix = vectorizer.fit_transform(corpus["text"])

print("Matricos dydis:", document_term_matrix.shape)
print("Žodyno dydis:", len(vectorizer.get_feature_names_out()))

empty_documents = (
    document_term_matrix.getnnz(axis=1) == 0
).sum()

print("Dokumentų be išlikusių terminų:", empty_documents)

# Apmokomas LDA modelis (4 temos, 15 iteraciju, random set seed)
lda_4 = LatentDirichletAllocation(
    n_components=4,
    max_iter=15,
    learning_method="batch",
    random_state=42
)

lda_4.fit(document_term_matrix)

feature_names = vectorizer.get_feature_names_out()

# sort and display top 10 words for each topic
for topic_number, topic in enumerate(lda_4.components_):
    top_indices = topic.argsort()[-10:][::-1]
    top_words = [feature_names[i] for i in top_indices]

    print(
        f"4 temų modelis – tema {topic_number + 1}:",
        ", ".join(top_words)
    )

# Apmokomas antras LDA modelis su 6 temomis
lda_6 = LatentDirichletAllocation(
    n_components=6,
    max_iter=15,
    learning_method="batch",
    random_state=42
)

lda_6.fit(document_term_matrix)

# Parodomi 10 svarbiausių kiekvienos temos žodžių
for topic_number, topic in enumerate(lda_6.components_):
    top_indices = topic.argsort()[-10:][::-1]
    top_words = [feature_names[i] for i in top_indices]

    print(
        f"6 temų modelis – tema {topic_number + 1}:",
        ", ".join(top_words)
    )

document_topics_4 = lda_4.transform(document_term_matrix)
document_topics_6 = lda_6.transform(document_term_matrix)

print(
    "Pirmos antraštės 4 temų svoriai:",
    document_topics_4[0]
)

print(
    "Pirmos antraštės 6 temų svoriai:",
    document_topics_6[0]
)

print("\nReprezentatyvios 4 temų modelio antraštės:")

for topic_number in range(4):
    top_documents = document_topics_4[:, topic_number].argsort()[-2:][::-1]

    print(f"\nTema {topic_number + 1}:")

    for document_index in top_documents:
        headline_id = corpus.iloc[document_index]["headline_id"]
        headline = corpus.iloc[document_index]["text"]
        weight = document_topics_4[document_index, topic_number]

        print(f"{headline_id} | {weight:.3f} | {headline}")

print("\nReprezentatyvios 6 temų modelio antraštės:")

for topic_number in range(6):
    top_documents = document_topics_6[:, topic_number].argsort()[-2:][::-1]

    print(f"\nTema {topic_number + 1}:")

    for document_index in top_documents:
        headline_id = corpus.iloc[document_index]["headline_id"]
        headline = corpus.iloc[document_index]["text"]
        weight = document_topics_6[document_index, topic_number]

        print(f"{headline_id} | {weight:.3f} | {headline}")


# Trečias bandymas: pašalinamos pasikartojančios šabloninės frazės
template_phrases = [
    "dėl rinkos reakcijos",
    "po pranešimo",
    "analitikų teigimu",
    "as markets react",
    "amid concerns"
]

changed_texts = corpus["text"].copy()

for phrase in template_phrases:
    changed_texts = changed_texts.str.replace(
        phrase,
        "",
        case=False,
        regex=False
    )

# Sutvarkomi po frazių pašalinimo likę tarpai
changed_texts = (
    changed_texts
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)

# Naudojami tokie patys vektorizavimo nustatymai
changed_vectorizer = CountVectorizer(
    lowercase=True,
    stop_words="english",
    max_features=3000,
    min_df=2
)

changed_matrix = changed_vectorizer.fit_transform(changed_texts)

print("\nTrečias bandymas – pašalintos šabloninės frazės")
print("Matricos dydis:", changed_matrix.shape)
print(
    "Žodyno dydis:",
    len(changed_vectorizer.get_feature_names_out())
)

changed_empty_documents = (
    changed_matrix.getnnz(axis=1) == 0
).sum()

print(
    "Dokumentų be išlikusių terminų:",
    changed_empty_documents
)

# Tas pats 6 temų LDA modelis ir tie patys nustatymai
lda_6_changed = LatentDirichletAllocation(
    n_components=6,
    max_iter=15,
    learning_method="batch",
    random_state=42
)

lda_6_changed.fit(changed_matrix)

changed_feature_names = (
    changed_vectorizer.get_feature_names_out()
)

# Parodomi svarbiausi pakeisto modelio žodžiai
for topic_number, topic in enumerate(lda_6_changed.components_):
    top_indices = topic.argsort()[-10:][::-1]
    top_words = [
        changed_feature_names[i] for i in top_indices
    ]

    print(
        f"Pakeistas 6 temų modelis – tema {topic_number + 1}:",
        ", ".join(top_words)
    )

# Gaunami dokumentų temų svoriai
changed_document_topics = lda_6_changed.transform(changed_matrix)

# Parodomos reprezentatyvios antraštės
print("\nReprezentatyvios pakeisto modelio antraštės:")

for topic_number in range(6):
    top_documents = (
        changed_document_topics[:, topic_number]
        .argsort()[-2:][::-1]
    )

    print(f"\nTema {topic_number + 1}:")

    for document_index in top_documents:
        headline_id = corpus.iloc[document_index]["headline_id"]
        headline = changed_texts.iloc[document_index]
        weight = changed_document_topics[
            document_index,
            topic_number
        ]

        print(
            f"{headline_id} | {weight:.3f} | {headline}"
        )


# Tų pačių antraščių palyginimas prieš ir po pakeitimo
comparison_ids = ["H254", "H370", "H1189"]

print("\nKonkrečių antraščių palyginimas:")

for headline_id in comparison_ids:
    matches = corpus.index[corpus["headline_id"] == headline_id]

    if len(matches) == 0:
        print(f"\n{headline_id} nerasta")
        continue

    document_index = matches[0]

    original_topic = (
        document_topics_6[document_index].argmax() + 1
    )
    original_weight = (
        document_topics_6[document_index].max()
    )

    changed_topic = (
        changed_document_topics[document_index].argmax() + 1
    )
    changed_weight = (
        changed_document_topics[document_index].max()
    )

    print(f"\n{headline_id}")
    print("Prieš:", corpus.iloc[document_index]["text"])
    print(
        f"Originalus modelis: tema {original_topic}, "
        f"svoris {original_weight:.3f}"
    )

    print("Po:", changed_texts.iloc[document_index])
    print(
        f"Pakeistas modelis: tema {changed_topic}, "
        f"svoris {changed_weight:.3f}"
    )


print("\nPradinių 20 antraščių rezultatai — B modelis:")

for document_index, row in initial_20.iterrows():
    weights = document_topics_6[document_index]
    topic_index = weights.argmax()

    top_indices = (
        lda_6.components_[topic_index]
        .argsort()[-10:][::-1]
    )
    top_words = [feature_names[i] for i in top_indices]

    print(f"\n{row['headline_id']} | {row['text']}")
    print(
        f"Tema: {topic_index + 1} | "
        f"Svoris: {weights[topic_index]:.3f}"
    )
    print("Temos žodžiai:", ", ".join(top_words))




# B modelio temų pavadinimai suteikti rankiniu būdu,
# įvertinus svarbiausius žodžius ir reprezentatyvias antraštes.
# Tai nėra automatiškai modelio sukurti pavadinimai.
b_topic_names = [
    "„Apple“ ir finansų rinkos (mišri)",
    "Verslo pajamos, sportas ir clickbait (mišri)",
    "Mašininis mokymasis, saugumas ir clickbait (mišri)",
    "Įrenginiai ir saugumas su nesusijusiais pavyzdžiais (neaiški)",
    "Atviras kodas, kompiuteriai ir finansai (mišri)",
    "Sportas ir startuolių finansavimas (mišri)"
]

# 5 užduotis: naujų antraščių analizė su B modeliu
# Naudojami jau apmokyti B modelio vectorizer ir lda_6.

print("\nNaujų antraščių analizė. Tuščia eilutė — baigti.")

while True:
    headline = input("\nĮveskite naują antraštę: ").strip()

    if headline == "":
        break

    prediction = input(
        "Jūsų prognozuojama tema arba neaiškumas: "
    ).strip()

    # transform() naudoja jau anksčiau sudarytą 313 terminų žodyną.
    new_matrix = vectorizer.transform([headline])

    # nnz parodo, kiek matricos reikšmių yra nelygios nuliui.
    # Jeigu nnz == 0, antraštėje nebuvo nė vieno B modelio žodyno termino.
    if new_matrix.nnz == 0:
        print("Jūsų prognozė:", prediction)
        print(
            "Antraštėje nėra žodyno terminų. "
            "Prasmingam priskyrimui nepakanka informacijos."
        )
        continue

    # Parodoma, kuriuos antraštės žodžius atpažino senasis žodynas.
    retained_indices = new_matrix.nonzero()[1]
    retained_terms = feature_names[retained_indices]

    print(
        "Atpažinti žodyno terminai:",
        ", ".join(retained_terms)
    )

    # transform() apskaičiuoja naujos antraštės svorį kiekvienai jau apmokyto B modelio temai.
    weights = lda_6.transform(new_matrix)[0]

    print("Jūsų prognozė:", prediction)
    print("\nVisų temų svoriai:")

    for topic_number, weight in enumerate(weights, start=1):
        topic_name = b_topic_names[topic_number - 1]
        print(
            f"Tema {topic_number} – {topic_name}: "
            f"{weight:.3f}"
        )

    best_topic_index = weights.argmax()
    best_topic_number = best_topic_index + 1
    best_topic_name = b_topic_names[best_topic_index]

    print(
        f"Didžiausio svorio tema: {best_topic_number} – "
        f"{best_topic_name}"
    )