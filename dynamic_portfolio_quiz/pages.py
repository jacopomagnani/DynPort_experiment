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
        prices_list = {"x_0_1": 8, "x_1_1": 16, "x_1_2": 4, "x_2_1": 32,
                       "x_2_2": 8, "x_2_3": 8, "x_2_4": 2, "x_3_1": 64,
                       "x_3_2": 16, "x_3_3": 16, "x_3_4": 4, "x_3_5": 16,
                       "x_3_6": 4, "x_3_7": 4, "x_3_8": 1
                       }
        wealth_list = {"w_0_1": 100, "w_1_1": 200, "w_1_2": 50, "w_2_1": "X",
                       "w_2_2": "", "w_2_3": "", "w_2_4": "", "w_3_1": "",
                       "w_3_2": "", "w_3_3": "", "w_3_4": "", "w_3_5": "",
                       "w_3_6": "", "w_3_7": "", "w_3_8": ""
                       }
        stock_list = {"s_0_1": 100, "s_1_1": 100, "s_1_2": "", "s_2_1": "",
                      "s_2_2": "", "s_2_3": "", "s_2_4": ""
                      }
        bond_list = {"b_0_1": 0, "b_1_1": 100, "b_1_2": "", "b_2_1": "",
                     "b_2_2": "", "b_2_3": "", "b_2_4": ""
                     }
        states_list = {"0": "", "1": "", "2": "", "3": ""}

        return {
            'num_periods': 3,
            'prices': json.dumps(prices_list),
            'wealth': json.dumps(wealth_list),
            'stock': json.dumps(stock_list),
            'bond': json.dumps(bond_list),
            'realized_states': json.dumps(states_list)
        }


class Question2(Page):
    form_model = 'player'
    form_fields = ['answer2']

    def vars_for_template(self):
        prices_list = {"x_0_1": 8, "x_1_1": 16, "x_1_2": 4, "x_2_1": 32,
                       "x_2_2": 8, "x_2_3": 8, "x_2_4": 2, "x_3_1": 64,
                       "x_3_2": 16, "x_3_3": 16, "x_3_4": 4, "x_3_5": 16,
                       "x_3_6": 4, "x_3_7": 4, "x_3_8": 1
                       }
        wealth_list = {"w_0_1": 100, "w_1_1": 200, "w_1_2": 50, "w_2_1": "",
                       "w_2_2": "X", "w_2_3": "", "w_2_4": "", "w_3_1": "",
                       "w_3_2": "", "w_3_3": "", "w_3_4": "", "w_3_5": "",
                       "w_3_6": "", "w_3_7": "", "w_3_8": ""
                       }
        stock_list = {"s_0_1": 100, "s_1_1": 100, "s_1_2": "", "s_2_1": "",
                      "s_2_2": "", "s_2_3": "", "s_2_4": ""
                      }
        bond_list = {"b_0_1": 0, "b_1_1": 100, "b_1_2": "", "b_2_1": "",
                     "b_2_2": "", "b_2_3": "", "b_2_4": ""
                     }
        states_list = {"0": "", "1": "", "2": "", "3": ""}

        return {
            'num_periods': 3,
            'prices': json.dumps(prices_list),
            'wealth': json.dumps(wealth_list),
            'stock': json.dumps(stock_list),
            'bond': json.dumps(bond_list),
            'realized_states': json.dumps(states_list)
        }


class Question3(Page):
    form_model = 'player'
    form_fields = ['answer3']

    def vars_for_template(self):
        prices_list = {"x_0_1": 8, "x_1_1": 16, "x_1_2": 4, "x_2_1": 32,
                       "x_2_2": 8, "x_2_3": 8, "x_2_4": 2, "x_3_1": 64,
                       "x_3_2": 16, "x_3_3": 16, "x_3_4": 4, "x_3_5": 16,
                       "x_3_6": 4, "x_3_7": 4, "x_3_8": 1
                       }
        wealth_list = {"w_0_1": 100, "w_1_1": 200, "w_1_2": 50, "w_2_1": "",
                       "w_2_2": "", "w_2_3": "", "w_2_4": "", "w_3_1": "",
                       "w_3_2": "", "w_3_3": "", "w_3_4": "", "w_3_5": "",
                       "w_3_6": "", "w_3_7": "", "w_3_8": ""
                       }
        stock_list = {"s_0_1": 100, "s_1_1": "", "s_1_2": 75, "s_2_1": "",
                      "s_2_2": "", "s_2_3": "", "s_2_4": ""
                      }
        bond_list = {"b_0_1": 0, "b_1_1": "", "b_1_2": "X", "b_2_1": "",
                     "b_2_2": "", "b_2_3": "", "b_2_4": ""
                     }
        states_list = {"0": "", "1": "", "2": "", "3": ""}

        return {
            'num_periods': 3,
            'prices': json.dumps(prices_list),
            'wealth': json.dumps(wealth_list),
            'stock': json.dumps(stock_list),
            'bond': json.dumps(bond_list),
            'realized_states': json.dumps(states_list)
        }


