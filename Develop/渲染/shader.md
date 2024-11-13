opengl和directx

GLSL shader语言用于OpenGL
HLSL shader语吉用于DirectX
CG是跨平台的，nvidia开发的

# 第一个Shader



```
Shader "Custom/NewSurfaceShader"
{
    Properties
    {
    }
    SubShader
    {
       PASS
       {
       CGPROGRAM

  // 在这里定义顶点着色器函数
               #pragma vertex vert
               // 在这里定义片元着色器函数
               #pragma fragment frag
               // System-Value Position 
               float4 vert(float4 vertex : POSITION) : SV_POSITION
               {
                   // 顶点变换逻辑，例如将顶点位置从模型空间转换到裁剪空间
                   return UnityObjectToClipPos(vertex);
               }
               fixed4 frag() : SV_Target
               {
                   // 片元颜色计算逻辑，例如返回一个固定颜色
                   return fixed4(1, 0, 0, 1);
               }
               ENDCG

        }
    }
    FallBack "Diffuse"
}
```


这一套写法虽然已经可以实现颜色的变化，但是数据信息太少了。
比如说顶点着色器vert中，只获得了顶点坐标vertex，但是并没有获得法线和纹理的坐标。也就是说，如果想获得更多的信息，我们需要传入一个结构体。





# 自定义输出结构体


```hlsl
Shader "Custom/NewSurfaceShader"
{
    Properties
    {
        _Color ("Color", Color) = (1,1,1,1)
    }
    SubShader
    {
       PASS
       {
       CGPROGRAM
       
       float4 _Color;

        // 在这里定义顶点着色器函数
        #pragma vertex vert
        // 在这里定义片元着色器函数
        #pragma fragment frag

		//Application to Vertex
        struct a2v
        {
        //模型空间的顶点位置
            float4 vertex :POSITION;
            float3 normal:NORMAL;
        };

		//Vertex to Fragment
        struct v2f
        {
            //不可省略！！要是没有了SV_POSITION，就无法得到裁剪空间的顶点信息了
            float4 pos:SV_POSITION;
            fixed3 color: COLOR0;
        };


        // System-Value Position ,代表裁剪空间的坐标信息
        v2f vert(a2v v)
        {
            v2f o;
            o.pos =  UnityObjectToClipPos(v.vertex);

            //v.normal * 0.5 会生成一个 float3 值，但没有偏移到适合颜色显示的范围（正常情况下颜色的范围在 [0,1]，而法线数据是向量，值的范围可能在 [-1,1]）。你可以用 normalize(v.normal) * 0.5 + 0.5 来确保法线映射到 [0,1] 范围内，更适合颜色输出。
            o.color = v.normal*0.5+0.5;
            return o;
        }
        float4 frag(v2f f) : SV_Target
        {
           float4 temp = float4( f.color,1.0) * _Color;
            return temp;
        }
        ENDCG

        }
    }
    FallBack "Diffuse"
}

```


![image-20231104204715051](../img/shader/image-20231104204715051.png)


