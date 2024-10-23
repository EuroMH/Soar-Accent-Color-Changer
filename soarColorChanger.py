import json
import os
import time

tkt = os.path.join("C:", os.sep, "Users", "Mathys", "AppData", "Local", ".soarclient", "game", "soar", "profile")

def update_accent_color(profile_name, color_choice):
    file_path = os.path.join("C:", os.sep, "Users", "Mathys", "AppData", "Local", ".soarclient", "game", "soar", "profile", profile_name)

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        if "Appearance" in data and "Accent Color" in data["Appearance"]:
            data["Appearance"]["Accent Color"] = color_choice
            
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)

            print(f"Accent Color updated to '{color_choice}' in '{profile_name}'")
            print("Exiting...")
            time.sleep(2)
        else:
            print(f"'Appearance' or 'Accent Color' not found in {profile_name}.")
            
    except FileNotFoundError:
        print(f"File '{profile_name}' not found in the specified path.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in '{profile_name}'. Please check the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def main():
    print(f"Here are all your profiles: \n{os.listdir(tkt)}\n\n")
    profile_name = input("Enter the profile name (including .json extension, e.g., example.json): ")
    try:
        with open(tkt + "\\" + str(profile_name), 'r') as file:
            data = json.load(file)
        
        if "Appearance" in data and "Accent Color" in data["Appearance"]:
            print(f"\nThe current AccentColor for {profile_name} is: {data["Appearance"]["Accent Color"]}")
    except Exception as e:
        print(e)

    colors = [
        "Evening Sunshine",
        "Light Orange",
        "Reef",
        "Amin",
        "Magic",
        "Mango Pulp",
        "Moon Purple",
        "Aqualicious",
        "Stripe",
        "Shifter",
        "Quepal",
        "Orca",
        "Sublime Vivid",
        "Moon Asteroid",
        "Summer Dog",
        "Pink Flavour",
        "Sin City Red",
        "Timber",
        "Pinot Noir",
        "Dirty Fog",
        "Piglet",
        "Little Leaf",
        "Nelson",
        "Turquoise flow",
        "SoundCloud",
        "Inbox",
        "Amethyst",
        "Blush"
    ]

    time.sleep(3)

    print("\nHere are the color names stripped down to just the text in quotes:")
    for index, color in enumerate(colors):
        print(f"{index + 1}. \"{color}\"")

    color_index = int(input("Enter the number corresponding to the color you want to set as Accent Color: ")) - 1

    if 0 <= color_index < len(colors):
        selected_color = colors[color_index]
        update_accent_color(profile_name, selected_color)
    else:
        print("Invalid selection. Please enter a number from the list.")

if __name__ == "__main__":
    main()