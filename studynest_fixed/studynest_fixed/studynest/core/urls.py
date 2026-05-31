from django.urls import path
from . import views

urlpatterns = [
    # Page
    path('', views.index, name='index'),

    # Auth
    path('api/auth/register/',         views.api_register,         name='api_register'),
    path('api/auth/login/',            views.api_login,            name='api_login'),
    path('api/auth/logout/',           views.api_logout,           name='api_logout'),
    path('api/auth/me/',               views.api_me,               name='api_me'),

    # Tasks
    path('api/tasks/',                 views.api_tasks,            name='api_tasks'),
    path('api/tasks/<int:task_id>/',   views.api_task_detail,      name='api_task_detail'),

    # Focus sessions
    path('api/sessions/complete/',     views.api_session_complete, name='api_session_complete'),
    path('api/stats/',                 views.api_stats,            name='api_stats'),

    # Social
    path('api/users/search/',          views.api_search_users,     name='api_search_users'),
    path('api/users/check/',           views.api_check_username,   name='api_check_username'),
    path('api/friends/',               views.api_friends,          name='api_friends'),
    path('api/requests/send/',         views.api_send_request,     name='api_send_request'),
    path('api/requests/respond/',      views.api_respond_request,  name='api_respond_request'),
    path('api/requests/pending/',      views.api_pending_requests, name='api_pending_requests'),

    # Messages
    path('api/messages/<int:peer_id>/', views.api_messages,        name='api_messages'),

    # AI Search (proxied — fixes CORS error from direct browser calls)
    path('api/ai/search/',             views.api_ai_search,        name='api_ai_search'),
]
