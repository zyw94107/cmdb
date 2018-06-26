import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

#
# class ReportView(View):
#     def post(self, request):
#         asset_data = request.POST.get('asset_data')
#         print(asset_data)
#         return HttpResponse("成功收到数据！")
#
from assets import asset_handler
from . import models


def report(request):
    if request.method == 'POST':
        asset_data = request.POST.get('asset_data')
        data = json.loads(asset_data)

        if not data:
            return HttpResponse("没有数据!")
        if not issubclass(dict, type(data)):
            return HttpResponse("数据必须为字典格式！")
        # 是否携带关键的sn号
        sn = data.get('sn', None)
        if sn:
            # 进入审批流程
            # 首先判断已经在线上的资产是否存在该sn
            asset_obj = models.Asset.objects.filter(sn=sn)
            if asset_obj:
                pass
                return HttpResponse("该资产已更新")
            else:
                # 调用其他操作方法写入数据
                obj = asset_handler.NewAsset(request, data)
                response = obj.add_to_new_assets_zone()
                return HttpResponse(response)
        else:
            return HttpResponse("没有sn号 ，请检查数据")
