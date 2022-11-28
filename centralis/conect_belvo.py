from belvo.client import Client
from decouple import config

SECRET_KEY_ID = config('SECRET_KEY_ID', 'SECRET_KEY_ID')
SECRET_KEY_PASS = config('SECRET_KEY_PASS', 'SECRET_KEY_PASS')

class ConectBelvo():
    def __init__(self):
        self.client = Client(SECRET_KEY_ID, SECRET_KEY_PASS, "https://sandbox.belvo.com")

    def create_links(self, institution, username, password):
        # Register a link
        links = self.client.Links.create(
            institution=institution,
            username= username,
            password= password
        )
        return links
    
    def all_institutions(self):
        return self.client.Institutions.list()
    
    def get_intitution(self, institution_id):
        return self.client.Institutions.get(id=institution_id)
    
    def all_transactions(self, link):
        return self.client.Transactions.list(link=link,page=1)
    
    def get_transaction(self, id):
        return self.client.Transactions.get(id=id)