# prints out all lines, from a list, which contain the query text
def find_query(lines, query):
    for line in lines:
        if line.find(query) != -1: print(line)

def main():
    lines = ["There once was a puppy called Dougal,","who was sometimes good,","but not very often.", "Because, like all puppies,","he liked to chew, bite, bark and sleep.","And once he'd done enough of those things to satisfy his needs,","he found that there wasn't much of the day left for anything else."]
    query = "was"
    
    print("Original lines of text:")
    for line in lines:
        print(line)
    print("\nSearch results: Found '", query, "' on these lines:", sep='')
    
    find_query(lines, query)

main()