class Question4(Page):
    form_model = 'player'
    form_fields = ['answer4']

    def vars_for_template(self):
        prices_list = {"x_0_1": 8, "x_1_1": 16, "x_1_2": 4, "x_2_1": 32,
                       "x_2_2": 8, "x_2_3": 8, "x_2_4": 2, "x_3_1": 64,
                       "x_3_2": 16, "x_3_3": 16, "x_3_4": 4, "x_3_5": 16,
                       "x_3_6": 4, "x_3_7": 4, "x_3_8": 1
                       }
        wealth_list = {"w_0_1": 100, "w_1_1": 200, "w_1_2": 50, "w_2_1": "",
                       "w_2_2": "", "w_2_3": "", "w_2_4": "", "w_3_1": "",
                       "w_3_2": "", "w_3_3": "", "w_3_4": "", "w_3_5": "",
                       "w_3_6": "", "w_3_7": "", "w_3_8": ""
                       }
        stock_list = {"s_0_1": 100, "s_1_1": "", "s_1_2": -75, "s_2_1": "",
                      "s_2_2": "", "s_2_3": "", "s_2_4": ""
                      }
        bond_list = {"b_0_1": 0, "b_1_1": "", "b_1_2": "X", "b_2_1": "",
                     "b_2_2": "", "b_2_3": "", "b_2_4": ""
                     }
        states_list = {"0": "", "1": "", "2": "", "3": ""}

        return {
            'num_periods': 3,
            'prices': json.dumps(prices_list),
            'wealth': json.dumps(wealth_list),
            'stock': json.dumps(stock_list),
            'bond': json.dumps(bond_list),
            'realized_states': json.dumps(states_list)
        }


class Question5(Page):
    form_model = 'player'
    form_fields = ['answer5']

    def vars_for_template(self):
        prices_list = {"x_0_1": 8, "x_1_1": 16, "x_1_2": 4, "x_2_1": 32,
                       "x_2_2": 8, "x_2_3": 8, "x_2_4": 2, "x_3_1": 64,
                       "x_3_2": 16, "x_3_3": 16, "x_3_4": 4, "x_3_5": 16,
                       "x_3_6": 4, "x_3_7": 4, "x_3_8": 1
                       }
        wealth_list = {"w_0_1": 100, "w_1_1": "Y", "w_1_2": "Z", "w_2_1": "",
                       "w_2_2": "", "w_2_3": "", "w_2_4": "", "w_3_1": "",
                       "w_3_2": "", "w_3_3": "", "w_3_4": "", "w_3_5": "",
                       "w_3_6": "", "w_3_7": "", "w_3_8": ""
                       }
        stock_list = {"s_0_1": "X", "s_1_1": "", "s_1_2": "", "s_2_1": "",
                      "s_2_2": "", "s_2_3": "", "s_2_4": ""
                      }
        bond_list = {"b_0_1": "", "b_1_1": "", "b_1_2": "", "b_2_1": "",
                     "b_2_2": "", "b_2_3": "", "b_2_4": ""
                     }
        states_list = {"0": "", "1": "", "2": "", "3": ""}

        return {
            'num_periods': 3,
            'prices': json.dumps(prices_list),
            'wealth': json.dumps(wealth_list),
            'stock': json.dumps(stock_list),
            'bond': json.dumps(bond_list),
            'realized_states': json.dumps(states_list)
        }


