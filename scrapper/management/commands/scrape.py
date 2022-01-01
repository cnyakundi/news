from django.core.management.base import BaseCommand
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import requests

from scrapper.models import Post


class Command(BaseCommand):
    help = "collect jobs"
    # define logic of command
    def handle(self, *args, **options):



        URL = 'https://www.cnyakundi.com/'
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        # grab all postings
        posts = soup.find_all('div', class_='zox-art-title')
        for post in posts:
            url = post.find('a')['href']
            title = post.find('h2').text

            # check if url in db
            try:
                # save in db
                Post.objects.create(
                    url=url,
                    title=title,

                )
                print('%s added' % (title,))

            except:
                print('%s already exists' % (title,))
        self.stdout.write( 'job complete' )