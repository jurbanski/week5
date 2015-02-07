""" machine class module """
# 2015-02-07
# Joseph Urbanski
# MPCS 50101

class CoinDispenser():
    """ CoinDispenser class contains:
        - A list of *coins* it will dispense.
        - An amount of *change* (>100) given as a list of coins.
    """
    coins = [25, 10, 5, 1]
    change = [0, 0, 0, 0]

    def make_change(self, amount):
        """ This function returns a list of quarters, dimes, nickels and
            pennies that would make change for the given amount.
        """
        self.change = [0, 0, 0, 0]

        # Quarters pass
        if amount < 25:
            pass
        elif amount < 50:
            amount -= 25
            self.change[0] = 1
        elif amount < 75:
            amount -= 50
            self.change[0] = 2
        else:
            amount -= 75
            self.change[0] = 3

        # Dimes pass
        if amount < 10:
            pass
        elif amount < 20:
            amount -= 10
            self.change[1] = 1
        else:
            amount -= 20
            self.change[1] = 2

        # Nickels pass
        if amount < 5:
            pass
        else:
            amount -= 5
            self.change[2] = 1

        # Pennies pass
        self.change[3] = amount

        # Return the list of coins we've generated.
        return self.change
