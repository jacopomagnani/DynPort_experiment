from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'static_portfolio_quiz'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer1 = models.IntegerField(
        choices=[
            [1, '1'],
            [2, '10'],
            [3, '100'],
            [4, '1000']
        ],
        widget=widgets.RadioSelect
    )

    def answer1_error_message(self, value):
        if value != 4:
            return 'Wrong answer, try again.'

    answer2 = models.IntegerField(
        choices=[
            [1, '2'],
            [2, '20'],
            [3, '200'],
            [4, '2000']
        ],
        widget=widgets.RadioSelect
    )

    def answer2_error_message(self, value):
        if value != 3:
            return 'Wrong answer, try again.'

    answer3 = models.IntegerField(
        choices=[
            [1, 'The first lottery.'],
            [2, 'The eighth lottery.'],
            [3, 'A randomly selected lottery.'],
            [4, 'All of the lotteries.']
        ],
        widget=widgets.RadioSelect
    )

    def answer3_error_message(self, value):
        if value != 3:
            return 'Wrong answer, try again.'

    answer4 = models.IntegerField(
        choices=[
            [1, '1/8'],
            [2, '2/8'],
            [3, '4/8'],
            [4, '6/8']
        ],
        widget=widgets.RadioSelect
    )

    def answer4_error_message(self, value):
        if value != 1:
            return 'Wrong answer, try again.'

    answer5 = models.IntegerField(
        choices=[
            [1, '1/8'],
            [2, '2/8'],
            [3, '4/8'],
            [4, '6/8']
        ],
        widget=widgets.RadioSelect
    )

    def answer5_error_message(self, value):
        if value != 1:
            return 'Wrong answer, try again.'

    answer6 = models.IntegerField(
        choices=[
            [1, '5'],
            [2, '7.41'],
            [3, '50'],
            [4, '3.7']
        ],
        widget=widgets.RadioSelect
    )

    def answer6_error_message(self, value):
        if value != 3:
            return 'Wrong answer, try again.'

    answer7 = models.IntegerField(
        choices=[
            [1, '0'],
            [2, '100'],
            [3, '200'],
            [4, '1000']
        ],
        widget=widgets.RadioSelect
    )

    def answer7_error_message(self, value):
        if value != 2:
            return 'Wrong answer, try again.'
