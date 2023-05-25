# ValueInvest
Value Investment based on Greenblatt's Magic Formula

This library provides functionality to analyze financial data and rank companies based on the principles outlined in the book "The Little Book that Still Beats the Market" by Joel Greenblatt.

## Usage

To use this library, follow these steps:

1. Get an API key from financialmodelingprep.com.
2. Clone this repository to your local machine.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Create a `.env` file in the root directory of the project and add the following line, replacing `<your-api-key>` with your actual API key:

   ```plaintext
   API_KEY=<your-api-key>

5. Modify the code in main.py according to your requirements.
6. Run the main.py script to analyze the financial data and generate rankings.

## Files

The library consists of the following files:

- main.py: This file contains the main script to analyze financial data and generate rankings based on the principles from "The Little Book that Still Beats the Market".
- F_API.py: This file includes functions to interact with the financialmodelingprep.com API and download financial data.
- F_SP500.py: This file provides functions to retrieve historical and current constituents of the S&P 500 index and mark stocks belonging to the index in the analyzed financial data.

## Ranking Companies based on "The Little Book that Still Beats the Market"

This library includes functionality to rank companies based on the principles outlined in the book "The Little Book that Still Beats the Market" by Joel Greenblatt. The ranking algorithm is implemented from scratch within this library, providing insights into company performance.

> Reference: Greenblatt, J. (2010). The Little Book that Still Beats the Market. Wiley.

## Disclaimer

This library is developed independently and is not affiliated with financialmodelingprep.com. The use of this library and any investment decisions made based on the analysis performed are the sole responsibility of the user. We take no responsibility for any risks or losses associated with the use of this library or investments made using the provided data.