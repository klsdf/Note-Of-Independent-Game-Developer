

### 直接调试法




1. 给游戏的exe后面加启动参数`--remote-debugging-port=9222`
2. 在浏览器输入http://localhost:9222
3. chrome会自动根据map来还原js
4. 直接看source，里面的代码默认放到了no domain



# 解包


1. 检查是否存在 app.asar 文件
2. 运行`npx asar extract app.asar app_unpacked`，这会把 `app.asar` 解包到 `app_unpacked` 目录下。
3. 

