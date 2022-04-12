mph = 0.44704
avg_wind_speed_wallowa = 23.98 * mph
avg_wind_speed_columbia = 8.25 * mph
blade_radius1 = 2
blade_radius2 = 3
high_efficiency = 0.98
low_efficiency = 0.10
print(avg_wind_speed_wallowa * blade_radius1)
print(avg_wind_speed_wallowa * blade_radius1 * high_efficiency)
print(avg_wind_speed_wallowa * blade_radius2)
print(avg_wind_speed_wallowa * blade_radius2 * low_efficiency)
print(avg_wind_speed_columbia * blade_radius1)
print(avg_wind_speed_columbia * blade_radius1 * high_efficiency)
print(avg_wind_speed_columbia * blade_radius2)
print(avg_wind_speed_columbia * blade_radius2 * low_efficiency)
joules_per_year = 2.57 * 10 ** 10
seconds_per_year = 31536000
wtj_wallowa_high_eff = avg_wind_speed_wallowa * blade_radius1 * high_efficiency
print(joules_per_year // wtj_wallowa_high_eff // seconds_per_year)
wtj_wallowa_low_eff = avg_wind_speed_wallowa * blade_radius2 * low_efficiency
print(joules_per_year // wtj_wallowa_low_eff // seconds_per_year)
wtj_columbia_high_eff = avg_wind_speed_columbia * blade_radius1 * high_efficiency
print(joules_per_year // wtj_columbia_high_eff // seconds_per_year)
wtj_columbia_low_eff = avg_wind_speed_columbia * blade_radius2 * low_efficiency
print(joules_per_year // wtj_columbia_low_eff // seconds_per_year)
kg_coal_joules = 29307600
print(joules_per_year // kg_coal_joules)



