from django.shortcuts import render

posts = \
    [{
        "title": "Blog Post 1 ",
        "author": "Corey Schafer",
        "content": "First post content",
        "date_posted": "16th Jan 2022",
    },
        {
            "title": "Blog Post 2 ",
            "author": "Jane Archaic",
            "content": "Second post content",
            "date_posted": "17th Jan 2022",
        }

    ]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
