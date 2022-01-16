from django.shortcuts import render

posts = \
    [{
        "title": "Django Tutorial ",
        "author": "Corey Schafer",
        "content": "Tutorial 1",
        "date_posted": "16th Jan 2022",
    },
        {
            "title": "Django Features ",
            "author": "Jane Archaic",
            "content": "Features 1",
            "date_posted": "17th Jan 2022",
        }

    ]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
