import sys

class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

class Notepad:
    def __init__(self, data):
        self.sheet = []
        self.load(data)

    def load(self, data):
        lines = data.split('\n')
        for line in lines:
            self.sheet.append(list(line))

    def insert_at_index(self, index, data):
        self.sheet.insert(index, list(data))

    def insert(self, data):
        self.sheet.append(list(data))

    def edit(self, index):
        if 0 <= index < len(self.sheet):
            return self.sheet[index]
        return None

    def list_to_string(self, temp=None):
        if temp is None:
            return ''.join(self.sheet[-1]) if self.sheet else ''
        return ''.join(temp)

class FrontEnd:
    def __init__(self, data):
        self.note = Notepad(data)
        self.menu = ["Insert a Line","Edit a Line","Delete a Line","Replace a Line"]
        self.EditedIndex = -1

    def menu_print(self):
        for i, item in enumerate(self.menu, 1):
            print(f"{i}. {item}")
        select = input("Select: ")
        return select

    def lines_print(self):
        for idx, line in enumerate(self.note.sheet, 1):
            print(f"{idx}: {''.join(line)}")

    def line_get(self):
        return input("Enter line: ")

    def edit(self):
        self.lines_print()
        idx = int(input("Select line to edit: ")) - 1
        if 0 <= idx < len(self.note.sheet):
            new_line = input("Edit line: ")
            self.note.sheet[idx] = list(new_line)

    def delete(self):
        self.lines_print()
        idx = int(input("Select line to delete: ")) - 1
        if 0 <= idx < len(self.note.sheet):
            del self.note.sheet[idx]

    def replace(self):
        self.lines_print()
        x = int(input("Enter line number 1: ")) - 1
        y = int(input("Enter line number 2: ")) - 1
        if 0 <= x < len(self.note.sheet) and 0 <= y < len(self.note.sheet):
            self.note.sheet[x], self.note.sheet[y] = self.note.sheet[y], self.note.sheet[x]

    def driver(self):
        while True:
            self.lines_print()
            select = self.menu_print()
            if select == "1":
                self.note.insert(self.line_get())
            elif select == "2":
                self.edit()
            elif select == "3":
                self.delete()
            elif select == "4":
                self.replace()
            else:
                print("Invalid selection.")

if __name__ == "__main__":
    f = FrontEnd("ALi is a good boy\n")
    f.driver()
