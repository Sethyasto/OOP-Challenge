from pet import Dog

def display_welcome():
    print(r"""
      / \__
     (    @\___
     /         O
    /   (_____/
   /_____/   U
    """)
    print("🐾 Welcome to your Digital Dog Simba! 🐾")
    print("Take care of your Golden Retriever puppy\n")

def main():
    simba = Dog()
    display_welcome()
    
    actions = {
        '1': ('Feed Simba', simba.eat),
        '2': ('Put Simba to sleep', simba.sleep),
        '3': ('Play with Simba', simba.play),
        '4': ('Hear Simba bark', simba.bark),
        '5': ('Train Simba', lambda: simba.train(input("What trick should Simba learn? "))),
        '6': ('See tricks Simba knows', simba.show_tricks),
        '7': ('Pet Simba (wag tail)', simba.wag_tail),
        '8': ('Check Simba\'s status', simba.get_status),
        '9': ('Quit', None)
    }
    
    while True:
        print("\nWhat would you like to do?")
        for key, (action, _) in actions.items():
            print(f"{key}. {action}")
        
        choice = input("> ").strip()
        
        if choice == '9':
            print(f"\nGoodbye! {simba.name} will miss you! 🐶💤")
            break
            
        if choice in actions:
            action = actions[choice][1]
            result = action() if action else ""
            print(f"\n{result}")
            print(simba.get_status())
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()