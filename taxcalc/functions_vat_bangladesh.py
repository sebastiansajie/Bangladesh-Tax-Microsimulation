"""
Auto-generated VAT functions module
"""

import numpy as np
from taxcalc.decorators import iterate_jit

@iterate_jit(nopython=True)
def cal_CONS_Food(CONS_food_basic, CONS_food_non_basic, CONS_Food):
    CONS_Food = (
        CONS_food_basic +
        CONS_food_non_basic
    )
    return CONS_Food

@iterate_jit(nopython=True)
def cal_CONS_Non_Food(CONS_cloth, CONS_clothes, CONS_donation, CONS_education_services_government, CONS_education_services_government_college, CONS_education_services_private, CONS_education_services_private_college, CONS_electronics_ict, CONS_electronics_ict_repair, CONS_entertainment_goods_music, CONS_entertainment_goods_sports, CONS_financial_services, CONS_footwear, CONS_footwear_services, CONS_fuel, CONS_fuel_biomass, CONS_furniture_fixtures, CONS_health_equipment, CONS_health_services, CONS_health_services_dental, CONS_health_services_paramedical, CONS_health_services_testing, CONS_hospital_services, CONS_hotel_services, CONS_house_repair_goods, CONS_house_repair_services, CONS_household_accessories_medical, CONS_household_electric_equipment, CONS_household_equipment, CONS_household_gardening, CONS_household_goods, CONS_household_items, CONS_household_repair_services, CONS_household_services, CONS_household_utensils, CONS_interest, CONS_jewellery, CONS_legal_services, CONS_medical_accessories, CONS_medical_life_saving, CONS_motor_vehicle_four_wheeler, CONS_motor_vehicle_two_wheeler, CONS_non_motorized_vehicle, CONS_other_services, CONS_personal_accessories, CONS_personal_accessories_services, CONS_personal_expenses_religious, CONS_personal_products, CONS_personal_services, CONS_recreation, CONS_religious_services, CONS_rent, CONS_restaurant, CONS_sports_recreation_services, CONS_stationery, CONS_tailoring_cleaning, CONS_tax, CONS_telecom_equipment, CONS_telecom_services, CONS_transport, CONS_transport_services, CONS_travel, CONS_travel_religious, CONS_utilities, CONS_vehicle_equipment, CONS_vehicle_services, CONS_Non_Food):
    CONS_Non_Food = (
        CONS_cloth +
        CONS_clothes +
        CONS_donation +
        CONS_education_services_government +
        CONS_education_services_government_college +
        CONS_education_services_private +
        CONS_education_services_private_college +
        CONS_electronics_ict +
        CONS_electronics_ict_repair +
        CONS_entertainment_goods_music +
        CONS_entertainment_goods_sports +
        CONS_financial_services +
        CONS_footwear +
        CONS_footwear_services +
        CONS_fuel +
        CONS_fuel_biomass +
        CONS_furniture_fixtures +
        CONS_health_equipment +
        CONS_health_services +
        CONS_health_services_dental +
        CONS_health_services_paramedical +
        CONS_health_services_testing +
        CONS_hospital_services +
        CONS_hotel_services +
        CONS_house_repair_goods +
        CONS_house_repair_services +
        CONS_household_accessories_medical +
        CONS_household_electric_equipment +
        CONS_household_equipment +
        CONS_household_gardening +
        CONS_household_goods +
        CONS_household_items +
        CONS_household_repair_services +
        CONS_household_services +
        CONS_household_utensils +
        CONS_interest +
        CONS_jewellery +
        CONS_legal_services +
        CONS_medical_accessories +
        CONS_medical_life_saving +
        CONS_motor_vehicle_four_wheeler +
        CONS_motor_vehicle_two_wheeler +
        CONS_non_motorized_vehicle +
        CONS_other_services +
        CONS_personal_accessories +
        CONS_personal_accessories_services +
        CONS_personal_expenses_religious +
        CONS_personal_products +
        CONS_personal_services +
        CONS_recreation +
        CONS_religious_services +
        CONS_rent +
        CONS_restaurant +
        CONS_sports_recreation_services +
        CONS_stationery +
        CONS_tailoring_cleaning +
        CONS_tax +
        CONS_telecom_equipment +
        CONS_telecom_services +
        CONS_transport +
        CONS_transport_services +
        CONS_travel +
        CONS_travel_religious +
        CONS_utilities +
        CONS_vehicle_equipment +
        CONS_vehicle_services
    )
    return CONS_Non_Food

