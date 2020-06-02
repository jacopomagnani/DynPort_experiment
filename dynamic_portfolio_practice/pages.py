from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class Dynamic(Page):
    form_model = 'player'
    form_fields = ['dyn_stock', 'dyn_bond', 'dyn_wealth']

    def before_next_page(self):
        self.player.dyn_get_outcome()


class DynamicResults(Page):
    pass


page_sequence = [
    Introduction,
    Dynamic,
    DynamicResults
]
