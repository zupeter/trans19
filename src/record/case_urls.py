from django.urls import path

from .case_views import(
	case_record_list_view,
	case_record_create_view,
	case_record_detail_view,
	case_record_update_view,
	case_record_delete_view,
	case_record_add_visit_view,
)

urlpatterns = [
	path('',case_record_list_view),
	path('create/',case_record_create_view),
	path('<int:case_num>/',case_record_detail_view),
	path('<int:case_num>/modify/',case_record_update_view),
	path('<int:case_num>/delete/',case_record_delete_view),
	path('<int:case_num>/visit/add/',case_record_add_visit_view)
]
