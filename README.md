# MOOC 挂课脚本 (◔◡◔)

## 最新版本
本人最近测试通过日期：
- 学堂在线：**2018-05-24** &emsp;（没课没更新咕咕咕咕）
- 智慧树：&emsp;**2020-03-23** &emsp;（已适配三月界面更新）

## 准备工作  
1. 首先你需要一只&nbsp;[chrome](https://www.google.com/chrome/)&nbsp;浏览器（其他浏览器可以举一反三，请自行搜索）
2. 下载同版本的&nbsp;[chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)&nbsp;并放到本机&nbsp;chrome.exe&nbsp;文件同目录下
3. 添加&nbsp;chrome&nbsp;目录到环境变量&nbsp;[Path](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)

这些文件我已经打包在百度云：[链接](https://pan.baidu.com/s/1EJzmyc4OxuVnakxAfi5tSQ)，密码：6dah<sub>&emsp;最近更新：2020-03-24</sub>

## 使用说明

### 可执行文件

以下自动播放脚本均提供单文件的 `.exe` 可执行文件版本，发布在&nbsp;Release&nbsp;页面，或者也可以从百度云链接里下载。  
由于平台限制（编译环境：Windows 10 x64），不能保证所有系统通用，如果无法运行，请使用 `.py` 文件执行脚本。

### 智慧树自动播放脚本

#### 安装依赖库

```bash
pip install selenium
pip install cryptography
```

#### 运行脚本

1. 首次运行请根据提示输入用户名（手机号）和密码  
   之后会~~不严谨地加密~~存储在 `USER_INFO` 文件中，无需再次输入

   - <strong>注意：</strong>目前由于不明原因无法自动登录，仍然需要每次手动登陆

     &emsp;&emsp;&emsp;欢迎大佬帮忙解决一下这个问题，然后提一个 Pull Request

2. 如果跳出登陆验证 / 密码过于简单的提示，请手动处理

3. 进入主页后，选择你要看的课程，点击进入播放页面

4. 当课程开始播放后（注意先关闭弹窗），即可让脚本完全接管

#### 运行示例

```
GitHub: bugstop

适用于 2020.3 智慧树更新。

请手动登陆，然后按任意键继续...
进入播放界面后按回车键，程序将接管...
Mon Apr  6 01:05:48 2020 :   1 / 88
Mon Apr  6 01:05:58 2020 :   2 / 88
    弹题    已关闭    继续播放
Mon Apr  6 01:09:41 2020 :   3 / 88
    弹题    已关闭    继续播放
Mon Apr  6 01:14:03 2020 :   4 / 88
    弹题    已关闭    继续播放
Mon Apr  6 01:16:36 2020 :   5 / 88
    弹题    已关闭    继续播放
...................................
Mon Apr  6 05:51:47 2020 :  88 / 88
按任意键退出...
```

### 学堂在线自动播放脚本

因为智慧树太良心，一直没选学堂在线，所以没法测试，不知道之前的还能不能用  
万一挂了的话还麻烦参考这两个脚本修一下，也同样欢迎 Pull Request

## 维护者

[@bugstop](https://github.com/bugstop)

## 如何贡献

非常欢迎你：[提一个 Issue](https://github.com/bugstop/mooc-autoplay/issues/new) 或者提交一个 Pull Request

## 使用许可

[GPL-3.0](LICENSE) © bugstop
