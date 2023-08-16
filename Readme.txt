urls
/restaurant/booking/tables
/restaurant/menu
/restaurant/menu/<int:pk>




in root / project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/',include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

]

in /restaurant
urlpatterns = [
    path('', views.index, name='index'),
    path('menu/',views.MenuItemView.as_view()),
    path('menu/<int:pk>/',views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),

]


