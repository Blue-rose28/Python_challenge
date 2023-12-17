# Python Challenge: PyBank and PyPoll

## Overview
This repository contains Python scripts, `main.py`, to analyze financial and election data for the PyBank and PyPoll challenges respectively. The scripts read CSV files containing financial and election data, perform calculations, and produce analysis results.
## Technology
Python
### Files Included:
- **PyBank**
  - `main.py`: Python script for analyzing financial data (`budget_data.csv`).
  - `Resources/budget_data.csv`: Dataset containing financial records (columns: Date, Profit/Losses).
  - `analysis/financial_analysis.txt`: Text file with results from the financial analysis.

- **PyPoll**
  - `main.py`: Python script for analyzing election data (`election_data.csv`).
  - `Resources/election_data.csv`: Dataset containing election records (columns: Voter ID, County, Candidate).
  - `analysis/election_results.txt`: Text file with results from the election analysis.

## Instructions
### PyBank
- The `main.py` script reads the `budget_data.csv` file.
- It calculates:
  - Total months included in the dataset.
  - Net total amount of "Profit/Losses" over the entire period.
  - Changes in "Profit/Losses" over the entire period and the average of those changes.
  - Greatest increase and decrease in profits with respective dates.
- Results are printed to the terminal and exported to `analysis/financial_analysis.txt`.

### PyPoll
- The `main.py` script reads the `election_data.csv` file.
- It calculates:
  - Total number of votes cast.
  - List of candidates who received votes.
  - Percentage of votes each candidate won and their total number of votes.
  - Winner of the election based on the popular vote.
- Results are printed to the terminal and exported to `analysis/election_results.txt`.

## Running the Scripts
- Ensure you have Python installed on your machine.
- Clone this repository to your local machine.
- Navigate to your terminal's respective folder (PyBank or PyPoll).
- Run the `main.py` script using the command: `python main.py`.


