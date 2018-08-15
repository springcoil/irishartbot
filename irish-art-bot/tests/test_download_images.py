import pytest
import os

import irishartbot.download_images as dl
import settings

single_painting = [
{
'contentId': 366641,
'artistName': 'James Barry',
'url': 'james-barry',
'lastNameFirst': 'Barry James ',
'birthDay': '/Date(-7202044800000)/',
'deathDay': '/Date(-5170867200000)/',
'birthDayAsString': '11 October 1741',
'deathDayAsString': '22 February 1806',
'image': 'https://uploads8.wikiart.org/temp/e5d029a2-cd5f-499b-afe1-092d9fd1426c.jpg!Portrait.jpg',
'wikipediaUrl': 'https://en.wikipedia.org/wiki/James_Barry_(painter)',
'dictonaries': [
8915,
2618,
309,
310
]},]

add_painting = [
{
'contentId': 358753,
'artistName': 'Paul Kane',
'url': 'paul-kane',
'lastNameFirst': 'Kane Paul ',
'birthDay': '/Date(-5027961600000)/',
'deathDay': '/Date(-3119817600000)/',
'birthDayAsString': '03 September 1810',
'deathDayAsString': '20 February 1871',
'image': 'https://uploads1.wikiart.org/images/paul-kane.jpg!Portrait.jpg',
'wikipediaUrl': 'http://en.wikipedia.org/wiki/Paul_Kane',
'dictonaries': [
15842,
2618,
310
]
},
]
def test_build_url():
    url = settings.BASE_URL + settings.COUNTRY_URL + str(1)
    assert url == 'https://www.wikiart.org/en/artists-by-nation/irish/results?json=1'


# Tests that paintings are extracted and added to a list
def test_parse_data():
    dl.parse_data(single_painting, add_painting)
    assert len(single_painting) == 2