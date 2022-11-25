import dataclasses


@dataclasses.dataclass
class Message:
    message: str
    name: str
    age: int
