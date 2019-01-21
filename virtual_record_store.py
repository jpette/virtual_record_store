# John Pette - Python Project 1 - Record Store
# This program simulates a consumer's experience in a record store.
# The major classes are RecordStore, Customer, Music, Record, Cassette, and
# CD. The bulk of the methods are defined within the Customer class.


class RecordStore():
    """Representation of a record store; inputs are the store name and total
    cash in the register.
    """

    def __init__(self, name, register):
        # Initialize RecordStore instance with name and an amount of cash
        # in the register. Set empty inventory list.
        self.name = name
        self.register = register
        self.inventory = []

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return self.__str__()

    def add_to_inventory(self, Music):
        # Add Music objects to store inventory.
        self.inventory.append(Music)


class Customer():
    """Representation of a record store shopper."""

    # Set empty shopping cart list.
    shopping_cart = []

    def __init__(self, name, cash, credit):
        # Initialize Customer instance with name, amount of cash on hand,
        # and amount of credit available.
        self.name = name
        self.cash = cash
        self.credit = credit

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return self.__str__()

    def enter_store(self):
        # This method enables a customer to enter the store and provides
        # action options once inside.
        action = input("Would you like to [b]rowse, [r]eview your shopping"
                       "cart, [p]ay, or [e]xit the store?")
        # Check for input errors.
        while action not in ['b', 'r', 'p', 'e']:
            print("You have not entered a valid choice. Please try again.")
            action = input("Would you like to [b]rowse, [r]eview your shopping"
                           "cart, [p]ay, or [e]xit the store?")
        if action == "b":
            return self.browse(my_store)
        elif action == "r":
            self.view_cart()
            self.enter_store()
        elif action == "p":
            if self.shopping_cart == []:
                print("Your shopping cart is empty. We like free money, but "
                      "you should probably select an item before trying to "
                      "pay.")
            self.enter_store()
        else:
            self.exit_store()

    def exit_store(self):
        # This method allows a customer to exit the store, emptying the
        # shopping cart so that the customer does not leave without paying.
        self.shopping_cart = []
        print("You have left the record store.")

    def browse(self, RecordStore):
        # This method defines browsing actions for the customer to peruse
        # the store's inventory. It allows the customer to specify a specific
        # genre or look through all. If a genre is specified, the method
        # creates a sub-list of that genre's items.
        browse_choice = input("Which genre would you like to explore: [all], "
                              "[rock], [ska]/reggae, or [soul]/r&b?")
        # Check for input errors.
        while browse_choice not in ['all', 'rock', 'ska', 'soul']:
            print("That wasn't one of the options. Please try again.")
            browse_choice = input("Which genre would you like to explore: "
                                  "[all], [rock], [ska]/reggae, or "
                                  "[soul]/r&b?")
        if browse_choice == "rock":
            inv_select = [
                item for item in RecordStore.inventory if item.genre == "rock"
                ]
        elif browse_choice == "ska":
            inv_select = [
                item for item in RecordStore.inventory
                if item.genre == "ska & reggae"
                ]
        elif browse_choice == "soul":
            inv_select = [
                item for item in RecordStore.inventory if item.genre == "soul"]
        else:
            inv_select = [item for item in RecordStore.inventory]
        # This is a loop displaying the details of each item in the inventory
        # list or sub-list, allowing the customer to add each item to the cart,
        # continue browsing, pay, or exit the store.
        for x in range(len(inv_select)):
            print("-----")
            print(inv_select[x].artist)
            print(inv_select[x].title, inv_select[x].size)
            print(inv_select[x].details)
            print("Price: $", inv_select[x].price)
            browse_next = input("Would you like to [c]ontinue browsing, "
                                "[a]dd item to your cart, [r]eview your cart, "
                                "[p]ay, or [e]xit?")
            while browse_next not in ['c', 'a', 'r', 'p', 'e']:
                print("That wasn't one of the options. Please try again.")
                browse_next = input("Would you like to [c]ontinue browsing, "
                                    "[a]dd item to your cart, [r]eview your "
                                    "cart, [p]ay, or [e]xit?")
            if browse_next == "c":
                if inv_select[x] == inv_select[-1]:
                    print("That was the last item in this category.")
                    self.enter_store()
                else:
                    continue
            elif browse_next == "a":
                self.add_to_cart(inv_select[x])
                if inv_select[x] == inv_select[-1]:
                    print("That was the last item in this category.")
                    self.enter_store()
                else:
                    continue
            elif browse_next == "r":
                self.view_cart()
                browse_more = input("Would you like to [c]ontinue "
                                    "browsing, [p]ay, or [e]xit?")
                while browse_more not in ['c', 'p', 'e']:
                    print("That wasn't one of the options. Please try again.")
                    browse_more = input("Would you like to [c]ontinue "
                                        "browsing, [p]ay, or [e]xit?")
                if browse_more == "c":
                    continue
                elif browse_more == "p":
                    return self.check_out(my_store)
                else:
                    self.exit_store()
            elif browse_next == "p":
                return self.check_out(my_store)
            else:
                self.exit_store()

    def add_to_cart(self, Music):
        # This method adds an item to the customer's shopping cart,
        # provided the item is not already there.
        if Music in self.shopping_cart:
            print("That item is already in your cart.")
        else:
            self.shopping_cart.append(Music)

    def view_cart(self):
        # This method allows the customer to review the contents of the
        # shopping cart.
        if self.shopping_cart == []:
            print("Your shopping cart is empty.")
        else:
            print("*****")
            print("Your cart contains: ")
            for item in self.shopping_cart:
                print("-----")
                print(item.artist)
                print(item.title, item.size)
                print(item.details)
                print("Price: $", item.price)
            print("*****")

    def check_out(self, RecordStore):
        # This method processes the customer's payment for the items in
        # the shopping cart. It displays the contents of the cart, calculates
        # the total, and allows for cash or credit payments. 
        print("*****")
        print("Your cart contains:")
        for item in self.shopping_cart:
                print("-----")
                print(item.artist)
                print(item.title, item.size)
                print("Price: $", item.price)
        print("-----")
        bill = sum([x.price for x in self.shopping_cart])
        print("Your total is $", bill, ".", sep='')
        print("You have $", self.cash, " in cash and $", self.credit, " in "
              "credit available.", sep='')
        pay_method = input("How would you like to pay? [cash]/[credit]")
        # Check for input errors.
        while pay_method not in ['cash', 'credit']:
            print("You can't pay that way. Please try again.")
            pay_method = input("How would you like to pay? [cash]/[credit]")
        if pay_method == "cash":
            # Check to see if the customer has sufficient cash to pay for the
            # items in the cart. If not, ask if the customer wants to pay with
            # credit or cancel the transaction.
            if self.cash < bill:
                cash_problems = input("You do not have enough cash. "
                                      "Would you like to pay with [credit] "
                                      "or [cancel] the transaction?")
                while cash_problems not in ['credit', 'cancel']:
                    print("You can't pay that way. Please try again.")
                    cash_problems = input("Would you like to pay with [credit]"
                                          " or [cancel] the transaction?")
                if cash_problems == "credit":
                    if self.credit < bill:
                        print("Sorry, you cannot afford this.")
                        self.shopping_cart = []
                        self.exit_store()
                    else:
                        self.credit -= bill
                        my_store.register += bill
                        for item in self.shopping_cart:
                            my_store.inventory.remove(item)
                        self.shopping_cart = []
                        print(my_store.name, " thanks you for your purchase. "
                              "You have a credit balance of "
                              "$", self.credit, ".", sep='')
                        self.exit_store()
                else:
                    print("Thank you for stopping in.")
                    self.exit_store()
            else:
                self.cash -= bill
                my_store.register += bill
                for item in self.shopping_cart:
                    my_store.inventory.remove(item)
                self.shopping_cart = []
                print(my_store.name, " thanks you for your purchase. "
                      "You have $", self.cash, " left on you in cash.", sep='')
                self.exit_store()
        else:
            # Check to see if the customer has sufficient credit to pay for the
            # items in the cart. If not, ask if the customer wants to pay with
            # cash or cancel the transaction.
            if self.credit < bill:
                cash_problems = input("Your card was declined. Would you like "
                                      "to pay with [cash] or [cancel] "
                                      "the transaction?")
                while cash_problems not in ['cash', 'cancel']:
                    print("You can't pay that way. Please try again.")
                    cash_problems = input("Would you like to pay with [cash] "
                                          "or [cancel] the transaction?")
                if cash_problems == "cash":
                    if self.cash < bill:
                        print("Sorry, you cannot afford this.")
                        self.shopping_cart = []
                        self.exit_store()
                    else:
                        self.cash -= bill
                        my_store.register += bill
                        for item in self.shopping_cart:
                            my_store.inventory.remove(item)
                        self.shopping_cart = []
                        print(my_store.name, " thanks you for your purchase. "
                              "You have $", self.cash, " left on you in cash.",
                              sep='')
                        self.exit_store()
                else:
                    print("Thank you for stopping in.")
                    self.exit_store()
            else:
                # Process credit transaction. Deduct the total cost from the
                # customer's credit balance, add the amount to the store's
                # register, remove items in shopping cart from store 
                # inventory, and empty shopping cart.
                self.credit -= bill
                my_store.register += bill
                for item in self.shopping_cart:
                    my_store.inventory.remove(item)
                self.shopping_cart = []
                print(my_store.name, " thanks you for your purchase. You "
                      "have a credit balance of $", self.credit, ".", sep='')
                self.exit_store()


