---
title: Hexo相关
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
>参考：https://mindawei.github.io/2018/05/01/%E5%A4%9A%E6%9C%BA%E4%BD%BF%E7%94%A8Hexo%E5%8D%9A%E5%AE%A2/

More info: [Deployment](https://hexo.io/docs/one-command-deployment.html)
