print("quel est ta note sur 20")
note=input()
note=int(note)
if note>15:
    print("Très bien!")
elif note<10:
    print("tu feras mieux la prochaine fois")
else:
    print("pas mal...")
