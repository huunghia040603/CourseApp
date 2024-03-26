from  rest_framework import serializers
from courses.models import  Category,Course,Lesson,Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
         model = Category
         fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        req = super().to_representation(instance)
        req['image'] = instance.image.url
        return req





class CourseSerializer(ItemSerializer):

    class Meta:
        model = Course
        fields = ['id','name','image','created_date']

class LessonSerializer(ItemSerializer):
    class Meta:
        model = Lesson
        fields =['id','subject','image','created_date']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields= ['id','name']


class LessonDetailsSerializer(LessonSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Lesson
        fields = LessonSerializer.Meta.fields + ['content','tags']


