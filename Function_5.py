def betuk(text):
    #maganhangzok = "["a","á","e","é","i","í","o","ó","ö","ő","u","ú","ü","ű","A","Á","E","É","I","Í","O","Ó","Ö","Ő","U","Ú","Ü","Ű"]"
    maganhangzok = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"
    mag_count = 0
    for c in text:
        for mgh in maganhangzok:
            if c == mgh:
                mag_count += 1
                break
    return mag_count

text = """aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"""
mgh= betuk(text)
print(f"Magánhangzók száma: {mgh}")