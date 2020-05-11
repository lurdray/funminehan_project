from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexFunc, name="index"),
    path('about/', views.AboutFunc, name="about"),
    path('contact/', views.ContactFunc, name="contact"),
    path('gallery/', views.GalleryFunc, name="gallery"),
    path('outreach/', views.OutreachFunc, name="outreach"),
    path('outreach/<slug:slug>/', views.OutreachDetailFunc, name="outreach_detail"),
    path('member/<slug:slug>/', views.MemberDetailFunc, name="member_detail"),
    
     path('donation/', views.PreDonationFunc, name="pre_donation"),
    path('donation/<int:donation_id>/', views.DonationFunc, name="donation"),
    
    path('postoutreach/', views.PostOutreachFunc, name="post_outreach"),
    path('postmember/', views.PostMemberFunc, name="post_member"),
    path('postevent/', views.PostEventFunc, name="post_event"),

]
