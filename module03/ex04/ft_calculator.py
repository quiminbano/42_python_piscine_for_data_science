class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        print(f"Dot product is: {sum([x * y for x, y in zip(V1, V2)])}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        temp = [x + y for x, y in zip(V1, V2)]
        print("Add Vector is : [" + ', '.join(f'{i:.1f}' for i in temp) + "]")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        temp = [x - y for x, y in zip(V1, V2)]
        print("Sous Vector is: [" + ', '.join(f'{i:.1f}' for i in temp) + "]")
