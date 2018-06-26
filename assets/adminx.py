import xadmin
from .models import NewAssetApprovalZone, Asset


class NewAssetAdmin(object):
    # 展示
    list_display = ['asset_type', 'sn', 'model', 'manufacturer', 'c_time', 'm_time']
    # 筛选
    list_filter = ['asset_type', 'manufacturer', 'c_time']
    # 搜索
    search_field = ['sn']


class AssetAdmin(object):
    list_display = ['asset_type', 'name', 'status', 'approved_by', 'c_time', "m_time"]


xadmin.site.register(NewAssetApprovalZone, NewAssetAdmin)
xadmin.site.register(Asset, AssetAdmin)