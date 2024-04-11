class MixinConsoleLog:

    def __repr__(self):
        # return f"{self.__class__.__name__}"
        return f"{self.__class__.__name__}({", ".join(map(str, self.__dict__.values()))})"
