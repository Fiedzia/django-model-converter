import os


class Root:
    """
    Top-level node of a filesystem
    """

    def __init__(self):
        self.entries = {}

    def add_directory(self, name: str, directory):
        if name in self.entries:
            raise Exception('{}: name already exists'.format(name))
        self.entries[name] = directory

    def add_file(self, name: str, file):
        if name in self.entries:
            raise Exception('{}: name already exists'.format(name))
        self.entries[name] = file

    def materialize(self, path: str):

        os.makedirs(path, exist_ok=True)

        for entry_name, entry in self.entries.items():
            entry.materialize(os.path.join(path, entry_name))

    def by_path(self, path):
        if path.startswith(os.path.sep):
            path_parts = path[1:].split(os.path.sep)
        else:
            path_parts = path.split(os.path.sep)

        entry = self
        for path_part in path_parts:
            entry = self.entries[path_parts]
        return entry


class Directory(Root):

    def materialize(self, path: str):

        if os.path.exists(path) and os.path.isdir(path):
            pass
        else:
            os.mkdir(path)

        for entry_name, entry in self.entries.items():
            entry.materialize(os.path.join(path, entry_name))


class File:

    def __init__(self, content: str=""):
        self.content = content

    def materialize(self, path: str):
        with open(path, 'w') as f:
            f.write(self.content)
