from django.shortcuts import render

def home(request):

    score = None
    result = None

    if request.method == "POST":
        link = request.POST.get("link")
        followers = int(request.POST.get("followers"))

        if followers > 1000:
            score = 90
            result = "Likely Human"
        elif followers > 500:
            score = 70
            result = "Likely Human"
        elif followers > 100:
            score = 50
            result = "Moderate Trust"
        else:
            score = 30
            result = "Suspicious Account"

    return render(request, "index.html", {"score": score, "result": result})
