from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator,get_available_image_extensions


def validate_comprobante(value):
	ext = get_available_image_extensions()
	print(ext)
	ext.append("pdf")
	return FileExtensionValidator(allowed_extensions=ext)(value)