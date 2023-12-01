class NotesBook:
    
    def __init__(self, path: str ='notes_book.txt') -> None:
        self.notes_book: list[dict[str, str]] = []
        self.path = path
        self.last_id = 0
    
    
    def open(self):
        with open (self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for note in data:
            note = note.strip().split('.')
            new = {'id': note[0], 'text_note':note[1]}
            self.notes_book.append(new) 

    def save(self):
        data = []
        for note in self.notes_book:
            note = ':'.join([value for value in note.values()])
            data.append(note)
        with open (self.path, 'w', encoding='UTF-8') as file:
            file.write('\n'.join(data))   

    def load(self) -> list[dict[str, str]]:
        return self.notes_book

    def add(self, new: dict[str, str]):
        self.last_id += 1
        new['id'] = str(self.last_id)
        self.notes_book.append(new)
        return new.get('text_note')

    def find(self, index: int) -> list[dict[str, str]]:
        result: list[dict[str, str]] = []
        for note in self.notes_book:
            if index == note.get('id'):
                result = {'id': note[0], 'text_note':note[1]}
                break
        return result
    
    def change(self, new: dict, index: int) -> str:
        for note in self.notes_book:
            if index == note.get('id'):
                note['text_notes'] = new.get('text_notes', note.get('text_notes'))                   
                return note.get('text_note')
    
    def delete(self, index: int):
        return self.notes_book.pop(index-1).get('text_note')
