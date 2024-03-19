
# pip3 install Faker
from utilities.common import Common
from faker import Faker
import uuid
import pandas as pd


class FakerReview(Common):
    def __init__(self):
        super().__init__()

    @staticmethod
    def run():
        unique_ids = [str(uuid.uuid1()) for _ in range(10)]
        df = pd.DataFrame(unique_ids, columns=['id'])
        df['email_subject'] = [Faker().sentence(nb_words=6) for _ in range(10)]
        df['email_body'] = [Faker().text(max_nb_chars=200) for _ in range(10)]
        df['sender_email'] = [Faker().email() for _ in range(10)]
        df['address'] = [Faker().address() for _ in range(10)]
        df['name'] = [Faker().name() for _ in range(10)]


if __name__ == '__main__':
    FakerReview().run()

