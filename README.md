## Space shooter game

game created with `pygame` with classic 8-bit assets and sprites. you can run it using following commands

```cmd
git clone https://github.com/Mhmd-sh3rawy/space_shooters_game.git
cd space_shooter_game/space_shooter_game/
pip install requirements.txt
python3 game_menu.py
```

---
## file hierarchy 


```md
space_shooter_game/
├── assets/                # Game assets (Backgrounds, Buttons background, etc.).
├── Font/                  # Font used in the game.
├── Graphics/              # Player and enimies sprites.
├── Sounds/                # Sound effects and background music.
├── alien.py               # (Alien / Mystery_ship) class.
├── button.py              # custom Button class.
├── game_menu.py           # start game menu.
├── game.py                # Core game loop and main logic.
├── highscore.txt          # Stores the player's high score.
├── laser.py               # Laser custom class.
├── loadfunctions.py       # Helper functions for loading files (for Linux users).
├── main.py                # the main game window and the main loop.
├── spaceship.py           # Spaceship behavior and controls.
```

--- 

## future task: 

- enabling multiplayer
- creating levels and changing 8-bit theme
