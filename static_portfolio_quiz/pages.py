from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import json


class Introduction(Page):
    pass


class Question1(Page):
    form_model = 'player'
    form_fields = ['answer1']

    def vars_for_template(self):
        prices_list = {"p_1": 0.04, "p_2": 0.07,
                       "p_3": 0.07, "p_4": 0.10,
                       "p_5": 0.07, "p_6": 0.10,
                       "p_7": 0.10, "p_8": 0.45
                       }

        quantities_list = {"q_1": 0, "q_2": 0,
                           "q_3": 0, "q_4": "X",
                           "q_5": 0, "q_6": 0,
                           "q_7": 0, "q_8": 0
                           }

        expenditures_list = {"e_1": 0, "e_2": 0,
                             "e_3": 0, "e_4": 100,
                             "e_5": 0, "e_6": 0,
                             "e_7": 0, "e_8": 0
                             }

        return {
            'num_states': 8,
            'prices': json.dumps(prices_list),
            'quantities': json.dumps(quantities_list),
            'expenditures': json.dumps(expenditures_list),
            'realized_state': "",
            'initial_wealth': 100
        }


class Question2(Page):
    form_model = 'player'
    form_fields = ['answer2']

    def vars_for_template(self):
        prices_list = {"p_1": 0.04, "p_2": 0.07,
                       "p_3": 0.07, "p_4": 0.10,
                       "p_5": 0.07, "p_6": 0.10,
                       "p_7": 0.10, "p_8": 0.45
                       }

        quantities_list = {"q_1": 0, "q_2": 0,
                           "q_3": 0, "q_4": 50,
                           "q_5": 0, "q_6": 50,
                           "q_7": 0, "q_8": "X"
                           }

        expenditures_list = {"e_1": 0, "e_2": 0,
                             "e_3": 0, "e_4": 5,
                             "e_5": 0, "e_6": 5,
                             "e_7": 0, "e_8": 90
                             }

        return {
            'num_states': 8,
            'prices': json.dumps(prices_list),
            'quantities': json.dumps(quantities_list),
            'expenditures': json.dumps(expenditures_list),
            'realized_state': "",
            'initial_wealth': 100
        }


class Question3(Page):
    form_model = 'player'
    form_fields = ['answer3']

    def vars_for_template(self):
        prices_list = {"p_1": 0.037, "p_2": 0.0741,
                       "p_3": 0.0741, "p_4": 0.1481,
                       "p_5": 0.0741, "p_6": 0.1481,
                       "p_7": 0.1481, "p_8": 0.2963
                       }

        quantities_list = {"q_1": 100, "q_2": 400,
                           "q_3": 200, "q_4": 150,
                           "q_5": 50, "q_6": 50,
                           "q_7": 50, "q_8": 37
                           }

        expenditures_list = {"e_1": 3.7, "e_2": 29.6,
                             "e_3": 14.8, "e_4": 22.2,
                             "e_5": 3.7, "e_6": 7.4,
                             "e_7": 7.4, "e_8": 11
                             }

        return {
            'num_states': 8,
            'prices': json.dumps(prices_list),
            'quantities': json.dumps(quantities_list),
            'expenditures': json.dumps(expenditures_list),
            'realized_state': "",
            'initial_wealth': 100
        }


class Question4(Page):
    form_model = 'player'
    form_fields = ['answer4']

    def vars_for_template(self):
        prices_list = {"p_1": 0.037, "p_2": 0.0741,
                       "p_3": 0.0741, "p_4": 0.1481,
                       "p_5": 0.0741, "p_6": 0.1481,
                       "p_7": 0.1481, "p_8": 0.2963
                       }

        quantities_list = {"q_1": 100, "q_2": 400,
                           "q_3": 200, "q_4": 150,
                           "q_5": 50, "q_6": 50,
                           "q_7": 50, "q_8": 37
                           }

        expenditures_list = {"e_1": 3.7, "e_2": 29.6,
                             "e_3": 14.8, "e_4": 22.2,
                             "e_5": 3.7, "e_6": 7.4,
                             "e_7": 7.4, "e_8": 11
                             }

        return {
            'num_states': 8,
            'prices': json.dumps(prices_list),
            'quantities': json.dumps(quantities_list),
            'expenditures': json.dumps(expenditures_list),
            'realized_state': 8,
            'initial_wealth': 100
        }


class Question5(Page):
    form_model = 'player'
    form_fields = ['answer5']

    def vars_for_template(self):
        prices_list = {"p_1": 0.037, "p_2": 0.0741,
                       "p_3": 0.0741, "p_4": 0.1481,
                       "p_5": 0.0741, "p_6": 0.1481,
                       "p_7": 0.1481, "p_8": 0.2963
                       }

        quantities_list = {"q_1": 100, "q_2": 400,
                           "q_3": 200, "q_4": 150,
                           "q_5": 50, "q_6": 50,
                           "q_7": 50, "q_8": 37
                           }

        expenditures_list = {"e_1": 3.7, "e_2": 29.6,
                             "e_3": 14.8, "e_4": 22.2,
                             "e_5": 3.7, "e_6": 7.4,
                             "e_7": 7.4, "e_8": 11
                             }

        return {
            'num_states': 8,
            'prices': json.dumps(prices_list),
            'quantities': json.dumps(quantities_list),
            'expenditures': json.dumps(expenditures_list),
            'realized_state': 3,
            'initial_wealth': 100
        }


class Question6(Page):
    form_model = 'player'
    form_fields = ['answer6']

    def vars_for_template(self):
        prices_list = {"p_1": 0.037, "p_2": 0.0741,
                       "p_3": 0.0741, "p_4": 0.1481,
                       "p_5": 0.0741, "p_6": 0.1481,
                       "p_7": 0.1481, "p_8": 0.2963
                       }

        quantities_list = {"q_1": 100, "q_2": 400,
                           "q_3": 200, "q_4": 150,
                           "q_5": 50, "q_6": 50,
                           "q_7": 50, "q_8": 37
                           }

        expenditures_list = {"e_1": 3.7, "e_2": 29.6,
                             "e_3": 14.8, "e_4": 22.2,
                             "e_5": 3.7, "e_6": 7.4,
                             "e_7": 7.4, "e_8": 11
                             }

        return {
            'num_states': 8,
            'prices': json.dumps(prices_list),
            'quantities': json.dumps(quantities_list),
            'expenditures': json.dumps(expenditures_list),
            'realized_state': 5,
            'initial_wealth': 100
        }


class Question7(Page):
    form_model = 'player'
    form_fields = ['answer7']

    def vars_for_template(self):
        prices_list = {"p_1": 0.037, "p_2": 0.0741,
                       "p_3": 0.0741, "p_4": 0.1481,
                       "p_5": 0.0741, "p_6": 0.1481,
                       "p_7": 0.1481, "p_8": 0.2963
                       }

        quantities_list = {"q_1": "", "q_2": "",
                           "q_3": "", "q_4": "",
                           "q_5": "", "q_6": "",
                           "q_7": "", "q_8": ""
                           }

        expenditures_list = {"e_1": "", "e_2": "",
                             "e_3": "", "e_4": "",
                             "e_5": "", "e_6": "",
                             "e_7": "", "e_8": ""
                             }

        return {
            'num_states': 8,
            'prices': json.dumps(prices_list),
            'quantities': json.dumps(quantities_list),
            'expenditures': json.dumps(expenditures_list),
            'realized_state': "",
            'initial_wealth': 100
        }


page_sequence = [
    Introduction,
    Question1,
    Question2,
    Question3,
    Question4,
    Question5,
    Question6,
    Question7
]
