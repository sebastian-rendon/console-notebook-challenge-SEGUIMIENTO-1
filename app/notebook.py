from datetime import datetime


class Note:
    HIGH: str = "HIGH"
    MEDIUM: str = "MEDIUM"
    LOW: str = "LOW"

    def __init__(self, code: str, title:str, text: str, importance: str)
        self.code : str = code
        self.title : str = title
        self.text: str = text
        self.importance: str = importance
        self.creation_date: datetime = datetime.now()
        self.tags: list[str] = []

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
        return f"Date: {self.creation_date} {self.title}: {self.text}"


class Notebook:
    def __init__(self):
        self.notes: list[Note] = []

    def add_note(self, title: str, text: str, importance: str) -> int:
        code = len(self.notes) + 1
        new_note = Note(code, title, text, importance)
        self.notes.append(new_note)
        return code

    def delete_note(self, code: int):
        self.notes = [note for note in self.notes if note.code != code]

    def important_notes(self):
        return [note for note in self.notes if note.importance in {Note.HIGH, Note.MEDIUM}]

    def notes_by_tag(self, tag: str):
        return [note for note in self.notes if tag in note.tags]
















