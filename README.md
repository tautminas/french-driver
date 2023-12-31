# French Driver Game

## About the game
French Driver is an educational game for learning top 1000 French words. It is made with Python turtle graphics. In a game you have to reach the highest possible distance by driving through the correct French words. Knowing the top 1000 words may cover roughly 70-80% of the vocabulary used in everyday conversations and written texts. Top 1000 French words were collected from [Wikipedia](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/French_wordlist_opensubtitles_5000). CSV file was generated using Google Sheets and its GOOGLETRANSLATE functionality for translation to the English.  
## Controls

- Arrows (←;↑;→;↓) control the car in the faster pace.
- W;A;S;D buttons control the car in the slower pace. Space button increases the speed to the maximum with nitro boost.

## Running the program

Create virtual environment:
```bash
python -m venv french-driver
```

Activate the virtual environment based on the operating system:
- On Windows:
```bash
french-driver\Scripts\activate
```
- On macOS and Linux:
```bash
source french-driver/bin/activate
```

Install the required packages:
```bash
pip install -r requirements.txt
```

Run the game:
```bash
python main.py
```

You can make an executable file for easier future replay:
```bash
pyinstaller --onefile --noconsole --add-data "assets;assets" --add-data "data;data" --icon="./assets/france.ico" --name="french-driver" main.py
```

The executable file will be generated in the dist/ directory. In case you would like to have the executable file in the different location please create a shortcut. Plain location change of the executable will not work. You can create the shortcut on Windows operating system by right-clicking on the executable file and selecting "Send to" -> "Desktop (create shortcut)." This will create a shortcut on your desktop.

After you are done playing leave the virtual environment:

```bash
deactivate
```
