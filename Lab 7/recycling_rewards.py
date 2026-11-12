import math


def parse_collection(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    parts = text.split(":")
    if len(parts) != 2:
        raise ValueError("Expected material:weight")

    material, kg_text = parts
    material = material.strip()

    try:
        kg = float(kg_text.strip())
    except (ValueError, OverflowError):
        raise ValueError("Invalid weight")

    if not material or not math.isfinite(kg) or kg < 0:
        raise ValueError("Invalid material or weight")

    return material.title(), kg


def weight_average(weights_csv):
    if not isinstance(weights_csv, str):
        raise ValueError("Input must be a string")

    parts = weights_csv.split(",")

    if not parts or any(not p.strip() for p in parts):
        raise ValueError("Empty weight")

    try:
        values = [int(p.strip()) for p in parts]
    except (ValueError, OverflowError):
        raise ValueError("Invalid weight")

    if any(v < 0 for v in values):
        raise ValueError("Negative weight")

    return sum(values) // len(values)


def net_points(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    parts = text.split("|")
    if len(parts) != 2:
        raise ValueError("Expected points|penalty")

    try:
        points = float(parts[0].strip())
        penalty = float(parts[1].strip())
    except (ValueError, OverflowError):
        raise ValueError("Invalid points")

    if (not math.isfinite(points) or
            not math.isfinite(penalty) or
            points < 0 or penalty < 0):
        raise ValueError("Invalid points or penalty")

    return max(points * 2 - penalty, 0)


def main():
    print("==== Running parse_collection ====")
    try:
        user_input = input("Enter material:weight in kg (e.g. paper:12): ")
        print("Material and Weight:", parse_collection(user_input))
    except ValueError as e:
        print("Invalid input:", e)

    print("\n==== Running weight_average ====")
    try:
        user_input = input("Enter weights in kg as CSV (e.g. 5,12,20): ")
        print("Average Weight:", weight_average(user_input))
    except ValueError as e:
        print("Invalid input:", e)

    print("\n==== Running net_points ====")
    try:
        user_input = input("Enter points|penalty (e.g. 80|10): ")
        print("Net Points:", net_points(user_input))
    except ValueError as e:
        print("Invalid input:", e)


if __name__ == "__main__":
    main()
