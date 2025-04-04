from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from .search_api_view import SearchAPIView

urlpatterns = [
    path('login', views.login_view, name='api-login'),
    path('webapp_login', views.webapp_login_view, name='webapp-api-login'),
    path('verify_otp', views.verify_otp_view, name='verify_otp'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('cars/', views.HomeAPIView.as_view(), name='cars-list'),
    path('cars/<int:cat_id>/', views.UserCarDetail.as_view(), name='car-detail'),  
    path('issues/<int:issue_id>/', views.UserIssueDetailView.as_view(), name='issue-detail'),  
    path('steps/<int:step_id>/', views.UserStepDetail.as_view(), name='step-detail'),
    path('subscription-plans/', views.SubscriptionPlanListView.as_view(), name='subscription-plan-list'),
    path('activate-subscription/', views.ActivateSubscriptionView.as_view(), name='activate-subscription'),
    path('user-subscription/', views.UserSubscriptionView.as_view(), name='user-subscription'),
    path('advertisements/', views.AdvertisementListView.as_view(), name='advertisement-list'),


    # URLهای مربوط به چت
    path('start-chat/', views.StartChatView.as_view(), name='start-chat'),
    path('send-message/', views.SendMessageView.as_view(), name='send_message'),
    path('close-chat/<int:session_id>/', views.CloseChatView.as_view(), name='close_chat'),
    path('chat/<int:session_id>/messages/', views.ChatMessagesAPIView.as_view(), name='chat-messages'),
    path('chat/<int:session_id>/mark_as_read/', views.MarkMessagesAsReadView.as_view(), name='mark_messages_as_read'),
    path('search/', SearchAPIView.as_view(), name='search-api'),  # Add the new search API endpoint


    path('articles/', views.ArticleListAPIView.as_view(), name='article-list'), 
    path('payment/request/', views.PaymentRequestAPIView.as_view(), name='payment_request'),
    path('payment/verify/', views.PaymentVerificationAPIView.as_view(), name='payment_verify'),
    path('payment/status/', views.PaymentStatusAPIView.as_view(), name='payment_status'),
    path('send-otp/', views.send_otp, name='send_otp'),
    path('resend-otp/', views.resend_otp, name='resend_otp'),
    path('verify-otp-and-signup/', views.verify_otp_and_signup, name='verify_otp_and_signup'),
    
    path('referral/<int:user_id>', views.ReferralCodeDetailAPIView.as_view(), name='referral-code'),
    path('discount-codes/<int:user_id>', views.DiscountCodeDetailAPIView.as_view(), name='discount-codes'),
    path('user-profile/', views.UserProfileAPIView.as_view(), name='user-profile'),
    path('articles/<int:article_id>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('categories/', views.CategoryAPIView.as_view(), name='categories'),

    path('password/reset/request-otp/', views.request_password_reset_otp, name='request-password-reset-otp'),
    path('password/reset/verify-otp/', views.verify_password_reset_otp, name='verify-password-reset-otp'),
    path('password/reset/complete/', views.complete_password_reset, name='complete-password-reset'),
]