class Question6(Page):
    form_model = 'player'
    form_fields = ['answer6']

    def vars_for_template(self):
        prices_list = {"x_0_1": 8, "x_1_1": 16, "x_1_2": 4, "x_2_1": 32,
                       "x_2_2": 8, "x_2_3": 8, "x_2_4": 2, "x_3_1": 64,
                       "x_3_2": 16, "x_3_3": 16, "x_3_4": 4, "x_3_5": 16,
                       "x_3_6": 4, "x_3_7": 4, "x_3_8": 1
                       }
        wealth_list = {"w_0_1": 100, "w_1_1": "Y", "w_1_2": "Z", "w_2_1": "",
                       "w_2_2": "", "w_2_3": "", "w_2_4": "", "w_3_1": "",
                       "w_3_2": "", "w_3_3": "", "w_3_4": "", "w_3_5": "",
                       "w_3_6": "", "w_3_7": "", "w_3_8": ""
                       }
        stock_list = {"s_0_1": "X", "s_1_1": "", "s_1_2": "", "s_2_1": "",
                      "s_2_2": "", "s_2_3": "", "s_2_4": ""
                      }
        bond_list = {"b_0_1": "", "b_1_1": "", "b_1_2": "", "b_2_1": "",
                     "b_2_2": "", "b_2_3": "", "b_2_4": ""
                     }
        states_list = {"0": "", "1": "", "2": "", "3": ""}

        return {
            'num_periods': 3,
            'prices': json.dumps(prices_list),
            'wealth': json.dumps(wealth_list),
            'stock': json.dumps(stock_list),
            'bond': json.dumps(bond_list),
            'realized_states': json.dumps(states_list)
        }


class Question7(Page):
    form_model = 'player'
    form_fields = ['answer7']

    def vars_for_template(self):
        prices_list = {"x_0_1": 8, "x_1_1": 16, "x_1_2": 4, "x_2_1": 32,
                       "x_2_2": 8, "x_2_3": 8, "x_2_4": 2, "x_3_1": 64,
                       "x_3_2": 16, "x_3_3": 16, "x_3_4": 4, "x_3_5": 16,
                       "x_3_6": 4, "x_3_7": 4, "x_3_8": 1
                       }
        wealth_list = {"w_0_1": 100, "w_1_1": 180, "w_1_2": 60, "w_2_1": 160,
                       "w_2_2": 190, "w_2_3": 90, "w_2_4": 75, "w_3_1": 220,
                       "w_3_2": 130, "w_3_3": 280, "w_3_4": 145, "w_3_5": 120,
                       "w_3_6": 75, "w_3_7": 75, "w_3_8": 75
                       }
        stock_list = {"s_0_1": 80, "s_1_1": -20, "s_1_2": 30, "s_2_1": 60,
                      "s_2_2": 90, "s_2_3": 30, "s_2_4": 0
                      }
        bond_list = {"b_0_1": 20, "b_1_1": 200, "b_1_2": 30, "b_2_1": 100,
                     "b_2_2": 100, "b_2_3": 60, "b_2_4": 75
                     }
        states_list = {"0": 1, "1": 2, "2": 4, "3": 8}

        return {
            'num_periods': 3,
            'prices': json.dumps(prices_list),
            'wealth': json.dumps(wealth_list),
            'stock': json.dumps(stock_list),
            'bond': json.dumps(bond_list),
            'realized_states': json.dumps(states_list)
        }


class Question8(Page):
    form_model = 'player'
    form_fields = ['answer8']

    def vars_for_template(self):
        prices_list = {"x_0_1": 8, "x_1_1": 16, "x_1_2": 4, "x_2_1": 32,
                       "x_2_2": 8, "x_2_3": 8, "x_2_4": 2, "x_3_1": 64,
                       "x_3_2": 16, "x_3_3": 16, "x_3_4": 4, "x_3_5": 16,
                       "x_3_6": 4, "x_3_7": 4, "x_3_8": 1
                       }
        wealth_list = {"w_0_1": 100, "w_1_1": 180, "w_1_2": 60, "w_2_1": 160,
                       "w_2_2": 190, "w_2_3": 90, "w_2_4": 75, "w_3_1": 220,
                       "w_3_2": 130, "w_3_3": 280, "w_3_4": 145, "w_3_5": 120,
                       "w_3_6": 75, "w_3_7": 75, "w_3_8": 75
                       }
        stock_list = {"s_0_1": 80, "s_1_1": -20, "s_1_2": 30, "s_2_1": 60,
                      "s_2_2": 90, "s_2_3": 30, "s_2_4": 0
                      }
        bond_list = {"b_0_1": 20, "b_1_1": 200, "b_1_2": 30, "b_2_1": 100,
                     "b_2_2": 100, "b_2_3": 60, "b_2_4": 75
                     }
        states_list = {"0": 1, "1": 1, "2": 2, "3": 3}

        return {
            'num_periods': 3,
            'prices': json.dumps(prices_list),
            'wealth': json.dumps(wealth_list),
            'stock': json.dumps(stock_list),
            'bond': json.dumps(bond_list),
            'realized_states': json.dumps(states_list)
        }