@iterate_jit(nopython=True)
def cal_CONS_Other(CONS_cloth, CONS_clothes, CONS_donation, CONS_education_services_government, CONS_education_services_government_college, CONS_education_services_private, CONS_education_services_private_college, CONS_electronics_ict, CONS_electronics_ict_repair, CONS_entertainment_goods_music, CONS_entertainment_goods_sports, CONS_financial_services, CONS_footwear, CONS_footwear_services, CONS_fuel, CONS_fuel_biomass, CONS_furniture_fixtures, CONS_health_equipment, CONS_health_services, CONS_health_services_dental, CONS_health_services_paramedical, CONS_health_services_testing, CONS_hospital_services, CONS_hotel_services, CONS_house_repair_goods, CONS_house_repair_services, CONS_household_accessories_medical, CONS_household_electric_equipment, CONS_household_equipment, CONS_household_gardening, CONS_household_goods, CONS_household_items, CONS_household_repair_services, CONS_household_services, CONS_household_utensils, CONS_interest, CONS_jewellery, CONS_legal_services, CONS_medical_accessories, CONS_medical_life_saving, CONS_motor_vehicle_four_wheeler, CONS_motor_vehicle_two_wheeler, CONS_non_motorized_vehicle, CONS_other_services, CONS_personal_accessories, CONS_personal_accessories_services, CONS_personal_expenses_religious, CONS_personal_products, CONS_personal_services, CONS_recreation, CONS_religious_services, CONS_rent, CONS_restaurant, CONS_sports_recreation_services, CONS_stationery, CONS_tailoring_cleaning, CONS_tax, CONS_telecom_equipment, CONS_telecom_services, CONS_transport, CONS_transport_services, CONS_travel, CONS_travel_religious, CONS_utilities, CONS_vehicle_equipment, CONS_vehicle_services, CONS_Other):
    CONS_Other = (
        CONS_cloth +
        CONS_clothes +
        CONS_donation +
        CONS_education_services_government +
        CONS_education_services_government_college +
        CONS_education_services_private +
        CONS_education_services_private_college +
        CONS_electronics_ict +
        CONS_electronics_ict_repair +
        CONS_entertainment_goods_music +
        CONS_entertainment_goods_sports +
        CONS_financial_services +
        CONS_footwear +
        CONS_footwear_services +
        CONS_fuel +
        CONS_fuel_biomass +
        CONS_furniture_fixtures +
        CONS_health_equipment +
        CONS_health_services +
        CONS_health_services_dental +
        CONS_health_services_paramedical +
        CONS_health_services_testing +
        CONS_hospital_services +
        CONS_hotel_services +
        CONS_house_repair_goods +
        CONS_house_repair_services +
        CONS_household_accessories_medical +
        CONS_household_electric_equipment +
        CONS_household_equipment +
        CONS_household_gardening +
        CONS_household_goods +
        CONS_household_items +
        CONS_household_repair_services +
        CONS_household_services +
        CONS_household_utensils +
        CONS_interest +
        CONS_jewellery +
        CONS_legal_services +
        CONS_medical_accessories +
        CONS_medical_life_saving +
        CONS_motor_vehicle_four_wheeler +
        CONS_motor_vehicle_two_wheeler +
        CONS_non_motorized_vehicle +
        CONS_other_services +
        CONS_personal_accessories +
        CONS_personal_accessories_services +
        CONS_personal_expenses_religious +
        CONS_personal_products +
        CONS_personal_services +
        CONS_recreation +
        CONS_religious_services +
        CONS_rent +
        CONS_restaurant +
        CONS_sports_recreation_services +
        CONS_stationery +
        CONS_tailoring_cleaning +
        CONS_tax +
        CONS_telecom_equipment +
        CONS_telecom_services +
        CONS_transport +
        CONS_transport_services +
        CONS_travel +
        CONS_travel_religious +
        CONS_utilities +
        CONS_vehicle_equipment +
        CONS_vehicle_services
    )
    return CONS_Other

@iterate_jit(nopython=True)
def cal_CONS_Total(CONS_Food, CONS_Other, CONS_Total):
    CONS_Total = CONS_Food + CONS_Other
    return CONS_Total

@iterate_jit(nopython=True)
def cal_Applicable_Elasticity_Food(
    elasticity_consumption_food_threshold,
    elasticity_consumption_food_value,
    CONS_Total,
    applicable_elasticity_food):
    elasticity_consumption_threshold0 = elasticity_consumption_food_threshold[0]
    elasticity_consumption_threshold1 = elasticity_consumption_food_threshold[1]
    elasticity_consumption_value0 = elasticity_consumption_food_value[0]
    elasticity_consumption_value1 = elasticity_consumption_food_value[1]
    elasticity_consumption_value2 = elasticity_consumption_food_value[2]
    if CONS_Total <= 0:
        applicable_elasticity_food = 0
    elif CONS_Total < elasticity_consumption_threshold0:
        applicable_elasticity_food = elasticity_consumption_value0
    elif CONS_Total < elasticity_consumption_threshold1:
        applicable_elasticity_food = elasticity_consumption_value1
    else:
        applicable_elasticity_food = elasticity_consumption_value2
    return applicable_elasticity_food

@iterate_jit(nopython=True)
def cal_Applicable_Elasticity_Non_Food(
    elasticity_consumption_non_food_threshold,
    elasticity_consumption_non_food_value,
    CONS_Total,
    applicable_elasticity_non_food):
    elasticity_consumption_threshold0 = elasticity_consumption_non_food_threshold[0]
    elasticity_consumption_threshold1 = elasticity_consumption_non_food_threshold[1]
    elasticity_consumption_value0 = elasticity_consumption_non_food_value[0]
    elasticity_consumption_value1 = elasticity_consumption_non_food_value[1]
    elasticity_consumption_value2 = elasticity_consumption_non_food_value[2]
    if CONS_Total <= 0:
        applicable_elasticity_non_food = 0
    elif CONS_Total < elasticity_consumption_threshold0:
        applicable_elasticity_non_food = elasticity_consumption_value0
    elif CONS_Total < elasticity_consumption_threshold1:
        applicable_elasticity_non_food = elasticity_consumption_value1
    else:
        applicable_elasticity_non_food = elasticity_consumption_value2
    return applicable_elasticity_non_food

@iterate_jit(nopython=True)
def cal_CONS_Food_behavior_and_vat(
    rate_food_basic, rate_food_basic_curr_law,
    rate_food_non_basic, rate_food_non_basic_curr_law,
    CONS_food_basic,
    CONS_food_non_basic,
    applicable_elasticity_food,
    vat_Food):
    frac_change_of_consumption_food_basic = applicable_elasticity_food * ((rate_food_basic - rate_food_basic_curr_law) / (1 + rate_food_basic_curr_law))
    frac_change_of_consumption_food_non_basic = applicable_elasticity_food * ((rate_food_non_basic - rate_food_non_basic_curr_law) / (1 + rate_food_non_basic_curr_law))

    CONS_food_basic_behavior = CONS_food_basic * (1 + frac_change_of_consumption_food_basic)
    CONS_food_non_basic_behavior = CONS_food_non_basic * (1 + frac_change_of_consumption_food_non_basic)

    vat_food_basic = rate_food_basic * CONS_food_basic_behavior
    vat_food_non_basic = rate_food_non_basic * CONS_food_non_basic_behavior

    vat_Food = (
        vat_food_basic +
        vat_food_non_basic
    )
    return vat_Food

