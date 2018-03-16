def read():
    command = input(">>> ")
    return command
    

def reply(command):
    if command == "run":
        print("escaped")
    elif command == "attack":
        print("enemy incapacitated")
    elif command == "pick up":
        print("picked up")
        
        
def main():
    playing = 1
    while playing == 1:
        move = read()
        if move == "leave":
            playing = 0
        reply(move)
    
    
main()        