class Question9(Page):
    form_model = 'player'
    form_fields = ['answer9']

    def vars_for_template(self):
        prices_list = {"x_0_1": 8, "x_1_1": 16, "x_1_2": 4, "x_2_1": 32,
                       "x_2_2": 8, "x_2_3": 8, "x_2_4": 2, "x_3_1": 64,
                       "x_3_2": 16, "x_3_3": 16, "x_3_4": 4, "x_3_5": 16,
                       "x_3_6": 4, "x_3_7": 4, "x_3_8": 1
                       }
        wealth_list = {"w_0_1": 100, "w_1_1": 180, "w_1_2": 60, "w_2_1": 160,
                       "w_2_2": 190, "w_2_3": 90, "w_2_4": 75, "w_3_1": 220,
                       "w_3_2": 130, "w_3_3": 280, "w_3_4": 145, "w_3_5": 120,
                       "w_3_6": 75, "w_3_7": 75, "w_3_8": 75
                       }
        stock_list = {"s_0_1": 80, "s_1_1": -20, "s_1_2": 30, "s_2_1": 60,
                      "s_2_2": 90, "s_2_3": 30, "s_2_4": 0
                      }
        bond_list = {"b_0_1": 20, "b_1_1": 200, "b_1_2": 30, "b_2_1": 100,
                     "b_2_2": 100, "b_2_3": 60, "b_2_4": 75
                     }
        states_list = {"0": 1, "1": 2, "2": 3, "3": 5}

        return {
            'num_periods': 3,
            'prices': json.dumps(prices_list),
            'wealth': json.dumps(wealth_list),
            'stock': json.dumps(stock_list),
            'bond': json.dumps(bond_list),
            'realized_states': json.dumps(states_list)
        }


class Question10(Page):
    form_model = 'player'
    form_fields = ['answer10']

    def vars_for_template(self):
        prices_list = {"x_0_1": 8, "x_1_1": 16, "x_1_2": 4, "x_2_1": 32,
                       "x_2_2": 8, "x_2_3": 8, "x_2_4": 2, "x_3_1": 64,
                       "x_3_2": 16, "x_3_3": 16, "x_3_4": 4, "x_3_5": 16,
                       "x_3_6": 4, "x_3_7": 4, "x_3_8": 1
                       }
        wealth_list = {"w_0_1": 100, "w_1_1": 180, "w_1_2": 60, "w_2_1": 160,
                       "w_2_2": 190, "w_2_3": 90, "w_2_4": 75, "w_3_1": 220,
                       "w_3_2": 130, "w_3_3": 280, "w_3_4": 145, "w_3_5": 120,
                       "w_3_6": 75, "w_3_7": 75, "w_3_8": 75
                       }
        stock_list = {"s_0_1": 80, "s_1_1": -20, "s_1_2": 30, "s_2_1": 60,
                      "s_2_2": 90, "s_2_3": 30, "s_2_4": 0
                      }
        bond_list = {"b_0_1": 20, "b_1_1": 200, "b_1_2": 30, "b_2_1": 100,
                     "b_2_2": 100, "b_2_3": 60, "b_2_4": 75
                     }
        states_list = {"0": "", "1": "", "2": "", "3": ""}

        return {
            'num_periods': 3,
            'prices': json.dumps(prices_list),
            'wealth': json.dumps(wealth_list),
            'stock': json.dumps(stock_list),
            'bond': json.dumps(bond_list),
            'realized_states': json.dumps(states_list)
        }


page_sequence = [
    Introduction,
    Question1,
    Question2,
    Question3,
    Question4,
    Question5,
    Question6,
    Question10,
    Question7,
    Question8,
    Question9
]