@iterate_jit(nopython=True)
def cal_CONS_Non_Food_behavior_and_vat(
    rate_cloth,
    rate_cloth_curr_law,
    rate_clothes,
    rate_clothes_curr_law,
    rate_donation,
    rate_donation_curr_law,
    rate_education_services_government,
    rate_education_services_government_curr_law,
    rate_education_services_government_college,
    rate_education_services_government_college_curr_law,
    rate_education_services_private,
    rate_education_services_private_curr_law,
    rate_education_services_private_college,
    rate_education_services_private_college_curr_law,
    rate_electronics_ict,
    rate_electronics_ict_curr_law,
    rate_electronics_ict_repair,
    rate_electronics_ict_repair_curr_law,
    rate_entertainment_goods_music,
    rate_entertainment_goods_music_curr_law,
    rate_entertainment_goods_sports,
    rate_entertainment_goods_sports_curr_law,
    rate_financial_services,
    rate_financial_services_curr_law,
    rate_footwear,
    rate_footwear_curr_law,
    rate_footwear_services,
    rate_footwear_services_curr_law,
    rate_fuel,
    rate_fuel_curr_law,
    rate_fuel_biomass,
    rate_fuel_biomass_curr_law,
    rate_furniture_fixtures,
    rate_furniture_fixtures_curr_law,
    rate_health_equipment,
    rate_health_equipment_curr_law,
    rate_health_services,
    rate_health_services_curr_law,
    rate_health_services_dental,
    rate_health_services_dental_curr_law,
    rate_health_services_paramedical,
    rate_health_services_paramedical_curr_law,
    rate_health_services_testing,
    rate_health_services_testing_curr_law,
    rate_hospital_services,
    rate_hospital_services_curr_law,
    rate_hotel_services,
    rate_hotel_services_curr_law,
    rate_house_repair_goods,
    rate_house_repair_goods_curr_law,
    rate_house_repair_services,
    rate_house_repair_services_curr_law,
    rate_household_accessories_medical,
    rate_household_accessories_medical_curr_law,
    rate_household_electric_equipment,
    rate_household_electric_equipment_curr_law,
    rate_household_equipment,
    rate_household_equipment_curr_law,
    rate_household_gardening,
    rate_household_gardening_curr_law,
    rate_household_goods,
    rate_household_goods_curr_law,
    rate_household_items,
    rate_household_items_curr_law,
    rate_household_repair_services,
    rate_household_repair_services_curr_law,
    rate_household_services,
    rate_household_services_curr_law,
    rate_household_utensils,
    rate_household_utensils_curr_law,
    rate_interest,
    rate_interest_curr_law,
    rate_jewellery,
    rate_jewellery_curr_law,
    rate_legal_services,
    rate_legal_services_curr_law,
    rate_medical_accessories,
    rate_medical_accessories_curr_law,
    rate_medical_life_saving,
    rate_medical_life_saving_curr_law,
    rate_motor_vehicle_four_wheeler,
    rate_motor_vehicle_four_wheeler_curr_law,
    rate_motor_vehicle_two_wheeler,
    rate_motor_vehicle_two_wheeler_curr_law,
    rate_non_motorized_vehicle,
    rate_non_motorized_vehicle_curr_law,
    rate_other_services,
    rate_other_services_curr_law,
    rate_personal_accessories,
    rate_personal_accessories_curr_law,
    rate_personal_accessories_services,
    rate_personal_accessories_services_curr_law,
    rate_personal_expenses_religious,
    rate_personal_expenses_religious_curr_law,
    rate_personal_products,
    rate_personal_products_curr_law,
    rate_personal_services,
    rate_personal_services_curr_law,
    rate_recreation,
    rate_recreation_curr_law,
    rate_religious_services,
    rate_religious_services_curr_law,
    rate_rent,
    rate_rent_curr_law,
    rate_restaurant,
    rate_restaurant_curr_law,
    rate_sports_recreation_services,
    rate_sports_recreation_services_curr_law,
    rate_stationery,
    rate_stationery_curr_law,
    rate_tailoring_cleaning,
    rate_tailoring_cleaning_curr_law,
    rate_tax,
    rate_tax_curr_law,
    rate_telecom_equipment,
    rate_telecom_equipment_curr_law,
    rate_telecom_services,
    rate_telecom_services_curr_law,
    rate_transport,
    rate_transport_curr_law,
    rate_transport_services,
    rate_transport_services_curr_law,
    rate_travel,
    rate_travel_curr_law,
    rate_travel_religious,
    rate_travel_religious_curr_law,
    rate_utilities,
    rate_utilities_curr_law,
    rate_vehicle_equipment,
    rate_vehicle_equipment_curr_law,
    rate_vehicle_services,
    rate_vehicle_services_curr_law,
    CONS_cloth,
    CONS_clothes,
    CONS_donation,
    CONS_education_services_government,
    CONS_education_services_government_college,
    CONS_education_services_private,
    CONS_education_services_private_college,
    CONS_electronics_ict,
    CONS_electronics_ict_repair,
    CONS_entertainment_goods_music,
    CONS_entertainment_goods_sports,
    CONS_financial_services,
    CONS_footwear,
    CONS_footwear_services,
    CONS_fuel,
    CONS_fuel_biomass,
    CONS_furniture_fixtures,
    CONS_health_equipment,
    CONS_health_services,
    CONS_health_services_dental,
    CONS_health_services_paramedical,
    CONS_health_services_testing,
    CONS_hospital_services,
    CONS_hotel_services,
    CONS_house_repair_goods,
    CONS_house_repair_services,
    CONS_household_accessories_medical,
    CONS_household_electric_equipment,
    CONS_household_equipment,
    CONS_household_gardening,
    CONS_household_goods,
    CONS_household_items,
    CONS_household_repair_services,
    CONS_household_services,
    CONS_household_utensils,
    CONS_interest,
    CONS_jewellery,
    CONS_legal_services,
    CONS_medical_accessories,
    CONS_medical_life_saving,
    CONS_motor_vehicle_four_wheeler,
    CONS_motor_vehicle_two_wheeler,
    CONS_non_motorized_vehicle,
    CONS_other_services,
    CONS_personal_accessories,
    CONS_personal_accessories_services,
    CONS_personal_expenses_religious,
    CONS_personal_products,
    CONS_personal_services,
    CONS_recreation,
    CONS_religious_services,
    CONS_rent,
    CONS_restaurant,
    CONS_sports_recreation_services,
    CONS_stationery,
    CONS_tailoring_cleaning,
    CONS_tax,
    CONS_telecom_equipment,
    CONS_telecom_services,
    CONS_transport,
    CONS_transport_services,
    CONS_travel,
    CONS_travel_religious,
    CONS_utilities,
    CONS_vehicle_equipment,
    CONS_vehicle_services,
    applicable_elasticity_non_food,
    vat_Non_Food,
):
    frac_change_of_consumption_cloth = applicable_elasticity_non_food * ((rate_cloth - rate_cloth_curr_law) / (1 + rate_cloth_curr_law))
    frac_change_of_consumption_clothes = applicable_elasticity_non_food * ((rate_clothes - rate_clothes_curr_law) / (1 + rate_clothes_curr_law))
    frac_change_of_consumption_donation = applicable_elasticity_non_food * ((rate_donation - rate_donation_curr_law) / (1 + rate_donation_curr_law))
    frac_change_of_consumption_education_services_government = applicable_elasticity_non_food * ((rate_education_services_government - rate_education_services_government_curr_law) / (1 + rate_education_services_government_curr_law))
    frac_change_of_consumption_education_services_government_college = applicable_elasticity_non_food * ((rate_education_services_government_college - rate_education_services_government_college_curr_law) / (1 + rate_education_services_government_college_curr_law))
    frac_change_of_consumption_education_services_private = applicable_elasticity_non_food * ((rate_education_services_private - rate_education_services_private_curr_law) / (1 + rate_education_services_private_curr_law))
    frac_change_of_consumption_education_services_private_college = applicable_elasticity_non_food * ((rate_education_services_private_college - rate_education_services_private_college_curr_law) / (1 + rate_education_services_private_college_curr_law))
    frac_change_of_consumption_electronics_ict = applicable_elasticity_non_food * ((rate_electronics_ict - rate_electronics_ict_curr_law) / (1 + rate_electronics_ict_curr_law))
    frac_change_of_consumption_electronics_ict_repair = applicable_elasticity_non_food * ((rate_electronics_ict_repair - rate_electronics_ict_repair_curr_law) / (1 + rate_electronics_ict_repair_curr_law))
    frac_change_of_consumption_entertainment_goods_music = applicable_elasticity_non_food * ((rate_entertainment_goods_music - rate_entertainment_goods_music_curr_law) / (1 + rate_entertainment_goods_music_curr_law))
    frac_change_of_consumption_entertainment_goods_sports = applicable_elasticity_non_food * ((rate_entertainment_goods_sports - rate_entertainment_goods_sports_curr_law) / (1 + rate_entertainment_goods_sports_curr_law))
    frac_change_of_consumption_financial_services = applicable_elasticity_non_food * ((rate_financial_services - rate_financial_services_curr_law) / (1 + rate_financial_services_curr_law))
    frac_change_of_consumption_footwear = applicable_elasticity_non_food * ((rate_footwear - rate_footwear_curr_law) / (1 + rate_footwear_curr_law))
    frac_change_of_consumption_footwear_services = applicable_elasticity_non_food * ((rate_footwear_services - rate_footwear_services_curr_law) / (1 + rate_footwear_services_curr_law))
    frac_change_of_consumption_fuel = applicable_elasticity_non_food * ((rate_fuel - rate_fuel_curr_law) / (1 + rate_fuel_curr_law))
    frac_change_of_consumption_fuel_biomass = applicable_elasticity_non_food * ((rate_fuel_biomass - rate_fuel_biomass_curr_law) / (1 + rate_fuel_biomass_curr_law))
    frac_change_of_consumption_furniture_fixtures = applicable_elasticity_non_food * ((rate_furniture_fixtures - rate_furniture_fixtures_curr_law) / (1 + rate_furniture_fixtures_curr_law))
    frac_change_of_consumption_health_equipment = applicable_elasticity_non_food * ((rate_health_equipment - rate_health_equipment_curr_law) / (1 + rate_health_equipment_curr_law))
    frac_change_of_consumption_health_services = applicable_elasticity_non_food * ((rate_health_services - rate_health_services_curr_law) / (1 + rate_health_services_curr_law))
    frac_change_of_consumption_health_services_dental = applicable_elasticity_non_food * ((rate_health_services_dental - rate_health_services_dental_curr_law) / (1 + rate_health_services_dental_curr_law))
    frac_change_of_consumption_health_services_paramedical = applicable_elasticity_non_food * ((rate_health_services_paramedical - rate_health_services_paramedical_curr_law) / (1 + rate_health_services_paramedical_curr_law))
    frac_change_of_consumption_health_services_testing = applicable_elasticity_non_food * ((rate_health_services_testing - rate_health_services_testing_curr_law) / (1 + rate_health_services_testing_curr_law))
    frac_change_of_consumption_hospital_services = applicable_elasticity_non_food * ((rate_hospital_services - rate_hospital_services_curr_law) / (1 + rate_hospital_services_curr_law))
    frac_change_of_consumption_hotel_services = applicable_elasticity_non_food * ((rate_hotel_services - rate_hotel_services_curr_law) / (1 + rate_hotel_services_curr_law))
    frac_change_of_consumption_house_repair_goods = applicable_elasticity_non_food * ((rate_house_repair_goods - rate_house_repair_goods_curr_law) / (1 + rate_house_repair_goods_curr_law))
    frac_change_of_consumption_house_repair_services = applicable_elasticity_non_food * ((rate_house_repair_services - rate_house_repair_services_curr_law) / (1 + rate_house_repair_services_curr_law))
    frac_change_of_consumption_household_accessories_medical = applicable_elasticity_non_food * ((rate_household_accessories_medical - rate_household_accessories_medical_curr_law) / (1 + rate_household_accessories_medical_curr_law))
    frac_change_of_consumption_household_electric_equipment = applicable_elasticity_non_food * ((rate_household_electric_equipment - rate_household_electric_equipment_curr_law) / (1 + rate_household_electric_equipment_curr_law))
    frac_change_of_consumption_household_equipment = applicable_elasticity_non_food * ((rate_household_equipment - rate_household_equipment_curr_law) / (1 + rate_household_equipment_curr_law))
    frac_change_of_consumption_household_gardening = applicable_elasticity_non_food * ((rate_household_gardening - rate_household_gardening_curr_law) / (1 + rate_household_gardening_curr_law))
    frac_change_of_consumption_household_goods = applicable_elasticity_non_food * ((rate_household_goods - rate_household_goods_curr_law) / (1 + rate_household_goods_curr_law))
    frac_change_of_consumption_household_items = applicable_elasticity_non_food * ((rate_household_items - rate_household_items_curr_law) / (1 + rate_household_items_curr_law))
    frac_change_of_consumption_household_repair_services = applicable_elasticity_non_food * ((rate_household_repair_services - rate_household_repair_services_curr_law) / (1 + rate_household_repair_services_curr_law))
    frac_change_of_consumption_household_services = applicable_elasticity_non_food * ((rate_household_services - rate_household_services_curr_law) / (1 + rate_household_services_curr_law))
    frac_change_of_consumption_household_utensils = applicable_elasticity_non_food * ((rate_household_utensils - rate_household_utensils_curr_law) / (1 + rate_household_utensils_curr_law))
    frac_change_of_consumption_interest = applicable_elasticity_non_food * ((rate_interest - rate_interest_curr_law) / (1 + rate_interest_curr_law))
    frac_change_of_consumption_jewellery = applicable_elasticity_non_food * ((rate_jewellery - rate_jewellery_curr_law) / (1 + rate_jewellery_curr_law))
    frac_change_of_consumption_legal_services = applicable_elasticity_non_food * ((rate_legal_services - rate_legal_services_curr_law) / (1 + rate_legal_services_curr_law))
    frac_change_of_consumption_medical_accessories = applicable_elasticity_non_food * ((rate_medical_accessories - rate_medical_accessories_curr_law) / (1 + rate_medical_accessories_curr_law))
    frac_change_of_consumption_medical_life_saving = applicable_elasticity_non_food * ((rate_medical_life_saving - rate_medical_life_saving_curr_law) / (1 + rate_medical_life_saving_curr_law))
    frac_change_of_consumption_motor_vehicle_four_wheeler = applicable_elasticity_non_food * ((rate_motor_vehicle_four_wheeler - rate_motor_vehicle_four_wheeler_curr_law) / (1 + rate_motor_vehicle_four_wheeler_curr_law))
    frac_change_of_consumption_motor_vehicle_two_wheeler = applicable_elasticity_non_food * ((rate_motor_vehicle_two_wheeler - rate_motor_vehicle_two_wheeler_curr_law) / (1 + rate_motor_vehicle_two_wheeler_curr_law))
    frac_change_of_consumption_non_motorized_vehicle = applicable_elasticity_non_food * ((rate_non_motorized_vehicle - rate_non_motorized_vehicle_curr_law) / (1 + rate_non_motorized_vehicle_curr_law))
    frac_change_of_consumption_other_services = applicable_elasticity_non_food * ((rate_other_services - rate_other_services_curr_law) / (1 + rate_other_services_curr_law))
    frac_change_of_consumption_personal_accessories = applicable_elasticity_non_food * ((rate_personal_accessories - rate_personal_accessories_curr_law) / (1 + rate_personal_accessories_curr_law))
    frac_change_of_consumption_personal_accessories_services = applicable_elasticity_non_food * ((rate_personal_accessories_services - rate_personal_accessories_services_curr_law) / (1 + rate_personal_accessories_services_curr_law))
    frac_change_of_consumption_personal_expenses_religious = applicable_elasticity_non_food * ((rate_personal_expenses_religious - rate_personal_expenses_religious_curr_law) / (1 + rate_personal_expenses_religious_curr_law))
    frac_change_of_consumption_personal_products = applicable_elasticity_non_food * ((rate_personal_products - rate_personal_products_curr_law) / (1 + rate_personal_products_curr_law))
    frac_change_of_consumption_personal_services = applicable_elasticity_non_food * ((rate_personal_services - rate_personal_services_curr_law) / (1 + rate_personal_services_curr_law))
    frac_change_of_consumption_recreation = applicable_elasticity_non_food * ((rate_recreation - rate_recreation_curr_law) / (1 + rate_recreation_curr_law))
    frac_change_of_consumption_religious_services = applicable_elasticity_non_food * ((rate_religious_services - rate_religious_services_curr_law) / (1 + rate_religious_services_curr_law))
    frac_change_of_consumption_rent = applicable_elasticity_non_food * ((rate_rent - rate_rent_curr_law) / (1 + rate_rent_curr_law))
    frac_change_of_consumption_restaurant = applicable_elasticity_non_food * ((rate_restaurant - rate_restaurant_curr_law) / (1 + rate_restaurant_curr_law))
    frac_change_of_consumption_sports_recreation_services = applicable_elasticity_non_food * ((rate_sports_recreation_services - rate_sports_recreation_services_curr_law) / (1 + rate_sports_recreation_services_curr_law))
    frac_change_of_consumption_stationery = applicable_elasticity_non_food * ((rate_stationery - rate_stationery_curr_law) / (1 + rate_stationery_curr_law))
    frac_change_of_consumption_tailoring_cleaning = applicable_elasticity_non_food * ((rate_tailoring_cleaning - rate_tailoring_cleaning_curr_law) / (1 + rate_tailoring_cleaning_curr_law))
    frac_change_of_consumption_tax = applicable_elasticity_non_food * ((rate_tax - rate_tax_curr_law) / (1 + rate_tax_curr_law))
    frac_change_of_consumption_telecom_equipment = applicable_elasticity_non_food * ((rate_telecom_equipment - rate_telecom_equipment_curr_law) / (1 + rate_telecom_equipment_curr_law))
    frac_change_of_consumption_telecom_services = applicable_elasticity_non_food * ((rate_telecom_services - rate_telecom_services_curr_law) / (1 + rate_telecom_services_curr_law))
    frac_change_of_consumption_transport = applicable_elasticity_non_food * ((rate_transport - rate_transport_curr_law) / (1 + rate_transport_curr_law))
    frac_change_of_consumption_transport_services = applicable_elasticity_non_food * ((rate_transport_services - rate_transport_services_curr_law) / (1 + rate_transport_services_curr_law))
    frac_change_of_consumption_travel = applicable_elasticity_non_food * ((rate_travel - rate_travel_curr_law) / (1 + rate_travel_curr_law))
    frac_change_of_consumption_travel_religious = applicable_elasticity_non_food * ((rate_travel_religious - rate_travel_religious_curr_law) / (1 + rate_travel_religious_curr_law))
    frac_change_of_consumption_utilities = applicable_elasticity_non_food * ((rate_utilities - rate_utilities_curr_law) / (1 + rate_utilities_curr_law))
    frac_change_of_consumption_vehicle_equipment = applicable_elasticity_non_food * ((rate_vehicle_equipment - rate_vehicle_equipment_curr_law) / (1 + rate_vehicle_equipment_curr_law))
    frac_change_of_consumption_vehicle_services = applicable_elasticity_non_food * ((rate_vehicle_services - rate_vehicle_services_curr_law) / (1 + rate_vehicle_services_curr_law))

    CONS_cloth_behavior = CONS_cloth * (1 + frac_change_of_consumption_cloth)
    CONS_clothes_behavior = CONS_clothes * (1 + frac_change_of_consumption_clothes)
    CONS_donation_behavior = CONS_donation * (1 + frac_change_of_consumption_donation)
    CONS_education_services_government_behavior = CONS_education_services_government * (1 + frac_change_of_consumption_education_services_government)
    CONS_education_services_government_college_behavior = CONS_education_services_government_college * (1 + frac_change_of_consumption_education_services_government_college)
    CONS_education_services_private_behavior = CONS_education_services_private * (1 + frac_change_of_consumption_education_services_private)
    CONS_education_services_private_college_behavior = CONS_education_services_private_college * (1 + frac_change_of_consumption_education_services_private_college)
    CONS_electronics_ict_behavior = CONS_electronics_ict * (1 + frac_change_of_consumption_electronics_ict)
    CONS_electronics_ict_repair_behavior = CONS_electronics_ict_repair * (1 + frac_change_of_consumption_electronics_ict_repair)
    CONS_entertainment_goods_music_behavior = CONS_entertainment_goods_music * (1 + frac_change_of_consumption_entertainment_goods_music)
    CONS_entertainment_goods_sports_behavior = CONS_entertainment_goods_sports * (1 + frac_change_of_consumption_entertainment_goods_sports)
    CONS_financial_services_behavior = CONS_financial_services * (1 + frac_change_of_consumption_financial_services)
    CONS_footwear_behavior = CONS_footwear * (1 + frac_change_of_consumption_footwear)
    CONS_footwear_services_behavior = CONS_footwear_services * (1 + frac_change_of_consumption_footwear_services)
    CONS_fuel_behavior = CONS_fuel * (1 + frac_change_of_consumption_fuel)
    CONS_fuel_biomass_behavior = CONS_fuel_biomass * (1 + frac_change_of_consumption_fuel_biomass)
    CONS_furniture_fixtures_behavior = CONS_furniture_fixtures * (1 + frac_change_of_consumption_furniture_fixtures)
    CONS_health_equipment_behavior = CONS_health_equipment * (1 + frac_change_of_consumption_health_equipment)
    CONS_health_services_behavior = CONS_health_services * (1 + frac_change_of_consumption_health_services)
    CONS_health_services_dental_behavior = CONS_health_services_dental * (1 + frac_change_of_consumption_health_services_dental)
    CONS_health_services_paramedical_behavior = CONS_health_services_paramedical * (1 + frac_change_of_consumption_health_services_paramedical)
    CONS_health_services_testing_behavior = CONS_health_services_testing * (1 + frac_change_of_consumption_health_services_testing)
    CONS_hospital_services_behavior = CONS_hospital_services * (1 + frac_change_of_consumption_hospital_services)
    CONS_hotel_services_behavior = CONS_hotel_services * (1 + frac_change_of_consumption_hotel_services)
    CONS_house_repair_goods_behavior = CONS_house_repair_goods * (1 + frac_change_of_consumption_house_repair_goods)
    CONS_house_repair_services_behavior = CONS_house_repair_services * (1 + frac_change_of_consumption_house_repair_services)
    CONS_household_accessories_medical_behavior = CONS_household_accessories_medical * (1 + frac_change_of_consumption_household_accessories_medical)
    CONS_household_electric_equipment_behavior = CONS_household_electric_equipment * (1 + frac_change_of_consumption_household_electric_equipment)
    CONS_household_equipment_behavior = CONS_household_equipment * (1 + frac_change_of_consumption_household_equipment)
    CONS_household_gardening_behavior = CONS_household_gardening * (1 + frac_change_of_consumption_household_gardening)
    CONS_household_goods_behavior = CONS_household_goods * (1 + frac_change_of_consumption_household_goods)
    CONS_household_items_behavior = CONS_household_items * (1 + frac_change_of_consumption_household_items)
    CONS_household_repair_services_behavior = CONS_household_repair_services * (1 + frac_change_of_consumption_household_repair_services)
    CONS_household_services_behavior = CONS_household_services * (1 + frac_change_of_consumption_household_services)
    CONS_household_utensils_behavior = CONS_household_utensils * (1 + frac_change_of_consumption_household_utensils)
    CONS_interest_behavior = CONS_interest * (1 + frac_change_of_consumption_interest)
    CONS_jewellery_behavior = CONS_jewellery * (1 + frac_change_of_consumption_jewellery)
    CONS_legal_services_behavior = CONS_legal_services * (1 + frac_change_of_consumption_legal_services)
    CONS_medical_accessories_behavior = CONS_medical_accessories * (1 + frac_change_of_consumption_medical_accessories)
    CONS_medical_life_saving_behavior = CONS_medical_life_saving * (1 + frac_change_of_consumption_medical_life_saving)
    CONS_motor_vehicle_four_wheeler_behavior = CONS_motor_vehicle_four_wheeler * (1 + frac_change_of_consumption_motor_vehicle_four_wheeler)
    CONS_motor_vehicle_two_wheeler_behavior = CONS_motor_vehicle_two_wheeler * (1 + frac_change_of_consumption_motor_vehicle_two_wheeler)
    CONS_non_motorized_vehicle_behavior = CONS_non_motorized_vehicle * (1 + frac_change_of_consumption_non_motorized_vehicle)
    CONS_other_services_behavior = CONS_other_services * (1 + frac_change_of_consumption_other_services)
    CONS_personal_accessories_behavior = CONS_personal_accessories * (1 + frac_change_of_consumption_personal_accessories)
    CONS_personal_accessories_services_behavior = CONS_personal_accessories_services * (1 + frac_change_of_consumption_personal_accessories_services)
    CONS_personal_expenses_religious_behavior = CONS_personal_expenses_religious * (1 + frac_change_of_consumption_personal_expenses_religious)
    CONS_personal_products_behavior = CONS_personal_products * (1 + frac_change_of_consumption_personal_products)
    CONS_personal_services_behavior = CONS_personal_services * (1 + frac_change_of_consumption_personal_services)
    CONS_recreation_behavior = CONS_recreation * (1 + frac_change_of_consumption_recreation)
    CONS_religious_services_behavior = CONS_religious_services * (1 + frac_change_of_consumption_religious_services)
    CONS_rent_behavior = CONS_rent * (1 + frac_change_of_consumption_rent)
    CONS_restaurant_behavior = CONS_restaurant * (1 + frac_change_of_consumption_restaurant)
    CONS_sports_recreation_services_behavior = CONS_sports_recreation_services * (1 + frac_change_of_consumption_sports_recreation_services)
    CONS_stationery_behavior = CONS_stationery * (1 + frac_change_of_consumption_stationery)
    CONS_tailoring_cleaning_behavior = CONS_tailoring_cleaning * (1 + frac_change_of_consumption_tailoring_cleaning)
    CONS_tax_behavior = CONS_tax * (1 + frac_change_of_consumption_tax)
    CONS_telecom_equipment_behavior = CONS_telecom_equipment * (1 + frac_change_of_consumption_telecom_equipment)
    CONS_telecom_services_behavior = CONS_telecom_services * (1 + frac_change_of_consumption_telecom_services)
    CONS_transport_behavior = CONS_transport * (1 + frac_change_of_consumption_transport)
    CONS_transport_services_behavior = CONS_transport_services * (1 + frac_change_of_consumption_transport_services)
    CONS_travel_behavior = CONS_travel * (1 + frac_change_of_consumption_travel)
    CONS_travel_religious_behavior = CONS_travel_religious * (1 + frac_change_of_consumption_travel_religious)
    CONS_utilities_behavior = CONS_utilities * (1 + frac_change_of_consumption_utilities)
    CONS_vehicle_equipment_behavior = CONS_vehicle_equipment * (1 + frac_change_of_consumption_vehicle_equipment)
    CONS_vehicle_services_behavior = CONS_vehicle_services * (1 + frac_change_of_consumption_vehicle_services)

    vat_cloth = rate_cloth * CONS_cloth_behavior
    vat_clothes = rate_clothes * CONS_clothes_behavior
    vat_donation = rate_donation * CONS_donation_behavior
    vat_education_services_government = rate_education_services_government * CONS_education_services_government_behavior
    vat_education_services_government_college = rate_education_services_government_college * CONS_education_services_government_college_behavior
    vat_education_services_private = rate_education_services_private * CONS_education_services_private_behavior
    vat_education_services_private_college = rate_education_services_private_college * CONS_education_services_private_college_behavior
    vat_electronics_ict = rate_electronics_ict * CONS_electronics_ict_behavior
    vat_electronics_ict_repair = rate_electronics_ict_repair * CONS_electronics_ict_repair_behavior
    vat_entertainment_goods_music = rate_entertainment_goods_music * CONS_entertainment_goods_music_behavior
    vat_entertainment_goods_sports = rate_entertainment_goods_sports * CONS_entertainment_goods_sports_behavior
    vat_financial_services = rate_financial_services * CONS_financial_services_behavior
    vat_footwear = rate_footwear * CONS_footwear_behavior
    vat_footwear_services = rate_footwear_services * CONS_footwear_services_behavior
    vat_fuel = rate_fuel * CONS_fuel_behavior
    vat_fuel_biomass = rate_fuel_biomass * CONS_fuel_biomass_behavior
    vat_furniture_fixtures = rate_furniture_fixtures * CONS_furniture_fixtures_behavior
    vat_health_equipment = rate_health_equipment * CONS_health_equipment_behavior
    vat_health_services = rate_health_services * CONS_health_services_behavior
    vat_health_services_dental = rate_health_services_dental * CONS_health_services_dental_behavior
    vat_health_services_paramedical = rate_health_services_paramedical * CONS_health_services_paramedical_behavior
    vat_health_services_testing = rate_health_services_testing * CONS_health_services_testing_behavior
    vat_hospital_services = rate_hospital_services * CONS_hospital_services_behavior
    vat_hotel_services = rate_hotel_services * CONS_hotel_services_behavior
    vat_house_repair_goods = rate_house_repair_goods * CONS_house_repair_goods_behavior
    vat_house_repair_services = rate_house_repair_services * CONS_house_repair_services_behavior
    vat_household_accessories_medical = rate_household_accessories_medical * CONS_household_accessories_medical_behavior
    vat_household_electric_equipment = rate_household_electric_equipment * CONS_household_electric_equipment_behavior
    vat_household_equipment = rate_household_equipment * CONS_household_equipment_behavior
    vat_household_gardening = rate_household_gardening * CONS_household_gardening_behavior
    vat_household_goods = rate_household_goods * CONS_household_goods_behavior
    vat_household_items = rate_household_items * CONS_household_items_behavior
    vat_household_repair_services = rate_household_repair_services * CONS_household_repair_services_behavior
    vat_household_services = rate_household_services * CONS_household_services_behavior
    vat_household_utensils = rate_household_utensils * CONS_household_utensils_behavior
    vat_interest = rate_interest * CONS_interest_behavior
    vat_jewellery = rate_jewellery * CONS_jewellery_behavior
    vat_legal_services = rate_legal_services * CONS_legal_services_behavior
    vat_medical_accessories = rate_medical_accessories * CONS_medical_accessories_behavior
    vat_medical_life_saving = rate_medical_life_saving * CONS_medical_life_saving_behavior
    vat_motor_vehicle_four_wheeler = rate_motor_vehicle_four_wheeler * CONS_motor_vehicle_four_wheeler_behavior
    vat_motor_vehicle_two_wheeler = rate_motor_vehicle_two_wheeler * CONS_motor_vehicle_two_wheeler_behavior
    vat_non_motorized_vehicle = rate_non_motorized_vehicle * CONS_non_motorized_vehicle_behavior
    vat_other_services = rate_other_services * CONS_other_services_behavior
    vat_personal_accessories = rate_personal_accessories * CONS_personal_accessories_behavior
    vat_personal_accessories_services = rate_personal_accessories_services * CONS_personal_accessories_services_behavior
    vat_personal_expenses_religious = rate_personal_expenses_religious * CONS_personal_expenses_religious_behavior
    vat_personal_products = rate_personal_products * CONS_personal_products_behavior
    vat_personal_services = rate_personal_services * CONS_personal_services_behavior
    vat_recreation = rate_recreation * CONS_recreation_behavior
    vat_religious_services = rate_religious_services * CONS_religious_services_behavior
    vat_rent = rate_rent * CONS_rent_behavior
    vat_restaurant = rate_restaurant * CONS_restaurant_behavior
    vat_sports_recreation_services = rate_sports_recreation_services * CONS_sports_recreation_services_behavior
    vat_stationery = rate_stationery * CONS_stationery_behavior
    vat_tailoring_cleaning = rate_tailoring_cleaning * CONS_tailoring_cleaning_behavior
    vat_tax = rate_tax * CONS_tax_behavior
    vat_telecom_equipment = rate_telecom_equipment * CONS_telecom_equipment_behavior
    vat_telecom_services = rate_telecom_services * CONS_telecom_services_behavior
    vat_transport = rate_transport * CONS_transport_behavior
    vat_transport_services = rate_transport_services * CONS_transport_services_behavior
    vat_travel = rate_travel * CONS_travel_behavior
    vat_travel_religious = rate_travel_religious * CONS_travel_religious_behavior
    vat_utilities = rate_utilities * CONS_utilities_behavior
    vat_vehicle_equipment = rate_vehicle_equipment * CONS_vehicle_equipment_behavior
    vat_vehicle_services = rate_vehicle_services * CONS_vehicle_services_behavior

    vat_Non_Food = (
        vat_cloth +
        vat_clothes +
        vat_donation +
        vat_education_services_government +
        vat_education_services_government_college +
        vat_education_services_private +
        vat_education_services_private_college +
        vat_electronics_ict +
        vat_electronics_ict_repair +
        vat_entertainment_goods_music +
        vat_entertainment_goods_sports +
        vat_financial_services +
        vat_footwear +
        vat_footwear_services +
        vat_fuel +
        vat_fuel_biomass +
        vat_furniture_fixtures +
        vat_health_equipment +
        vat_health_services +
        vat_health_services_dental +
        vat_health_services_paramedical +
        vat_health_services_testing +
        vat_hospital_services +
        vat_hotel_services +
        vat_house_repair_goods +
        vat_house_repair_services +
        vat_household_accessories_medical +
        vat_household_electric_equipment +
        vat_household_equipment +
        vat_household_gardening +
        vat_household_goods +
        vat_household_items +
        vat_household_repair_services +
        vat_household_services +
        vat_household_utensils +
        vat_interest +
        vat_jewellery +
        vat_legal_services +
        vat_medical_accessories +
        vat_medical_life_saving +
        vat_motor_vehicle_four_wheeler +
        vat_motor_vehicle_two_wheeler +
        vat_non_motorized_vehicle +
        vat_other_services +
        vat_personal_accessories +
        vat_personal_accessories_services +
        vat_personal_expenses_religious +
        vat_personal_products +
        vat_personal_services +
        vat_recreation +
        vat_religious_services +
        vat_rent +
        vat_restaurant +
        vat_sports_recreation_services +
        vat_stationery +
        vat_tailoring_cleaning +
        vat_tax +
        vat_telecom_equipment +
        vat_telecom_services +
        vat_transport +
        vat_transport_services +
        vat_travel +
        vat_travel_religious +
        vat_utilities +
        vat_vehicle_equipment +
        vat_vehicle_services
    )
    return vat_Non_Food

@iterate_jit(nopython=True)
def cal_vat(vat_Food, vat_Non_Food, vatax):
    vatax = vat_Food + vat_Non_Food
    return vatax
