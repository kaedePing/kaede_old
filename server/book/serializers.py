from rest_framework.serializers import ModelSerializer
from book.models import Book


class BookSerializers(ModelSerializer):
    class Meta:
        model = Book  # 指定需要校验的模型
        fields = '__all__'  # 校验所有字段

    def validate(self, attrs):
        return attrs
