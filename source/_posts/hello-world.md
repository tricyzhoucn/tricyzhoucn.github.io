---
title: Hexo相关
categories: 工具
---

![测试图片](./hello-world/2022020901.jpeg)

> Welcome to [Hexo](https://hexo.io/)! This is your very first post. Check [documentation](https://hexo.io/docs/) for more info. If you get any problems when using Hexo, you can find the answer in [troubleshooting](https://hexo.io/docs/troubleshooting.html) or you can ask me on [GitHub](https://github.com/hexojs/hexo/issues).

<!-- more -->

## Quick Start

### Create a new post

``` bash
$ hexo new "My New Post"
```

More info: [Writing](https://hexo.io/docs/writing.html)

### CLEAN

```bash
$ hexo clean
```



### Run server

``` bash
$ hexo server / hexo s
```

More info: [Server](https://hexo.io/docs/server.html)

### Generate static files

``` bash
$ hexo generate / hexo g
```

More info: [Generating](https://hexo.io/docs/generating.html)

### Deploy to remote sites

``` bash
$ hexo deploy / hexo d
```

More info: [Deployment](https://hexo.io/docs/one-command-deployment.html)

官网：https://hexo.io/zh-cn/

### 彻底解决Hexo图片不显示问题

**保证图片在和md同名文件夹，文件x.md，图片./x/y.png**

1. 首先安装hexo-renderer-marked

   ```javascript
   npm install hexo-renderer-marked --save
   ```

2. 修改配置_config.yml

   ```
   post_asset_folder: true
   marked:
     prependRoot: true
     postAsset: true
   ```

3. md里图片引用

   ```
   ![y.png] 注意和md引用写法区别，此时typora打开，图片不显示
   ![./x/y.png] 只有配置成这个样子，md编辑器才能正常渲染，如下：
   ```

4. md中也想显示怎么办？（亲测有效）

   *核心原理就是在md渲染html前把路径替换掉*

   ```javascript
   // scripts/asset-path-fix.js注意和source同级目录
   'use strict';
   
   function getPosition(str, m, i) {
     return str.split(m, i).join(m).length;
   }
   
   hexo.extend.filter.register('before_post_render', function(data) {
     var config = hexo.config;
     if (!config.post_asset_folder) return;
   
     // 提取 slug
     var link = data.permalink;
     var beginPos = getPosition(link, '/', 3) + 1;
     var endPos = link.lastIndexOf('/') + 1;
     link = link.substring(beginPos, endPos);
     var slug = link.split('/').filter(function(elem) { return elem !== ''; }).pop();
   
     // 替换 Markdown 中的 ./slug/xxx 为 xxx
     // 例如: ./hello-world/2022020901.jpeg -> 2022020901.jpeg
     var pattern = new RegExp('!\\[([^\\]]*)\\]\\(\\./' + slug + '/([^)]+)\\)', 'g');
   
     data.content = data.content.replace(pattern, '![$1]($2)');
   
     return data;
   });
   ```

### 补充

>Q: github 403
>A: hexo用户和git默认用户不一致，增加新用户并在～/.ssh/config配置，另外在_config.yml中https改为ssh
>
>Q: next主题设置失败
>A: 原因是hexo在5.0之后把swig给删除了需要自己手动安装 npm i hexo-renderer-swig
>
>参考：https://zhuanlan.zhihu.com/p/26625249
>
>Q:hexo多机部署主题丢失
>
>参考：[使用 master 和 hexo 两个分支](https://mindawei.github.io/2018/05/01/%E5%A4%9A%E6%9C%BA%E4%BD%BF%E7%94%A8Hexo%E5%8D%9A%E5%AE%A2/)
