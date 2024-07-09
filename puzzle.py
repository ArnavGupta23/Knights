from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A can either be a knight or knave
    Or(AKnight, AKnave),
    # A cannot be both a knight and knave
    Not(And(AKnave, AKnight)),
    # If A is a knight, then A's statement must be true
    Implication(AKnight, And(AKnight, AKnave)),
    # If A is a knave, then A's statement must be false
    Implication(AKnight, Not(And(AKnight, AKnave)))   
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A and B are either knights or knaves
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    
    # A and B cannot be both knights and knaves
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),

    # If A is a knight, then A's statement must be true 
    Implication(AKnight, And(AKnave, BKnave)),
    # If A is a knave, then A's statement must be false
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A and B are either knights or knaves
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),

    # A and B cannot be both knights and knaves
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),

    # If A is a knight, A and B are the same
    Implication(AKnight, Biconditional(AKnight, BKnight)),
    # If A is a knave, A and B are different
    Implication(AKnave, Not(Biconditional(AKnight, BKnight))),
    # If B is a knight, A and B are different
    Implication(BKnight, Not(Biconditional(AKnight, BKnight))),
    # If B is a knave, A and B are the same
    Implication(BKnave, Biconditional(AKnight, BKnight))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A, B, and C are either knights or knaves
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),

    # A, B, and C cannot be both knights and knaves
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    # If A is a knight, then A's statement must be true
    Implication(AKnight, Or(AKnight, AKnave)),
    # If A is a knave, then A's statement must be false
    Implication(AKnave, Not(Or(AKnight, AKnave))),
    # If B is a knight, then B's statements must be true
    Implication(BKnight, And(Implication(AKnight, AKnave), CKnave)),
    # If B is a knave, then B's statements must be false
    Implication(BKnave, Not(And(Implication(AKnight, AKnave), CKnave))),
    # If C is a knight, then C's statement must be true
    Implication(CKnight, AKnight),
    # If C is a knave, then C's statement must be false
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
