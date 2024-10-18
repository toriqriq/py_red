def get_day_name(day_number):
    if day_number == 1:
        return "Senin"
    elif day_number == 2:
        return "Selasa"
    elif day_number == 3:
        return "Rabu"
    elif day_number == 4:
        return "Kamis"
    elif day_number == 5:
        return "Jumat"
    elif day_number == 6:
        return "Sabtu"
    elif day_number == 7:
        return "Minggu"
    else:
        return "Hari tidak valid"

print(get_day_name(4)) 
