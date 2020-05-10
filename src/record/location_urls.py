from django.urls import path

from .location_views import (
	location_record_list_view,
	location_record_create_view,
	location_record_detail_view,
	location_record_update_view,
	location_record_delete_view,
)
from .case_views import case_record_delete_visit_view

urlpatterns = [
	path('',location_record_list_view),
	path('create/',location_record_create_view),
	path('<int:pkey>/detail/',location_record_detail_view),
	path('<int:pkey>/modify/',location_record_update_view),
	path('<int:pkey>/delete/',location_record_delete_view),
	path('<int:pkey>/delete/visit/<int:vpkey>/delete',case_record_delete_visit_view),
]
# when you dont want to use int as reference,
# and using str, then redesign the whole url patten
