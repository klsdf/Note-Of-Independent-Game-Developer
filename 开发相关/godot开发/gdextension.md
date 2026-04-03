
# 环境搭建



1. 下载官方的模板库 https://github.com/godotengine/godot-cpp-template
2. 更新子模块`git submodule update --init`, 因为这玩意是依赖godot-cpp库的
3. 安装vs, 安装c++桌面开发
4. 安装python
5. 安装pip `python -m ensurepip --upgrade`
6. 安装scons环境 `pip install scons`, 当然了我是用的虚拟环境, 理论上装到全局就ok
		`python -m pip install scons`

7. 在项目的根目录 运行` c:\Users\17966\Downloads\godot-cpp-template-main\godot-cpp-template\.venv\Scripts\scons.exe platform=windows target=template_debug debug_symbols=yes`
8. 然后可以看到, 在项目bin中出现了新的dll
9. ![[{BE97D750-1A5A-483E-8364-FA2A750C91D3}.png]]







# 可以修改配置的名字



1. register_types.cpp里面, 导出的这个example_library_init, 就是 Godot 加载 GDExtension 时调用的入口函数名. 必须和example.gdextension里面的`entry_symbol = "example_library_init"`一模一样才行

```cpp
extern "C"
{
	// Initialization
	GDExtensionBool GDE_EXPORT example_library_init(GDExtensionInterfaceGetProcAddress p_get_proc_address, GDExtensionClassLibraryPtr p_library, GDExtensionInitialization *r_initialization)
	{
		GDExtensionBinding::InitObject init_obj(p_get_proc_address, p_library, r_initialization);
		init_obj.register_initializer(initialize_gdextension_types);
		init_obj.register_terminator(uninitialize_gdextension_types);
		init_obj.set_minimum_library_initialization_level(MODULE_INITIALIZATION_LEVEL_SCENE);

		return init_obj.init();
	}
}
```

2. 如果想改导出的dll的名字
	1. SConstruct里面, libname = "EXTENSION-NAME"改一下
	2. deno里面的bin的example.gdextension路径重新改一下




# 如何编写自定义的函数


自定义函数print_error


1. 先声明头文件

```c

#pragma once

#include "godot_cpp/classes/ref_counted.hpp"
#include "godot_cpp/classes/wrapped.hpp"
#include "godot_cpp/variant/variant.hpp"

using namespace godot;

class ExampleClass : public RefCounted {
	GDCLASS(ExampleClass, RefCounted)

protected:
	static void _bind_methods();

public:
	ExampleClass() = default;
	~ExampleClass() override = default;

	void print_type(const Variant &p_variant) const;

	//自定义的错误信息
	void print_error(const String &p_message) const;
};
```


2. 定义函数, 别忘了去_bind_methods里面绑定一下方法
```c#
#include "example_class.h"
// 添加必要的头文件
#include "godot_cpp/variant/string.hpp"

void ExampleClass::_bind_methods() {
	godot::ClassDB::bind_method(D_METHOD("print_type", "variant"), &ExampleClass::print_type);
	// 绑定新方法
	godot::ClassDB::bind_method(D_METHOD("print_error", "message"), &ExampleClass::print_error);
}

void ExampleClass::print_type(const Variant &p_variant) const {
	print_line(vformat("Type: %d", p_variant.get_type()));
}


void ExampleClass::print_error(const String &p_message) const {
	print_line(vformat("自定义Error: %s", p_message));
}
```

3. 重新编译



# 自定义类



1. 自定义.h文件
```c
#pragma once

#include "godot_cpp/classes/ref_counted.hpp"
#include "godot_cpp/classes/wrapped.hpp"
#include "godot_cpp/variant/variant.hpp"

using namespace godot;

class YanClass : public RefCounted {
	GDCLASS(YanClass, RefCounted)

protected:
	static void _bind_methods();

public:
	YanClass() = default;
	~YanClass() override = default;

	void log_info(const String &p_message) const;
};

```


