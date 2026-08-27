# Memory Cards

A desktop 2D puzzle game built using Python and Pygame. The objective is to test your memory by flipping cards over to find matching pairs. Once all pairs are successfully matched, you win the game.

## Features
* **Classic Matching Mechanics:** Click to flip two cards. If they match, they stay face up. If they don't, they automatically flip back down after a half-second delay.
* **Dynamic Grid:** A randomized shuffle system ensures the 12 cards (6 matching pairs) are in different positions every time you play.
* **Interactive UI:** Features a custom main menu, active click detection on cards and buttons, and a post-game dialog box to easily replay or return to the menu.
* **Asset Integration:** Utilizes custom fonts, card face images, and background graphics.

## Controls
* **Mouse Left Click:** Flip cards and interact with menu buttons.

## Download and Play (Windows)
If you want to play the game without setting up a Python environment, you can download the standalone Windows executable:

- Link: [Download Memory Cards](https://github.com/AP-Abhishek/Memory-Cards/releases/tag/v1.0.0)
- Extract the downloaded files if necessary and run the `.exe`.
- **Note:** Because this is an indie project without a paid digital signature, Windows SmartScreen may flag the executable. Click **More info** and then **Run anyway** to launch the game.

## How to Run from Source
To run or modify the game from the source code, you will need Python installed on your computer.

1. Clone this repository:
   ```bash
   git clone https://github.com/AP-Abhishek/Memory-Cards.git
   ```
1. Navigate to the project folder:
    ```bash
    cd Memory-Cards
    ```
1. Install the required dependencies (Pygame):
    ```bash
    pip install pygame
    ```
1. Run the game:
    ```bash
    python Game.py
    ```

## Project Structure
```
Memory-Cards
├─ assets
│  ├─ Font
│  │  └─ CaveatBrush.ttf
│  └─ Images
│     ├─ Apple.png
│     ├─ Back-View.png
│     ├─ Game-BG.png
│     ├─ Grape.png
│     ├─ Lime.png
│     ├─ Logo.png
│     ├─ Orange.png
│     ├─ Strawberry.png
│     └─ Watermelon.png
├─ Card.py
├─ Game.py
├─ README.md
└─ utils.py

```
