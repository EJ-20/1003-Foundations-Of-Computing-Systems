import re

# Replaces all instances of "steal" with "eat".
def main():
    text = "(1) A person is guilty of burglary if—\n\t(a) he or she enters any building or part of a building as a trespasser and with intent to steal anything in the building or that part of it; or\n\t(b) having entered any building or part of a building as a trespasser he steals or attempts to steal anything in the building or that part of it."
    
    original = "steal"
    replacement = "eat"
    
    print("Original:\n", text)
    text = re.sub(original, replacement, text)
    print("\nEdited:\n", text)

main()
