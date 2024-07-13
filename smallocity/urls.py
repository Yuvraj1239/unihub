from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from core.views import frontpage, about ,homepage,aboute
from events import views as event_views
from django.contrib.auth.urls import views as auth_views
from main import views
from main.views import home,user_login,unregister_from_event,register_for_event,MessageListView,ModeratorProfileView,SpeakerDeleteView,SpeakerUpdateView,SpeakerCreateView,SpeakerProfileView,SpeakerListView,CategoryDeleteView,CategoryUpdateView,CategoryCreateView,CategoryListView,EventListView,ModEventListView,EventDetailView,EventCreateView,EventUpdateView,EventDeleteView,ParticipantListView,ParticipantDeleteView,ParticipantProfileView,UserRegisterView,UserLogoutView
from django.views.generic import RedirectView
favicon_view = RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico', permanent=True)


urlpatterns = [
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
    re_path(r'^events/', include('events.urls')),
    re_path(r'^accounts/', include('accounts.urls')),
    re_path(r'^aboute/$', aboute, name='aboute'),
    re_path(r'^e/$', event_views.event_list, name="carhome"),

    path('h/', home, name='home'),
    path('events/', EventListView.as_view(), name='events'),
    path('event_list/', ModEventListView.as_view(), name='events_list'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('event/new/', EventCreateView.as_view(), name='event_create'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event_update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('participants/', ParticipantListView.as_view(), name='participants'),
    path('participants/<int:pk>/delete/', ParticipantDeleteView.as_view(), name='participant_delete'),
    path('participants/<int:pk>/', ParticipantProfileView.as_view(), name='participant_profile'),
    path('account/register/', UserRegisterView.as_view(), name='register'),
    path('account/login/', user_login, name='login'),
    path('account/logout/', UserLogoutView.as_view(), name='logout'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/new/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    path('speakers/', SpeakerListView.as_view(), name='speakers'),
    path('speakers/<int:pk>/', SpeakerProfileView.as_view(), name='speaker_profile'),
    path('speakers/new/', SpeakerCreateView.as_view(), name='speaker_create'),
    path('speakers/<int:pk>/update/', SpeakerUpdateView.as_view(), name='speaker_update'),
    path('speakers/<int:pk>/delete/', SpeakerDeleteView.as_view(), name='speaker_delete'),
    path('moderators/<int:pk>/', ModeratorProfileView.as_view(), name='mod_profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('events/<int:event_id>/register/', register_for_event, name='register_for_event'),
    path('events/<int:event_id>/unregister/', unregister_from_event, name='unregister_from_event'),
    path('messages/', MessageListView.as_view(), name='messages'),
    path('messages/<int:pk>/', views.MessageDetailView.as_view(), name='message_detail'),
    path('contact/', views.MessageCreateView.as_view(), name='contact'),
    path('messages/<int:pk>/delete/', views.MessageDeleteView.as_view(), name='message_delete'),
    path('about/', views.about, name='about'),
    re_path(r'^favicon\.ico$', favicon_view),
    

    path('', include('userprofile.urls')),
    path('', include('store.urls')),
    path('', frontpage, name='frontpage',),

   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
