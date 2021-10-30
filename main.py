from utilities.lexer import readSource
from utilities.types import Types

tokens = readSource('./Examples/SuccessfulExample.c')

for token in tokens:
  if token.type not in [Types.SPACE, Types.LINE_BREAK, Types.COMENT_BLOCK, Types.COMENT_LINE]:
    print(token)
