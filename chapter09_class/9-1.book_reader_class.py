class BookReader:
    name = str()

    def read_book():
        print(name + ' is reading Book!!')


reader = BookReader()
reader.name = "Chris"
reader.read_book()