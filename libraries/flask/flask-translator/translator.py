from abc import ABC, abstractmethod

# Interface equivalent in Python
class TranslatorService(ABC):
    @abstractmethod
    def translate(self, word):
        pass


# Implementation for German translation
class TranslatorServiceGerman(TranslatorService):
    def translate(self, word):
        translations = {"hello":"Hallo", "world":"Welt", "cat":"Katze", "mouse":"Maus", "horse":"Pferd"}
        return translations.get(word.lower(), f"Keine Übersetzung für '{word}' gefunden.")


# Implementation for French translation
class TranslatorServiceFrench(TranslatorService):
    def translate(self, word):
        translations = {"hello": "Bonjour", "world": "Monde", "cat":"Chatte", "mouse":"Souris", "horse":"Cheval"}
        return translations.get(word.lower(), f"Aucune traduction trouvée pour '{word}'.")
