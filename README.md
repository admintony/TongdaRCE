# TongdaRCE
通达OA&lt;v11.5&amp;v11.6版本RCE Exploit

直接根据V11.6版本的Exp进行改造，加入以下内容：

* 自动判断版本，根据``/module/appbuilder/assets/print.php``是否存在，该文件仅存在于V11.6

* v11.5以下版本直接获取Session，然后再进行上传利用。

* 改造用法：python tongda_rce.py target_url
