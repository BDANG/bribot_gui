### A GUI interface for a Supreme New York Bot
#### By Brian Dang

The purpose of the repository is to offer a simple and free/open-source Tkinter GUI. The underlying backend functionality is maintained privately. The GUI offers users a starting place for education and/or adaptation.

#### Dependencies
* `Python 3.6.3`

## Demo
`python Bot.py`

## Roadmap
* continue building out base functionality
    * editing products/cards
    * linking products/cards, with error handling
    * encrypted cards file
* prepare backend points-of-entry in the GUI
* incorporate backend functionality when season is live
* robust error handling
* quality of life improvements: disabling/enabling certain actions
* socket/upgrading/feature toggling

## Tab Breakdown
#### Run
Holds the necessary functions for starting/running the bot.
* `Initialize` button that activates the chromedrivers (for `selenium`)
* `Run` button that actually starts the bot to search for the new drop / products
* `Automatic Drop Detection` toggle for detecting a new drop (new products).
    * `enabled` - the bot will not search for products until a new drop is detected
    * `disabled` - the bot will immediately search for products when `Run` button is clicked
* `Automatic Product Search` toggle for automatically finding products with keywords
    * `enabled` - the bot will automatically search to find a product via keywords
    * `disabled` - the USER must MANUALLY select a product
* `Automatic Checkout` toggle for pressing the checkout button automatically
    * `enabled` - the bot will "press" the checkout button.
    * `disabled` - the USER must MANUALLY press the checkout button.

#### Products
Maintains the list of products being purchased.

#### Cards
Maintains the list of cards being charged to purchase certain products.

#### Upgrades
Holds the necessary functions for upgrading functionality (speed, number of products, number of cards).

#### Settings
Holds the possible settings/options that affect the general bot operation
* `Refresh Rate` - how many seconds to wait before checking for a new drop
* `Checkout Delay`- how many seconds to wait before pressing the checkout button.
