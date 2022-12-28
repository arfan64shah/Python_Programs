# my_app/views.py
import otree

from otree.api import Currency as c, currency_range
from otree.api import Submission
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

class Constants(BaseConstants):
    name_in_url = 'my_game'
    players_per_group = 2
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    contribution = models.CurrencyField(min=0, max=100)

    def other_player(self):
        return self.get_others_in_group()[0]

def before_next_page(self):
    self.group.total_contribution = sum([p.contribution for p in self.group.get_players()])

class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

class Results(Page):
    pass
