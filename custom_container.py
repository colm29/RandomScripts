class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, value):
        self.__tags[tag.lower()] = value

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add('Python')
cloud.add('python')
cloud.add('python')
print(cloud['python'])
cloud['python'] = 2
print(len(cloud))
print(cloud['python'])

print(cloud.__dict__)
print(cloud._TagCloud__tags)
