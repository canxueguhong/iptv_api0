# 配置文件，包含直播源URL、黑名单URL、公告信息、EPG URL、测速超时时间和线程池最大工作线程数

# 优先使用的IP版本，这里设置为ipv4
ip_version_priority = "ipv4"

# 直播源URL列表
source_urls = [
    "https://raw.giteeusercontent.com/miaowancun/tv/raw/master/mw.txt?metadata=eyJyIjoibWFzdGVyIiwiZnAiOiJtdy50eHQiLCJ1aWQiOjE2Mzc1Mjc0LCJwaWQiOjQ2MDY4MTE4LCJzdG8iOiJnaXQtc2hhcmRpbmctc3RvLTEwdC0wMTgiLCJycCI6InJlcG9zL2E4LzRmL2E4NGY3MmU1YWUxOTdiOGVhODM4YTEwNzA4YjU5YjJkYjM1NTdkOWNjZGUyM2RjYmJjMjRlYmMwYjZmMGNjMmQuZ2l0IiwiaXNwIjp0cnVlLCJleHBpcmVfYXQiOjE3ODE0OTU0MDB9&signature=RBX5d-CytYw7kxQKsGVq04dGx0sl08Pm9-JdJTNgVEY",
    "https://gitee.com/szwxk/watch-television/raw/master/wxk.m3u",
    "https://raw.githubusercontent.com/zhaiyaa/iptv-api/refs/heads/master/output/ipv4/result.m3u",
    "https://gongdian.top/tv/iptv",
    "http://gh-proxy.org/raw.githubusercontent.com/Supprise0901/TVBox_live/main/live.txt",
    "https://raw.githubusercontent.com/Supprise0901/TVBox_live/refs/heads/main/live.txt",
    "https://gitee.com/king12985/tv/raw/master/lives/20180818.txt",
    "https://gitee.com/king12985/tv/raw/master/lives/zhizhu/20180818china.txt",
    "https://iptv-org.github.io/iptv/index.m3u", 
    "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/tw.m3u", 
    "https://epg.pw/test_channels_taiwan.m3u", 
    "https://freetv.fun/test_channels_taiwan_new.m3u",
    "https://raw.githubusercontent.com/YueChan/Live/refs/heads/main/Adult.m3u", 
    "https://raw.githubusercontent.com/YueChan/Live/refs/heads/main/GNTV.m3u", 
    "https://raw.githubusercontent.com/YueChan/Live/refs/heads/main/Global.m3u", 
    "https://raw.githubusercontent.com/hujingguang/ChinaIPTV/main/cnTV_AutoUpdate.m3u8 ",
    "https://gh-proxy.com/raw.githubusercontent.com/vbskycn/iptv/refs/heads/master/tv/iptv4.txt", 
    "https://raw.githubusercontent.com/iptv-org/iptv/gh-pages/countries/cn.m3u",
    "https://raw.githubusercontent.com/AdeelWajid/iptv_validated_list/refs/heads/main/validated_streams.json",
    "https://raw.githubusercontent.com/IPTVSolutions/IPTV_Online/refs/heads/main/playlists/playlist_all.m3u8",
    "https://raw.githubusercontent.com/zbefine/iptv/main/iptv.m3u",
    "https://raw.githubusercontent.com/develop202/migu_video/refs/heads/main/interface.txt",
    "https://gh-proxy.org/github.com/ioptu/IPTV.txt2m3u.player/raw/refs/heads/main/migu.m3u",
    "https://raw.githubusercontent.com/Jsnzkpg/Jsnzkpg/refs/heads/Jsnzkpg/Jsnzkpg1",
    "http://rihou.cc:555/gggg.nzk",
    "https://raw.githubusercontent.com/TianmuTNT/iptv/main/iptv.m3u",
    "https://gh-proxy.com/raw.githubusercontent.com/suxuang/myIPTV/main/ipv4.m3u",
    "https://raw.githubusercontent.com/kakaxi-1/IPTV/main/ipv4.txt", 
    "http://iptv.4666888.xyz/FYTV.txt",
    "https://live.hacks.tools/tv/iptv4.txt",
    "https://raw.githubusercontent.com/zilong7728/Collect-IPTV/refs/heads/main/best_sorted.m3u",
    "https://www.kaniptv.cc.cd/abc123",
    "https://raw.githubusercontent.com/Lei9008/iptv_api_1/main/self_use/IPTV2_speed_test/output/live_ipv4_source_sorted.m3u",
    "https://raw.githubusercontent.com/fuxinyi0505/Ku9-IPTV-source/refs/heads/main/Ku9-IPTV-source.txt",
    "https://raw.githubusercontent.com/mymsnn/DailyIPTV/main/outputs/full_validated.m3u",
    "https://raw.githubusercontent.com/n3rddd/CTVLive/refs/heads/main/live.txt",
    "https://raw.githubusercontent.com/qwerttvv/Beijing-IPTV/master/IPTV-Unicom.m3u",
    "https://raw.githubusercontent.com/xiongjian83/TvBox/refs/heads/main/live.txt",
    "https://raw.githubusercontent.com/yoursmile66/TVBox/refs/heads/main/live.txt",
    "https://raw.githubusercontent.com/zxmlxw520/5566/refs/heads/main/cjdszb.txt",
    "https://raw.githubusercontent.com/zxmlxw520/5566/refs/heads/main/gqds+.txt",
    "https://raw.githubusercontent.com/zzmaze/iptv/main/itvlist.txt",
    "https://raw.githubusercontent.com/BP3388/BP001.github.io/main/tivi.list",
    "https://raw.githubusercontent.com/Supprise0901/TVBox_live/main/live.txt",
    "https://raw.githubusercontent.com/gaotianliuyun/gao/master/list.txt",
    "https://raw.githubusercontent.com/zwc456baby/iptv_alive/master/live.txt",
    "https://raw.githubusercontent.com/junge3333/juds6/main/yszb1.txt",
    "https://raw.githubusercontent.com/maitel2020/iptv-self-use/main/iptv.txt",
    "https://raw.githubusercontent.com/alienlu/iptv/refs/heads/master/iptv.txt",
    "https://raw.githubusercontent.com/zwc456baby/iptv_alive/refs/heads/master/live.m3u",
    "https://raw.githubusercontent.com/cyalias/mytvs-github/refs/heads/main/mytv.txt",
    "https://jihulab.com/-/snippets/5265/raw/main/.txt",
    "https://3043.kstore.space/bhvip/bhzb.txt",
    "https://raw.githubusercontent.com/plsy1/iptv/main/unicast/unicast-ku9.m3u",
    "https://raw.githubusercontent.com/plsy1/iqilu/main/iqilu-generic.m3u",
    "https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-jining.m3u",
    "https://raw.githubusercontent.com/cyh92/iptv-api-cctv/refs/heads/master/output/cctv.m3u",
    "https://raw.githubusercontent.com/skddyj/iptv/refs/heads/main/IPTV.m3u",
    "https://raw.githubusercontent.com/best-fan/iptv-sources/refs/heads/main/cn_all_status.m3u8",
    "https://raw.githubusercontent.com/0610840119/iptv-api/refs/heads/master/output/xp_result.m3u",
    "https://raw.githubusercontent.com/cyh92/iptv-api-cctv/refs/heads/master/output/cctv.m3u",
    "https://gitee.com/alexkw/app/raw/master/kgk.txt",
    "https://raw.githubusercontent.com/alantang1977/jtv/refs/heads/main/%E7%BD%91%E7%BB%9C%E6%94%B6%E9%9B%86.txt",
    "https://live.hacks.tools/tv/ipv4/categories/卫视频道.m3u",
    "https://tv.850930.xyz/kdsb.txt",
    "https://tv.850930.xyz/pix.m3u",
    "https://raw.githubusercontent.com/BurningC4/Chinese-IPTV/master/TV-IPV4.m3u",
    "https://raw.githubusercontent.com/iptvjs/iptv/main/txt/o_s_cn_cctv.txt",





    
    
    "https://raw.githubusercontent.com/Jsnzkpg/Jsnzkpg/Jsnzkpg/Jsnzkpg1",
    "https://raw.githubusercontent.com/fafa002/yf2025/refs/heads/main/yiyifafa.txt",
    "https://raw.githubusercontent.com/zxmlxw520/5566/refs/heads/main/cjdszb.txt",
    "https://raw.githubusercontent.com/suxuang/myIPTV/main/ipv4.m3u",
    "https://tv.anbox.ip-ddns.com/live",
    "https://raw.githubusercontent.com/mymsnn/DailyIPTV/main/outputs/full_validated.m3u",
    "/https://raw.githubusercontent.com/JE668/m3u-checker-max/main/output/live.txt",
    "https://d.kstore.dev/download/15114/gztv.txt",    
    "https://raw.githubusercontent.com/807080747/zv/refs/heads/main/sese.txt",
    "https://raw.githubusercontent.com/fleung49/star/refs/heads/main/mit",
    "http://ge.html-5.me//ii/黄蚂蚁先锋推流源.txt",
    "https://www.985pan.com/down.php/bf5e9607ff407fcdd71f63928ea5bc79.txt",
    "http://iptv.ruyitv.cc/m3u/tv.txt",
    "",
    "https://cloud.7so.top/f/xv80ux/天浪.txt",
    "https://cloud.7so.top/f/yr7BHL/HKTV.txt",
    "https://gitee.com/main-stream/tv/raw/master/BOSS.json",
    "https://raw.githubusercontent.com/alantang1977/iptv-auto/refs/heads/main/my.txt",
    "https://fastgit.cc/https://raw.githubusercontent.com/iTCoffe/Collect-iTV/main/Internet_iTV.m3u",
    "https://gitee.com/alexkw/app/raw/master/kgk.txt",
    "https://d.kstore.dev/download/15114/HKTV.txt",
    "",
    "",
    "",
    "",
    "",
    "https://raw.githubusercontent.com/iodata999/frxz751113-IPTVzb1/refs/heads/main/结果.m3u",
    "https://raw.githubusercontent.com/alantang1977/jtv/refs/heads/main/网络收集.txt",
    "",
    "https://raw.githubusercontent.com/zxmlxw520/5566/refs/heads/main/cjdszb.txt",
    "https://raw.githubusercontent.com/zxmlxw520/5566/refs/heads/main/gqds+.txt",
    "https://raw.githubusercontent.com/develop202/migu_video/main/interface.txt",
    "https://www.iyouhun.com/tv/myIPTV/ipv6.m3u",
    "https://www.iyouhun.com/tv/myIPTV/ipv4.m3u",
    "",   
    "https://live.izbds.com/tv/iptv4.txt",
    "https://l.gmbbk.com/upload/39183918.txt",
    "http://rihou.cc:555/gggg.nzk",
    "http://1.94.31.214/live/livelite.txt",
    "https://cdn.jsdelivr.net/gh/Guovin/iptv-api@gd/output/result.m3u",
    "",
    "",
    "",
    "",
    "https://iptv.catvod.com/tv.m3u",
    "https://live.zbds.top/tv/iptv4.txt",
    "",


]

