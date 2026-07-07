import json
import os

import faiss

from sentence_transformers import SentenceTransformer


class VectorStore:

    def __init__(self):

        base_dir = os.path.dirname(os.path.dirname(__file__))

        self.knowledge_path = os.path.join(
            base_dir,
            "data",
            "knowledge.json"
        )

        self.model = SentenceTransformer(
            "paraphrase-multilingual-MiniLM-L12-v2"
        )

        with open(
            self.knowledge_path,
            encoding="utf8"
        ) as f:

            self.data = json.load(f)

        self.build_index()

    def build_index(self):

        documents = []

        for item in self.data:

            category = item.get("category", "")

            keywords = " ".join(
                item.get("keywords", [])
            )

            related = " ".join(
                item.get("related", [])
            )

            answer = item.get("answer", "")

            text = f"{category} {keywords} {related} {answer}".strip()

            documents.append(text)

        embeddings = self.model.encode(
            documents,
            convert_to_numpy=True
        )

        faiss.normalize_L2(embeddings)

        self.index = faiss.IndexFlatIP(
            embeddings.shape[1]
        )

        self.index.add(embeddings)

    def search(
        self,
        question,
        top_k=3,
        threshold=0.42
    ):

        query = self.model.encode(
            [question],
            convert_to_numpy=True
        )

        faiss.normalize_L2(query)

        scores, ids = self.index.search(
            query,
            top_k
        )

        results = []

        for score, idx in zip(
            scores[0],
            ids[0]
        ):

            if idx == -1:
                continue

            if score < threshold:
                continue

            item = self.data[idx].copy()

            item["score"] = float(score)

            results.append(item)

        return results