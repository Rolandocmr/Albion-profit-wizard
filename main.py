import requests
from Albionitemlist import itemlisting
import json


def createItemList(desiredItemType):
  depuredList = []
  for searchQuery in desiredItemType:
    for dataItem in itemlisting:
      if searchQuery in dataItem:
        depuredList.append(dataItem)

  string_search = ','.join(depuredList)
  return string_search


def createAlbionUrl(itemlist, citylistId, itemQuality):
    albion_api_link = f"https://www.albion-online-data.com/api/v2/stats/prices/{itemlist}?locations={citylistId}&qualities={itemQuality}"
    return albion_api_link


# city list
all_cities = "Caerleon,Bridgewatch,Lymhurst,Fortsterling,Thetford,Martlock"
city_list = [all_cities, "Black Market" "Caerleon", "Bridgewatch", "Lymhurst", "Fortsterling", "Thetford", "Martlock"]

# item list
armor_query = ["T4_ARMOR", "T5_ARMOR", "T6_ARMOR", "T7_ARMOR", "T8_ARMOR", "T4_HEAD", "T5_HEAD", "T6_HEAD", "T7_HEAD",
               "T8_HEAD", "T4_SHOES", "T5_SHOES", "T6_SHOES", "T7_SHOES", "T8_SHOES"]
weapons_query = ["T4_MAIN", "T5_MAIN", "T6_MAIN", "T7_MAIN", "T8_MAIN", "T4_2H", "T5_2H", "T6_2H", "T7_2H", "T8_2H"]
raw_materials_query = ["_ORE", "_HIDE", "_FIBER", "_WOOD", "_ROCK"]
ref_materials_query = ["_METALBAR", "_LEATHER", "_FABRIC", "_WOOD", "_ROCK"]
all_items = armor_query + weapons_query + raw_materials_query + ref_materials_query
search_promt = [all_items, armor_query, weapons_query, raw_materials_query, ref_materials_query]

# input general
##city choice
print(
    "from which City?\n0.all\n1.blackmarket\n2.caerleon\n3.bridgewatch\n4.Lymhurst\n5.Fortsterling\n6.Thetford\n7.Martlock\n\n")
string_city_result = input("Type the city number: ")
int_city_result = int(string_city_result)
##item choice
print("from which Type?\n0.All\n1.Armor\n2.weapons\n3.Raw_materials\n4.Ref_materials\n\n")
string_item_result = input("Type the quality number: ")
int_item_result = int(string_item_result)
desiredItemList = createItemList(search_promt[int_item_result])

##quality choice
print("from which Quality?\n0.all\n1.one\n2.two\n3.three\n4.four\n5.five\n\n")
string_quality = input("Type the quality number: ")
int_quality = int(string_quality)

albion_api_link = createAlbionUrl(desiredItemList, city_list[int_city_result], int_quality)

# asking the API for shit
print(albion_api_link)
# albiondata = requests.get(albion_api_link)
# print(albiondata.status_code)
# print(albiondata.json())