from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import json


class Page1(Page):
    pass


class DummyPage(Page):
    def vars_for_template(self):
        prices_list = {"p_1": 0.50, "p_2": 0.20,
                       "p_3": 0.20, "p_4": 0.10
                       }

        quantities_list = {"q_1": 100, "q_2": 0,
                           "q_3": 200, "q_4": 300
                           }

        expenditures_list = {"e_1": 50, "e_2": 0,
                             "e_3": 40, "e_4": 30
                             }

        return {
            'num_states': 4,
            'prices': json.dumps(prices_list),
            'quantities': json.dumps(quantities_list),
            'expenditures': json.dumps(expenditures_list),
            'realized_state': "",
            'initial_wealth': 120
        }


page_sequence = [
    Page1
]
