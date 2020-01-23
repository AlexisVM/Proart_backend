from django.contrib.admin.widgets import AdminFileWidget

class AdminImagePdfWidget(AdminFileWidget):
    template_name = 'admin/widgets/image_field_preview.html'