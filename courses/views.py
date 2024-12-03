from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from courses.models import Course
from courses.forms import CourseModelForm
from django.urls import reverse


# BASE VIEW CLass = VIEW
class CourseView(View):
    template_name = "courses/detail.html"

    def get(self, request, my_id=None, *args, **kwargs):
        # GET method
        context = {}
        if my_id is not None:
            obj = get_object_or_404(Course, id=my_id)
            context["object"] = obj
        return render(request, self.template_name, context)


class CourseListView(View):
    template_name = "courses/list.html"
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {
            "object_list": self.get_queryset()
        }
        return render(request, self.template_name, context)


class CourseCreateView(View):
    template_name = "courses/create.html"

    def get(self, request, my_id=None, *args, **kwargs):
        form = CourseModelForm()
        context = {
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CourseModelForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            form = CourseModelForm()

        context = {
            "form": form
        }
        return render(request, self.template_name, context)


class CourseUpdateView(View):
    template_name = "courses/update.html"

    def get_object(self):
        id_ = self.kwargs.get("my_id")
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id_)
        return obj

    def get(self, request, my_id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context["object"] = obj
            context["form"] = form
        return render(request, self.template_name, context)

    def post(self, request, my_id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context["form"] = form
            context["object"] = obj
        return render(request, self.template_name, context)


class CourseDeleteView(View):
    template_name = "courses/delete.html"

    def get_object(self):
        id_ = self.kwargs.get("my_id")
        return get_object_or_404(Course, id=id_)

    def get(self, request, my_id=None, *args, **kwargs):
        obj = self.get_object()
        context = {}
        if obj is not None:
            context["object"] = obj
        return render(request, self.template_name, context)

    def post(self, request, my_id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context["object"] = None
            return redirect("/courses/list/")
        return render(request, self.template_name, context)


class CourseObjectMixin(object):
    model = Course
    lookup = "my_id"

    def get_object(self):
        id_ = self.kwargs.get(self.lookup)
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id_)
        return obj


class CourseDeleteViewMixin(CourseObjectMixin, View):
    template_name = "courses/delete.html"

    def get(self, request, my_id=None, *args, **kwargs):
        obj = self.get_object()
        context = {}
        if obj is not None:
            context["object"] = obj
        return render(request, self.template_name, context)

    def post(self, request, my_id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context["object"] = None
            return redirect("/courses/list/")
        return render(request, self.template_name, context)
