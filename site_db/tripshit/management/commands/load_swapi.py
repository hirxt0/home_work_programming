from django.core.management.base import BaseCommand
import requests
from tripshit.models import Starship, Movie, Personage
import time

class Command(BaseCommand):

    help = 'загрузка данных в ДБ'


    def fetch_all(self, endpoint):

        data = []
        url = f'https://swapi.dev/api/{endpoint}/'

        while url:
            try:
                self.stdout.write(f'Запрос: {url}')
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                
                result = response.json()
                data.extend(result['results'])
                url = result['next']
                
                time.sleep(0.5)
                
            except requests.exceptions.JSONDecodeError as e:
                self.stdout.write(self.style.ERROR(f'Ошибка JSON для {url}'))
                self.stdout.write(self.style.WARNING(f'Ответ: {response.text[:500]}'))
                break
            except requests.exceptions.RequestException as e:
                self.stdout.write(self.style.ERROR(f'Ошибка запроса: {e}'))
                time.sleep(2)
                break
        
        return data 
    

    def handle(self, *args, **options):
        
        self.stdout.write("загрузка фильмов")
        films_data = self.fetch_all('films')

        for film_data in films_data:
            Movie.objects.update_or_create(
                url=film_data['url'],
                defaults={
                    'title': film_data['title'],
                    'release_date': film_data['release_date'],
                }
            )

        
        self.stdout.write("загрузка кораблей")
        ships_data = self.fetch_all('starships')

        for ship_data in ships_data:
            starship, _ = Starship.objects.update_or_create(
                url=ship_data['url'],
                defaults={
                    'name': ship_data['name'],
                    'max_atmosphering_speed': ship_data['max_atmosphering_speed'],

                }
            )
            
            if ship_data.get('films'):
                film_objects = Movie.objects.filter(url__in=ship_data['films'])
                starship.films.set(film_objects)

            if ship_data.get('pilots'):
                pilot_objects = Personage.objects.filter(url__in=ship_data['pilots'])
                starship.pilots.set(pilot_objects)


        self.stdout.write("загрузка персонажей")
        persons_data = self.fetch_all('people')


        for person_data in persons_data:

            person, _ = Personage.objects.update_or_create(
                    url=person_data['url'],
                    defaults={
                        'name': person_data['name'],
                        'height': person_data['height'],
                        'mass': person_data['mass'],
                        'birth_year': person_data['birth_year']
                    }
                )
                
            if person_data.get('films'):
                film_objects = Movie.objects.filter(url__in=person_data['films'])
                person.films.set(film_objects)
                
            if person_data.get('starships'):
                starship_objects = Starship.objects.filter(url__in=person_data['starships'])
                person.starships.set(starship_objects)

