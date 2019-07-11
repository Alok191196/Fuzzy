from django.conf.urls import url
import Fuzzy.views as v

urlpatterns = [
    # url(r'compileTest', v.compile_debug, name='compileTest'),
    # url(r'compile', v.compile_test_cases, name='compile'),
    # url(r'add', staff_member_required(v.add_question, login_url="/login"), name='add_question'),
    url(r'^subject$', v.subject, name='subject'),
    url(r'^save_marks$', v.save_marks, name='save_marks'),
    url(r'^$', v.dashboard, name='dashboard'),
    url(r'^login$', v.login_user, name='login'),
    url(r'^signup$', v.signup_user, name='signup'),
    url(r'^student', v.student, name='addData'),
    url(r'^algo$', v.algo, name='algo'),
    url(r'^algo1$', v.algo1, name='algo'),
    # url(r'^show$', v.show, name='show'),
    url(r'^logout$', v.logout_user, name='logout'),
    url(r'^show/(?P<idn>\d+)/$', v.show, name='show'),
    url(r'^eligibility$', v.eligibility, name='eligibility'),
    url(r'^search$', v.search, name='search'),
]
