


# built in 转URP
1. 下载universal RP
2. 创建URP assert
3. 在project settings中，设置assert
4. 选择Window =>Rendering(渲染) =>Render Pipeline Convert(渲染管线转换)
5. 打开渲染管线转换面板之后选择 Built-in to URP
6. 然后把面板中所有选项都勾选了
7. 初始化并convert



# Opaque Texture和毛玻璃生成

**"Opaque Texture"** 选项在 URP Asset 中用于启用对不透明物体的纹理提取。启用这个选项后，URP 会在渲染过程中为场景中的不透明物体生成一个纹理，这个纹理可以用于后处理效果或者 Shader 中的其他操作。

因此在urp中，将物体设置为opaque也可以看到后面的物体，但是后面透明物体无法被渲染上，因为 `Opaque Texture` 仅用于存储不透明物体的纹理信息。

用这种效果很容易制作毛玻璃。
只需要把物体本身设置为透明，物体后面的物体就会正常渲染，然后利用screen position和scene color，就可以再复制一份物体背后的投影。然后做若干组不同方向的uv偏移，就可以得到模糊的画面。



# 泰森多边形（VORONOI）


# 屏幕后处理

1. 确认项目是URP的
2. 创建shader graph，把material设置为fullscreen
3. 可以开始写效果了
4. 确认当前的URP assert已经挂载了
5. 把对应的URP data找到，并add renderer feature，fullscreen pass
6. 用刚才的shader生成材质，并挂载到fullscreen pass上面
7. ok



# 场景扫描的效果

核心是在透明物体上挂载shader，用scene depth减去Position（view）。scene depth不会把透明物体的深度信息记录到深度缓冲区，所以这两个值相减的时候。
1. 当物体没有接触，并且不透明物体在上方时，深度信息和顶点信息一样，为0 。所以不透明物体不能挂载这个shader。
2. 当物体没有接触，并且透明物体在 上方时，会用不透明物体的深度减去透明物体的顶点，是正数，大于1，saturate并one minus之后变为0。把这个值传入alpha，此时不透明。
3. 当接触时，深度信息是不透明物体的，但是透明物体已经穿模了。导致减去之后为负数。
	此时saturate并one minus变为1，也就是会有接触部分高亮的效果。