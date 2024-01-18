from abc import ABC, abstractmethod
import random
import string


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


def RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 8, include_numbers: bool = False, include_symbols: bool = False)
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

    def generate(self):
        return ''.join([random.choice(self.characters) for _ in range(self.length)])


class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self, num_of_words: int = 6, separator: str = '-', capitalize: bool = False, vocabulary: list = None):
        if vocabulary is None:
            self.vocabulary = ['amir', 'mamad', 'mohamad', 'sarina', 'nika', 'elahe', 'niloofar', 'azarakhsh', 'hamidreza']

        self.num_of_words = num_of_words
        self.separator = separator
        self.capitalize = capitalize


    def generate(self):
        password_words = [random.choice(self.vocabulary) for _ in range(self.num_of_words)]
        if self.capitalize:
            password_words = [word.upper() if random.choice([True, False]) else word.lower() for word in self.vocabulary]

        return self.separator.join(password_words)


class PinGenerator(PasswordGenerator):
    def __init__(self, length):
        self.length = length

    def generate(self):
        return ''.join([random.choice(string.digits) for _ in range(self.length)])


if __name__ == '__main__':
    pin_pass = PinGenerator(length=10)
    pin_pass.generate()
