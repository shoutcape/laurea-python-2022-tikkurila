def lue(määre: str, alaraja: int, ylaraja: int):
    while True:
        virhe = False
        try:
            luku = int(input(määre))
            if luku < alaraja or luku > ylaraja:
                virhe = True

        except:
            virhe = True
        if virhe:
            print(f"Syötteen on oltava kokonaisluku väliltä {alaraja}...{ylaraja}")
        else:
            return luku


if __name__ == "__main__":
    luku = lue("syötä luku: ", 5, 10)
    print("syötit luvun:", luku)