# PortfolioCS
This is a collection of programs I made during AP CSP
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Security Log Analyzer
Project Summary
This project processes system security logs and identifies IP addresses associated with specific log events. It scans through paired lists of log messages and IP addresses, then extracts the IPs linked to events such as successful logins or unauthorized access attempts. The script helps visualize patterns in system activity and detect suspicious behavior.

Key Features
Event‑based IP extraction — Searches logs for a specific event (e.g., “Login success”) and returns all matching IP addresses.

Simple log‑scanning function — Uses a custom function to iterate through logs and collect relevant IPs.

Security insight generation — Helps identify unauthorized login attempts and potential threats by grouping IPs tied to suspicious events.
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Guessing Game
Project Summary
This interactive number‑guessing game challenges players across three difficulty levels: easy, medium, and hard. Each mode generates a random number and limits the number of attempts, adding tension with countdown timers or time‑pressure mechanics. The game blends randomness, user input, and timed responses to create a simple but engaging console experience.

Key Features
Multiple difficulty modes — Easy (1–5), Medium (1–10), and Hard (1–20), each with unique rules and attempt limits.

Countdown timer mechanics — Easy and Hard modes include a visible countdown before each guess, increasing suspense.

Randomized number generation — Ensures each playthrough is unpredictable and replayable.

Attempt‑tracking system — Players must guess correctly before running out of tries.
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Applicant Job Filter Program
Project Summary
This program filters a large dataset of applicants based on their job expertise and years of experience. By scanning three parallel lists—names, experience, and job titles—it identifies candidates who match specific hiring criteria. The script can return all applicants with a given skill or only those who meet a minimum experience requirement.

Key Features
Expertise‑based filtering — Finds all applicants who match a specific job title (e.g., “Python Developer”).

Experience threshold search — Returns only applicants who meet or exceed a required number of years.

Large dataset handling — Works with over 200 applicants using parallel list indexing.

Reusable search functions — Includes two search modes: expertise‑only and expertise‑plus‑experience.
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Hogwarts House Sorter
Project Summary
This interactive program assigns users to one of the four Hogwarts houses based on their name or a random selection. Known characters are automatically placed into their canonical houses, while all other users receive a randomized assignment. The script includes a dramatic loading sequence and allows repeated sorting.

Key Features
Name‑based sorting — Recognizes iconic characters (Harry, Draco, Luna, etc.) and assigns them to their correct houses.

Randomized house assignment — For all other names, the program selects a house using random number generation.

Interactive experience — Includes timed pauses (“…”) to build suspense before revealing the house.
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Rock, Paper, Scissors Game
Project Summary
This interactive console game simulates a classic match of Rock, Paper, Scissors against the computer. The player chooses their move, the computer randomly selects its own, and the program determines the winner. The game keeps track of wins and losses and allows the player to continue playing as long as they wish.

Key Features
Randomized computer choices — The computer selects rock, paper, or scissors using random number generation.

Win/loss tracking — The program keeps a running total of the player’s wins and losses across rounds.

Input validation — Ensures the player enters a valid move before continuing.

Replay system — After each round, the player can choose to play again or exit the game.
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Slot Machine Game
Project Summary
This project simulates a three‑slot casino machine where players deposit credits, spin the reels, and try their luck at winning bonus payouts. Each spin costs 10 credits, and the slot machine randomly generates symbols to determine wins, losses, or a jackpot. The game includes a banking system, credit validation, and a continuous play loop.

Key Features
Credit deposit system — Players can deposit fixed credit amounts (20, 50, or 100) through an in‑game bank before spinning.

Randomized slot reels — Each spin selects three symbols from a list, including the jackpot “7”.

Win conditions — Matching all three symbols awards +50 credits, while triple “7” triggers a +100 credit jackpot.

Replay and banking options — Players can spin, quit, or return to the bank when funds run low.

Input validation — Ensures only accepted deposit amounts and valid commands are processed.
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Universal Planner (To‑Do List Manager)
Project Summary
This interactive console‑based planner allows users to manage a personal to‑do list by adding tasks, marking items as completed, removing tasks, or clearing the entire list. The program displays both active and completed tasks and guides the user through a menu‑driven interface with built‑in input validation and timed prompts for a smoother experience.

Key Features
Task creation — Users can add new items to the to‑do list with simple text input.

Completion tracking — Completed tasks are moved from the active list to a dedicated completed list.

Removal and clearing options — Users can remove specific tasks or clear the entire to‑do list.

Menu‑driven interface — A numbered menu guides users through all available actions.

Input validation — Prevents empty entries and handles invalid menu selections gracefully.
---------------------------------------------------------------------------------------------------------------------------------------------------------------
