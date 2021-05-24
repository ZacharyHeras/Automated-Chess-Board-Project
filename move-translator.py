'''
Translates chess.com move notation into string that arduino can use to make a
move.

ZacharyHeras, May 24th, 2021

'''

## Use dictionary to define each square
## Determine move string length to catagorize it into a read-type
## Figure out what piece is moving where
## If piece is moving into occupied square, remove other piece
## Place piece into new square location

# Defines all of the positions on the board with pieces in starting positions
positions = {
    "A8": "R",
    "B8": "N",
    "C8": "B",
    "D8": "Q",
    "E8": "K",
    "F8": "B",
    "G8": "N",
    "H8": "R",

    "A7": "P",
    "B7": "P",
    "C7": "P",
    "D7": "P",
    "E7": "P",
    "F7": "P",
    "G7": "P",
    "H7": "P",

    "A6": "-",
    "B6": "-",
    "C6": "-",
    "D6": "-",
    "E6": "-",
    "F6": "-",
    "G6": "-",
    "H6": "-",

    "A5": "-",
    "B5": "-",
    "C5": "-",
    "D5": "-",
    "E5": "-",
    "F5": "-",
    "G5": "-",
    "H5": "-",

    "A4": "-",
    "B4": "-",
    "C4": "-",
    "D4": "-",
    "E4": "-",
    "F4": "-",
    "G4": "-",
    "H4": "-",

    "A3": "-",
    "B3": "-",
    "C3": "-",
    "D3": "-",
    "E3": "-",
    "F3": "-",
    "G3": "-",
    "H3": "-",

    "A2": "P",
    "B2": "P",
    "C2": "P",
    "D2": "P",
    "E2": "P",
    "F2": "P",
    "G2": "P",
    "H2": "P",

    "A1": "R",
    "B1": "N",
    "C1": "B",
    "D1": "Q",
    "E1": "K",
    "F1": "B",
    "G1": "N",
    "H1": "R"
    
}
print("enter chess.com notation")

moveNotation = input()

if (moveNotation[0].islower()):
    print("P")
else:
    print(moveNotation[0])

print(moveNotation)
