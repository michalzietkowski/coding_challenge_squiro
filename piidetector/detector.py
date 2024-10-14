from commonregex import CommonRegex
import spacy
from helpers import base_64_encoding
from bidict import bidict

from piidetector.models import InputData


class Detector:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.masked_data = bidict()

    def process(self, input_data: InputData) -> tuple:
        """Process both 'prompt' and 'context' and return masked versions."""
        masked_prompt = self._process_text(input_data.prompt)
        masked_context = self._process_text(input_data.context)
        return masked_prompt, masked_context

    def _process_text(self, text: str) -> str:
        """A helper method to process and mask individual text strings."""
        pii_data = self.find_pii_data(text=text)
        return self.mask_data(pii_data, text)

    def find_pii_data(self, text: str) -> set:
        pii_data_llm = self.find_pii_data_from_llm(text)
        pii_data_regex = self.find_pii_data_from_regexes(text)
        return pii_data_llm.union(pii_data_regex)

    def find_pii_data_from_llm(self, text: str) -> set:
        pii_data = set()
        doc = self.nlp(text)
        for entity in doc.ents:
            pii_data.add(entity.text)
        return pii_data

    @staticmethod
    def find_pii_data_from_regexes(text: str) -> set:
        pii_data = set()
        common_regex_detector = CommonRegex(text)
        common_regex_attributes = vars(common_regex_detector)
        for key, value in common_regex_attributes.items():
            if isinstance(value, list) and value:
                pii_data.update(value)
        return pii_data

    def mask_data(self, pii_data: set, text: str) -> str:
        for document in pii_data:
            if document not in self.masked_data:
                self.masked_data[document] = base_64_encoding(document)
            text = text.replace(document, self.masked_data[document])
        return text

    def demask_data(self, text: str) -> str:
        for encoded_text, original_text in self.masked_data.inverse.items():
            text = text.replace(encoded_text, original_text)
        return text
