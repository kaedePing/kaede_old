from rest_framework.serializers import ModelSerializer
from article.models import Article
from custom import Constant


class ArticleSerializers(ModelSerializer):
    class Meta:
        model = Article  # 指定需要校验的模型
        fields = '__all__'  # 校验所有字段

    def validate(self, attrs):
        return attrs

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # 对 cover_url 进行处理,业务逻辑需要区分服务器进行拼接地址
        if representation.get('cover_url'):
            representation['cover_url'] = 'http://' + Constant.host + '/' + representation['cover_url']
        return representation
