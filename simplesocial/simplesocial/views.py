from django.views.generic import TemplateView
# from django.shortcuts import render
# from ..weather.views import weather_app



class TestPage(TemplateView):
    template_name = "test.html"


class ThanksPage(TemplateView):
    template_name = "thanks.html"


class HomePage(TemplateView):
    template_name = "index.html"

# def HomePage(request):
#     last_3_blogs = blog_app.get_last_3_posts()
#     last_3_images = image_gallery_app.get_last_3_images()
#     highest_ranked_movies = movie_ranking_app.get_top_3()
#     context = {'blog_posts': last_3_blogs, 'images': last_3_images, 'movies': highest_ranked_movies}
#     return render(request, 'home/index.html', context)
