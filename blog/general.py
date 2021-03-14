from django.utils.translation import ugettext_lazy as _

LANGUAGE_CHOICES = [
        ('EN', 'English'),
        ('DE', 'Deutsch'),
        ('IT', 'Italiano'),
        ('FR', 'Français'),
        ('ZH', '中文'),
        ('HI', 'हिन्दी'),
        ('BN', 'বাংলা'),
        ('PT', 'Português'),
        ('RU', 'Русский язык'),
        ('JA', '日本語'),
]

COUNTRY_CHOICES = [
        ('CN', _('🇨🇳China')),
        ('US', _('🇺🇸USA')),
        ('GB', _('🇬🇧United Kingdom')),
        ('DE', _('🇩🇪Germany')),
        ('IT', _('🇮🇹Italy')),
        ('FR', _('🇫🇷France')),
        ('TH', _('🇹🇭Thailand')),
        ('JP', _('🇯🇵Japan')),
        ('IN', _('🇮🇳India')),
]

YEAR_CHOICES = [
    (2019, 2019),
    (2020, 2020),
    (2021, 2021),
]