from django.urls import path

from pharmacy.views import index, MedicineCreateView, MedicineListView, ManufacturerListView, MedicineDetailView, \
    DepartmentListView, DepartmentDetailView, ManufacturerCreateView, ManufacturerUpdateView, ManufacturerDeleteView, \
    MedicineUpdateView, MedicineDeleteView


urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/",
         ManufacturerListView.as_view(),
         name="manufacturer-list"),
    path(
        "manufacturers/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer-create"
    ),
    path(
        "manufacturers/<int:pk>/update/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update"
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        ManufacturerDeleteView.as_view(),
        name="manufacturer-delete"
    ),
    path(
        "medicine/",
        MedicineListView.as_view(),
        name="medicine-list"
    ),
    path(
        "medicine/<int:pk>/",
        MedicineDetailView.as_view(),
        name="medicine-detail"
    ),
    path(
        "medicine/create/",
        MedicineCreateView.as_view(),
        name="medicine-create"
    ),
    path(
        "medicine/<int:pk>/update/",
        MedicineUpdateView.as_view(),
        name="medicine-update"
    ),
    path(
        "medicine/<int:pk>/delete/",
        MedicineDeleteView.as_view(),
        name="medicine-delete"
    ),
    path("accounts/", DepartmentListView.as_view(), name="department-list"),
    path(
        "accounts/<int:pk>/",
        DepartmentDetailView.as_view(),
        name="department-detail"
    ),
]

app_name = "pharmacy"