# 直播源黑名单URL列表，去除了重复项
url_blacklist = [
    "epg.pw/stream/",
    "103.40.13.71:12390",
    "[2409:8087:1a01:df::4077]/PLTV/",
    "http://[2409:8087:1a01:df::7005]:80/ottrrs.hl.chinamobile.com/PLTV/88888888/224/3221226419/index.m3u8",
    "http://[2409:8087:5e00:24::1e]:6060/000000001000/1000000006000233001/1.m3u8",
    "8.210.140.75:68",
    "154.12.50.54",
    "yinhe.live_hls.zte.com",
    "8.137.59.151",
    "[2409:8087:7000:20:1000::22]:6060",
    "histar.zapi.us.kg",
    "www.tfiplaytv.vip",
    "dp.sxtv.top",
    "111.230.30.193",
    "148.135.93.213:81",
    "live.goodiptv.club",
    "iptv.luas.edu.cn",
    "[2409:8087:2001:20:2800:0:df6e:eb22]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb23]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb1d]/ott.mobaibox.com/",
    "[2409:8087:2001:20:2800:0:df6e:eb1d]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb24]",
    "2409:8087:2001:20:2800:0:df6e:eb25]:80",
    "stream1.freetv.fun",
    "chinamobile",
    "gaoma",
    "[2409:8087:2001:20:2800:0:df6e:eb27]"
]

# 公告信息
announcements = [
    {
        "channel": "更新日期",
        "entries": [
            {
                "name": None,
                "url": "https://cnb.cool/junchao.tang/jtv/-/git/raw/main/Pictures/Robot.mp4",
                "logo": "https://cnb.cool/junchao.tang/jtv/-/git/raw/main/Pictures/Chao.png"
            }
        ]
    }
]

# EPG（电子节目指南）URL列表
epg_urls = [
    "https://epg.v1.mk/fy.xml",
    "http://epg.51zmt.top:8000/e.xml",
    "https://epg.pw/xmltv/epg_CN.xml",
    "https://epg.pw/xmltv/epg_HK.xml",
    "https://epg.pw/xmltv/epg_TW.xml"
]
# 测速超时时间（秒）
TEST_TIMEOUT = 7

# 测速线程池最大工作线程数
MAX_WORKERS = 20