# 光照
·漫反射模型
```
Shader "Custom/光照"
{
    Properties
    {
        _Color("漫反射颜色",Color) = (1,1,1,1)
    }
    SubShader
    {
        Pass
        {
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag

            #include "Lighting.cginc"
            
            float4 _Color;
            struct a2v
            {
                float4 vertex: POSITION;
                float3 normal: NORMAL;
            };
            struct v2f
            {
                float4 position: SV_POSITION;
                float3 worldNormal : TEXCOORD0;
                float3 color :COLOR;
            };

            v2f vert(a2v v)
            {
                v2f o;
                o.position = UnityObjectToClipPos(v.vertex);

                /*
                UNITY_LIGHTMODEL_AMBIENT：

这是 Unity 内置的宏，表示场景中的环境光模型。在 Unity 的渲染管线中，环境光是用来照亮场景的基础光源，它通常是一个全局的颜色，不依赖于场景中的具体光源位置或方向。
UNITY_LIGHTMODEL_AMBIENT 是一个 float4 类型的值，通常包含 RGBA 四个分量，其中 RGB 分量代表环境光的颜色，而 A 分量通常用于表示透明度。
.xyz：

通过 .xyz 访问 UNITY_LIGHTMODEL_AMBIENT 的前三个分量，提取出环境光的 RGB 颜色值。这样，ambient 变量将只包含环境光的颜色信息（而不包括透明度）。
                */
                float3  ambient = UNITY_LIGHTMODEL_AMBIENT.xyz;


                /*
                v.normal：

这是输入结构体 v 中的法线属性，通常是在顶点着色器中传递的。v.normal 是一个 float3 类型的向量，表示模型空间中的法线。
unity_WorldToObject：

这是 Unity 的一个内置矩阵，表示从世界空间到对象空间的变换矩阵。它通常用于将世界空间中的点或法线转换回对象空间。
在这里，我们需要使用其逆转置矩阵（通常称为 法线矩阵）来将法线从对象空间转换为世界空间。
(float3x3)unity_WorldToObject：

通过 (float3x3) 将 unity_WorldToObject 矩阵转换为 3x3 的浮点矩阵。因为法线不需要平移部分（只需要旋转和缩放），所以只取矩阵的前 3 行和 3 列。
mul(v.normal, (float3x3)unity_WorldToObject)：

使用 mul 函数将法线 v.normal 与法线变换矩阵相乘，以将法线从对象空间转换到世界空间。这个操作会考虑对象的旋转和缩放，从而得到正确的法线方向。
                */
                float3 worldNormal = normalize(mul(v.normal,(float3x3)unity_WorldToObject ));

                float3 worldLightDirection  = normalize(_WorldSpaceLightPos0.xyz);

                float3 diffuse = _LightColor0.rgb *_Color.rgb*saturate( dot(worldNormal,worldLightDirection));


                o.color = ambient+diffuse;
                //o.worldNormal

                return o;
            }

            float4 frag(v2f f):SV_TARGET
            {
                return float4(f.color,1.0);
            }

            ENDCG
        }
    }

    FallBack "Diffuse"
}
```


# 压缩数组

`float3`   `int4` 

![image-20231104205804404](img/shader/image-20231104205804404.png)

```
片元着色器：颜色

//涂抹语法  smearing

0.Albedo = 1  //(0,0,0)

//遮罩语法 masking

0.Albedo.gb = Color.gb

获取矩阵的值

float4X4 matrix

float first = matrix._m00;

float last= matrix._m33;

获取行或者对角线的值
```


![image-20231104211558733](img/shader/image-20231104211558733.png)

# 贴图滚动特效

```c
Shader "ShaderStudy/纹理映射"
{
    Properties
    {
        _Color ("Color", Color) = (1,1,1,1)
        _MainTex ("Albedo (RGB)", 2D) = "white" {}
        _ScrollingXSpeed("ScrollingXSpeed",Range(0,10))= 0
        _ScrollingYSpeed("ScrollingYSpeed",Range(0,10))= 2
    }
    SubShader
    {
        Tags { "RenderType"="Opaque" }
        LOD 200

        CGPROGRAM
        // Physically based Standard lighting model, and enable shadows on all light types
        #pragma surface surf Standard fullforwardshadows

        // Use shader model 3.0 target, to get nicer looking lighting
        #pragma target 3.0

        sampler2D _MainTex;

        struct Input
        {
            float2 uv_MainTex; 
        };


        fixed4 _Color;

        float _ScrollingXSpeed;
        float _ScrollingYSpeed;


        UNITY_INSTANCING_BUFFER_START(Props)
        UNITY_INSTANCING_BUFFER_END(Props)

        void surf (Input IN, inout SurfaceOutputStandard o)
        {
            fixed2  scrollUV = IN.uv_MainTex;

            fixed xScroll = _ScrollingXSpeed * _Time;
            fixed yScroll = _ScrollingYSpeed * _Time;
            scrollUV += fixed2(xScroll,yScroll);



            // tex2D就是根据纹理的坐标来找到这个贴图对应点的颜色
            fixed4 c = tex2D (_MainTex, scrollUV) * _Color;
            o.Albedo = c.rgb;

            o.Alpha = c.a;
        }
        ENDCG
    }
    FallBack "Diffuse"
}

```

# 法线映射

![image-20231104225556457](../img/shader/image-20231104225556457.png)

