class Singletone:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
    
database = Singletone()
database2 = Singletone()

print(database, database2)