class Music():
    """Representation of all physical forms of music.
    Receives name and price as inputs. Defines class comparisons.
    """

    def __init__(self, name, price):
        # Initialize a Music object instance with a name and price.
        self.name = name
        self.price = price

    def __eq__(self, other):
        # Define comparison functions to sort music objects by name.
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name


class Record(Music):
    """Representation of a physical vinyl record. Child class of Music."""
    media_type = 'record'

    def __init__(self, name, price, artist, title, size, genre, details):
        # Initialize a Record instance with name and price from parent
        # class, plus artist, title, size, genre, and details attributes.
        Music.__init__(self, name, price)
        self.artist = artist
        self.title = title
        self.size = size
        self.genre = genre
        self.details = details

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return self.__str__()


class Cassette(Music):
    """Representation of a physical cassette. Child class of Music."""
    media_type = 'cassette'
    size = 'Cassette'

    def __init__(self, name, price, artist, title, genre, details):
        # Initialize a Cassette instance with name and price from parent
        # class, plus artist, title, genre, and details attributes.
        Music.__init__(self, name, price)
        self.artist = artist
        self.title = title
        self.genre = genre
        self.details = details

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return self.__str__()


class CD(Music):
    """Representation of a physical CD. Child class of Music."""
    media_type = 'cd'
    size = 'CD'

    def __init__(self, name, price, artist, title, genre, details):
        # Initialize a CD instance with name and price from parent
        # class, plus artist, title, genre, and details attributes.
        Music.__init__(self, name, price)
        self.artist = artist
        self.title = title
        self.genre = genre
        self.details = details

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return self.__str__()


