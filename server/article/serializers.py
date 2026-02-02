from rest_framework.serializers import ModelSerializer
from article.models import Article


class ArticleSerializers(ModelSerializer):
    class Meta:
        model = Article  # 指定需要校验的模型
        fields = '__all__'  # 校验所有字段

    def validate(self, attrs):
        return attrs
