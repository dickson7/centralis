from belvo.client import Client
from decouple import config

SECRET_KEY_ID = config('SECRET_KEY_ID', 'SECRET_KEY_ID')
SECRET_KEY_PASS = config('SECRET_KEY_PASS', 'SECRET_KEY_PASS')

class ConectBelvo():
    """
    Class for conxion with the belvo api
    """
    def __init__(self):
        self.client = Client(SECRET_KEY_ID, SECRET_KEY_PASS, "https://sandbox.belvo.com")

    def create_links(self, institution, username, password):
        """method to create a connection link to the institution

        Args:
            institution (str): institution
            username (str): username
            password (str): password

        Returns:
            link: uuid
        """
        # Register a link
        links = self.client.Links.create(
            institution=institution,
            username= username,
            password= password
        )
        return links
    
    def all_institutions(self):
        """method to obtain all institutions

        Returns:
            list: institutions
        """
        return self.client.Institutions.list()
    
    def get_intitution(self, institution_id):
        """method to obtain institution

        Returns:
            list: institution
        """
        return self.client.Institutions.get(id=institution_id)
    
    def all_transactions(self, link):
        """method to obtain all transactions

        Returns:
            list: transactions
        """
        return self.client.Transactions.list(link=link,page=1)
    
    def get_transaction(self, id):
        """method to obtain details transaction

        Returns:
            list: transaction
        """
        return self.client.Transactions.get(id=id)