import json
import os
import requests

def map():

  BASE_URL = 'https://datsblack.datsteam.dev/api'
  headers = {
      "x-api-Key": "dff47333-0c90-4954-be6f-60fa24043181"
  }

  response = requests.get(f"{BASE_URL}/map", headers=headers)

  get_map_url = response.json()['mapUrl']

  map_island = requests.get(get_map_url, headers=headers).json()

  map = [[0] * 2000 for _ in range(2000)]

  for island in map_island['islands']:
    # Начальная точка
    dot = [island['start'][0]-1, island['start'][1]-1]

    # Перебираем линии острова (по y)
    for i_y in range( len(island['map']) ):
      if dot[1] == 2000: break
      # Массив линии c X
      mass_x = island['map'][i_y]

      for i_x in range( len(mass_x) ):
        if dot[0] == 2000: break
        # print(dot)
        map[dot[0]][dot[1]] = island['map'][i_y][i_x]
        dot[0] += 1

      dot[1] += 1
      dot[0] = island['start'][0]
  
  # return map

  # Создание директории, если она не существует
  # os.makedirs("data", exist_ok=True)

  # # Открытие файла для записи
  # with open("data/map.json", "w") as json_file:
  #     json.dump({'map': map}, json_file)
      


    
  return map

# print(map())

