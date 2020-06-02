from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class DynamicResults(Page):
    def vars_for_template(self):
        r = self.round_number
        return {
            'num_periods': self.session.vars["dyn_num_periods_round{}".format(r)],
            'prices': self.session.vars["dyn_prices_round{}".format(r)],
            'wealth': self.participant.vars["dyn_wealth_round{}".format(r)],
            'stock': self.participant.vars["dyn_stock_round{}".format(r)],
            'bond': self.participant.vars["dyn_bond_round{}".format(r)],
            'realized_states': self.participant.vars["dyn_realized_states_round{}".format(r)],
            'realized_wealth': self.participant.vars["dyn_realized_wealth_round{}".format(r)]
        }


page_sequence = [
    DynamicResults
]
