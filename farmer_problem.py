total_land_acres = 80
segments = 5
segment_acres = total_land_acres / segments

tomato_acres = segment_acres
potato_acres = segment_acres
cabbage_acres = segment_acres
sunflower_acres = segment_acres
sugarcane_acres = segment_acres

tomato_yield_tonnes = (tomato_acres * 0.3 * 10) + (tomato_acres * 0.7 * 12)
tomato_sales = tomato_yield_tonnes * 1000 * 7

potato_sales = potato_acres * 10 * 1000 * 20
cabbage_sales = cabbage_acres * 14 * 1000 * 24
sunflower_sales = sunflower_acres * 0.7 * 1000 * 200
sugarcane_sales = sugarcane_acres * 45 * 4000

overall_sales = (
    tomato_sales +
    potato_sales +
    cabbage_sales +
    sunflower_sales +
    sugarcane_sales
)

chemical_free_sales_11_months = (
    tomato_sales +
    potato_sales +
    cabbage_sales +
    sunflower_sales
)

print("Overall Sales from 80 acres:", overall_sales)
print("Chemical Free Sales at end of 11 months:", chemical_free_sales_11_months)
