# The Ultimate Pygame Structure  
### This repository is a structure to help you organize and build your pygame projects and get them running in the browser with pygbag
Github Links: [pygame-ce](https://github.com/pygame-community/pygame-ce) [pygbag](https://github.com/pygame-web/pygbag)
  
## Getting Started  
Install Python 3.11+ at: https://www.python.org/  
  
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
📂 **assets** : Store all your game assets here.  
    
📂 **baseclasses** :  Define all your abstract base classes and their respective managers here.

📂 **components** : Define all the components for your game here. Split them into separate files and folders if needed.

📂 **config** : Initialisation of the window, settings and keybinds are defined in here. Assets and universal constants too.

📂 **scenes** : Create all of your scenes here in separate files. Follow the layout specified by the _Scene_ baseclass.

📂 **utilities** : Useful scripts such as decorators, typehints and helper functions.  
  
## Running Your Game  
Simply execute the `main.py` file to run your Pygame project on your local machine:
```sh
python main.py
```

## Building Your Game (For Browser)  
Install the pygbag library (if you don't already have it)  
  
Inside of your main project directory run:
```sh
python -m pygbag .
```
You can now open http://localhost:8000/ in your browser to test your project  
  
A web build has been created in a new folder `/build`  
Just compress the `web` directory inside of `/build` and upload this compressed file to Itch.io  
  
### Feel free to customize and extend this structure to suit your project's needs. Happy coding!
