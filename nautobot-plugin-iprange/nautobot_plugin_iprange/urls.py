from django.urls import path
from nautobot.extras.views import ObjectChangeLogView

from nautobot_plugin_iprange import models, views

urlpatterns = [
    path("", views.IPRangeListView.as_view(), name="iprange_list"),
    path("add/", views.IPRangeEditView.as_view(), name="iprange_add"),
    path("edit/", views.IPRangeBulkEditView.as_view(), name="iprange_bulk_edit"),
    path("delete/", views.IPRangeBulkDeleteVIew.as_view(), name="iprange_bulk_delete"),
    path("<uuid:pk>/", views.IPRangeDetailView.as_view(), name="iprange"),
    path("<uuid:pk>/edit/", views.IPRangeEditView.as_view(), name="iprange_edit"),
    path("<uuid:pk>/delete/", views.IPRangeDeleteView.as_view(), name="iprange_delete"),
    path(
        "<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="iprange_changelog",
        kwargs={"model": models.IPRange},
    ),
]
