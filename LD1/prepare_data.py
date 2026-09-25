import pandas as pd

df = pd.read_csv("headlines_train.csv")
print("Pradinių eilučių:", len(df))

#sutvarkomas tekstas
df["text"] = df["text"].str.strip()
df = df.dropna(subset=["text"])
df = df[df["text"] != ""]
print("Po tuščių pašalinimo:", len(df))

df = df.drop_duplicates(subset=["text"])
print("Po dublikatų pašalinimo:", len(df))

corpus = df.sample(n=1500, random_state=42).reset_index(drop=True)
print("Modeliavimo rinkinio dydis:", len(corpus))

corpus["headline_id"] = [
    "H" + str(i + 1) for i in range(len(corpus))
]

initial_20 = corpus.sample(n=20, random_state=43)

print(initial_20[["headline_id", "text"]].to_string(index=False))