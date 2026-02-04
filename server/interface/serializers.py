from rest_framework.serializers import ModelSerializer

from custom import Constant
from interface.models import MusicKuGou, RequestInfo, MusicPlayer
import time
from rest_framework import serializers


class MusicKuGouSerializers(ModelSerializer):
    class Meta:
        model = MusicKuGou  # 指定需要校验的模型
        fields = '__all__'  # 校验所有字段

    def validate(self, attrs):
        attrs['dateCreatedStr'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        # 对格式化后的歌曲名和歌手名进行格式化
        attrs['format_sing_title'] = attrs['sing_title'].lower().replace(' ', '').strip()
        attrs['format_singer'] = attrs['singer'].lower().replace(' ', '').strip()

        # raise serializers.ValidationError('非法上传')
        return attrs


class RequestInfoSerializers(ModelSerializer):
    class Meta:
        model = RequestInfo  # 指定需要校验的模型
        fields = '__all__'  # 校验所有字段

    def validate(self, attrs):
        attrs['dateCreatedStr'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        return attrs


class MusicPlayerSerializers(ModelSerializer):
    class Meta:
        model = MusicPlayer  # 指定需要校验的模型
        fields = '__all__'  # 校验所有字段

    def validate(self, attrs):
        return attrs

    # 前端音乐播放接口根据业务逻辑需要区分服务器进行拼接地址
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if representation.get('url'):
            representation['url'] = 'http://' + Constant.host + '/' + representation['url']
        return representation
