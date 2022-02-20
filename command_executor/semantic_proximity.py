from typing import List, Tuple, Iterable

from sentence_transformers import SentenceTransformer, util

from helpers.text_helper import clean_phrase
from helpers.meta_singleton import MetaSingleton


class Embedding:
    def __init__(self, sentence: str, embedding: List[float]):
        self.sentence = sentence
        self.embedding = embedding

    def get_cos_distance(self, other: 'Embedding') -> float:
        return 1 - float(util.pytorch_cos_sim(self.embedding, other.embedding))

    def __str__(self) -> str:
        return self.sentence


class SemanticController(metaclass=MetaSingleton):
    def __init__(self):
        self._model = SentenceTransformer('distiluse-base-multilingual-cased')

    def get_embedding(self, sent: str) -> Embedding:
        return Embedding(sent, self._model.encode(clean_phrase(sent)))

    @staticmethod
    def get_closest(pattern: Embedding, sentences: Iterable[Embedding]) -> Tuple[Embedding, float]:
        return min(
            [(sentence, pattern.get_cos_distance(sentence)) for sentence in sentences],
            key=lambda x: x[1]
        )
