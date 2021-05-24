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

positions = { }
print("enter chess.com notation")

moveNotation = input()

if (moveNotation[0].islower()):
    print("P")
else:
    print(moveNotation[0])

print(moveNotation)
