import pathlib
from django.shortcuts import render
from django.http import HttpResponse

from core.models import PageCore

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *arg, **kwargs):
    qs = PageCore.objects.all()
    page_qs = PageCore.objects.filter(path=request.path)
    my_title = "My Page"
    html_template = "home.html"
    my_context ={
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent_page_visit_count": (page_qs.count() / qs.count()) * 100 if qs.count() > 0 else 0,
        "total_page_count": qs.count()
    }
    PageCore.objects.create(path=request.path)

    return render(request, html_template, my_context)



def my_old_home_page_view(request, *arg, **kwargs):
    my_title = "My Page"
    my_context ={
        "page_title": my_title
    }
    html_ = """
<!DOCTYPE html>
<html>

<head>

    <title>Saas</title>

</head>

<body>

    <h1>{page_title} is anything? </h1>


</body>
</html>
""".format(**my_context)
    #html_file_path = this_dir / "home.html"
    #html_= html_file_path.read_text()
    return HttpResponse(html_)
    