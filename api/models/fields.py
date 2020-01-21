from django.utils.translation import ugettext as _
from django.db.models import SmallIntegerField
from multiselectfield import MultiSelectField

DAY_OF_THE_WEEK = {
	'1' : _(u'Monday'),
	'2' : _(u'Tuesday'),
	'3' : _(u'Wednesday'),
	'4' : _(u'Thursday'),
	'5' : _(u'Friday'),
	'6' : _(u'Saturday'), 
	'7' : _(u'Sunday'),
}

class DayOfTheWeekField(MultiSelectField):
	def __init__(self, *args, **kwargs):
		kwargs['choices']=tuple(sorted(DAY_OF_THE_WEEK.items()))
		super(DayOfTheWeekField,self).__init__(*args, **kwargs)