```glsl
Shader "ShaderStudy/法线贴图"
{
    Properties
    {
        _Color ("Color", Color) = (1,1,1,1)
        _NormalMap ("NormalMap",2D)="bunp"{}

        _NormalMapStrength("NormalMapStrength",Range(0,1)) = 1
    }
    SubShader

    {
        Tags { "RenderType"="Opaque" }
        LOD 200

        CGPROGRAM
        // Physically based Standard lighting model, and enable shadows on all light types
        #pragma surface surf Standard fullforwardshadows

        // Use shader model 3.0 target, to get nicer looking lighting
        #pragma target 3.0

        sampler2D _NormalMap;

        struct Input
        {
            float2 uv_NormalMap;
        };


        fixed4 _Color;
        float _NormalMapStrength;

        UNITY_INSTANCING_BUFFER_START(Props)
        UNITY_INSTANCING_BUFFER_END(Props)

        void surf (Input IN, inout SurfaceOutputStandard o)
        {


           float3 normalMap =  UnpackNormal( tex2D (_NormalMap, IN.uv_NormalMap));
           normalMap.x*= _NormalMapStrength;
           normalMap.y*= _NormalMapStrength;
          normalMap = normalize(normalMap);

        
            o.Albedo = _Color.rgb;
            o.Normal =normalMap;
        o.Alpha = _Color.a;
        }
        ENDCG
    }
    FallBack "Diffuse"
}

```

# 透明材质

1. 需要把tag修改

       Tags { "RenderType"="Opaque" } //Opaque代表不透明

![image-20231105002054108](img/shader/image-20231105002054108.png)

```shader
Shader "ShaderStudy/透明材质"
{
    Properties
    {
        _Color ("Color", Color) = (1,1,1,1)
        _MainTex ("Albedo (RGB)", 2D) = "white" {}
  
    }
    SubShader

    {
        Tags { 
        "RenderType"="Transparent" 
        "IgnoreProjector"="True" //不会产生影子
        "Queue"="Transparent"  //使用透明的渲染队列，保证先渲染不透明物体再渲染透明的
        }
        LOD 200
        Cull Off

        CGPROGRAM
        // Physically based Standard lighting model, and enable shadows on all light types
        #pragma surface surf Standard alpha:fade

        // Use shader model 3.0 target, to get nicer looking lighting
        #pragma target 3.0

    
      sampler2D _MainTex;
        struct Input
        {
            float2 uv_MainTex;
        };


        fixed4 _Color;
   
      

        UNITY_INSTANCING_BUFFER_START(Props)
        UNITY_INSTANCING_BUFFER_END(Props)

        void surf (Input IN, inout SurfaceOutputStandard o)
        {
            fixed4 c = tex2D (_MainTex,IN.uv_MainTex)*_Color;
            o.Albedo = c.rgb;
            o.Alpha = c.a;
        }
        ENDCG
    }
    FallBack "Diffuse"
}

```

原理：

1. 透明的物体是在非透明物体之后才渲染的，所以会有透明感
2. 当不透明物体出现在透明物体前面时，如果还渲染透明物体会很奇怪
3. 所以当不透明物体遮挡之后，默认不绘制透明物体

Cull Back这个东西又是什么意思？

"Cull Back" 主要用于计算机图形学中的面剔除（Face Culling）。当我们渲染一个图形时，不需要渲染那些用户无法看到的面。例如，当你看一个立方体时，你一次只能看到三个面，其他三个面在立方体的另一边，所以没必要去渲染他们。

"Cull Back" 表示剔除背向观察者的面，将它们从渲染过程中排除，以此来提高渲染的效率。具体来说，这通常是通过比较面的法向量和从观察者到面的向量来实现的。如果两个向量的方向相反，那么这个面就被认为是背向观察者的，应当被剔除。

我这个材质是一个玻璃材质，使用Cull Back会不会很奇怪？因为我玻璃是透明的，但是我却看不到背面

你提出了一个很好的问题。一般来说，对于完全透明的对象如玻璃，我们通常不会使用剔除（Culling），因为既然是透明的，我们需要从一侧看到另一侧。如果使用了"Cull Back"，那么你看到的将只是玻璃的前面，而看不到它的背面，这将产生一种不自然或者说不真实的效果。所以在实际应用中，我们通常不会对透明物体使用背面剔除。

那么我是不是应该写Cull off？

是的，对于一个透明的物体如玻璃，"Cull Off" 是比较合适的设置。"Cull Off" 会禁用面剔除功能，这意味着图形的所有面都会被渲染，包括那些从相机角度看不见的面。这对于玻璃这样的透明物体来说，能够创建出正常的渲染效果，让你可以从一个面看到另一个面。
