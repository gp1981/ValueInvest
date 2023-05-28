# ValueInvest
Value Investment based on Greenblatt's Magic Formula

This library provides functionality to analyze financial data and rank companies based on the principles outlined in the book "The Little Book that Still Beats the Market" by Joel Greenblatt.

## Disclaimer

This library is developed independently and is not affiliated with financialmodelingprep.com nor with magicformula.com or other organizations. The use of this library and any investment decisions made based on the analysis performed are the sole responsibility of the user. We take no responsibility for any risks or losses associated with the use of this library or investments made using the provided data.

## Usage

To use this library, follow these steps:

1. Get an API key from financialmodelingprep.com.
2. Clone this repository to your local machine.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Create a `.env` file in the root directory of the project and add the following line, replacing `*your-api-key*` with your actual API key:

   ```plaintext
   API_KEY=*your-api-key*

5. Modify the code in main.py according to your requirements.
6. Run the main.py script to analyze the financial data and generate rankings.

## Files

The library consists of the following files:

| File | Description | Status |
| ----------- | ----------- | ----------- |
| main.py | Main script for analyzing financial data | To update with new functions |
| F_SP500.py | Script for retrieving historical constituents of the S&P 500 index | To test (note 1) |
| F_API.py | Script for downloading financial data from financialmodelingprep.com API | Complete|
| F_Analysis.py | Script for analyzing the financial performance of companies | Work in progress (note 2) |
| F_Output.py | Script for printing the filtered, analyzed, and ranked companies | Work in progress (note 2)|

---
**NOTE**

1. This was part of the initial commit "initialization". Other function ```F_Name.py``` will be developed and tested in the corresponding branches before being merged in the *main* branch.
2. These are functions still be initiated.

---
## Ranking Companies based on "The Little Book that Still Beats the Market"

This library includes functionality to rank companies based on the principles outlined in the book "The Little Book that Still Beats the Market" by Joel Greenblatt. The ranking algorithm is implemented from scratch within this library, providing insights into company performance.

* Reference: Greenblatt, J. (2010). The Little Book that Still Beats the Market. Wiley.

## Contributing Guidelines

### Commit Descriptions
When making commits to the repository, please follow these guidelines for writing descriptive commit messages:

- **Feat**: Use this prefix for new features or enhancements to existing functionality.
- **Fix**: Use this prefix for bug fixes or resolving issues.
- **Docs**: Use this prefix for documentation updates or improvements.
- **refactor** : Use this prefix for code refactoring or restructuring without changing functionality.
- **test** : Use this prefix for adding or modifying test cases.
Please provide a clear and concise description of the changes made in the commit message.

### Branch Naming
When creating branches, please use descriptive names that indicate the purpose or functionality of the branch. Some common branch naming conventions include:

- *Feature*-*branch-name*: Use this prefix for branches that add new features or enhancements.
- *Bugfix*-*branch-name*: Use this prefix for branches that fix bugs or resolve issues.
- *Refactor*-*branch-name*: Use this prefix for branches that involve code refactoring 
- *docs*-*branch-name*: Use this prefix for branches that involve documentation updates or improvements.
Choose a branch name that clearly represents the purpose of the branch and provides context to other contributors.
