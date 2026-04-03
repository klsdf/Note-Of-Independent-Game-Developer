+

神秘js
```js

class Game {
    static behaviours = [];

    static register(behaviour) {
        this.behaviours.push(behaviour);
    }

    static start() {
        for (const b of this.behaviours) {
            if (typeof b.start === 'function') {
                b.start();
            }
        }
    }

    static update() {
        for (const b of this.behaviours) {
            if (typeof b.update === 'function') {
                b.update();
            }
        }
        requestAnimationFrame(() => this.update());
    }

    static run() {
        this.start();
        this.update();
    }
}

// 基类：任何继承自它的对象都会被注册
class Behaviour {
    constructor() {
        Game.register(this);
    }

    start() {
        // 子类实现
    }

    update() {
        // 子类实现
    }
}



class Player extends Behaviour {
    constructor() {
        super();
        this.x = 0;
    }

    start() {
        console.log("Player start!");
    }

    // update() {
    //     this.x += 1;
    //     console.log("Player X:", this.x);
    // }
}

new Player(); // 自动注册并执行

Game.run();   // 启动游戏


```











神秘8bit音效网站

https://sfxr.me/










- 视频素材（需要花钱）
https://www.xinpianchang.com/recommend



- 免费视频素材 
https://mixkit.co/free-stock-video/nature/






神秘godot代码


```python
class_name DynamicTest
extends Node2D

# 获取Label节点的引用
@onready var label = $Label

@onready var 执行动态代码 = $动态代码测试

@onready var 执行动态代码2 = $动态代码测试2


@onready var 用户输入 = $用户输入




@onready var 用户输入代码 = $用户输入代码


signal testSignal

func _ready():
	# 在场景开始时给Label写入文字
	label.text = "欢迎使用动态测试场景！"
	
	# 可选：设置Label的样式
	label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	label.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
	
	执行动态代码.pressed.connect(test_dynamic_script)
	
	执行动态代码2.pressed.connect(test2)

	print("场景已初始化，Label文字已设置")
	
	# 初始化代码编辑器
	init_code_edit()
	
	# 测试动态代码加载
	test_dynamic_script()
	testSignal.connect(test2)


func init_code_edit():
	# 设置默认代码示例
# 	用户输入代码.text = """func test():
# 	return "Hello from dynamic code!"
# """
	# 为CodeEdit设置语法高亮
	# CodeEdit在Godot 4中内置了GDScript语法高亮

	if 用户输入代码.syntax_highlighter == null:
		用户输入代码.syntax_highlighter = preload("res://MyHighlighter.gd").new()

	
	# 设置字体大小（可选）
	用户输入代码.add_theme_font_size_override("font_size", 14)
	
	# 设置代码补全
	setup_code_completion()
	
	# 强制刷新语法高亮
	用户输入代码.queue_redraw()

func setup_code_completion():
	# 启用代码补全
	用户输入代码.code_completion_enabled = true
	
	# 设置补全前缀
	var prefixes = PackedStringArray()
	prefixes.append_array([
		"func", "var", "const", "if", "else", "elif", "for", "while", "match", "return",
		"true", "false", "null", "extends", "class_name", "pass", "break", "continue",
		"print", "str", "int", "float", "bool", "Vector2", "Vector3", "Color", "Rect2",
		"Array", "Dictionary", "String", "Node", "Node2D", "Control", "RefCounted"
	])
	用户输入代码.code_completion_prefixes = prefixes

# 动态代码加载功能
func test_dynamic_script():
	# 1. 创建一个新的GDScript对象
	var script = GDScript.new()
	
	# 2. 设置脚本源代码（字符串形式）
	script.set_source_code("""
extends RefCounted  # Godot 4中使用RefCounted替代Reference


func say_hello(name):
	return "Hello, " + name + "!"

""")
	
	# 3. 重新加载脚本使其生效
	script.reload()
	
	# 4. 创建脚本实例
	var instance = script.new()
	
	# 5. 调用动态方法
	var text = 用户输入.text

	var result2 = instance.say_hello(text)


	
	# 更新Label显示动态脚本的执行结果
	label.text = "动态脚本执行成功！\n问候语: " + result2


func test():
	return "test"

func test2():
	# 获取用户输入的代码字符串
	var user_code = 用户输入代码.text
	
	# 检查用户输入是否为空
	if user_code.is_empty():
		label.text = "请输入代码！"
		return
	
	# 创建动态脚本
	var script = GDScript.new()
	
	# 构建完整的脚本代码
	# 为用户代码的每一行添加缩进
	var indented_code = ""
	# var lines = user_code.split("\n")
	# for line in lines:
	# 	if line.strip_edges() != "":  # 跳过空行
	# 		indented_code += "\t" + line + "\n"
	
	var full_code = """
extends RefCounted
%s
""" % user_code
	
	# 设置脚本源代码
	script.set_source_code(full_code)
	
	# 重新加载脚本
	script.reload()
	
	# 创建实例并执行
	var instance = script.new()
	
	# 执行用户代码
	var result = instance.test()
	label.text = "代码执行成功！\n结果: " + str(result)
	print("用户代码执行结果: ", result)


```












【【生肉】碧蓝档案主线剧情vol1 第三章（第五部）】 https://www.bilibili.com/video/BV1jW42197Gp/?p=3&share_source=copy_web&vd_source=7de8c277f16e8e03b48a5328dddfe2ce

ba中, 通过双引号可以表现出来sensi的话和星野的话.
标点不一样, 说话人也不一样

![[asserts/image.png]]












神秘的清除c盘软件
TreeSizeFree.exe

geek.exe