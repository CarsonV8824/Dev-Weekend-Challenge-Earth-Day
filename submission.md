*This is a submission for [Weekend Challenge: Earth Day Edition](https://dev.to/challenges/weekend-2026-04-16)*

## What I Built

**Franklin and the Diver** is an engaging ocean-themed action game that combines entertainment with environmental education. Players control a net-wielding diver protecting Franklin the turtle from incoming pollution in two iconic ocean zones: the Atlantic and Pacific.

The game features wave-based progression across 3 intense levels per ocean, with escalating difficulty. Between waves, educational ocean facts display seamlessly without interrupting gameplay. Players build competitive scores tracked across a multiplayer leaderboard where they can compare achievements with other players.

**Goal**: Create an engaging educational game that inspires environmental awareness while showcasing technical skills in game development, UI design, and data persistence.

## Demo

To run locally:

```bash
git clone https://github.com/CarsonV8824/Dev-Weekend-Challenge-Earth-Day.git
cd Dev-Weekend-Challenge-Earth-Day
pip install -r requirements.txt
python main.py
```

**Gameplay Overview**:
1. Enter your name on the home screen
2. Select Atlantic or Pacific ocean
3. Move your net to catch falling trash before it hits the turtle
4. Catch trash to increase score and complete waves
5. Survive 3 waves to win and unlock the leaderboard

## Code

{% github CarsonV8824/Dev-Weekend-Challenge-Earth-Day %}

**Project Structure**:
- `menus/` — PySide6 UI components (Home, Map, Stats pages, Leaderboard)
- `oceans/` — Game logic for Atlantic and Pacific modes
- `sprites/` — Pygame sprite classes (Player, Turtle, Trash)
- `data/` — SQLite database management and game state
- `assets/` — Styling and visual resources

## How I Built It

**Technology Stack**: PySide6 (UI), Pygame (game engine), SQLite3 (data), Matplotlib & Seaborn (stats), Pandas (data analysis), GitHub Copilot (development assistance)

**Key Technical Approach**:

1. **Non-Blocking Game Pauses** — Replaced blocking `time.sleep()` calls with delta-time based timers, allowing graceful pauses during fact displays without freezing the UI or game thread.

2. **Sprite-Based Collision System** — Leveraged Pygame's sprite groups and collision detection for efficient player-trash interactions and smooth movement without lag.

3. **Wave Difficulty Progression** — Implemented dynamic difficulty scaling where spawn intervals decrease and wave durations increase, creating natural progression curves.

4. **Real-Time Leaderboard** — Combined SQLite GROUP BY queries with Pandas DataFrames to track top-10 rankings across three categories (score, Atlantic wins, Pacific wins), updating instantly after each game.

5. **Theme-Based Architecture** — Each ocean loads unique color palettes from JSON files, enabling visual customization without code changes and preventing duplication.

6. **Threaded Game Execution** — Game windows run in separate threads, preventing UI freezing and allowing seamless menu navigation without application restart.

**GitHub Copilot Integration**: Copilot accelerated development by reducing debugging time for game timing issues, UI synchronization problems, and JSON file path resolution. It also optimized PySide6 styling patterns and suggested improvements to non-blocking state management, allowing focus on gameplay mechanics rather than boilerplate code.

See [AI Usage Log](copiolit_usage.md) for detailed optimization notes.

## Prize Categories

**Best Use of GitHub Copilot** — GitHub Copilot significantly streamlined development through intelligent debugging, code optimization suggestions, and architectural improvements. This enabled faster iteration on core gameplay features and complex UI state management.

---

Thanks for considering this submission! 

