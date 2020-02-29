## 查看运行APP当前页面的Activity名称

    adb shell "dumpsys window | grep mCurrentFocus"

>com.wisedu.cpdaily/com.wisorg.wisedu.home.ui.HomeActivity
>com.wisedu.cpdaily/com.wisorg.wisedu.common.BrowsePageActivity
>com.tencent.mobileqq/com.tencent.mobileqq.activity.SplashActivity

## ADB命令启动应用程序
    adb shell am start -n 包名/类名
    如：adb shell am start -n com.wisedu.cpdaily/com.wisorg.wisedu.home.ui.HomeActivity

## ADB命令滑动屏幕

    adb shell input swipe <x1> <y1> <x2> <y2> [duration(ms)]
