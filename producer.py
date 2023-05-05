import csv
import psycopg2
import time
import random

conn = psycopg2.connect(database = "root", user = "root", password = "secret", host = "127.0.0.1", port = "5432")
cur = conn.cursor()

# cur.execute("TRUNCATE food_coded RESTART IDENTITY;")
# conn.commit()

# with open('food_coded.csv') as f:
#     lines = f.readlines()
#     line_count = 0
#     for line in lines:
#         sleep = round(random.uniform(0, 2), 2)
   
#         print(f"SLEEP: {sleep}s")
#         time.sleep(sleep)
#         if line_count > 0:
#             # if(line_count > 20):
#             #     break
#             for row in csv.reader([line.replace("'", "%27")], delimiter=','):
#                 row_len = len(row)
#                 data = {
#                     "GPA": row[0] if row_len > 0 else '',
#                     "Gender": row[1] if row_len > 1 else '',
#                     "breakfast": row[2] if row_len > 2 else '',
#                     "calories_chicken": row[3] if row_len > 3 else '',
#                     "calories_day": row[4] if row_len > 4 else '',
#                     "calories_scone": row[5] if row_len > 5 else '',
#                     "coffee": row[6] if row_len > 6 else '',
#                     "comfort_food": row[7] if row_len > 7 else '',
#                     "comfort_food_reasons": row[8] if row_len > 8 else '',
#                     "comfort_food_reasons_coded": row[9] if row_len > 9 else '',
#                     "cook": row[10] if row_len > 10 else '',
#                     "comfort_food_reasons_coded2": row[11] if row_len > 11 else '',
#                     "cuisine": row[12] if row_len > 12 else '',
#                     "diet_current": row[13] if row_len > 13 else '',
#                     "diet_current_coded": row[14] if row_len > 14 else '',
#                     "drink": row[15] if row_len > 15 else '',
#                     "eating_changes": row[16] if row_len > 16 else '',
#                     "eating_changes_coded": row[17] if row_len > 17 else '',
#                     "eating_changes_coded1": row[18] if row_len > 18 else '',
#                     "eating_out": row[19] if row_len > 19 else '',
#                     "employment": row[20] if row_len > 20 else '',
#                     "ethnic_food": row[21] if row_len > 21 else '',
#                     "exercise": row[22] if row_len > 22 else '',
#                     "father_education": row[23] if row_len > 23 else '',
#                     "father_profession": row[24] if row_len > 24 else '',
#                     "fav_cuisine": row[25] if row_len > 25 else '',
#                     "fav_cuisine_coded": row[26] if row_len > 26 else '',
#                     "fav_food": row[27] if row_len > 27 else '',
#                     "food_childhood": row[28] if row_len > 28 else '',
#                     "fries": row[29] if row_len > 29 else '',
#                     "fruit_day": row[30] if row_len > 30 else '',
#                     "grade_level":row[31] if row_len > 31 else '',
#                     "greek_food": row[32] if row_len > 32 else '',
#                     "healthy_feeling": row[33] if row_len > 33 else '',
#                     "healthy_meal": row[34] if row_len > 34 else '',
#                     "ideal_diet": row[35] if row_len > 35 else '',
#                     "ideal_diet_coded": row[36] if row_len > 36 else '',
#                     "income": row[37] if row_len > 37 else '',
#                     "indian_food": row[38] if row_len > 38 else '',
#                     "italian_food": row[39] if row_len > 39 else '',
#                     "life_rewarding": row[40] if row_len > 40 else '',
#                     "marital_status": row[41] if row_len > 41 else '',
#                     "meals_dinner_friend": row[42] if row_len > 42 else '',
#                     "mother_education": row[43] if row_len > 43 else '',
#                     "mother_profession": row[44] if row_len > 44 else '',
#                     "nutritional_check": row[45] if row_len > 45 else '',
#                     "on_off_campus": row[46] if row_len > 46 else '',
#                     "parents_cook": row[47] if row_len > 47 else '',
#                     "pay_meal_out": row[48] if row_len > 48 else '',
#                     "persian_food": row[49] if row_len > 49 else '',
#                     "self_perception_weight": row[50] if row_len > 50 else '',
#                     "soup": row[51] if row_len > 51 else '',
#                     "sports": row[52] if row_len > 52 else '',
#                     "thai_food": row[53] if row_len > 53 else '',
#                     "tortilla_calories": row[54] if row_len > 54 else '',
#                     "turkey_calories": row[55] if row_len > 55 else '',
#                     "type_sports": row[56] if row_len > 56 else '',
#                     "veggies_day": row[57] if row_len > 57 else '',
#                     "vitamins": row[58] if row_len > 58 else '',
#                     "waffle_calories": row[59] if row_len > 59 else '',
#                     "weight": row[60] if row_len > 60 else ''
#                 }

