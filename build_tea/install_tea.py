'''Runs the install script for the tea package manager'''

# Run sh <(curl tea.xyz) and specify yes for both options

import os 

if __name__ == '__main__':
    os.system("sh <(curl tea.xyz) -y -y")