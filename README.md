# The Ultimate Pygame Structure  
### This repository is a structure to help you organize and build your Pygame games efficiently.
  
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
**assets/**:  
- Store all your game assets organised in subfolders here.  
    
**baseclasses/**:  
- `scenemanager.py` Contains abstract _Scene_ class that needs to be inherited, and a _SceneManager_ class to run the scenes.
- `statemachine.py` Contains abstract _State_ class that needs to be inherited, and a _StateMachine_ class to run the states.

**config/**:
- `core.py` Initialises Pygame and runs the game loop. Uses the SceneManager to run the current scene and its respective logic. Captures input keys and passes it along to the scene using an input buffer. Calculates delta time if your scenes need it.  
- `settings.py` Stores all of the game constants.

**scenes/**:
- Create all of your scenes here in separate files. Follow the layout specified by the _Scene_ baseclass.

**utilities/**:
- A folder to hold helpful decorators, typehints and functions.  

## Running Your Game  
Simply execute the `main.py` file to run your Pygame project:
```sh
python main.py
```
### More updates to this structure coming soon :))
### Feel free to customize and extend this structure to suit your game's needs. Happy coding!
