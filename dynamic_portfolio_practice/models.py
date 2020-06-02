import json
import numpy

from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'dynamic_portfolio_practice'
    players_per_group = None
    num_rounds = 4
    initial_wealth_list = [120, 80, 200, 50]
    initial_stock_price = 8
    up_prob = 0.5
    up_tick = 2
    down_tick = 0.5
    num_periods = 2


class Subsession(BaseSubsession):
    num_periods = models.IntegerField()
    initial_wealth = models.IntegerField()
    dyn_prices = models.StringField()

    def creating_session(self):
        if self.round_number == 1:
            num_rounds = Constants.num_rounds
            for r in range(1, num_rounds+1):
                t = Constants.num_periods
                self.in_round(r).num_periods = t
                self.in_round(r).initial_wealth = Constants.initial_wealth_list[r-1]
                price_label = "x_{}_{}"
                dyn_prices_list = {"x_0_1": Constants.initial_stock_price}
                for s in range(1, t+1, 1):
                    for i in range(1, 2**s+1, 1):
                        previous_i = int((i + 1)/2)
                        previous_price = dyn_prices_list[price_label.format(s-1, previous_i)]
                        if i % 2 == 0:
                            current_price = previous_price * Constants.down_tick
                        else:
                            current_price = previous_price * Constants.up_tick
                        dyn_prices_list[price_label.format(s, i)] = current_price
                self.in_round(r).dyn_prices = json.dumps(dyn_prices_list)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    dyn_wealth = models.StringField()
    dyn_stock = models.StringField()
    dyn_bond = models.StringField()
    dyn_realized_states = models.StringField()
    dyn_realized_wealth = models.FloatField()

    def dyn_get_outcome(self):
        upticks = numpy.random.binomial(1, Constants.up_prob, size=self.subsession.num_periods)
        downticks = 1 - upticks
        downticks = downticks.tolist()  # type: numpy.ndarray
        realized_states = {"0": 1}
        for t in range(1, self.subsession.num_periods+1, 1):
            state = 1
            for s in range(t):
                state = state + downticks[s] * 2**(t-s-1)
                realized_states[str(t)] = state
        self.dyn_realized_states = json.dumps(realized_states)
        wealth_list = json.loads(self.dyn_wealth)
        wealth_label = "w_{}_{}"
        final_t = self.subsession.num_periods
        final_state = realized_states[str(final_t)]
        self.dyn_realized_wealth = wealth_list[wealth_label.format(final_t, final_state)]
