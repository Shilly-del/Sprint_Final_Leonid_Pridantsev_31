class Url:
    API = 'https://qa-desk.stand.praktikum-services.ru/api'
    SIGNUP = f'{API}/signup'
    SIGNIN = f'{API}/signin'
    CREATE_ANNOUNCE = f'{API}/create-listing'
    EDIT_ANNOUNCE = f'{API}/update-offer'
    REMOVE_ANNOUNCE = f'{API}/listings'

class AnnounceData:
    COND = ['Новый', 'Б/У']
    CATEGORIES = ['Авто', 'Книги', 'Садоводство', 'Хобби', 'Технологии']
    CITIES = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Нижний Новгород', 'Казань']

class ApiMessage:
    INTOKEN = "Токен не действителен"
    REMAIL = "Почта уже используется"
    ANNONCEREM = "Объявление удалено успешно"
