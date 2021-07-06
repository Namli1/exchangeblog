# Generated by Django 3.2 on 2021-07-03 10:34

from django.db import migrations, models
import imagekit.models.fields
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exchangeblog', '0003_alter_blogpost_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogauthor',
            name='social_media_link',
        ),
        migrations.AddField(
            model_name='blogauthor',
            name='profile_image',
            field=imagekit.models.fields.ProcessedImageField(default='images/default_profile_image.jpg', upload_to='profile_images/', verbose_name='Profile Image'),
        ),
        migrations.AlterField(
            model_name='blogauthor',
            name='allowed_countries',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('AF', '🇦🇫Afghanistan'), ('AL', '🇦🇱Albania'), ('DZ', '🇩🇿Algeria'), ('AD', '🇦🇩Andorra'), ('AO', '🇦🇴Angola'), ('AQ', '🇦🇶Antarctica'), ('AR', '🇦🇷Argentina'), ('AM', '🇦🇲Armenia'), ('AW', '🇦🇼Aruba'), ('AU', '🇦🇺Australia'), ('AT', '🇦🇹Austria'), ('AZ', '🇦🇿Azerbaijan'), ('BS', '🇧🇸Bahamas'), ('BH', '🇧🇭Bahrain'), ('BD', '🇧🇩Bangladesh'), ('BB', '🇧🇧Barbados'), ('BY', '🇧🇾Belarus'), ('BE', '🇧🇪Belgium'), ('BZ', '🇧🇿Belize'), ('BJ', '🇧🇯Benin'), ('BM', '🇧🇲Bermuda'), ('BT', '🇧🇹Bhutan'), ('BO', '🇧🇴Bolivia'), ('BA', '🇧🇦Bosnia & Herzegovina'), ('BW', '🇧🇼Botswana'), ('BR', '🇧🇷Brazil'), ('BN', '🇧🇳Brunei'), ('BG', '🇧🇬Bulgaria'), ('BF', '🇧🇫Burkina Faso'), ('BI', '🇧🇮Burundi'), ('KH', '🇰🇭Cambodia'), ('CM', '🇨🇲Cameroon'), ('CA', '🇨🇦Canada'), ('CV', '🇨🇻Cape Verde'), ('CF', '🇨🇫Central African Republic'), ('TD', '🇹🇩Chad'), ('CL', '🇨🇱Chile'), ('CN', '🇨🇳China'), ('CO', '🇨🇴Colombia'), ('KM', '🇰🇲Comoros'), ('CG', '🇨🇬Congo - Brazzaville'), ('CD', '🇨🇩Congo - Kinshasa'), ('CR', '🇨🇷Costa Rica'), ('CI', '🇨🇮Côte d’Ivoire'), ('HR', '🇭🇷Croatia'), ('CU', '🇨🇺Cuba'), ('CW', '🇨🇼Curaçao'), ('CY', '🇨🇾Cyprus'), ('CZ', '🇨🇿Czechia'), ('DK', '🇩🇰Denmark'), ('DJ', '🇩🇯Djibouti'), ('DM', '🇩🇲Dominica'), ('DO', '🇩🇴Dominican Republic'), ('EC', '🇪🇨Ecuador'), ('EG', '🇪🇬Egypt'), ('SV', '🇸🇻El Salvador'), ('GQ', '🇬🇶Equatorial Guinea'), ('ER', '🇪🇷Eritrea'), ('EE', '🇪🇪Estonia'), ('SZ', '🇸🇿Eswatini'), ('ET', '🇪🇹Ethiopia'), ('FK', '🇫🇰Falkland Islands'), ('FO', '🇫🇴Faroe Islands'), ('FJ', '🇫🇯Fiji'), ('FI', '🇫🇮Finland'), ('FR', '🇫🇷France'), ('GF', '🇬🇫French Guiana'), ('PF', '🇵🇫French Polynesia'), ('GA', '🇬🇦Gabon'), ('GM', '🇬🇲Gambia'), ('GE', '🇬🇪Georgia'), ('DE', '🇩🇪Germany'), ('GH', '🇬🇭Ghana'), ('GI', '🇬🇮Gibraltar'), ('GR', '🇬🇷Greece'), ('GL', '🇬🇱Greenland'), ('GD', '🇬🇩Grenada'), ('GP', '🇬🇵Guadeloupe'), ('GU', '🇬🇺Guam'), ('GT', '🇬🇹Guatemala'), ('GG', '🇬🇬Guernsey'), ('GN', '🇬🇳Guinea'), ('GW', '🇬🇼Guinea-Bissau'), ('GY', '🇬🇾Guyana'), ('HT', '🇭🇹Haiti'), ('HN', '🇭🇳Honduras'), ('HK', '🇭🇰Hong Kong SAR China'), ('HU', '🇭🇺Hungary'), ('IS', '🇮🇸Iceland'), ('IN', '🇮🇳India'), ('ID', '🇮🇩Indonesia'), ('IR', '🇮🇷Iran'), ('IQ', '🇮🇶Iraq'), ('IE', '🇮🇪Ireland'), ('IM', '🇮🇲Isle of Man'), ('IL', '🇮🇱Israel'), ('IT', '🇮🇹Italy'), ('JM', '🇯🇲Jamaica'), ('JP', '🇯🇵Japan'), ('JE', '🇯🇪Jersey'), ('JO', '🇯🇴Jordan'), ('KZ', '🇰🇿Kazakhstan'), ('KE', '🇰🇪Kenya'), ('KI', '🇰🇮Kiribati'), ('KW', '🇰🇼Kuwait'), ('KG', '🇰🇬Kyrgyzstan'), ('LA', '🇱🇦Laos'), ('LV', '🇱🇻Latvia'), ('LB', '🇱🇧Lebanon'), ('LS', '🇱🇸Lesotho'), ('LR', '🇱🇷Liberia'), ('LY', '🇱🇾Libya'), ('LI', '🇱🇮Liechtenstein'), ('LT', '🇱🇹Lithuania'), ('LU', '🇱🇺Luxembourg'), ('MO', '🇲🇴Macao SAR China'), ('MG', '🇲🇬Madagascar'), ('MW', '🇲🇼Malawi'), ('MY', '🇲🇾Malaysia'), ('MV', '🇲🇻Maldives'), ('ML', '🇲🇱Mali'), ('MT', '🇲🇹Malta'), ('MH', '🇲🇭Marshall Islands'), ('MQ', '🇲🇶Martinique'), ('MR', '🇲🇷Mauritania'), ('MU', '🇲🇺Mauritius'), ('YT', '🇾🇹Mayotte'), ('MX', '🇲🇽Mexico'), ('FM', '🇫🇲Micronesia'), ('MD', '🇲🇩Moldova'), ('MC', '🇲🇨Monaco'), ('MN', '🇲🇳Mongolia'), ('ME', '🇲🇪Montenegro'), ('MS', '🇲🇸Montserrat'), ('MA', '🇲🇦Morocco'), ('MZ', '🇲🇿Mozambique'), ('MM', '🇲🇲Myanmar (Burma)'), ('NA', '🇳🇦Namibia'), ('NR', '🇳🇷Nauru'), ('NP', '🇳🇵Nepal'), ('NL', '🇳🇱Netherlands'), ('NC', '🇳🇨New Caledonia'), ('NZ', '🇳🇿New Zealand'), ('NI', '🇳🇮Nicaragua'), ('NE', '🇳🇪Niger'), ('NG', '🇳🇬Nigeria'), ('NU', '🇳🇺Niue'), ('NF', '🇳🇫Norfolk Island'), ('KP', '🇰🇵North Korea'), ('MK', '🇲🇰North Macedonia'), ('NO', '🇳🇴Norway'), ('OM', '🇴🇲Oman'), ('PK', '🇵🇰Pakistan'), ('PW', '🇵🇼Palau'), ('PS', '🇵🇸Palestinian Territories'), ('PA', '🇵🇦Panama'), ('PG', '🇵🇬Papua New Guinea'), ('PY', '🇵🇾Paraguay'), ('PE', '🇵🇪Peru'), ('PH', '🇵🇭Philippines'), ('PN', '🇵🇳Pitcairn Islands'), ('PL', '🇵🇱Poland'), ('PT', '🇵🇹Portugal'), ('PR', '🇵🇷Puerto Rico'), ('QA', '🇶🇦Qatar'), ('RE', '🇷🇪Réunion'), ('RO', '🇷🇴Romania'), ('RU', '🇷🇺Russia'), ('RW', '🇷🇼Rwanda'), ('WS', '🇼🇸Samoa'), ('SM', '🇸🇲San Marino'), ('ST', '🇸🇹São Tomé & Príncipe'), ('SA', '🇸🇦Saudi Arabia'), ('SN', '🇸🇳Senegal'), ('RS', '🇷🇸Serbia'), ('SC', '🇸🇨Seychelles'), ('SL', '🇸🇱Sierra Leone'), ('SG', '🇸🇬Singapore'), ('SX', '🇸🇽Sint Maarten'), ('SK', '🇸🇰Slovakia'), ('SI', '🇸🇮Slovenia'), ('SB', '🇸🇧Solomon Islands'), ('SO', '🇸🇴Somalia'), ('ZA', '🇿🇦South Africa'), ('KR', '🇰🇷South Korea'), ('SS', '🇸🇸South Sudan'), ('ES', '🇪🇸Spain'), ('LK', '🇱🇰Sri Lanka'), ('SH', '🇸🇭St. Helena'), ('LC', '🇱🇨St. Lucia'), ('MF', '🇲🇫St. Martin'), ('SD', '🇸🇩Sudan'), ('SR', '🇸🇷Suriname'), ('SE', '🇸🇪Sweden'), ('CH', '🇨🇭Switzerland'), ('SY', '🇸🇾Syria'), ('TW', '🇹🇼Taiwan'), ('TJ', '🇹🇯Tajikistan'), ('TZ', '🇹🇿Tanzania'), ('TH', '🇹🇭Thailand'), ('TL', '🇹🇱Timor-Leste'), ('TG', '🇹🇬Togo'), ('TK', '🇹🇰Tokelau'), ('TO', '🇹🇴Tonga'), ('TT', '🇹🇹Trinidad & Tobago'), ('TN', '🇹🇳Tunisia'), ('TR', '🇹🇷Turkey'), ('TM', '🇹🇲Turkmenistan'), ('TC', '🇹🇨Turks & Caicos Islands'), ('TV', '🇹🇻Tuvalu'), ('UG', '🇺🇬Uganda'), ('UA', '🇺🇦Ukraine'), ('AE', '🇦🇪United Arab Emirates'), ('GB', '🇬🇧United Kingdom'), ('US', '🇺🇸United States'), ('UY', '🇺🇾Uruguay'), ('UZ', '🇺🇿Uzbekistan'), ('VU', '🇻🇺Vanuatu'), ('VA', '🇻🇦Vatican City'), ('VE', '🇻🇪Venezuela'), ('VN', '🇻🇳Vietnam'), ('WF', '🇼🇫Wallis & Futuna'), ('EH', '🇪🇭Western Sahara'), ('YE', '🇾🇪Yemen'), ('ZM', '🇿🇲Zambia'), ('ZW', '🇿🇼Zimbabwe')], help_text='The countries this author can write about in a country guide post.', max_length=677, null=True, verbose_name='Allowed countries'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='country',
            field=models.CharField(choices=[('AF', '🇦🇫Afghanistan'), ('AL', '🇦🇱Albania'), ('DZ', '🇩🇿Algeria'), ('AD', '🇦🇩Andorra'), ('AO', '🇦🇴Angola'), ('AQ', '🇦🇶Antarctica'), ('AR', '🇦🇷Argentina'), ('AM', '🇦🇲Armenia'), ('AW', '🇦🇼Aruba'), ('AU', '🇦🇺Australia'), ('AT', '🇦🇹Austria'), ('AZ', '🇦🇿Azerbaijan'), ('BS', '🇧🇸Bahamas'), ('BH', '🇧🇭Bahrain'), ('BD', '🇧🇩Bangladesh'), ('BB', '🇧🇧Barbados'), ('BY', '🇧🇾Belarus'), ('BE', '🇧🇪Belgium'), ('BZ', '🇧🇿Belize'), ('BJ', '🇧🇯Benin'), ('BM', '🇧🇲Bermuda'), ('BT', '🇧🇹Bhutan'), ('BO', '🇧🇴Bolivia'), ('BA', '🇧🇦Bosnia & Herzegovina'), ('BW', '🇧🇼Botswana'), ('BR', '🇧🇷Brazil'), ('BN', '🇧🇳Brunei'), ('BG', '🇧🇬Bulgaria'), ('BF', '🇧🇫Burkina Faso'), ('BI', '🇧🇮Burundi'), ('KH', '🇰🇭Cambodia'), ('CM', '🇨🇲Cameroon'), ('CA', '🇨🇦Canada'), ('CV', '🇨🇻Cape Verde'), ('CF', '🇨🇫Central African Republic'), ('TD', '🇹🇩Chad'), ('CL', '🇨🇱Chile'), ('CN', '🇨🇳China'), ('CO', '🇨🇴Colombia'), ('KM', '🇰🇲Comoros'), ('CG', '🇨🇬Congo - Brazzaville'), ('CD', '🇨🇩Congo - Kinshasa'), ('CR', '🇨🇷Costa Rica'), ('CI', '🇨🇮Côte d’Ivoire'), ('HR', '🇭🇷Croatia'), ('CU', '🇨🇺Cuba'), ('CW', '🇨🇼Curaçao'), ('CY', '🇨🇾Cyprus'), ('CZ', '🇨🇿Czechia'), ('DK', '🇩🇰Denmark'), ('DJ', '🇩🇯Djibouti'), ('DM', '🇩🇲Dominica'), ('DO', '🇩🇴Dominican Republic'), ('EC', '🇪🇨Ecuador'), ('EG', '🇪🇬Egypt'), ('SV', '🇸🇻El Salvador'), ('GQ', '🇬🇶Equatorial Guinea'), ('ER', '🇪🇷Eritrea'), ('EE', '🇪🇪Estonia'), ('SZ', '🇸🇿Eswatini'), ('ET', '🇪🇹Ethiopia'), ('FK', '🇫🇰Falkland Islands'), ('FO', '🇫🇴Faroe Islands'), ('FJ', '🇫🇯Fiji'), ('FI', '🇫🇮Finland'), ('FR', '🇫🇷France'), ('GF', '🇬🇫French Guiana'), ('PF', '🇵🇫French Polynesia'), ('GA', '🇬🇦Gabon'), ('GM', '🇬🇲Gambia'), ('GE', '🇬🇪Georgia'), ('DE', '🇩🇪Germany'), ('GH', '🇬🇭Ghana'), ('GI', '🇬🇮Gibraltar'), ('GR', '🇬🇷Greece'), ('GL', '🇬🇱Greenland'), ('GD', '🇬🇩Grenada'), ('GP', '🇬🇵Guadeloupe'), ('GU', '🇬🇺Guam'), ('GT', '🇬🇹Guatemala'), ('GG', '🇬🇬Guernsey'), ('GN', '🇬🇳Guinea'), ('GW', '🇬🇼Guinea-Bissau'), ('GY', '🇬🇾Guyana'), ('HT', '🇭🇹Haiti'), ('HN', '🇭🇳Honduras'), ('HK', '🇭🇰Hong Kong SAR China'), ('HU', '🇭🇺Hungary'), ('IS', '🇮🇸Iceland'), ('IN', '🇮🇳India'), ('ID', '🇮🇩Indonesia'), ('IR', '🇮🇷Iran'), ('IQ', '🇮🇶Iraq'), ('IE', '🇮🇪Ireland'), ('IM', '🇮🇲Isle of Man'), ('IL', '🇮🇱Israel'), ('IT', '🇮🇹Italy'), ('JM', '🇯🇲Jamaica'), ('JP', '🇯🇵Japan'), ('JE', '🇯🇪Jersey'), ('JO', '🇯🇴Jordan'), ('KZ', '🇰🇿Kazakhstan'), ('KE', '🇰🇪Kenya'), ('KI', '🇰🇮Kiribati'), ('KW', '🇰🇼Kuwait'), ('KG', '🇰🇬Kyrgyzstan'), ('LA', '🇱🇦Laos'), ('LV', '🇱🇻Latvia'), ('LB', '🇱🇧Lebanon'), ('LS', '🇱🇸Lesotho'), ('LR', '🇱🇷Liberia'), ('LY', '🇱🇾Libya'), ('LI', '🇱🇮Liechtenstein'), ('LT', '🇱🇹Lithuania'), ('LU', '🇱🇺Luxembourg'), ('MO', '🇲🇴Macao SAR China'), ('MG', '🇲🇬Madagascar'), ('MW', '🇲🇼Malawi'), ('MY', '🇲🇾Malaysia'), ('MV', '🇲🇻Maldives'), ('ML', '🇲🇱Mali'), ('MT', '🇲🇹Malta'), ('MH', '🇲🇭Marshall Islands'), ('MQ', '🇲🇶Martinique'), ('MR', '🇲🇷Mauritania'), ('MU', '🇲🇺Mauritius'), ('YT', '🇾🇹Mayotte'), ('MX', '🇲🇽Mexico'), ('FM', '🇫🇲Micronesia'), ('MD', '🇲🇩Moldova'), ('MC', '🇲🇨Monaco'), ('MN', '🇲🇳Mongolia'), ('ME', '🇲🇪Montenegro'), ('MS', '🇲🇸Montserrat'), ('MA', '🇲🇦Morocco'), ('MZ', '🇲🇿Mozambique'), ('MM', '🇲🇲Myanmar (Burma)'), ('NA', '🇳🇦Namibia'), ('NR', '🇳🇷Nauru'), ('NP', '🇳🇵Nepal'), ('NL', '🇳🇱Netherlands'), ('NC', '🇳🇨New Caledonia'), ('NZ', '🇳🇿New Zealand'), ('NI', '🇳🇮Nicaragua'), ('NE', '🇳🇪Niger'), ('NG', '🇳🇬Nigeria'), ('NU', '🇳🇺Niue'), ('NF', '🇳🇫Norfolk Island'), ('KP', '🇰🇵North Korea'), ('MK', '🇲🇰North Macedonia'), ('NO', '🇳🇴Norway'), ('OM', '🇴🇲Oman'), ('PK', '🇵🇰Pakistan'), ('PW', '🇵🇼Palau'), ('PS', '🇵🇸Palestinian Territories'), ('PA', '🇵🇦Panama'), ('PG', '🇵🇬Papua New Guinea'), ('PY', '🇵🇾Paraguay'), ('PE', '🇵🇪Peru'), ('PH', '🇵🇭Philippines'), ('PN', '🇵🇳Pitcairn Islands'), ('PL', '🇵🇱Poland'), ('PT', '🇵🇹Portugal'), ('PR', '🇵🇷Puerto Rico'), ('QA', '🇶🇦Qatar'), ('RE', '🇷🇪Réunion'), ('RO', '🇷🇴Romania'), ('RU', '🇷🇺Russia'), ('RW', '🇷🇼Rwanda'), ('WS', '🇼🇸Samoa'), ('SM', '🇸🇲San Marino'), ('ST', '🇸🇹São Tomé & Príncipe'), ('SA', '🇸🇦Saudi Arabia'), ('SN', '🇸🇳Senegal'), ('RS', '🇷🇸Serbia'), ('SC', '🇸🇨Seychelles'), ('SL', '🇸🇱Sierra Leone'), ('SG', '🇸🇬Singapore'), ('SX', '🇸🇽Sint Maarten'), ('SK', '🇸🇰Slovakia'), ('SI', '🇸🇮Slovenia'), ('SB', '🇸🇧Solomon Islands'), ('SO', '🇸🇴Somalia'), ('ZA', '🇿🇦South Africa'), ('KR', '🇰🇷South Korea'), ('SS', '🇸🇸South Sudan'), ('ES', '🇪🇸Spain'), ('LK', '🇱🇰Sri Lanka'), ('SH', '🇸🇭St. Helena'), ('LC', '🇱🇨St. Lucia'), ('MF', '🇲🇫St. Martin'), ('SD', '🇸🇩Sudan'), ('SR', '🇸🇷Suriname'), ('SE', '🇸🇪Sweden'), ('CH', '🇨🇭Switzerland'), ('SY', '🇸🇾Syria'), ('TW', '🇹🇼Taiwan'), ('TJ', '🇹🇯Tajikistan'), ('TZ', '🇹🇿Tanzania'), ('TH', '🇹🇭Thailand'), ('TL', '🇹🇱Timor-Leste'), ('TG', '🇹🇬Togo'), ('TK', '🇹🇰Tokelau'), ('TO', '🇹🇴Tonga'), ('TT', '🇹🇹Trinidad & Tobago'), ('TN', '🇹🇳Tunisia'), ('TR', '🇹🇷Turkey'), ('TM', '🇹🇲Turkmenistan'), ('TC', '🇹🇨Turks & Caicos Islands'), ('TV', '🇹🇻Tuvalu'), ('UG', '🇺🇬Uganda'), ('UA', '🇺🇦Ukraine'), ('AE', '🇦🇪United Arab Emirates'), ('GB', '🇬🇧United Kingdom'), ('US', '🇺🇸United States'), ('UY', '🇺🇾Uruguay'), ('UZ', '🇺🇿Uzbekistan'), ('VU', '🇻🇺Vanuatu'), ('VA', '🇻🇦Vatican City'), ('VE', '🇻🇪Venezuela'), ('VN', '🇻🇳Vietnam'), ('WF', '🇼🇫Wallis & Futuna'), ('EH', '🇪🇭Western Sahara'), ('YE', '🇾🇪Yemen'), ('ZM', '🇿🇲Zambia'), ('ZW', '🇿🇼Zimbabwe')], default='CH', help_text='Select the exchange country.', max_length=2, verbose_name='Country'),
        ),
    ]
