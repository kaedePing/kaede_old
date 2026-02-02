from rest_framework.serializers import ModelSerializer
from api.models import Api
import time


class ApiSerializers(ModelSerializer):
    class Meta:
        model = Api  # 指定需要校验的模型
        fields = '__all__'  # 校验所有字段

    def validate(self, attrs):
        attrs['dateCreatedStr'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        return attrs
