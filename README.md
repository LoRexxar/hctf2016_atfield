# wp

出题的思路主要是302绕过域名判断1，然后扫目录得到README.md,拿到提示之后，扫nosql的端口和docker默认的内网ip，找到入口，由于是python的站，所以python urllib头注入通过redis向crontab写文件，getshell


具体有很多细节，所以稍后会重新整理wp

请关注[http://lorexxar.cn](http://lorexxar.cn)