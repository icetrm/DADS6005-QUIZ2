CREATE TABLE food_coded (
    food_id SERIAL PRIMARY KEY,
    GPA varchar(355),
    Gender varchar(355),
    breakfast varchar(355),
    calories_chicken varchar(355),
    calories_day varchar(355),
    calories_scone varchar(355),
    coffee varchar(355),
    comfort_food varchar(355),
    comfort_food_reasons varchar(355),
    comfort_food_reasons_coded varchar(355),
    cook varchar(355),
    comfort_food_reasons_coded2 varchar(355),
    cuisine varchar(355),
    diet_current varchar(355),
    diet_current_coded varchar(355),
    drink varchar(355),
    eating_changes varchar(355),
    eating_changes_coded varchar(355),
    eating_changes_coded1 varchar(355),
    eating_out varchar(355),
    employment varchar(355),
    ethnic_food varchar(355),
    exercise varchar(355),
    father_education varchar(355),
    father_profession varchar(355),
    fav_cuisine varchar(355),
    fav_cuisine_coded varchar(355),
    fav_food varchar(355),
    food_childhood varchar(355),
    fries varchar(355),
    fruit_day varchar(355),
    grade_level varchar(355),
    greek_food varchar(355),
    healthy_feeling varchar(355),
    healthy_meal varchar(355),
    ideal_diet varchar(355),
    ideal_diet_coded varchar(355),
    income varchar(355),
    indian_food varchar(355),
    italian_food varchar(355),
    life_rewarding varchar(355),
    marital_status varchar(355),
    meals_dinner_friend varchar(355),
    mother_education varchar(355),
    mother_profession varchar(355),
    nutritional_check varchar(355),
    on_off_campus varchar(355),
    parents_cook varchar(355),
    pay_meal_out varchar(355),
    persian_food varchar(355),
    self_perception_weight varchar(355),
    soup varchar(355),
    sports varchar(355),
    thai_food varchar(355),
    tortilla_calories varchar(355),
    turkey_calories varchar(355),
    type_sports varchar(355),
    veggies_day varchar(355),
    vitamins varchar(355),
    waffle_calories varchar(355),
    weight varchar(355)
);

CREATE TABLE comfort_food_reasons_coded (
    coded_id INT PRIMARY KEY,
    label varchar(355)
);

INSERT INTO food_coded (GPA,Gender,breakfast,calories_chicken,calories_day,calories_scone,coffee,comfort_food,comfort_food_reasons,comfort_food_reasons_coded,cook,comfort_food_reasons_coded2,cuisine,diet_current,diet_current_coded,drink,eating_changes,eating_changes_coded,eating_changes_coded1,eating_out,employment,ethnic_food,exercise,father_education,father_profession,fav_cuisine,fav_cuisine_coded,fav_food,food_childhood,fries,fruit_day,grade_level,greek_food,healthy_feeling,healthy_meal,ideal_diet,ideal_diet_coded,income,indian_food,italian_food,life_rewarding,marital_status,meals_dinner_friend,mother_education,mother_profession,nutritional_check,on_off_campus,parents_cook,pay_meal_out,persian_food,self_perception_weight,soup,sports,thai_food,tortilla_calories,turkey_calories,type_sports,veggies_day,vitamins,waffle_calories,weight) VALUES ('55','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','');

INSERT INTO comfort_food_reasons_coded (coded_id,label) VALUES (1, 'stress');
INSERT INTO comfort_food_reasons_coded (coded_id,label) VALUES (2, 'boredom');
INSERT INTO comfort_food_reasons_coded (coded_id,label) VALUES (3, 'depression/sadness');
INSERT INTO comfort_food_reasons_coded (coded_id,label) VALUES (4, 'hunger');
INSERT INTO comfort_food_reasons_coded (coded_id,label) VALUES (5, 'laziness');
INSERT INTO comfort_food_reasons_coded (coded_id,label) VALUES (6, 'cold weather');
INSERT INTO comfort_food_reasons_coded (coded_id,label) VALUES (7, 'happiness');
INSERT INTO comfort_food_reasons_coded (coded_id,label) VALUES (8, 'watching tv');
INSERT INTO comfort_food_reasons_coded (coded_id,label) VALUES (9, 'none');
