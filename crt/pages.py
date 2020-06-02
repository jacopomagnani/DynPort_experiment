from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['answer1', 'answer2', 'answer3']

    def before_next_page(self):
        self.player.get_outcome()


class Results(Page):
    pass


page_sequence = [
    MyPage,
    Results
]
