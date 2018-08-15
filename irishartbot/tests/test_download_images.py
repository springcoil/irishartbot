import pytest
import os

import irishartbot.download_images as dl
import settings

single_painting = [
    {'artistName': 'Felix Vallotton',
'image': 'https://uploads1.wikiart.org/images/felix-vallotton/portrait-of-thadee-nathanson-1897.jpg',
'map': '01234567*',
'paintingUrl': '/en/felix-vallotton/portrait-of-thadee-nathanson-1897',
'artistUrl': '/en/felix-vallotton',
'albums': None,
'flags': 2,
'images': None}]

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
    url = settings.BASE_URL + settings.STYLE_URL + '&' + settings.PAGINATION_URL + str(1)
    assert url == 'https://www.wikiart.org/en/paintings-by-style/magic-realism?json=2&page=1'


# Tests that paintings are extracted and added to a list
def test_parse_data():
    dl.parse_data(single_painting, add_painting)
    assert len(single_painting) == 2