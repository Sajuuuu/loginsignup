from django.urls import path
from. import views
from logSin.settings import DEBUG,STATIC_URL,STATIC_ROOT,MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static


urlpatterns =[
    path('library',views.librarypage,name='library'),
    path('uploadform',views.uploadform,name='uploadform'),

]

if DEBUG:
    urlpatterns += static(STATIC_URL,document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL,document_root = MEDIA_ROOT)