# GitHub合作开发原则

## GitHub Branch

项目的分支结构入下：

![image-20201029085653031](https://gitee.com/yunruowu/PictureForBolg/raw/master/img/image-20201029085653031.png)

除了主分支main，每个人还有一个自己的开发分支，命名为名字的首字母+dev，比如我的就是xyydev。每个人对项目代码的更改都应该在这个分支下面进行，这样可以隔离大家对同一个代码更改带来的冲突。

步骤：

1. 首先本地新建一个文件夹，执行git命令，clone分支：

    主要是标红的地方每个人对应使用自己的分支

    git clone --branch xyydev https://github.com/oneprojecttest/All.git

![image-20201029090106807](https://gitee.com/yunruowu/PictureForBolg/raw/master/img/image-20201029090106807.png)

2. 下面的开发和平时无异， push，pull。

3. 之后可以在github或者git命令进行pull request，就是希望将自己的分支合并到mian分支上。

    ![image-20201029090649852](https://gitee.com/yunruowu/PictureForBolg/raw/master/img/image-20201029090649852.png)	可以在下面写清楚自己提交的是什么东西，功能等

4. 下面就是合并这个pull request

    

    ![image-20201029090936310](https://gitee.com/yunruowu/PictureForBolg/raw/master/img/image-20201029090936310.png)

![image-20201029090949888](https://gitee.com/yunruowu/PictureForBolg/raw/master/img/image-20201029090949888.png)

这个分支这里是没有冲突的，可以直接合并。很多情况下，会出现来你的pull 和主分支是不同的，所以需要处理冲突，这时候是需要人工进行筛选的。

5. 合并成功
 ![image-20201029091155805](https://gitee.com/yunruowu/PictureForBolg/raw/master/img/image-20201029091155805.png)

## 关于合并冲突

可以按照下面这个方法进行，**尽量将冲突控制在自己的分支内。**

当你在本地修改了项目的同时，其他队友或许已在此期间给团队的仓库提交了新的代码。因此在完成了一系列 commit 将要 push 到远程之前，先要同步到与团队一致的版本，避免在 pull request 时产生冲突。

为此我们要做两件事：更新远程仓库的代码到本地仓库（fetch），然后将内容合并到当前分支（merge）。（在合并的时候可能会出现冲突，冲突的解决方式将会在后续说明。）

## 关于commit的规范

尽量按照姓名+功能（你这次提交做了什么事情）

## 相关博客

[GitHub分支创建及合并](https://blog.csdn.net/qq_30607843/article/details/84404000)

下面这个工具不同，但是原理是一样的

[超详细！Github团队协作教程（Gitkraken版）_weixin_30491641的博客-CSDN博客](https://blog.csdn.net/weixin_30491641/article/details/96532012?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.add_param_isCf&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.add_param_isCf)