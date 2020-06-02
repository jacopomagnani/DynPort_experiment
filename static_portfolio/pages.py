from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1


class Static(Page):
    form_model = 'player'
    form_fields = ['static_securities']

    def vars_for_template(self):
        return {'num_states': 2 ** self.subsession.num_periods}

    def before_next_page(self):
        self.player.static_get_outcome()


page_sequence = [
    Intro,
    Static]
