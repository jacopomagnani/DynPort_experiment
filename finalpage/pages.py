from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    def vars_for_template(self):
        return {
            'fee': self.session.config['participation_fee']
        }


page_sequence = [
    MyPage
]
