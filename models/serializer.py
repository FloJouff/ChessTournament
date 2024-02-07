import json


class Serializer[T]:
    def serialize(self, o):
        generic_type = self.__orig_class__.__args__[0]
        file_name = f"{generic_type.__name__}.json"
        with open(file_name, "w") as file:
            json.dump(o.__dict__, file, indent=2)

    def deserialize(self):
        generic_type = self.__orig_class__.args__[0]
        file_name = f"{generic_type.__name__}.json"
        print(generic_type)
        with open(file_name, "r") as file:
            dct = json.load(file)
            values = [v for v in dct.values()]
            return generic_type(*values)
