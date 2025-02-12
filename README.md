# 哈工大(深圳)校园网络登陆助手
-- 用于无图形化界面的Linux服务器

## 安装步骤

1.下载代码
>`git clone git@github.com:siliconx/hitsz_net.git`

2.安装selenium
>`pip3 install selenium`

3.下载并安装chrome浏览器(https://www.google.com/chrome/)
>`sudo dpkg -i google-chrome-xxx.deb`

4.下载并解压chrome驱动(https://npm.taobao.org/)
>`unzip chromedriver_linux64.zip`
>
>注意浏览器和驱动的版本应一致

5.把chrome驱动移动到任一环境变量中的目录，如`/usr/local/bin`
>`sudo mv chromedriver /usr/local/bin`

6.给hitsz_net.py加可执行权限
>`chmod +x hitsz_net.py`

7.把hitsz_net.py移动到任一环境变量中的目录，如`/usr/local/bin`
>`sudo mv hitsz_net.py /usr/local/bin`

8.通过以上步骤，就可以通过在命令行输入 `hitsz_net.py` 来登陆校园网络了。
>当然, 可以给Python脚本起一个更容易记忆的名字，如`hitsz_net`

9.release log
* 20250212: 由于本人已经毕业多年，项目已经很久没更新，校园网认证系统升级后存在不兼容的问题，感谢@seer8616提交的MR

!注：不同的操作系统及浏览器可能有所不同，我的环境是Ubuntu16.04 + Google Chrome 77.0.3865.90, (64-bit)