#             cur.execute(f"""INSERT INTO food_coded (GPA,Gender,breakfast,calories_chicken,calories_day,calories_scone,coffee,comfort_food,comfort_food_reasons,comfort_food_reasons_coded,cook,comfort_food_reasons_coded2,cuisine,diet_current,diet_current_coded,drink,eating_changes,eating_changes_coded,eating_changes_coded1,eating_out,employment,ethnic_food,exercise,father_education,father_profession,fav_cuisine,fav_cuisine_coded,fav_food,food_childhood,fries,fruit_day,grade_level,greek_food,healthy_feeling,healthy_meal,ideal_diet,ideal_diet_coded,income,indian_food,italian_food,life_rewarding,marital_status,meals_dinner_friend,mother_education,mother_profession,nutritional_check,on_off_campus,parents_cook,pay_meal_out,persian_food,self_perception_weight,soup,sports,thai_food,tortilla_calories,turkey_calories,type_sports,veggies_day,vitamins,waffle_calories,weight) VALUES ('{data['GPA']}','{data['Gender']}','{data['breakfast']}','{data['calories_chicken']}','{data['calories_day']}','{data['calories_scone']}','{data['coffee']}','{data['comfort_food']}','{data['comfort_food_reasons']}','{data['comfort_food_reasons_coded']}','{data['cook']}','{data['comfort_food_reasons_coded2']}','{data['cuisine']}','{data['diet_current']}','{data['diet_current_coded']}','{data['drink']}','{data['eating_changes']}','{data['eating_changes_coded']}','{data['eating_changes_coded1']}','{data['eating_out']}','{data['employment']}','{data['ethnic_food']}','{data['exercise']}','{data['father_education']}','{data['father_profession']}','{data['fav_cuisine']}','{data['fav_cuisine_coded']}','{data['fav_food']}','{data['food_childhood']}','{data['fries']}','{data['fruit_day']}','{data['grade_level']}','{data['greek_food']}','{data['healthy_feeling']}','{data['healthy_meal']}','{data['ideal_diet']}','{data['ideal_diet_coded']}','{data['income']}','{data['indian_food']}','{data['italian_food']}','{data['life_rewarding']}','{data['marital_status']}','{data['meals_dinner_friend']}','{data['mother_education']}','{data['mother_profession']}','{data['nutritional_check']}','{data['on_off_campus']}','{data['parents_cook']}','{data['pay_meal_out']}','{data['persian_food']}','{data['self_perception_weight']}','{data['soup']}','{data['sports']}','{data['thai_food']}','{data['tortilla_calories']}','{data['turkey_calories']}','{data['type_sports']}','{data['veggies_day']}','{data['vitamins']}','{data['waffle_calories']}','{data['weight']}')""")
#             conn.commit()
#             print(f"INSERT LINE: {line_count}")
#         line_count += 1

# cur.close()
# conn.close()
# print("Records created successfully")

# with open('food_coded.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         # if line_count == 0:
#             # print(f'Column names are {", ".join(row)}')
#             # line_count += 1
#         # print(f'\t{row}')
#         if line_count == 3:
#            print(f'\t{row}') 
#         line_count += 1
#     print(f'Processed {line_count} lines.')

