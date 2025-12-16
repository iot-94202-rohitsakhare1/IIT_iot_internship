def km_to_m(distance):
    return distance * 1000

def m_to_cm(distance):
    return distance * 100

def cm_to_mm(distance):
    return distance * 10

def ft_to_in(distance):
    return distance * 12

def in_to_cm(distance):
    return distance * 2.54

def distance_converter(distance, conversion_type, conversion_func):
    result = conversion_func(distance)
    from_unit, to_unit = conversion_type.split(' to ')
    print(f"{distance} {from_unit} is {result} {to_unit}")

distance = float(input("Enter distance in kilometers: "))
distance_converter(distance, "km to m", km_to_m)
distance = km_to_m(distance)
distance_converter(distance, "m to cm", m_to_cm)
distance = m_to_cm(distance)
distance_converter(distance, "cm to mm", cm_to_mm)
distance_ft = distance 
distance_converter(distance_ft, "ft to in", ft_to_in)
distance_in = ft_to_in(distance_ft)
distance_converter(distance_in, "in to cm", in_to_cm)
