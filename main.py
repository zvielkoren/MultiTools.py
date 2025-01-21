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
    pass


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


def load_features():
    clear_screen()
    load_logo()
    print("""
    You have selected to load features
    
    """)
    input("Press Enter to Continue...")
    features_dir = pathlib.Path(__file__).parent / 'features'
    features = os.listdir(features_dir)
    print(features)

def main():
    loading_animation()
    load_logo()
    time.sleep(5)
    select_static_option()

if __name__ == '__main__':
    main()
