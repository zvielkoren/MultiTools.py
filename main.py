import os
import pathlib
import time
import sys


def loading_animation():
    os.system('cls')
    chars = "/—\|"
    for char in chars:
        sys.stdout.write('\r' + 'loading...' + char)
        time.sleep(.5)
        sys.stdout.flush()


def clear_screen():
    os.system('cls')

def load_logo():
    # looading animation
    clear_screen()
    # logo
    print("""
    
        ███╗   ███╗██╗   ██╗██╗  ████████╗██╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
        ████╗ ████║██║   ██║██║  ╚══██╔══╝██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
        ██╔████╔██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     ███████╗
        ██║╚██╔╝██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     ╚════██║
        ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
        ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                                                    
        """)


def load_data():
    clear_screen()
    load_logo()
    print(""" no Available Data""")
    print("")
    input("Press Enter to Continue...")
    select_static_option()


def select_static_option():
    clear_screen()
    load_logo()
    print("""
    
        1. Load Features
        2. Load Data
        4. Exit
    
    """)

    option = int(input("Enter Option: "))
    if option == 1:
        load_features()
    elif option == 2:
        load_data()
    elif option == 4:
        exit()
    else:
        print("Invalid Option")
        input("Press Enter to Continue...")
        select_static_option()


def exec_feature(feature):
    clear_screen()
    load_logo()
    print(f"""
    You have selected to load feature: {feature}
    
    """)
    input("Press Enter to Continue...")
    ## load features on py files in features/{folder_names}/{filename}.py
    # else load features on py files in features/{folder_names}/{filename}.py
    features_dir = pathlib.Path(__file__).parent / 'features'
    feature_dir = features_dir / feature
    feature_files = os.listdir(feature_dir)
    for feature_file in feature_files:
        if feature_file.endswith('.py'):
            with open(feature_dir / feature_file, 'r') as f:
                exec(f.read())
    input("Press Enter to Continue...")
    select_static_option()



def load_features():
    clear_screen()
    load_logo()
    print("""
    You have selected to load features
    
    """)
    input("Press Enter to Continue...")
    # if feature folder not exist create folder
    if not os.path.exists('features'):
        os.mkdir('features')
    features_dir = pathlib.Path(__file__).parent / 'features'
    features = os.listdir(features_dir)

    print("Available Features: ")
    for index, feature in enumerate(features):
        # skip pycache directory
        if feature == '__pycache__':
            continue
        # skip __init__.py file
        if feature == '__init__.py':
            continue
        # if feature folder clean send "feature not Available"
        # if on folder not .py files send "feature not Available"

        feature_dir = features_dir / feature
        feature_files = os.listdir(feature_dir)
        is_feature_available = False
        for feature_file in feature_files:
            if feature_file.endswith('.py'):
                is_feature_available = True
                break
        if not is_feature_available:
            print(f"{index + 1}. {feature} (Feature not Available)")
            continue
        # if feature folder not clean send "feature Available"
        print(f"{index + 1}. {feature} (Feature Available)")

        # if feature folder clean send "feature not Available"
    print("0. Back")
    option = int(input("Enter Option: "))
    if option == 0:
        select_static_option()
    else:

        feature = features[option - 1]
        exec_feature(feature)


def main():
    loading_animation()
    load_logo()
    time.sleep(5)
    select_static_option()

if __name__ == '__main__':
    main()
