from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import json
import numpy

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'static_portfolio_practice'
    players_per_group = None
    num_rounds = 2
    initial_wealth = 100
    up_prob = 0.5
    up_tick = 2
    down_tick = 0.5
    initial_wealth_list = [120, 80]
    num_periods = 2


class Subsession(BaseSubsession):
    num_periods = models.IntegerField()
    static_prices = models.StringField()
    initial_wealth = models.IntegerField()

    def creating_session(self):
        if self.round_number == 1:
            num_rounds = Constants.num_rounds
            for r in range(1, num_rounds+1):
                t = Constants.num_periods
                self.in_round(r).num_periods = t
                self.in_round(r).initial_wealth = Constants.initial_wealth_list[r - 1]
                price_label = "p_{}"
                static_price_list = {"p_1": 0}
                for i in range(1, 2**t+1, 1):
                    num_up = 0
                    j = i
                    for s in range(t):
                        if j % 2 == 1:
                            num_up = num_up + 1
                        j = int((j + 1)/2)
                    num_down = t - num_up
                    price = (1/3)**num_up * (2/3)**num_down
                    static_price_list[price_label.format(i)] = round(price, 4)
                self.in_round(r).static_prices = json.dumps(static_price_list)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    static_securities = models.StringField()
    static_realized_state = models.IntegerField()
    static_realized_pay = models.FloatField()

    def static_get_outcome(self):
        self.static_realized_state = numpy.random.randint(1, 2**self.subsession.num_periods+1)
        securities_list = json.loads(self.static_securities)
        security_label = "q_{}"
        self.static_realized_pay = securities_list[security_label.format(self.static_realized_state)]
