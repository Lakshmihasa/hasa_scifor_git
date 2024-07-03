import winsound  

def play_sound(animal):
    if animal.lower() == 'cat':
        print("Meow!")
        winsound.PlaySound('cat_sound.wav', winsound.SND_FILENAME)  
    elif animal.lower() == 'dog':
        print("Woof!")
        winsound.PlaySound('dog_sound.wav', winsound.SND_FILENAME) 
        winsound.PlaySound('cow_sound.wav', winsound.SND_FILENAME)  
    elif animal.lower() == 'duck':
        print("Quack!")
        winsound.PlaySound('duck_sound.wav', winsound.SND_FILENAME)  
        print(f"Sorry, I don't know the sound of '{animal}'.")

def main():
    print("Welcome to the  Awesome Animal Sound Player!")
    print("=================================")
    print("Choose an animal to hear its sound:")
    print("1. Cat")
    print("2. Dog")
    print("3. Cow")
    print("4. Duck")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        play_sound('cat')
    elif choice == '2':
        play_sound('dog')
    elif choice == '3':
        play_sound('cow')
    elif choice == '4':
        play_sound('duck')
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
