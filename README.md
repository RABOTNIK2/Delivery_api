<h1 align='center'>API Приложения по Доставке еды</h1>

Проект представляет собой приложение по доставке еды сделанное с использованием технологии Django Rest Framework. В проекте реализован весь CRUD, авторизация(использовалась библиотека djoser), дополнительные @action под тематику проекта 

### Тестирование
* Тестирование поиска блюда.
* Тестирование добавления блюда в корзину.


### API Endpoint

#### Authentication

* **/auth/users/** (Регистрация пользователя)
* **/auth/token/login/** (Авторизация пользователя)
* **/api/users/logout/** (Выход пользователя)


#### Users

* **/food_api/user/** (Вывод всех пользователей, 'GET')
* **/food_api/user/** (Добавление пользователя, 'POST')
* **/food_api/user/pk/** (Чтение пользователя, 'GET')
* **/food_api/user/pk/** (Редактирование пользователя, 'PUT')
* **/food_api/user/pk/** (Удаление пользователя, 'DELETE')
* **/food_api/user/del_dish/?id=&q** (Удаление из корзины, 'PUT')
* **/food_api/user/add_to_dish/?id=&q** (Добавление в корзину, 'PUT')
  

#### Dish

* **/food_api/dish/** (Вывод всех блюд, 'GET')
* **/food_api/dish/** (Добавление блюда, 'POST')
* **/food_api/dish/pk/** (Чтение блюда, 'GET')
* **/food_api/dish/pk/** (Редактирование блюда, 'PUT')
* **/food_api/dish/pk/** (Удаление блюда, 'DELETE')
* **/food_api/dish/search_dish/?q** (Поиск блюда, 'GET')


#### Kitchen

* **/food_api/kitchen/** (Вывод кухонь, 'GET')
* **/food_api/kitchen/** (Добавление кухни, 'POST')
* **/food_api/kitchen/pk/** (Чтение кухни, 'GET')
* **/food_api/kitchen/pk/** (Редактирование кухни, 'PUT')
* **/food_api/kitchen/pk/** (Удаление кухни, 'DELETE')


#### Order

* **/food_api/order/** (Вывод заказов, 'GET')
* **/food_api/order/** (Добавление заказа, 'POST')
* **/food_api/order/pk/** (Чтение заказа, 'GET')
* **/food_api/order/pk/** (Редактирование заказа, 'PUT')
* **/food_api/order/pk/** (Удаление заказа, 'DELETE')



### Install 

    pip install -r req.txt

### Usage

    python manage.py test

### License

  Этот проект лицензирован под MIT License.


    

