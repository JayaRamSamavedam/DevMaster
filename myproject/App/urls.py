
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from App import views

urlpatterns = [
    # path('',include("App.urls")),
    path("",views.index,name="index"),
    path("home",views.index,name="home"),
    path("aboutus",views.aboutus,name="aboutus"),
    path("contact",views.contact,name="contact"),
    path("faq",views.faq,name="faq"),
    path("productdetail",views.productdetail,name="productdetail"),
    path("products",views.products,name="products"),
    path("signup",views.signup,name="signup"),
    path("signin",views.signin,name="signin"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
