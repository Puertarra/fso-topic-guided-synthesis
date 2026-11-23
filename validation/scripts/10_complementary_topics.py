"""Assign complementary-search studies to the original BERTopic topics via c-TF-IDF similarity.

The fitted BERTopic model is no longer available, so each new document is assigned to the topic
whose class-based TF-IDF (c-TF-IDF) representation, computed from the original topic assignments
of the 145 modelled documents, is most similar (cosine). c-TF-IDF follows BERTopic:
W[t,c] = tf[t,c] / sum_t tf[t,c] * log(1 + A / f_t), with A the mean number of words per class.
The procedure is checked by leave-one-out on the 145 documents.
Usage: python ctfidf_assign.py <topics_documents.pkl> <seven_text.json> <out_dir>
"""
import json, sys
from pathlib import Path
import numpy as np, pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

pkl, seven, out = sys.argv[1], sys.argv[2], Path(sys.argv[3]); out.mkdir(exist_ok=True)
d = pd.read_pickle(pkl)[["Document", "Topic", "Mistral"]].reset_index(drop=True)
new = json.load(open(seven))
cv = CountVectorizer(stop_words="english", min_df=2)
X = cv.fit_transform(d.Document).toarray().astype(float)
topics = sorted(d.Topic.unique())
names = {t: str(d[d.Topic == t].Mistral.iloc[0]).strip("[]").split("'")[1] for t in topics}

def class_matrix(mask):
    tf = np.vstack([X[(d.Topic == t).values & mask].sum(0) for t in topics])
    A = tf.sum(1).mean(); f = tf.sum(0)
    idf = np.log(1 + A / np.maximum(f, 1))
    W = tf / np.maximum(tf.sum(1, keepdims=True), 1) * idf
    return W / np.maximum(np.linalg.norm(W, axis=1, keepdims=True), 1e-12), idf

def score(vec, W, idf):
    v = vec / max(vec.sum(), 1) * idf
    return W @ (v / max(np.linalg.norm(v), 1e-12))

# leave-one-out on the 145 modelled documents
hits, hits_nonoise = 0, []
for i in range(len(d)):
    m = np.ones(len(d), bool); m[i] = False
    W, idf = class_matrix(m)
    s = score(X[i], W, idf)
    best = topics[int(np.argmax(s))]
    hits += best == d.Topic[i]
    if d.Topic[i] != -1:
        cand = [j for j, t in enumerate(topics) if t != -1]
        hits_nonoise.append(topics[cand[int(np.argmax(s[cand]))]] == d.Topic[i])
loo_all, loo_nn = hits / len(d), float(np.mean(hits_nonoise))

W, idf = class_matrix(np.ones(len(d), bool))
rows = []
for key, rec in new.items():
    for rep, text in (("title+abstract+conclusions", rec["text"]), ("title+abstract", rec["ta"])):
        s = score(cv.transform([text]).toarray()[0].astype(float), W, idf)
        order = np.argsort(-s)
        nn = [j for j in order if topics[j] != -1]
        rows.append({"study": key, "representation": rep,
                     "topic": topics[nn[0]], "topic_name": names[topics[nn[0]]], "similarity": round(float(s[nn[0]]), 3),
                     "second_topic": topics[nn[1]], "second_similarity": round(float(s[nn[1]]), 3),
                     "margin": round(float(s[nn[0]] - s[nn[1]]), 3),
                     "outlier_class_similarity": round(float(s[topics.index(-1)]), 3)})
res = pd.DataFrame(rows); res.to_csv(out / "complementary_topics.csv", index=False)
summary = [f"Leave-one-out on 145 modelled documents: original topic recovered for {loo_all:.1%} (all classes incl. -1), "
           f"{loo_nn:.1%} of the {len(hits_nonoise)} non-outlier documents (outlier class excluded).",
           f"Vocabulary: {X.shape[1]} terms (English stop words removed, min_df=2)."]
(out / "complementary_topics_summary.txt").write_text("\n".join(summary) + "\n")
print("\n".join(summary)); print(res.to_string(index=False))