2. 自定义.cpp文件, <span style="background:rgba(136, 49, 204, 0.2)">别忘了引用头文件</span>
```c

#include "yan_class.h"
// 添加必要的头文件
#include "godot_cpp/variant/string.hpp"

void YanClass::_bind_methods() {
	godot::ClassDB::bind_method(D_METHOD("log_info", "message"), &YanClass::log_info);
}

void YanClass::log_info(const String &p_message) const {
	print_line(vformat("自定义Info: %s", p_message));
}
```


3. 给register_types.cpp里面定义和注册yan class

主要就是`#include "yan_class.h"`, 还有`GDREGISTER_CLASS(YanClass);`
```c
#include "register_types.h"

#include <gdextension_interface.h>
#include <godot_cpp/core/class_db.hpp>
#include <godot_cpp/core/defs.hpp>
#include <godot_cpp/godot.hpp>

#include "example_class.h"
#include "yan_class.h"

using namespace godot;

void initialize_gdextension_types(ModuleInitializationLevel p_level)
{
	if (p_level != MODULE_INITIALIZATION_LEVEL_SCENE) {
		return;
	}
	GDREGISTER_CLASS(ExampleClass);
	GDREGISTER_CLASS(YanClass);
}

void uninitialize_gdextension_types(ModuleInitializationLevel p_level) {
	if (p_level != MODULE_INITIALIZATION_LEVEL_SCENE) {
		return;
	}
}

extern "C"
{
	// Initialization
	GDExtensionBool GDE_EXPORT example_library_init(GDExtensionInterfaceGetProcAddress p_get_proc_address, GDExtensionClassLibraryPtr p_library, GDExtensionInitialization *r_initialization)
	{
		GDExtensionBinding::InitObject init_obj(p_get_proc_address, p_library, r_initialization);
		init_obj.register_initializer(initialize_gdextension_types);
		init_obj.register_terminator(uninitialize_gdextension_types);
		init_obj.set_minimum_library_initialization_level(MODULE_INITIALIZATION_LEVEL_SCENE);

		return init_obj.init();
	}
}
```


4. 使用
```python
extends Node


func _ready() -> void:
	var example := ExampleClass.new()
	example.print_type(example)
	example.print_error("自定义Error")

	var yan := YanClass.new()
	yan.log_info("自定义Info")
```



# 清除编译 ,重新编译

## 清理之前的编译文件

scons -c platform=windows target=template_debug debug_symbols=yes

  

## 重新编译

scons platform=windows target=template_debug debug_symbols=yes





```


    # 使用YanClass替代GDScript来获得详细的错误信息

    var script = YanClass.new()
   
	# 使用新的验证方法设置源代码
	var validation_result = script.set_source_code_with_validation(full_code)
	
	# 检查验证结果
	if not validation_result["success"]:
		var error_code = validation_result["error_code"]
		var error_message = validation_result["error_message"]
		var error_type = validation_result["error_type"]
		
		# 构建详细的错误信息
		var error_output = []
		error_output.append("编译失败！")
		error_output.append("错误类型: %s" % error_type)
		error_output.append("错误信息: %s" % error_message)
		error_output.append("错误码: %s" % str(error_code))
		
		# 根据错误类型提供具体建议
		match error_code:
			ERR_PARSE_ERROR:
				error_output.append("\n常见问题：")
				error_output.append("- 检查括号是否匹配")
				error_output.append("- 检查字符串是否闭合")
				error_output.append("- 检查冒号使用是否正确")
			ERR_COMPILATION_FAILED:
				error_output.append("\n常见问题：")
				error_output.append("- 检查函数定义语法")
				error_output.append("- 检查变量声明")
				error_output.append("- 检查缩进是否正确")
			ERR_INVALID_DATA:
				error_output.append("\n常见问题：")
				error_output.append("- 检查代码格式")
				error_output.append("- 检查特殊字符")
		
		output.text = "\n".join(error_output)
		dialog_system.speak("代码编译失败，请检查语法！")
```