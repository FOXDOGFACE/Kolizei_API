# kolizei-api
![Version](https://img.shields.io/badge/version-0.0.1-blue.svg)

# Description

This package is created to communicate with Kolizei api, which is a simple vk mini app. 
This app can be used to create a system of points in a community and easily administrate it.

# Links
* My github link: [Foxdogface](https://github.com/Foxdogface).
* Repository link: [Python Kolizei API](https://github.com/Foxdogface/Kolizei_API).
* Description of original get-post Kolizei api made by originals creators: [Kolizei API](https://docs.appcm.ru/rasshirennyi-funkcional/api).

# Installation
This library is installable as a pip package.
```
pip install soundcloud-lib
```

# Documentation

### Create api object
```python
import kolizei_api

api = kolizei_api.Kolizei_api(secret_token="", group_id=None)
```
##### Class Kolizei_api, arguments: 
* secret_token(str) - secret token which you must receive from kolizei application how a group administrator. Mandatory argument.
* group_id(int) - id of you group where the kolizei app is installed. Mandatory argument.

### Kolizei_api.get_rating
```python
import kolizei_api

api = kolizei_api.Kolizei_api(secret_token="", group_id=None)
api.get_rating(count=None, offset=None)
```
##### Method Kolizei_api.get_rating, arguments: 
* count(int) - Number of firsts places of rating to recive. The biggest number is 1000. If you need to receive more use the "offset" argument. The default is 1000.
* offset(int) - The argument to set an offset to collect some specials users. The default is 1000.

### Kolizei_api.get_by_id
```python
import kolizei_api

api = kolizei_api.Kolizei_api(secret_token="", group_id=None)
api.get_by_id(user_id=None)
```
##### Method Kolizei_api.get_by_id, arguments: 
* user_id(int) - VK user id. Mandatory argument.

### Kolizei_api.users_changePoints
```python
import kolizei_api

api = kolizei_api.Kolizei_api(secret_token="", group_id=None)
api.users_changePoints(user_ids=None, points=None)
```
##### Method Kolizei_api.users_changePoints, arguments: 
* user_ids(list with numbers(int)) - Ids of users whose scores you need to change. Mandatory argument.
* points(list with numbers(int)) - How many points you need to add or subtract (number with a minus "-"). You can add only one number for all users or few numbers for each users, if the number of users isn't equal to the length of points list the last digit will be applied to unmatched ones. Mandatory argument.

### Kolizei_api.users_resetPoints
```python
import kolizei_api

api = kolizei_api.Kolizei_api(secret_token="", group_id=None)
api.users_resetPoints(user_ids=None)
```
##### Method Kolizei_api.users_resetPoints, arguments:
* user_ids(list with numbers(int)) - Ids of vk users which you need to remove all points. Mandatory argument.

### Kolizei_api.users_ban
```python
import kolizei_api

api = kolizei_api.Kolizei_api(secret_token="", group_id=None)
api.users_ban(user_ids=None)
```
##### Method Kolizei_api.users_ban, arguments:
* user_ids(list with numbers(int)) - Ids of vk users which you need to ban.

### Kolizei_api.users_unban
```python
import kolizei_api

api = kolizei_api.Kolizei_api(secret_token="", group_id=None)
api.users_unban(user_ids=None)
```
##### Method Kolizei_api.users_ban, arguments:
* user_ids(list with numbers(int)) - Ids of vk users which you need to unban.

# Bugs and features
I will accept with pleasure any critics and other advice because it's actually my first python module created by myself.
You can report them using the issues tab. Also feel free to request new features.