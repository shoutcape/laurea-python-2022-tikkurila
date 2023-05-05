kerrokset = int(input("Kerrokset: "))
koko = 2 * kerrokset - 1

for rivi in range(koko):
    for sarake in range(koko):
        kirjain_kerros = min(rivi, sarake, koko - rivi - 1, koko - sarake - 1)
        kirjain = chr(ord('A') + kerrokset - kirjain_kerros - 1)
        print(kirjain, end="")
    print()

