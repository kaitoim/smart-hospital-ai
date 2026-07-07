from backend.vector_store import VectorStore


class KnowledgeBase:

    
    PRIORITY_TIE_MARGIN = 0.05

    def __init__(self):

        self.vector = VectorStore()

    def search(self, question):

        results = self.vector.search(question)

        if not results:
            return None

 
        results.sort(key=lambda x: -x["score"])

        best = results[0]


        close_candidates = [
            r for r in results
            if best["score"] - r["score"] <= self.PRIORITY_TIE_MARGIN
        ]


        close_candidates.sort(
            key=lambda x: (
                x["priority"],
                -x["score"]
            )
        )

        return close_candidates[0]