def importe_total_carroPS5(request):
    total=0
    if request.user.is_authenticated:
        for key, value in request.sessionPS5["carroPS5"].items():
            total=total+float(value["precioPS5"])
    
    return {"importe_total_carroPS5":total}
