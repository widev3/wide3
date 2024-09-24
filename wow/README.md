```bash
sudo apt install python3 -y
sudo apt install python3-pandas -y
sudo apt install python3-pyqt5  -y
```

## Project structure
Consider the following requirements
1. Every folder is an independent python software
2. Every software is divided in two parts
   1. ```lib```: contains the set of functions, classes, objects and properties needed to manage the software (something like the backend). There is no structure to respect for files and folders inside lib.
   2. ```view```: contains the set of functions, classes, objects and properties needed to show views of that software (something like the frontend)
      1. Every view folder has a ```view.py``` file
      2. Every ```view.py``` file has a public ```def view(args)``` function which is called at the beginning
      3. Every ```view.py``` file has a ```main``` function in order to test the independence of each software:
            ```python
            if __name__ == "__main__":
                view(Config())
            ```