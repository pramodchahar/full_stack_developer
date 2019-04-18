class CreditCard:
    """ A consumer credit card"""

     

    #invoke the constructor
    def __init__(self,customer,bank,account_num,credit_limit):
        """ Create a new credit card instance """

        #The initial balance is 0

        self._customer=customer
        self._bank=bank
        self._account_num=account_num
        self._credit_limit=credit_limit
        self._outstanding=0

    def get_customer(self):
        """Return name of customer"""
        return self._customer

    def get_bank(self):
        """ Return name of the bank"""
        return self._bank

    def get_account(self):
        """ Return card number """
        return self._account_num

    def get_credit_limit(self):
        """ Return credit limit  of the user"""
        return self._credit_limit
    
    def get_outstanding(self):
        """ Return balance amount of the card"""
        return self._outstanding
    
    def expense(self,price):
        """Spend given price to the card, assuming sufficient credit limit
        Return True if charge was processed; False if charge was denied."""

        if price +self._outstanding > self._credit_limit:
            return False
        else:
            self._outstanding+=price
            return True
    
    def make_payment(self,amount):
        """Process customer payment that reduces balance"""
        self._outstanding -=amount

if __name__=='__main__':
    wallet=[]

    wallet.append(CreditCard('Pramod Singh','Kotak','1111 2222 3333 4444',2500))
    wallet.append(CreditCard('Pramod Singh','HDFC','7676 4343 4444 8888',3500))
    wallet.append(CreditCard('Pramod Singh','Citi','4343 2424 5555 1212',5000))

    for amount in range(1,20):
        wallet[0].expense(amount)
        wallet[1].expense(2*amount)
        wallet[2].expense(3*amount)

    for c in range(3):
        print('Customer = ',wallet[c].get_customer())
        print('Bank= ',wallet[c].get_bank())
        print('Account = ',wallet[c].get_account())
        print('Limit= ',wallet[c].get_credit_limit())
        print('Outstanding = ',wallet[c].get_outstanding())

        while wallet[c].get_outstanding() > 100:
            wallet[c].make_payment(100)
            print('New Outstanding = ',wallet[c].get_outstanding())
    print()
        
