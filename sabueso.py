import os, argparse

def seek(target: str, loc: str):
    for root, dirs, files in os.walk(loc):
        if target in files:
            return os.path.join(root, target)

        for dir in dirs:
            found = seek(target, os.path.join(root, dir))
            if found:
                return found
                
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find a file in a directory tree.")
    
    parser.add_argument("--target", help="The file to search for.")
    parser.add_argument("--loc", help="The directory to search in.")
    
    args = parser.parse_args()

    if not args.target:
        target = input("Enter the file to search for: ")
    if not args.loc:
        loc = os.getcwd()
    
    found = seek(target, loc)

    if found:
        print(found)
    else:
        print(f"{args.target} not found in {args.loc}")