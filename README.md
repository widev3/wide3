# Whistle of Wind radio telescope

<p align="center">
  <img src="https://github.com/user-attachments/assets/c5fb736e-5ffb-4102-8ebd-a200df3dfa0d" width="256">
</p>

## Installation

```bash
sudo apt install python3 -y
sudo apt install python3-matplotlib -y
sudo apt install python3-pyqt5 -y
sudo apt install python3-pandas -y
sudo apt install python3-scipy -y
sudo apt install python3-astropy -y
sudo apt install python3-astroquery -y
pip3 install RsInstrument --break-system-packages
sudo apt install python3-pyvisa -y
```

```bat
pip install matplotlib
pip install pyqt5
pip instal pandas
pip install scipy
pip install astropy
pip install astroquery
pip install RsInstrument
```

## Execution in [tools](./tools) folder

```bash
python3 tools.py
```

## Tools structure

Consider the following requirements

1. Every folder is an independent python software
2. Every software is divided in **3 mandatory** parts
   1. ```lib```: contains the set of functions, classes, objects and properties needed to manage the software (something like the backend). There is no structure to respect for files and folders inside lib.
   2. ```view```: contains the set of functions, classes, objects and properties needed to show views of that software (something like the frontend)
      1. Every view folder has a ```view.py``` file
      2. Every ```view.py``` file has a public ```def view(args)``` function which is called at the beginning
      3. Every ```view.py``` file has a ```main``` function in order to test the independence of each software:

            ```python
            if __name__ == "__main__":
                view(Config())
            ```

   3. ```config.json``` file with some configurations about the software like its actual name ```"name": "Actual name"``` (mandatory) or the icon to use ```"icon": "icon_for_the_mandatory_software.png"``` (not mandatory)

## Usefull links

<https://www.atnf.csiro.au/research/radio-school/2011/talks/parkesrs2011_interferometryi_full.pdf>
<https://websites.umich.edu/~lowbrows/reflections/2007/jabshier.1.html>
<https://www.aoc.nrao.edu/events/synthesis/2004/presentations.html>
<https://ntrs.nasa.gov/api/citations/19940017222/downloads/19940017222.pdf>
<https://www.ccera.ca/papers/memo-0008-a-cheap-simple-fx-correlator/>
<https://www.aanda.org/articles/aa/full/2007/05/aa4519-05/aa4519-05.html>
<https://arxiv.org/pdf/1702.00844>
<https://leo.phys.unm.edu/~gbtaylor/>
<https://www.atnf.csiro.au/research/radio-school/2011/index.html>
<https://websites.umich.edu/~lowbrows/reflections/2007/jabshier.1.html>
