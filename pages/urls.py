from django.urls import path
from pages.views import contact_us
from pages.views import about_us
from pages.views import terms_and_condition
from pages.views import return_and_refund
from pages.views import shipping_policy
from pages.views import privacy_policy

urlpatterns = [
    path('about_us/', about_us, name = 'about_us'),
    path('contact_us/', contact_us, name = 'contact_us'),
    path('terms_and_conditions/', terms_and_condition, name = 'terms_and_conditions'),
    path('return_and_refund/', return_and_refund, name = 'return_and_refund'),
    path('shipping_policy/', shipping_policy, name = 'shipping_policy'),
    path('privacy_policy/', privacy_policy, name = 'privacy_policy'),
]