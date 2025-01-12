# The Ultimate Pygame Structure  
### This repository is a structure to help you organize and build your pygame projects and get them running in the browser with pygbag

## Getting Started  
Install the latest version of Python from: https://www.python.org/  
  
Clone the repository to your local machine:
```sh
git clone https://github.com/SebZanardo/The-Ultimate-Pygame-Structure.git
cd The-Ultimate-Pygame-Structure
```
Install the required dependencies:  
(Using a virtual environment is a good idea)
```sh
pip install -r requirements.txt
```

## Project Structure  
📂 **assets** : Store all your game assets here.  

📂 **components** : Define all the components for your game here. Split them into separate files and folders if needed.  

📂 **core** : Initialisation of the window, settings and keybinds are defined in here. Assets and universal constants too.  

📂 **scenes** : Create all of your scenes here in separate files. Follow the layout specified by the _Scene_ baseclass.  

📂 **utilities** : Useful helper functions.  

## Running Your Game  
Simply execute the `main.py` file located in `src/` to run your Pygame project on your local machine:
```sh
python main.py
```

## Building Your Game (For Browser)  
Install pygbag  
```sh
pip install pygbag
```
  
Inside of the `src/` directory run:
```sh
pygbag --template custom.tmpl .
```
You can now open http://localhost:8000/ in your browser to test your project  
  
A web build has been created in a new folder `/build`  
Just compress the `web` directory inside of `/build` and upload this compressed file to Itch.io  
  
## Resources
Virtual Environments:  
https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/  

Pygame-ce:  
https://github.com/pygame-community/pygame-ce  
https://pyga.me/docs/  

Pygbag:  
https://github.com/pygame-web/pygbag  
https://pygame-web.github.io/wiki/pygbag/  

### Feel free to customize and extend this structure to suit your project's needs. Happy coding!
