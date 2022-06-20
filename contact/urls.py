from django.urls import path
from . import views
contact_urlpatterns=([
    path('create-contact/',views.create_contact,name='create-contact'),
    path('list-contact/',views.list_contact,name='list-contact'),
    path('detail-contact/<int:pk>',views.detail_contact,name='detail-contact'),
    path('edit-contact/<int:pk>',views.edit_contact,name='edit-contact'),
    path('delete-contact/<int:pk>',views.delete_contact,name='delete-contact')
],'contact')