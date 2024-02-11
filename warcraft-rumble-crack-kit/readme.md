先处理zhCN文件夹

1. wem转换为wav
for %i in (*) do "F:\魔兽大作战\隔离测试\vgmstream-win\vgmstream-cli.exe" "%i"
2. 解包bnk文件
打开wwiser.pyz
Load dirs...选择bnk所在目录
Generate TXTP
3. 匹配txtp和音频序号
用zhCN下的bnk匹配zhCN下的wav，大部分匹配。包含sfx和vo。368个文件无法匹配。而且未完全被汉化。有中文vo的对应英语vo。
用直属Android下的bnk匹配zhCN下的wav，无法匹配。

用zhCN下的bnk匹配直属Android下的wav，少部分匹配且全是刀剑脚步等sfx
用直属Android下的bnk匹配直属Android下的wav，大部分匹配，有sfx和BGM

txtp文件名不带{r}的里面的wem一般是vo
