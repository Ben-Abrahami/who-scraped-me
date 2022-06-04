import random

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import requests
import cloudscraper
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import json
from IPython.display import clear_output, display
import csv

### Testing
TEST_URL = 'https://www.whosampled.com/Jesse-Lee-Pratcher/Green-Sally,-Up/'
TEST_2_URL = "https://www.whosampled.com/The-Beatles/Come-Together/"
TEST_3_URL = "https://www.whosampled.com/Kanye-West/Power/"
TEST_4_URL = 'https://www.whosampled.com/The-Pharcyde/Runnin%27/'
NO_ALBUM_URL = 'https://www.whosampled.com/Tems/Higher-(Live)/'
SEE_ALL_URL ='https://www.whosampled.com/The-Beatles/Come-Together/covered/'
SEE_ALL_URL_2 = 'https://www.whosampled.com/Kanye-West/Power/samples/'

####
YEAR_TO_SCRAPE = '1960'  # TODO: This is the only field to edit before scraping
"""
------------------------------------------ Do not cross this line please -----------------------------------------------
"""


user_agents = [
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/100.0.4896.127 Safari\/537.36","system":"Chrome 100.0 Win10"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/101.0.4951.54 Safari\/537.36","system":"Chrome 101.0 Win10"},
{"useragent":"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/100.0.4896.127 Safari\/537.36","system":"Chrome 100.0 macOS"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko\/20100101 Firefox\/100.0","system":"Firefox 100.0 Win10"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/101.0.4951.67 Safari\/537.36","system":"Chrome 101.0 Win10"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko\/20100101 Firefox\/99.0","system":"Firefox 99.0 Win10"},
{"useragent":"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/605.1.15 (KHTML, like Gecko) Version\/15.4 Safari\/605.1.15","system":"Safari 15.4 macOS"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; rv:91.0) Gecko\/20100101 Firefox\/91.0","system":"Firefox 91.0 Win10"},
{"useragent":"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/101.0.4951.64 Safari\/537.36","system":"Chrome 101.0 macOS"},
{"useragent":"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/101.0.4951.54 Safari\/537.36","system":"Chrome 101.0 macOS"},
{"useragent":"Mozilla\/5.0 (X11; Linux x86_64; rv:100.0) Gecko\/20100101 Firefox\/100.0","system":"Firefox 100.0 Linux"},
{"useragent":"Mozilla\/5.0 (X11; Linux x86_64; rv:99.0) Gecko\/20100101 Firefox\/99.0","system":"Firefox 99.0 Linux"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/101.0.4951.41 Safari\/537.36","system":"Chrome 101.0 Win10"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/101.0.4951.64 Safari\/537.36","system":"Chrome 101.0 Win10"},
{"useragent":"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko\/20100101 Firefox\/99.0","system":"Firefox 99.0 macOS"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/100.0.4896.127 Safari\/537.36 Edg\/100.0.1185.50","system":"Edge 100.0 Win10"},
{"useragent":"Mozilla\/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko\/20100101 Firefox\/99.0","system":"Firefox 99.0 Linux"},
{"useragent":"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10.15; rv:100.0) Gecko\/20100101 Firefox\/100.0","system":"Firefox 100.0 macOS"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/100.0.4896.75 Safari\/537.36","system":"Chrome 100.0 Win10"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/100.0.4896.88 Safari\/537.36","system":"Chrome 100.0 Win10"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/101.0.4951.64 Safari\/537.36 Edg\/101.0.1210.47","system":"Edge 101.0 Win10"},
{"useragent":"Mozilla\/5.0 (X11; Linux x86_64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/100.0.4896.127 Safari\/537.36","system":"Chrome 100.0 Linux"},
{"useragent":"Mozilla\/5.0 (X11; Linux x86_64; rv:91.0) Gecko\/20100101 Firefox\/91.0","system":"Firefox 91.0 Linux"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/101.0.4951.54 Safari\/537.36 Edg\/101.0.1210.39","system":"Edge 101.0 Win10"},
{"useragent":"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/100.0.4896.88 Safari\/537.36","system":"Chrome 100.0 macOS"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/101.0.4951.41 Safari\/537.36 Edg\/101.0.1210.32","system":"Edge 101.0 Win10"},
{"useragent":"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/605.1.15 (KHTML, like Gecko) Version\/15.3 Safari\/605.1.15","system":"Safari 15.3 macOS"},
{"useragent":"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/101.0.4951.41 Safari\/537.36","system":"Chrome 101.0 macOS"},
{"useragent":"Mozilla\/5.0 (X11; Linux x86_64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/101.0.4951.54 Safari\/537.36","system":"Chrome 101.0 Linux"},
{"useragent":"Mozilla\/5.0 (X11; Linux x86_64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/101.0.4951.64 Safari\/537.36","system":"Chrome 101.0 Linux"},
{"useragent":"Mozilla\/5.0 (X11; Linux x86_64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/101.0.4951.41 Safari\/537.36","system":"Chrome 101.0 Linux"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/99.0.4844.84 Safari\/537.36 OPR\/85.0.4341.75","system":"Opera Generic Win10"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/101.0.0.0 Safari\/537.36","system":"Chrome 101.0 Win10"},
{"useragent":"Mozilla\/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/100.0.4896.127 Safari\/537.36","system":"Chrome 100.0 Win7"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/100.0.4896.127 Safari\/537.36 Edg\/100.0.1185.44","system":"Edge 100.0 Win10"},
{"useragent":"Mozilla\/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/101.0.4951.54 Safari\/537.36","system":"Chrome 101.0 Win7"},
{"useragent":"Mozilla\/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko\/20100101 Firefox\/100.0","system":"Firefox 100.0 Linux"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/98.0.4758.141 YaBrowser\/22.3.3.852 Yowser\/2.5 Safari\/537.36","system":"Yandex Browser Generic Win10"},
{"useragent":"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/605.1.15 (KHTML, like Gecko) Version\/15.2 Safari\/605.1.15","system":"Safari 15.2 macOS"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko\/20100101 Firefox\/91.0","system":"Firefox 91.0 Win10"},
{"useragent":"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/100.0.4896.75 Safari\/537.36","system":"Chrome 100.0 macOS"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/100.0.4896.60 Safari\/537.36","system":"Chrome 100.0 Win10"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/99.0.4844.84 Safari\/537.36","system":"Chrome 99.0 Win10"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; WOW64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/100.0.4896.127 Safari\/537.36","system":"Chrome 100.0 Win10"},
{"useragent":"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/605.1.15 (KHTML, like Gecko) Version\/14.1.2 Safari\/605.1.15","system":"Safari 14.1 macOS"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/99.0.4844.51 Safari\/537.36","system":"Chrome 99.0 Win10"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/99.0.4844.84 Safari\/537.36 OPR\/85.0.4341.72","system":"Opera Generic Win10"},
{"useragent":"Mozilla\/5.0 (X11; Linux x86_64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/100.0.4896.75 Safari\/537.36","system":"Chrome 100.0 Linux"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko\/20100101 Firefox\/98.0","system":"Firefox 98.0 Win10"},
{"useragent":"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/605.1.15 (KHTML, like Gecko) Version\/15.1 Safari\/605.1.15","system":"Safari 15.1 macOS"},
{"useragent":"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/605.1.15 (KHTML, like Gecko) Version\/15.5 Safari\/605.1.15","system":"Safari Generic macOS"},
{"useragent":"Mozilla\/5.0 (X11; Linux x86_64; rv:78.0) Gecko\/20100101 Firefox\/78.0","system":"Firefox 78.0 Linux"},
{"useragent":"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/79.0.3945.88 Safari\/537.36","system":"Chrome 79.0 macOS"},
{"useragent":"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit\/605.1.15 (KHTML, like Gecko) Version\/15.4 Safari\/605.1.15","system":"Safari 15.4 macOS"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/100.0.4896.127 Safari\/537.36 OPR\/86.0.4363.59","system":"Chrome 100.0 Win10"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/99.0.4844.84 Safari\/537.36 OPR\/85.0.4341.71","system":"Opera Generic Win10"},
{"useragent":"Mozilla\/5.0 (Windows NT 6.1; Win64; x64; rv:100.0) Gecko\/20100101 Firefox\/100.0","system":"Firefox 100.0 Win7"},
{"useragent":"Mozilla\/5.0 (Windows NT 6.1; Win64; x64; rv:99.0) Gecko\/20100101 Firefox\/99.0","system":"Firefox 99.0 Win7"},
{"useragent":"Mozilla\/5.0 (X11; Fedora; Linux x86_64; rv:99.0) Gecko\/20100101 Firefox\/99.0","system":"Firefox 99.0 Linux"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/98.0.4758.141 YaBrowser\/22.3.2.644 Yowser\/2.5 Safari\/537.36","system":"Yandex Browser Generic Win10"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/99.0.4844.82 Safari\/537.36","system":"Chrome 99.0 Win10"},
{"useragent":"Mozilla\/5.0 (X11; Fedora; Linux x86_64; rv:100.0) Gecko\/20100101 Firefox\/100.0","system":"Firefox 100.0 Linux"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/99.0.7113.93 Safari\/537.36","system":"Chrome 99.0 Win10"},
{"useragent":"Mozilla\/5.0 (Windows NT 10.0) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/99.0.7113.93 Safari\/537.36","system":"Chrome 99.0 Win10"}]
user_agent_rnd = random.randint(0, len(user_agents))

URL = f'https://www.whosampled.com/browse/year/{YEAR_TO_SCRAPE}/'


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# driver.execute_cdp_cmd('Network.setUserAgentOverride', user_agents[user_agent_rnd])


driver.get(URL) # i play with this for testing
driver.set_window_size(1000, 1500)
# Defining dicts
main_dict = {f'{YEAR_TO_SCRAPE}': []}
errors_dict = {f'{YEAR_TO_SCRAPE}': []}


# 1095 of 3240
def scrape():
    driver.implicitly_wait(10)
    songs_scraped = 0
    num_pages = get_number_of_pages()
    estimated_songs_to_scrape = num_pages*10

    # This loop runs on all pages
    for j in range(1, num_pages):
        all_songs_on_page = driver.find_elements(By.CLASS_NAME, 'trackCover')
        curr_url = driver.current_url

        # This loop runs on every song on single page
        for i in range(len(all_songs_on_page)):
            try:
                driver.implicitly_wait(20)
                main_dict[f'{YEAR_TO_SCRAPE}'].append(get_data_from_song(all_songs_on_page[i].get_attribute('href'), curr_url, songs_scraped))
                all_songs_on_page = driver.find_elements(By.CLASS_NAME, 'trackCover')

                songs_scraped += 1
                print(f"### {songs_scraped} songs were scraped of estimated {estimated_songs_to_scrape}")
                print(str(songs_scraped/estimated_songs_to_scrape*100) + '%')

                write_to_file('good')
            except:
                err = {
                    'url': all_songs_on_page[i].get_attribute('href')
                }
                errors_dict[f'{YEAR_TO_SCRAPE}'].append(err.copy())
                write_to_file('err')

        next_wrapper = driver.find_element(By.CLASS_NAME, 'next')
        next_button = next_wrapper.find_element(By.TAG_NAME, 'a').get_attribute('href')
        driver.get(next_button)

    driver.implicitly_wait(20)
    all_songs_on_page = driver.find_elements(By.CLASS_NAME, 'trackCover')
    curr_url = driver.current_url
    for i in range(len(all_songs_on_page)):
        main_dict[f'{YEAR_TO_SCRAPE}'].append(get_data_from_song(all_songs_on_page[i].get_attribute('href'), curr_url, songs_scraped))
        songs_scraped += 1
        print(f"### {songs_scraped} songs were scraped")
        all_songs_on_page = driver.find_elements(By.CLASS_NAME, 'trackCover')
        write_to_file('good')

    driver.quit()


def get_number_of_pages():
    pagination = driver.find_element(By.CLASS_NAME, 'pagination')
    button = pagination.find_elements(By.TAG_NAME, 'span')[-2]
    num_pages = int(button.find_element(By.TAG_NAME, 'a').text)
    return num_pages


def get_data_from_song(song_url, prev_page_url, songs_scraped):
    try:
        driver.get(song_url)
        local_song_info = {}
        driver.implicitly_wait(20)

        local_song_info['url'] = song_url  # get the current url

        local_song_info['song name'] = driver.find_element(By.TAG_NAME, 'h1').text.strip().split('\n')[0]

        dirty_artists = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/section[1]/div[2]/h1/span').text.strip()
        local_song_info['main artists'], local_song_info['featuring artists'] = clean_artists_names(dirty_artists, True)

        track_release_details = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/section[1]/div[2]/div[2]/div[1]')
        local_song_info['album'], \
        local_song_info['record label'], \
        local_song_info['producer'] = get_track_release_details(track_release_details)

        local_song_info['genre'] = get_genre()

        local_song_info['connections'] = get_all_connections()

        driver.get(prev_page_url)

        return local_song_info.copy()
    except:
        print(f'there was a problem scraping song num {songs_scraped}')
        err = {
            'url': driver.current_url
        }
        errors_dict[f'{YEAR_TO_SCRAPE}'].append(err.copy())
        write_to_file('err')


def get_all_connections():

    local_dict = {'Contains samples of': 'Nan',
                  'Was sampled in': 'Nan',
                  'Is a remix of': 'Nan',
                  'Was remixed in': 'Nan',
                  'Is a cover of': 'Nan',
                  'Was covered in': 'Nan'}

    try:
        headers = driver.find_elements(By.CLASS_NAME, 'sectionHeader')  # gets all section headers
        list_stop = 0
        for i in range(len(headers)):
            headers = driver.find_elements(By.CLASS_NAME, 'sectionHeader')  # gets all section headers
            section_name = headers[i].find_element(By.TAG_NAME, 'span').text.rsplit(' ', 2)[0]
            num_songs = int(headers[i].find_element(By.TAG_NAME, 'span').text.rsplit(' ', 2)[1])
            if num_songs > 3:
                curr_url = driver.current_url
                see_all_url = headers[i].find_element(By.TAG_NAME, 'a').get_attribute('href')
                list_stop += 3
                driver.get(see_all_url)
                time.sleep(5)
                local_dict[f'{section_name}'] = get_connections_from_see_all(curr_url)

            else:
                local_dict[f'{section_name}'] = []
                list_entries = driver.find_elements(By.CLASS_NAME, 'listEntry')
                for j in range(list_stop, list_stop + num_songs):
                    a_tags = list_entries[j].find_elements(By.TAG_NAME, 'a')

                    temp_dict = {'song name': a_tags[1].text.strip(),
                                 'artist name': clean_artists_names(list_entries[j].find_element(By.CLASS_NAME, 'trackArtist').text[:-7], False),
                                 'year': list_entries[j].find_element(By.TAG_NAME, 'span').text.rsplit(' ', 1)[1].strip('\n').strip('()')}
                    local_dict[f'{section_name}'].append(temp_dict.copy())
                list_stop += num_songs

        return local_dict.copy()


    except:
        return local_dict.copy()


def get_connections_from_see_all(prev_url):

    local_lst = []
    while True:
        list_entries = driver.find_elements(By.CLASS_NAME, 'listEntry')  # gets all list entries
        for song in list_entries:
            a_tags = song.find_elements(By.TAG_NAME, 'a')
            temp_dict = {'song name': a_tags[1].text.strip(),
                         'artist name': clean_artists_names(song.find_element(By.CLASS_NAME, 'trackArtist').text[:-7], False),
                         'year': song.find_element(By.TAG_NAME, 'span').text.rsplit(' ', 1)[1].strip('\n').strip('()')}
            local_lst.append(temp_dict.copy())
        try:
            next_wrapper = driver.find_element(By.CLASS_NAME, 'next')
            next_button = next_wrapper.find_element(By.TAG_NAME, 'a').get_attribute('href')
            driver.get(next_button)
            time.sleep(random.randint(3, 10))

        except:
            driver.get(prev_url)
            return local_lst.copy()


def get_genre():  # TODO: fix the rturn, why / ?
    genre_displayed = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/section[2]/div[1]/div[1]/a/span').is_displayed()
    try:
        element = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/section[2]/div[1]/div[1]/a/span')
        is_genre = element.get_attribute('itemprop') == 'genre'
    except:
        is_genre = False
    if genre_displayed and is_genre:
        genre = element.text.split(' / ')
        return genre
    return 'Nan'


def get_track_release_details(details):
    """
    :param details: A <div> with class = 'trackReleaseDetails', holding three h3 tags with relevant data.
    :return: cleaned, album, record label and producer data.
    """
    h3_tags = details.find_elements(By.TAG_NAME, 'h3')
    album = 'Nan'
    record_label = 'Nan'
    producer = 'Nan'
    for tag in h3_tags:
        # print(tag.text.strip())  # for debugging
        if tag.get_attribute('class') == "release-name":
            album = tag.text.strip()

        elif tag.get_attribute('class') == "label-details":
            record_label = tag.find_element(By.TAG_NAME, "span").text.strip()
            if record_label == '':
                record_label = 'Nan'

        elif tag.is_displayed():
            producers = tag.find_elements(By.TAG_NAME, 'a')
            producer = []
            for single_producer in producers:
                producer.append(single_producer.text.strip())

    return album, record_label, producer


def clean_artists_names(artists_names, main):
    artists_names = artists_names[3:]
    if main:
        if 'feat.' in artists_names:
            feat_index = artists_names.index(' feat. ')
            featuring_artists = artists_names[feat_index + 7:]
            artists_names = artists_names[:feat_index]
        else:
            featuring_artists = 'Nan'
        if 'and' in artists_names:
            artists_names = artists_names.split(' and ')

        if 'and' in featuring_artists:
            featuring_artists = featuring_artists.split(' and ')

        return artists_names, featuring_artists

    else:
        if 'feat.' in artists_names:
            feat_index = artists_names.index(' feat. ')
            artists_names = artists_names[:feat_index]
        if 'and' in artists_names:
            artists_names = artists_names.split(' and ')
        return artists_names


def write_to_file(which_file):
    if which_file == 'err':
        file = open(f'{YEAR_TO_SCRAPE} errors.json', "w")
        json.dump(main_dict, file, indent=4, sort_keys=False)
        file.close()
        print("added to *error* file!")
    else:
        file = open(f'{YEAR_TO_SCRAPE}.json', "w")
        json.dump(main_dict, file, indent=4, sort_keys=False)
        file.close()
        print("added to file!")
        print()


if __name__ == '__main__':
    scrape()
    # get_data_from_song(TEST_2_URL, URL_1960, 0)
    # get_all_connections(TEST_4_URL)
    # get_connections_from_see_all(url='https://www.whosampled.com/The-Pharcyde/Runnin%27/', prev_url=TEST_4_URL)
    driver.quit()
