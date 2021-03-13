from django.test import TestCase

# Create your tests here.

# import json
# from django.core import serializers

# def getObject(request, id):
#     obj = MyModel.objects.get(pk=id)
#     data = serializers.serialize('json', [obj,])
#     struct = json.loads(data)
#     data = json.dumps(struct[0])
#     return HttpResponse(data, mimetype='application/json')


## for database dwnloading
# from django.conf import settings
# from django.core.files import File
# db_path = settings.DATABASES['default']['NAME']
# dbfile = File(open(db_path, "rb"))
# response = HttpResponse(dbfile, mimetype='application/x-sqlite3')
# response['Content-Disposition'] = 'attachment; filename=%s' % db_path
# response['Content-Length'] = dbfile.size

# return response



## for selecting specific fields inserializer
#context['data'] = serializers.serialize('python', list(self.model.objects.all()),exclude=('no_of_events','solo_Performances'))

# 'some_other_field2': forms.DateInput(attrs={'readonly': True}),
