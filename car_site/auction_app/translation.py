from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(UserProfile)
class UserProfileTranslationOptions(TranslationOptions):
    fields = ('first_name','last_name', )

@register(Brand)
class BrandTranslationOptions(TranslationOptions):
    fields = ('brand_name',)


@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ( 'description', 'car_model')


@register(Feedback)
class FeedbackTranslationOptions(TranslationOptions):
    fields = ('comment',)

