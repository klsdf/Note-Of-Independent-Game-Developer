



opengl和directx

GLSL shader语言用于OpenGL
HLSL shader语吉用于DirectX
CG是跨平台的，nvidia开发的


# 输出结构体的内容





```
  void surf (Input IN, inout SurfaceOutputStandard o)
        {
            fixed4 c =  _Color;
            o.Albedo = c.rgb;

        }
```



![image-20231104204715051](img/shader/image-20231104204715051.png)









# 压缩数组

`float3`   `int4`



![image-20231104205804404](img/shader/image-20231104205804404.png)



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

![image-20231104211558733](img/shader/image-20231104211558733.png)







# 贴图滚动特效



```glsl
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

![image-20231104225556457](img/shader/image-20231104225556457.png)





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

   ​    Tags { "RenderType"="Opaque" } //Opaque代表不透明



![image-20231105002054108](img/shader/image-20231105002054108.png)

```
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
