def satr_ascii_jam(satrlar):
    natijalar = []
    for satr in satrlar:
        jam = sum(ord(harf) for harf in satr)
        natijalar.append(jam)
    return natijalar

satrlar = ["salom", "dunyo", "python"]
print(satr_ascii_jam(satrlar))
