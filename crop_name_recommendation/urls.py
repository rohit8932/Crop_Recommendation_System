from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='login'),
    url(r'^login/$', views.signin, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^home/$', views.home, name='home'),
    url(r'^svm/$', views.svm, name='svm'),
    url(r'^naivebayes/$', views.naivebayes, name='naivebayes'),
    url(r'^neuralnetwork/$', views.neuralnetwork, name='neuralnetwork'),
    url(r'^randomforest/$', views.randomforest, name='randomforest'),
    url(r'^naive_bayes_algo/$', views.naiveBayesAlgo, name='naive_bayes_algo'),
    url(r'^svm_algo/$', views.svmAlgo, name='svm_algo'),
    url(r'^neural_network_algo/$', views.neuralNetworkAlgo, name='neural_network_algo'),
    url(r'^random_forest_algo/$', views.randomForestAlgo, name='random_forest_algo'),
    url(r'^hybrid_algo/$', views.hybrideAlgo, name='hybrid_algo'),
    url(r'^e_algo/$', views.runEAlgo, name='e_algo'),
    url(r'^ensembleTech/$', views.ensembleTech, name='ensembleTech'),
    url(r'^logout/$', views.userLogout, name='logout'),
]
