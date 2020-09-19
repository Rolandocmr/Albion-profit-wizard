import requests
from Albionitemlist import itemlisting
import json

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


# def createAlbionUrl(itemlist, citylistId, itemQuality):
def createAlbionUrl(itemlist):
    # albion_api_link = f"https://www.albion-online-data.com/api/v2/stats/prices/{itemlist}?locations={citylistId}&qualities={itemQuality}"
    albion_api_link = f"https://www.albion-online-data.com/api/v2/stats/prices/{itemlist}?locations={all_cities}"
    return albion_api_link


def createItemList(desiredItemType):
    depuredList = []
    for searchQuery in desiredItemType:
        for dataItem in itemlisting:
            if searchQuery in dataItem:
                depuredList.append(dataItem)

    string_search = ','.join(depuredList)
    return string_search


def createItemList2(item, tier, enchantment):
    return tier_query[tier] + "_" + ref_materials_query[item] + refine_shit[enchantment] + rarity_query[enchantment]


# item category
# item choice (not for now)
# tier
# enchant

# tier_itemChoice_refineShit_rarity

# input general
##city choice
# print("from which City?\n0.blackmarket\n1.caerleon\n2.bridgewatch\n3.Lymhurst\n4.Fortsterling\n5.Thetford\n6.Martlock\n\n7.all\n")
# string_city_result = input("Type the city number: ")
# int_city_result = int(string_city_result)
##item choice
print("from which Category?\n0.Armor\n1.weapons\n2.Raw_materials\n3.Ref_materials\n4.All\n\n")
choice_category = int(input("Type the category: "))
# desiredItemList = createItemList(search_promt[int_item_result])

print("from which Item?\n0.Metal Bars\n1.Leather\n2.Cloth\n3.Plank\n4.Stone\n5.All\n\n")
choice_item = int(input("Type the Item number: "))

print("from which Tier?\n0.T4\n1.T5\n2.T6\n3.T7\n4.T8\n5.All\n\n")
choice_tier = int(input("Type the tier: "))

print("from which Enchantment?\n0.0\n1.1\n2.2\n3.3\n4.All\n\n")
choice_enchantment = int(input("Type the enchantment: "))

# build a string depending on choices

desiredItemList = createItemList2(choice_item, choice_tier, choice_enchantment)

##quality choice
# print("from which Quality?\n0.one\n1.two\n2.three\n3.four\n4.five\n\n")
# string_quality = input("Type the quality number: ")
# int_quality = int(string_quality)

# albion_api_link = createAlbionUrl(desiredItemList, city_list[int_city_result], int_quality)
albion_api_link = createAlbionUrl(desiredItemList)

# asking the API for shit
print(albion_api_link)

response = requests.get(albion_api_link)
# print(albiondata.status_code)
print(response.json())

print(response.text)

text_file = open("albion_data.txt", "w")
n = text_file.write(response.text)
text_file.close()
