from dataclasses import dataclass, field


class OldPerson:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def __repr__(self):
        class_str = f'{self.__class__.__name__}' \
                   f'({self.name} {self.lastname})'
        return class_str

    def __eq__(self, other):
        return self.lastname == other.lastname


@dataclass
class Person:
    name: str
    lastname: str
    active: bool = False
    addresses: list =field(default_factory=list, repr=False)
    full_name: str = field(default='Missing', init=True)

    def __post_init__(self):
        self.full_name = self.name + ' ' + self.lastname

if __name__ == '__main__':
    john1 = Person('John', 'Doe')
    john1.active = True
    print(john1)
