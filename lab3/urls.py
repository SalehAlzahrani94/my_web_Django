from django.urls import path
from .  import views


app_name="lab3"

urlpatterns = [# list to use all views 
path("aboutpag/", views.about_us, name="path"),
path("adding/",views.add_book,name="add_new_book"),
path("home/",views.about_us,name="frist_page"),
#path("home/",views.home_pa,name="frist_page"),
path("",views.home,name="index"),
path("added",views.book_added,name="added"),
path("Games",views.Games,name="Games"),
path("AI",views.AI,name="AI"),
path("academic_marks",views.academic_marks,name="academic_marks"),
path("search",views.search,name="search_par"),


]