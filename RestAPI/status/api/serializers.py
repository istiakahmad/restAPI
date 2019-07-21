from rest_framework import serializers
from status.models import Status


class StatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]

    '''
    def validate_content(self, value):
        if len(value) > 10000:
            raise serializers.ValidationError("This is too long")
        return value
    '''

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image needed")
        return data
'''
class StatusForms(forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]
        
Terminal Command:  ::::::::::::SHELL EXAMPLE::::::::::::::

python manage.py shell (InteractiveConsole)
>>> import json
>>> data = {'abc': 123}
>>> data_list = ['abc']
>>> data_json = json.dumps(data)
>>> data_json
'{"abc": 123}'
>>> load_json = json.loads(data_json)
>>> load_json['abc']
123
>>> load_json['abc'] * 2
246


>>> from status.models import Status
>>> from status.api.serializers import StatusSerializers
>>> obj = Status.objects.all()
>>> obj
<StatusQuerySet [<Status: aaa>, <Status: jjgjg>]>
>>> obj = Status.objects.first()
>>> obj
<Status: aaa>
>>> data = StatusSerializers(obj)
>>> data
StatusSerializers(<Status: aaa>):
    user = PrimaryKeyRelatedField(queryset=User.objects.all())
    content = CharField(allow_blank=True, allow_null=True, required=False, style={'base_
template': 'textarea.html'})
    image = ImageField(allow_null=True, max_length=100, required=False)
>>> data.data
{'user': 1, 'content': 'aaa', 'image': None}


>>> from rest_framework.renderers import JSONRenderer
>>> new_json_data = JSONRenderer().render(data.data)
>>> print(new_json_data)
b'{"user":1,"content":"aaa","image":null}'


>>> from django.utils.six import BytesIO
>>> from rest_framework.parsers import JSONParser
>>> json = new_json_data
>>> stream = BytesIO(json)
>>> data = JSONParser().parse(stream)
>>> data
{'user': 1, 'content': 'aaa', 'image': None}


>>> qs = Status.objects.all()
>>> serializer = StatusSerializers(qs, many=True)
>>> serializer.data
[OrderedDict([('user', 1), ('content', 'aaa'), ('image', None)]), OrderedDict([('user',
1), ('content', 'jjgjg'), ('image', None)])]

>>> json_data = JSONRenderer().render(serializer.data)
>>> json_data
b'[{"user":1,"content":"aaa","image":null},{"user":1,"content":"jjgjg","image":null}]'
>>>


>>> json.loads(json_data)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'bytes' object has no attribute 'loads'
>>> import json
>>> json.loads(json_data)
[{'user': 1, 'content': 'aaa', 'image': None}, {'user': 1, 'content': 'jjgjg', 'image':
None}]


>>> stream = BytesIO(json_data)
>>> data = JSONParser().parse(stream)
>>> data
[{'user': 1, 'content': 'aaa', 'image': None}, {'user': 1, 'content': 'jjgjg', 'image':
None}]

'''