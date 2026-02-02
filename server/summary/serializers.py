from rest_framework.serializers import ModelSerializer
from summary.models import Summary


class SummarySerializers(ModelSerializer):
    class Meta:
        model = Summary  # 指定需要校验的模型
        fields = '__all__'  # 校验所有字段

    def validate(self, attrs):
        return attrs
