from transformers import RobertaConfig, RobertaModel, RobertaTokenizer

model = RobertaModel.from_pretrained("roberta-base")
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
tokenized = tokenizer(
    "Germany (German: Deutschland, German pronunciation: [ˈdɔʏtʃlant]), officially the Federal Republic of Germany (German: Bundesrepublik Deutschland, About this soundlisten),[e] is a country in Central and Western Europe.",
    return_tensors="pt"
)

# I have absolutely no idea how to read it
print(tokenized["input_ids"])
outputs = model(**tokenized)
print(outputs)