from datasets import load_dataset

if __name__ == "__main__":
    xsum = load_dataset("xsum")
    subset = xsum["train"].select(range(100))

    ids = subset["id"]
    for doc_id, doc in zip(ids, subset["document"]):
        with open(f"cache/xsum/raw/{doc_id}.txt", "w") as f:
            f.write(doc)
    
    with open(f"cache/xsum/raw/index.txt", "w") as f:
            f.write("\n".join([doc_id + ".txt" for doc_id in ids]))