from tastypie.resources import ModelResource
from api.models import Note, State
from tastypie.authorization import Authorization

class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'
        authorization = Authorization()


class StateResource(ModelResource):
    class Meta:
        queryset = State.objects.all()
        resource_name = 'state'
        authorization = Authorization()