# python-8x8x-api

一个 8x8x (没错就是那个) 的 python API !

片库: https://github.com/8xx8x/8x8x



# 支持

* 获取页面上的所有视频信息(封面, 标题, 视频ID);

* 获取单个视频的信息(视频下载链接, 封面, 标题);

* 搜索(网站的问题导致搜索可能无法使用).


# 介绍

1. `analysis_page`: 获取指定页面的所有视频信息

返回结果如下:

```json
[
    {
        "name": "美xxxxx刚xx完就xx要xxxxxxxxx-xxxx",	//视频标题
        "pic": "https://h2bccytq4w.ng8wu.com/p2/46xxxxxxxxf15f8b9826fd7908d44098.webp",	//视频封面
        "vid": "88366"	//视频ID
    },
    {
        "name": "热门推荐-十年来未见面xxxxx越来越xx-家庭xx",
        "pic": "https://h2bccytq4w.ng8wu.com/p2/f6xxxxxxxxe0bb62666bb801fe58cd0e.webp",
        "vid": "88239"
    }
]
```

需要传入`page`参数.(`page`是页码数)

---

2. `analysis_video`: 获取指定视频的信息

返回结果如下:

```json
{
    "name": "国产xx：xxxxxxxxxx-年xxx",	//视频标题
    "background": "https://h2bccytq4w.ng8wu.com/p2/23cxxxxxxxxx87539a15cb2befd.webp",	//视频封面
    "download": "https://8xj8j.xyz/assets/23c7xxxxxxxxxxx39a15cb2befd.mp4"	//视频下载链接
}
```

需要传入`vid`参数.(`vid`是视频ID)

---

3. `search`: 搜索

返回结果未知.(网站的这个搜索功能老是失效)

需要传入`word`, `page`两个参数.(`word`是搜索关键词)

## 情况

* 如果失效的话请去片库仓库自行获取链接替换程序中的`domain`参数.