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


#def createAlbionUrl(itemlist, citylistId, itemQuality):
def createAlbionUrl(itemlist):
    #albion_api_link = f"https://www.albion-online-data.com/api/v2/stats/prices/{itemlist}?locations={citylistId}&qualities={itemQuality}"
    albion_api_link = f"https://www.albion-online-data.com/api/v2/stats/prices/{itemlist}?locations={all_cities}"
    return albion_api_link


# city list
all_cities = "Caerleon,Bridgewatch,Lymhurst,Fortsterling,Thetford,Martlock"
city_list = ["Black Market", "Caerleon", "Bridgewatch", "Lymhurst", "Fortsterling", "Thetford", "Martlock", all_cities]

# item list
armor_query = ["ARMOR", "HEAD", "SHOES"]
tier_query = ["T4", "T5", "T6", "T7", "T8"]
refine_shit = ["", "_LEVEL1", "_LEVEL2", "_LEVEL3"]
rarity_query = ["", "@1", "@2", "@3"]
weapons_query = ["MAIN", "2H"]
raw_materials_query = ["ORE", "HIDE", "FIBER", "WOOD", "ROCK"]
ref_materials_query = ["METALBAR", "LEATHER", "CLOTH", "PLANK", "STONE"]
all_items = armor_query + weapons_query + raw_materials_query + ref_materials_query
search_promt = [all_items, armor_query, weapons_query, raw_materials_query, ref_materials_query]

# item category
# item choice (not for now)
# tier
# enchant

# tier_itemChoice_refineShit_rarity
"T4_CLOTH",
"T5_CLOTH",
"T6_CLOTH",
"T7_CLOTH",
"T8_CLOTH",
"T4_CLOTH_LEVEL1@1",
"T5_CLOTH_LEVEL1@1",
"T6_CLOTH_LEVEL1@1",
"T7_CLOTH_LEVEL1@1",
"T8_CLOTH_LEVEL1@1",
"T4_CLOTH_LEVEL2@2",
"T5_CLOTH_LEVEL2@2",
"T6_CLOTH_LEVEL2@2",
"T7_CLOTH_LEVEL2@2",
"T8_CLOTH_LEVEL2@2",
"T4_CLOTH_LEVEL3@3",
"T5_CLOTH_LEVEL3@3",
"T6_CLOTH_LEVEL3@3",
"T7_CLOTH_LEVEL3@3",
"T8_CLOTH_LEVEL3@3",


# input general
##city choice
#print("from which City?\n0.blackmarket\n1.caerleon\n2.bridgewatch\n3.Lymhurst\n4.Fortsterling\n5.Thetford\n6.Martlock\n\n7.all\n")
#string_city_result = input("Type the city number: ")
#int_city_result = int(string_city_result)
##item choice
print("from which Type?\n0.All\n1.Armor\n2.weapons\n3.Raw_materials\n4.Ref_materials\n\n")
string_item_result = input("Type the quality number: ")
int_item_result = int(string_item_result)
desiredItemList = createItemList(search_promt[int_item_result])

##quality choice
#print("from which Quality?\n0.one\n1.two\n2.three\n3.four\n4.five\n\n")
#string_quality = input("Type the quality number: ")
#int_quality = int(string_quality)

#albion_api_link = createAlbionUrl(desiredItemList, city_list[int_city_result], int_quality)
albion_api_link = createAlbionUrl(desiredItemList)

# asking the API for shit
print(albion_api_link)

albiondata = requests.get(albion_api_link)
# print(albiondata.status_code)
# print(albiondata.json())

text_file = open("albion_data.txt", "w")
n = text_file.write(albiondata)
text_file.close()
