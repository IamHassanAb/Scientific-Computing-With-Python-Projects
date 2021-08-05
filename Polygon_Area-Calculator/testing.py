def get_picture(height, width):
    if width or height > 50:
        return "Too big for picture"
    picture = ""
    star= ""
    for lines in range(height):
        for stars in range(width):
            star +="*"
        picture += star+"\n"
        star = ""
    return (picture)




print(get_picture(50,10))