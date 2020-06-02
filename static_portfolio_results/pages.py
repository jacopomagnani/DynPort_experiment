from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class StaticResults(Page):

    def vars_for_template(self):
        r = self.round_number
        return {
            'num_states': 2 ** self.session.vars["static_num_periods_round{}".format(r)],
            'prices': self.session.vars["static_prices_round{}".format(r)],
            'quantities': self.participant.vars["static_securities_round{}".format(r)],
            'realized_state': self.participant.vars["static_realized_state_round{}".format(r)],
            'realized_pay': self.participant.vars["static_realized_pay_round{}".format(r)]
        }


page_sequence = [
    StaticResults
]