with open('food_coded.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # if line_count > 5:
        #     break
        if line_count > 0:
            
            sleep = round(random.uniform(0, 2), 2)
            print(f"SLEEP: {sleep}s")
            time.sleep(sleep)

            data = {
                    "GPA": row[0].replace("'", "%27"),
                    "Gender": row[1].replace("'", "%27"),
                    "breakfast": row[2].replace("'", "%27"),
                    "calories_chicken": row[3].replace("'", "%27"),
                    "calories_day": row[4].replace("'", "%27"),
                    "calories_scone": row[5].replace("'", "%27"),
                    "coffee": row[6].replace("'", "%27"),
                    "comfort_food": row[7].replace("'", "%27"),
                    "comfort_food_reasons": row[8].replace("'", "%27"),
                    "comfort_food_reasons_coded": row[9].replace("'", "%27"),
                    "cook": row[10].replace("'", "%27"),
                    "comfort_food_reasons_coded2": row[11].replace("'", "%27"),
                    "cuisine": row[12].replace("'", "%27"),
                    "diet_current": row[13].replace("'", "%27"),
                    "diet_current_coded": row[14].replace("'", "%27"),
                    "drink": row[15].replace("'", "%27"),
                    "eating_changes": row[16].replace("'", "%27"),
                    "eating_changes_coded": row[17].replace("'", "%27"),
                    "eating_changes_coded1": row[18].replace("'", "%27"),
                    "eating_out": row[19].replace("'", "%27"),
                    "employment": row[20].replace("'", "%27"),
                    "ethnic_food": row[21].replace("'", "%27"),
                    "exercise": row[22].replace("'", "%27"),
                    "father_education": row[23].replace("'", "%27"),
                    "father_profession": row[24].replace("'", "%27"),
                    "fav_cuisine": row[25].replace("'", "%27"),
                    "fav_cuisine_coded": row[26].replace("'", "%27"),
                    "fav_food": row[27].replace("'", "%27"),
                    "food_childhood": row[28].replace("'", "%27"),
                    "fries": row[29].replace("'", "%27"),
                    "fruit_day": row[30].replace("'", "%27"),
                    "grade_level":row[31].replace("'", "%27"),
                    "greek_food": row[32].replace("'", "%27"),
                    "healthy_feeling": row[33].replace("'", "%27"),
                    "healthy_meal": row[34].replace("'", "%27"),
                    "ideal_diet": row[35].replace("'", "%27"),
                    "ideal_diet_coded": row[36].replace("'", "%27"),
                    "income": row[37].replace("'", "%27"),
                    "indian_food": row[38].replace("'", "%27"),
                    "italian_food": row[39].replace("'", "%27"),
                    "life_rewarding": row[40].replace("'", "%27"),
                    "marital_status": row[41].replace("'", "%27"),
                    "meals_dinner_friend": row[42].replace("'", "%27"),
                    "mother_education": row[43].replace("'", "%27"),
                    "mother_profession": row[44].replace("'", "%27"),
                    "nutritional_check": row[45].replace("'", "%27"),
                    "on_off_campus": row[46].replace("'", "%27"),
                    "parents_cook": row[47].replace("'", "%27"),
                    "pay_meal_out": row[48].replace("'", "%27"),
                    "persian_food": row[49].replace("'", "%27"),
                    "self_perception_weight": row[50].replace("'", "%27"),
                    "soup": row[51].replace("'", "%27"),
                    "sports": row[52].replace("'", "%27"),
                    "thai_food": row[53].replace("'", "%27"),
                    "tortilla_calories": row[54].replace("'", "%27"),
                    "turkey_calories": row[55].replace("'", "%27"),
                    "type_sports": row[56].replace("'", "%27"),
                    "veggies_day": row[57].replace("'", "%27"),
                    "vitamins": row[58].replace("'", "%27"),
                    "waffle_calories": row[59].replace("'", "%27"),
                    "weight": row[60].replace("'", "%27")
                }
            cur.execute(f"""INSERT INTO food_coded (GPA,Gender,breakfast,calories_chicken,calories_day,calories_scone,coffee,comfort_food,comfort_food_reasons,comfort_food_reasons_coded,cook,comfort_food_reasons_coded2,cuisine,diet_current,diet_current_coded,drink,eating_changes,eating_changes_coded,eating_changes_coded1,eating_out,employment,ethnic_food,exercise,father_education,father_profession,fav_cuisine,fav_cuisine_coded,fav_food,food_childhood,fries,fruit_day,grade_level,greek_food,healthy_feeling,healthy_meal,ideal_diet,ideal_diet_coded,income,indian_food,italian_food,life_rewarding,marital_status,meals_dinner_friend,mother_education,mother_profession,nutritional_check,on_off_campus,parents_cook,pay_meal_out,persian_food,self_perception_weight,soup,sports,thai_food,tortilla_calories,turkey_calories,type_sports,veggies_day,vitamins,waffle_calories,weight) VALUES ('{data['GPA']}','{data['Gender']}','{data['breakfast']}','{data['calories_chicken']}','{data['calories_day']}','{data['calories_scone']}','{data['coffee']}','{data['comfort_food']}','{data['comfort_food_reasons']}','{data['comfort_food_reasons_coded']}','{data['cook']}','{data['comfort_food_reasons_coded2']}','{data['cuisine']}','{data['diet_current']}','{data['diet_current_coded']}','{data['drink']}','{data['eating_changes']}','{data['eating_changes_coded']}','{data['eating_changes_coded1']}','{data['eating_out']}','{data['employment']}','{data['ethnic_food']}','{data['exercise']}','{data['father_education']}','{data['father_profession']}','{data['fav_cuisine']}','{data['fav_cuisine_coded']}','{data['fav_food']}','{data['food_childhood']}','{data['fries']}','{data['fruit_day']}','{data['grade_level']}','{data['greek_food']}','{data['healthy_feeling']}','{data['healthy_meal']}','{data['ideal_diet']}','{data['ideal_diet_coded']}','{data['income']}','{data['indian_food']}','{data['italian_food']}','{data['life_rewarding']}','{data['marital_status']}','{data['meals_dinner_friend']}','{data['mother_education']}','{data['mother_profession']}','{data['nutritional_check']}','{data['on_off_campus']}','{data['parents_cook']}','{data['pay_meal_out']}','{data['persian_food']}','{data['self_perception_weight']}','{data['soup']}','{data['sports']}','{data['thai_food']}','{data['tortilla_calories']}','{data['turkey_calories']}','{data['type_sports']}','{data['veggies_day']}','{data['vitamins']}','{data['waffle_calories']}','{data['weight']}')""")
            conn.commit()
            print(f"INSERT LINE: {line_count}")
        line_count += 1

cur.close()
conn.close()
print("Records created successfully")

# with open('food_coded.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
    