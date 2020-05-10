from django.urls import path

from .case_views import(
	case_record_list_view,
	case_record_create_view,
	case_record_detail_view,
	case_record_update_view,
	case_record_delete_view,
	case_record_add_visit_view,
	case_record_modify_visit_view,
	case_record_delete_visit_view,
	case_search_connections,
)

urlpatterns = [
	path('',case_record_list_view),
	path('create/',case_record_create_view),
	path('<int:pkey>/',case_record_detail_view),
	path('<int:pkey>/modify/',case_record_update_view),
	path('<int:pkey>/delete/',case_record_delete_view),
	path('<int:pkey>/trace',case_search_connections),
	path('<int:pkey>/visit/add/',case_record_add_visit_view),
	path('<int:pkey>/visit/<int:vpkey>/modify',case_record_modify_visit_view),
	path('<int:pkey>/visit/<int:vpkey>/delete',case_record_delete_visit_view),
]
