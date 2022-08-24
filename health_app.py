IDEAL_LOWER_BMI = 19
IDEAL_HIGHER_BMI = 25


def main():
    weight_in_kg = float(input("Weight (kg)? "))
    height_in_metres = float(input("Height (m)? "))

    bmi = calculate_bmi(height_in_metres, weight_in_kg)

    ideal_higher_weight, ideal_lower_weight = get_ideal_weight_range(height_in_metres)

    if bmi < 19:
        print("Underweight")
        print(f"Your ideal weight range should be: {ideal_lower_weight:.1f} - {ideal_higher_weight:.1f}")
    elif 19 <= bmi <= 25:
        print("Nice weight")
    else:
        print("Overweight")
        print(f"Your ideal weight range should be: {ideal_lower_weight:.1f} - {ideal_higher_weight:.1f}")


def get_ideal_weight_range(height_in_metres):
    """Return  ideal weight range in kg."""
    ideal_lower_weight = IDEAL_LOWER_BMI * height_in_metres * height_in_metres
    ideal_higher_weight = IDEAL_HIGHER_BMI * height_in_metres * height_in_metres
    return ideal_higher_weight, ideal_lower_weight


def calculate_bmi(height_in_metres, weight_in_kg):
    """Return BMI based on weight and height."""
    return weight_in_kg / height_in_metres ** 2


main()