# The following code is a program demo using sample data.
my_store = RecordStore("Shattered World Records", 2500)

# Sample data for program demo.
rocket1 = Record("rocket1", 1200, "Rocket from the Crypt", "Rocket Pack",
                 "7\"", "rock", "Limited to 75 copies.")
screaming1 = Cassette("screaming1", 60, "Screaming Trees", "Other Worlds",
                      "rock", "Original version from 1985, "
                      "limited to 1000 copies.")
fishbone1 = Record("fishbone1", 15, "Fishbone", "Truth and Soul", "LP",
                   "rock", "Original U.S. pressing.")
various1 = CD("various1", 25, "Various Artists", "Sought After Soul", "soul",
              "Rare four-CD set.")
nirvana1 = Record("nirvana1", 240, "Nirvana", "Bleach", "LP", "rock",
                  "Blue vinyl third pressing from 1992.")
skatalites1 = Record("skatalites1", 75, "The Skatalites", "SKA Authentic",
                     "LP", "ska & reggae", "Original Jamaican pressing on "
                     "ND Records. Heavy wear.")
slackers1 = Record("slackers1", 30, "The Slackers", "Redlilght", "LP",
                   "ska & reggae", "Re-press on color vinyl.")
starr1 = Record("starr1", 25, "Edwin Starr", "Soul Master", "LP", "soul",
                "Early Gordy pressing. Some water damage on the sleeve.")

test_inv = [
        rocket1, screaming1, fishbone1, various1,
        nirvana1, skatalites1, slackers1, starr1
        ]

for item in test_inv:
    my_store.add_to_inventory(item)

my_store.inventory.sort()

shopper = Customer("Norm", 120, 2000)

print("You are a consumer named ", shopper.name, ".", sep='')
print("You have $", shopper.cash, " on you in cash and $",
      shopper.credit, " available in credit.", sep='')

options = input("You are standing in front of a record store. "
                "That's weird. What are you doing? "
                "Would you like to go in? [y/n]")
while options not in ["y", "n"]:
    print("That was an odd response. You are clearly not serious "
          "about this process.")
    options = input("You are standing in front of a record store. "
                    "That's weird. What are you doing? "
                    "Would you like to go in? [y/n]")
if options == "y":
    shopper.enter_store()
else:
    print("Well, then. There is nothing else to do here. Move along.")