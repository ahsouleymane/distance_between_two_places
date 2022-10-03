




def trouver_addresse_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def centre_coordonnees(latA, lonA, latB=None, lonB=None):
    cord = (latA, lonA)
    if latB:
        cord = [(latA + latB)/2, (lonA + lonB)/2]
    return cord

def zoomer(distance):
    if distance <= 100:
        return 8
    elif distance > 100 and distance <= 5000:
        return 4
    else:
        return 2

