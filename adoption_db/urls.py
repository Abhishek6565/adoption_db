"""adoption_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from adoptionapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url('^log/$',views.login,name='login'),
    url('^forgetpass/$',views.forgetpass,name='forgetpass'),
    url('^otp/$',views.otp,name='otp'),
    url('^pass_db/$',views.pass_db,name='pass_db'),
    url('^reg/$',views.reg,name='reg'),
    url('^changepass/$',views.changepass,name='changepass'),

    url('^babyinfo/$', views.babyinfo, name='babyinfo'),
    url('^parentsinfo/$', views.parentsinfo, name='parentsinfo'),
    url('^reqstatus/$', views.reqstatus, name='reqstatus'),
    url('^homevststatus/(?P<pk>\d+)/$', views.homevststatus, name='homevststatus'),
    url('^surityinfo/$', views.surityinfo, name='surityinfo'),
    url('^charityinfo/$', views.charityinfo, name='charityinfo'),
    url('^donationinfo/$', views.donationinfo, name='donationinfo'),
    url('^orphanageinfo/$', views.orphanageinfo, name='orphanageinfo'),
    url('^orphnhltsts/$', views.orphnhltsts, name='orphnhltsts'),
    url('^UserRegistration_view/$', views.UserRegistration_view, name='UserRegistration_view'),

    url('^BabyInfo_view/$', views.BabyInfo_view, name='BabyInfo_view'),
    url('^BabyInfo_view_p/$', views.BabyInfo_view_p, name='BabyInfo_view_p'),
    url('^BabyInfo_view_m/$', views.BabyInfo_view_m, name='BabyInfo_view_m'),
    url('^adoption_status_view_p/$', views.adoption_status_view_p, name='adoption_status_view_p'),


    url('^babyinfo_del/(?P<pk>\d+)/$',views.babyinfo_del,name='babyinfo_del'),
    url('^BabyInfo_update/(?P<pk>\d+)/$', views.BabyInfo_update, name='BabyInfo_update'),
    url('^babyinfo_db/$',views.babyinfo_db,name='babyinfo_db'),

    url('^ParentsInfo_view/(?P<pk>\d+)/$', views.ParentsInfo_view, name='ParentsInfo_view'),
    url('^parents_del/(?P<pk>\d+)/$',views.parents_del,name='parents_del'),
    url('^parents_update/(?P<pk>\d+)/$', views.parents_update, name='parents_update'),
    url('^parentsinfo_db/$',views.parentsinfo_db,name='parentsinfo_db'),

    url('^Requeststatus_view/$', views.Requeststatus_view, name='Requeststatus_view'),
    url('^req_status_update/(?P<pk>\d+)/$', views.req_status_update, name='req_status_update'),
    url('^req_status_db/$',views.req_status_db,name='req_status_db'),
    url('^req_status_del/(?P<pk>\d+)/$', views.req_status_del, name='req_status_del'),

    url('^Homevstngstatus_view/$', views.Homevstngstatus_view, name='Homevstngstatus_view'),
    url('^Homevstngstatus_view_p/$', views.Homevstngstatus_view_p, name='Homevstngstatus_view_p'),
    url('^homevstngstatus_update/(?P<pk>\d+)/$', views.homevstngstatus_update, name='homevstngstatus_update'),
    url('^homevstngstatus_db/$',views.homevstngstatus_db,name='homevstngstatus_db'),
    url('^homevstngstatus_del/(?P<pk>\d+)/$', views.homevstngstatus_del, name='homevstngstatus_del'),

    url('^SurityInfo_view/$', views.SurityInfo_view, name='SurityInfo_view'),
    url('^SurityInfo_view_s/(?P<pk>\d+)/$', views.SurityInfo_view_s, name='SurityInfo_view_s'),
    url('^surityInfo_update/(?P<pk>\d+)/$', views.surityInfo_update, name='surityInfo_update'),
    url('^surityInfo_db/$',views.surityInfo_db,name='surityInfo_db'),
    url('^surityInfo_del/(?P<pk>\d+)/$', views.surityInfo_del, name='surityInfo_del'),

    url('^CharityInfo_view/$', views.CharityInfo_view, name='CharityInfo_view'),
    url('^CharityInfo_view_m/$', views.CharityInfo_view_m, name='CharityInfo_view_m'),

    url('^charityInfo_update/(?P<pk>\d+)/$', views.charityInfo_update, name='charityInfo_update'),
    url('^CharityInfo_db/$', views.CharityInfo_db, name='CharityInfo_db'),
    url('^CharityInfo_del/(?P<pk>\d+)/$', views.CharityInfo_del, name='CharityInfo_del'),

    url('^DonationInfo_view/$', views.DonationInfo_view, name='DonationInfo_view'),
    url('^DonationInfo_view_m/$', views.DonationInfo_view_m, name='DonationInfo_view_m'),
    url('^donationInfo_update/(?P<pk>\d+)/$', views.donationInfo_update, name='donationInfo_update'),
    url('^donationInfo_db/$', views.donationInfo_db, name='donationInfo_db'),
    url('^donationInfo_del/(?P<pk>\d+)/$', views.donationInfo_del, name='donationInfo_del'),

    url('^OrphanageInfo_view/$', views.OrphanageInfo_view, name='OrphanageInfo_view'),
    url('^OrphanageInfo_view_d/$', views.OrphanageInfo_view_d, name='OrphanageInfo_view_d'),
    url('^OrphanageInfo_update/(?P<pk>\d+)/$', views.OrphanageInfo_update, name='OrphanageInfo_update'),
    url('^OrphanageInfo_db/$', views.OrphanageInfo_db, name='OrphanageInfo_db'),
    url('^OrphanageInfo_del/(?P<pk>\d+)/$', views.OrphanageInfo_del, name='OrphanageInfo_del'),

    url('^OrphnHltSts_view/$', views.OrphnHltSts_view, name='OrphnHltSts_view'),
    url('^OrphnHltSts_update/(?P<pk>\d+)/$', views.OrphnHltSts_update, name='OrphnHltSts_update'),
    url('^OrphnHltSts_db/$', views.OrphnHltSts_db, name='OrphnHltSts_db'),
    url('^OrphnHltSts_del/(?P<pk>\d+)/$', views.OrphnHltSts_del, name='OrphnHltSts_del'),
    url('^parent_home/$', views.parent_home, name='parent_home'),
    url('^admin_home/$', views.admin_home, name='admin_home'),
    url('^donor_home/$', views.donor_home, name='donor_home'),
    url('^manager_home/$', views.manager_home, name='manager_home'),
    url('^adoption_request/(?P<pk>\d+)/$', views.adoption_request, name='adoption_request'),
    url('^adoption_request_view_m/$', views.adoption_request_view_m, name='adoption_request_view_m'),
    url('^adoption_request_update/$', views.adoption_request_update, name='adoption_request_update'),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
