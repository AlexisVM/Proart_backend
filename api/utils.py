import os.path
import hashlib
from django.conf import settings
"""
Utils code are all helpers functions

"""
def hashImage(instance,filename):
	base = settings.COMPROBANTES_DIR
	parts = os.path.splitext(filename)
	ctx = hashlib.sha256()
	if instance.archivo.multiple_chunks():
		for data in instance.archivo.chunks(HASH_CHUNK_SIZE):
			ctx.update(data)
	else:
		ctx.update(instance.archivo.read())

	return os.path.join(base, ctx.hexdigest() + parts[1])