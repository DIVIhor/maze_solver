# MazeSolver

**MazeSolver** is a Python-based maze generator that creates a labyrinth and then attempts to solve it.

You can specify maze's complexity (its grid size, up to 50x50) and set a delay to give yourself time to try solving the puzzle before the script begins.

Here's an example of a maze with a 20x20 grid size and a 2-second delay before the app starts solving it:
![MazeSolver Demo](https://github.com/user-attachments/assets/7f30e1fd-b9e5-46c7-a53b-81c6a0d54760)

## Table of contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation Guide](#installation-guide)
- [Usage](#usage)
  - [On Linux or MacOS](#on-linux-or-macos)
  - [On Windows](#on-windows)
  - [Parameters](#parameters)
  - [Notes](#notes)

## Features

- Generates a maze with a size ranging from 4x4 to 50x50 _(20x20 by default; columns and rows can have different values)_.
- Can wait up to 2 minutes before starting to solve the puzzle.
- Marks visited incorrect paths in grey.
- Marks the correct path in red.
- Displays a CLI message indicating whether the maze was successfully solved.

## Requirements

Any desktop OS: Linux (or WSL for Windows) / MacOS / Windows.

To use the app you need to have **Python version 3.11+** on your computer.

## Installation Guide

Clone the repository with `git clone <URL>` or download and unzip it.

_The app relies solely on the standard library, so there's no need to create a virtual environment._

## Usage

Open your CLI in the app's root folder.

### On Linux or MacOS

```bash
python3 main.py [delay] [number_of_columns] [number_of_rows]
```

### On Windows

```powershell
py main.py [delay] [number_of_columns] [number_of_rows]
```

### Parameters

- `delay` (optional): Integer value representing the delay in seconds (range: 0–120; default: 0)
- `number_of_columns` (optional): Integer specifying the number of columns in the maze grid (range: 4–50; default: 20)
- `number_of_rows` (optional): Integer specifying the number of rows in the maze grid (range: 4–50; default: 20)

### Notes

- You can specify just the delay by omitting the other arguments.
- If you want to set the number of columns or rows, **you must provide all three parameters**.
