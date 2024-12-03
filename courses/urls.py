from django.urls import path
from courses.views import CourseView, CourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView

app_name = "courses"
urlpatterns = [
    path("", CourseView.as_view(template_name="courses/about.html"), name="course-about"),
    path("<int:my_id>/", CourseView.as_view(), name="course-details"),
    path("list/", CourseListView.as_view(), name="course-list"),
    path("create/", CourseCreateView.as_view(), name="course-create"),
    path("<int:my_id>/update/", CourseUpdateView.as_view(), name="course-update"),
    path("<int:my_id>/delete/", CourseDeleteView.as_view(), name="course-delete")

]
