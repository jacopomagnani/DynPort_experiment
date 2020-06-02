from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 5.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'DynPort',
        'display_name': "Experiment",
        'num_demo_participants': 1,
        'app_sequence': ['introduction',
                         'dynamic_portfolio_instructions',
                         'dynamic_portfolio_practice',
                         'dynamic_portfolio_quiz',
                         'dynamic_portfolio',
                         'static_portfolio_instructions',
                         'static_portfolio_practice',
                         'static_portfolio_quiz',
                         'static_portfolio',
                         'dynamic_portfolio_results',
                         'static_portfolio_results',
                         'crt',
                         'survey',
                         'finalpage'],
        'round1_T': 3,
        'round2_T': 4
    },
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'AUD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '@p7=^gv5pzv0udwk!c0b0hboi#0z5t0-#8v&!*y=zj4km!t@-^'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
