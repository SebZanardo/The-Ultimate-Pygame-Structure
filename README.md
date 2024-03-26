# The Ultimate Pygame Structure  
### This repository is a structure to help you organize and build your Pygame projects efficiently.
  
## Getting Started  
Clone the repository to your local machine:
```sh
git clone https://github.com/SebZanardo/The-Ultimate-Pygame-Structure.git
cd The-Ultimate-Pygame-Structure
```
Install the required dependencies:
```sh
pip install -r requirements.txt
```

## Project Structure  
📂 **assets** : Store all your game assets organised in subfolders here.  
    
📂 **baseclasses** :  Define all your abstract base classes and their respective managers here.

📂 **components** : Define all the components for your game here. Split them into separate files and folders if needed.

📂 **config** : Initialisation of the window, settings and keybinds are defined in here.

📂 **scenes** : Create all of your scenes here in separate files. Follow the layout specified by the _Scene_ baseclass.

📂 **utilities** : Useful scripts such as decorators, typehints and helper functions.  
  
## Running Your Game  
Simply execute the `main.py` file to run your Pygame project:
```sh
python main.py
```
### More updates to this structure coming soon :))
### Feel free to customize and extend this structure to suit your game's needs. Happy coding!
