1. 建一个Editor文件夹。里面的任何代码资源都不会被打包
2. 写一个静态方法


# URP后处理

```c#
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.Rendering.Universal;
public class TestFeature : ScriptableRendererFeature
{

    class TestRenderPass : ScriptableRenderPass
    {
        public Material testMaterial;



        private RTHandle m_TempRT;


        public TestRenderPass(Material material, RenderPassEvent renderPassEvent)
        {

            testMaterial = material;
            this.renderPassEvent = renderPassEvent;
        }

        public override void OnCameraSetup(CommandBuffer cmd, ref RenderingData renderingData)
        {

            if (m_TempRT == null)

            {

                m_TempRT = RTHandles.Alloc(renderingData.cameraData.cameraTargetDescriptor, name: "_TempRT");
            }
        }

        public override void Execute(ScriptableRenderContext context, ref RenderingData renderingData)
        {
            CommandBuffer cmd = CommandBufferPool.Get("测试的后处理");
            RenderTargetIdentifier source = renderingData.cameraData.renderer.cameraColorTargetHandle;

            cmd.Blit(source, m_TempRT, testMaterial);
            cmd.Blit(m_TempRT, source);
            context.ExecuteCommandBuffer(cmd);
            CommandBufferPool.Release(cmd);
        }

        public override void OnCameraCleanup(CommandBuffer cmd)
        {

            if (m_TempRT != null)
            {
                RTHandles.Release(m_TempRT);
                m_TempRT = null;
            }
        }
    }

    public Material testMaterial;
    TestRenderPass testPass;

    public RenderPassEvent renderPassEvent = RenderPassEvent.AfterRendering;

    public override void Create()
    {
        testPass = new TestRenderPass(testMaterial, renderPassEvent);
    }
    public override void AddRenderPasses(ScriptableRenderer renderer, ref RenderingData renderingData)
    {
        if (testMaterial != null)
        {
            renderer.EnqueuePass(testPass);
        }
    }
}
```



测试的shader
```shader
Shader "Hidden/RedTintPostProcess"
{
    Properties
    {
        _Color("Color", Color) = (1,0,0,1)
    }
    SubShader
    {
        Tags 
        { 
            "RenderType"="Transparent" 
            "Queue"="Transparent"
            "RenderPipeline" = "UniversalPipeline"
        }

        Pass
        {
            Name "RedTint"
            ZTest Always 
            Cull Off 
            ZWrite Off
            Blend SrcAlpha OneMinusSrcAlpha

            HLSLPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"

            struct Attributes
            {
                float4 positionOS : POSITION;
                float2 uv : TEXCOORD0;
            };

            struct Varyings
            {
                float4 positionCS : SV_POSITION;
                float2 uv : TEXCOORD0;
            };

            TEXTURE2D(_MainTex);
            SAMPLER(sampler_MainTex);
            float4 _Color;

            Varyings vert(Attributes input)
            {
                Varyings output;
                output.positionCS = TransformObjectToHClip(input.positionOS.xyz);
                output.uv = input.uv;
                return output;
            }

            float4 frag(Varyings input) : SV_Target
            {
                float4 color = SAMPLE_TEXTURE2D(_MainTex, sampler_MainTex, input.uv);
                return lerp(color, _Color, _Color.a);
            }
            ENDHLSL
        }
    }
}

```





带temp RT的
``` c#
using UnityEngine;

using UnityEngine.Rendering;

using UnityEngine.Rendering.Universal;

using Beffio.Dithering;

  

public class CustomFullScreenPassRendererFeature : ScriptableRendererFeature

{

    [SerializeField]

    [Header("调色板")]

    private Palette _palette; // 用于抖动效果的颜色调色板

    public Palette Palette { get { return _palette; } set { _palette = value; } }

  
  

    [SerializeField]

    [Header("抖动效果的模式/图案")]

    private Pattern _pattern;// 抖动效果的模式/图案

    public Pattern Pattern { get { return _pattern; } set { _pattern = value; } }

  
  
  

    [SerializeField]

    [Header("自定义的抖动纹理")]

    private Texture2D _patternTexture;// 自定义的抖动纹理

    public Texture2D PatternTexture { get { return _patternTexture; } set { _patternTexture = value; } }

  
  

    class CustomFullscreenPass : ScriptableRenderPass

    {

        public Material grayscaleMaterial;

        public Palette palette;

        public Pattern pattern;

        public Texture2D patternTexture;

  

        private RTHandle m_TempRT;

        public CustomFullscreenPass(Material material, RenderPassEvent renderPassEvent, Palette palette, Pattern pattern, Texture2D patternTexture)

        {

            grayscaleMaterial = material;

            this.renderPassEvent = renderPassEvent;

            this.palette = palette;

            this.pattern = pattern;

            this.patternTexture = patternTexture;

        }

        public override void OnCameraSetup(CommandBuffer cmd, ref RenderingData renderingData)

        {

            if (m_TempRT == null)

            {

                m_TempRT = RTHandles.Alloc(renderingData.cameraData.cameraTargetDescriptor, name: "_TempRT");

            }

        }

        public override void Execute(ScriptableRenderContext context, ref RenderingData renderingData)

        {

            CommandBuffer cmd = CommandBufferPool.Get("自定义后处理");

  

            RenderTargetIdentifier source = renderingData.cameraData.renderer.cameraColorTargetHandle;

  

            /*

  

            测试部分

            */

  

            if (palette == null || (pattern == null && patternTexture == null))

            {

                return;

            }

  

            if (!palette.HasTexture || (patternTexture == null && !pattern.HasTexture))

            {

                return;

            }

  

            Texture2D patTex = (pattern == null ? patternTexture : pattern.Texture);

  

            grayscaleMaterial.SetFloat("_PaletteColorCount", palette.MixedColorCount);

            grayscaleMaterial.SetFloat("_PaletteHeight", palette.Texture.height);

            grayscaleMaterial.SetTexture("_PaletteTex", palette.Texture);

            grayscaleMaterial.SetFloat("_PatternSize", patTex.width);

            grayscaleMaterial.SetTexture("_PatternTex", patTex);

            /*

  

            测试结束

            */

            cmd.Blit(source, m_TempRT, grayscaleMaterial);

            cmd.Blit(m_TempRT, source);

  

            context.ExecuteCommandBuffer(cmd);

            CommandBufferPool.Release(cmd);

        }

        public override void OnCameraCleanup(CommandBuffer cmd)

        {

            if (m_TempRT != null)

            {

                RTHandles.Release(m_TempRT);

                m_TempRT = null;

            }

        }

    }

  

    public Material grayscaleMaterial;

    CustomFullscreenPass grayscalePass;

    private RenderPassEvent renderPassEvent = RenderPassEvent.BeforeRenderingPostProcessing;

  
  

    public override void Create()

    {

        grayscalePass = new CustomFullscreenPass(grayscaleMaterial, renderPassEvent, Palette, Pattern, PatternTexture);

    }

  

    public override void AddRenderPasses(ScriptableRenderer renderer, ref RenderingData renderingData)

    {

        if (grayscaleMaterial != null)

        {

            renderer.EnqueuePass(grayscalePass);

        }

    }

}
```




# 网络请求

```c#
using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using System.IO;
using UnityEngine.UI;
using System.Text;



public class ComfyUIData
{
    public string task_id;
    public int seed;
    public string prompt;
    public string negative_prompt;

    public ComfyUIData(string task_id, int seed, string prompt, string negative_prompt)
    {
        this.task_id = task_id;
        this.seed = seed;
        this.prompt = prompt;
        this.negative_prompt = negative_prompt;
    }
}

public class ComfyUIResponse
{
    public float total_time;
    public float execution_time;
    public string image;
}


public class URL请求 : MonoBehaviour
{
    ComfyUIData postData;

    string url = "https://u166586-ab95-e29cbb18.westx.seetacloud.com:8443/sync/prompt";

    async void Start()
    {
  
     }
    IEnumerator GetImage(Action callBack)
    {
        postData = new ComfyUIData("dog", UnityEngine.Random.Range(0, 100000000), "a red dog, tie, cute, natural, high quality", "strong light, shadow, jpeg artifacts, abnormal structure");
        using (UnityWebRequest request = new UnityWebRequest(url, "POST"))
        {

            string jsonString = JsonUtility.ToJson(postData);
            byte[] data = System.Text.Encoding.UTF8.GetBytes(jsonString);
            request.uploadHandler = (UploadHandler)new UploadHandlerRaw(data);
            request.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
            request.SetRequestHeader("Content-Type", "application/json");
            yield return request.SendWebRequest();

            if (request.responseCode == 200)
            {
                string respondedString = request.downloadHandler.text;
                ComfyUIResponse response = JsonUtility.FromJson<ComfyUIResponse>(respondedString);
                print(response.total_time);
                print(response.execution_time);
                print(response.image);
                byte[] imageBytes = Convert.FromBase64String(response.image);
                File.WriteAllBytes(Application.dataPath + "/" + postData.task_id + ".png", imageBytes);
                callBack?.Invoke();
                Debug.Log("保存成功");
            }
            else
            {
                Debug.LogError("请求失败");
                Debug.Log(request.error);
            }
    }
    }
}


```







# 画线

linePrefab里面：

1. edge collider 2d
2. rigidbody 2d
3. line render
4. line merge



```c#
using UnityEngine;
using System.Collections.Generic;
public class DrawLine : MonoBehaviour
{
    //单例模式
    private static DrawLine instance;
    public static  DrawLine Instance
    {
        get
        {
            if (instance == null)
            {
                instance = FindObjectOfType<DrawLine>();
            }
            return instance;
        }
    }
    public GameObject linePrefab;
    public GameObject currentLine;
    public LineRenderer lineRenderer;
    private EdgeCollider2D edgeCollider;
    private List<Vector2> mousePositions;


    public bool hasCreateLine = false;






    // private Stack<List<Vector2>> lines = new Stack<List<Vector2>>();
    public List<GameObject> lines = new List<GameObject>();





    private List<AnimationCurve> lineCurves = new List<AnimationCurve>();
    private int curveIndex = 0;


    private List<Color> lineColors = new List<Color>();
    private int colorIndex = 0;






    private AnimationCurve CreateCurve(params float[] keys)
    {
        AnimationCurve curve = new AnimationCurve();
        for (int i = 0; i < keys.Length; i += 2)
        {
            curve.AddKey(keys[i], keys[i + 1]);
        }
        return curve;
    }

    void Start()
    {
        mousePositions = new List<Vector2>();

        lineColors.Add(Color.red);
        lineColors.Add(Color.blue);
        lineColors.Add(Color.white);

        //等宽的线
        AnimationCurve curve1 = CreateCurve(0, 0.1f, 1, 0.1f);
        lineCurves.Add(curve1);

        //头尾粗的线
        AnimationCurve curve2 = CreateCurve(0, 0.1f, 0.5f, 0.5f, 1, 0.1f);
        lineCurves.Add(curve2);

        //头粗的线
        AnimationCurve curve3 = CreateCurve(0, 0.6f, 1, 0.1f);
        lineCurves.Add(curve3);

    }

    void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            mousePositions.Clear();
            mousePositions.Add(Camera.main.ScreenToWorldPoint(Input.mousePosition));
            // CreateLine();
            hasCreateLine = false;
        }
        if (Input.GetMouseButton(0))
        {


            Vector2 mousePos = Camera.main.ScreenToWorldPoint(Input.mousePosition);
            if (Vector2.Distance(mousePos, mousePositions[mousePositions.Count - 1]) > .1f)
            {
                UpdateLine(mousePos);

            }
        }

        if (Input.GetMouseButtonUp(0))
        {
            EndLine();

        }



        if (Input.GetKey(KeyCode.LeftControl) || Input.GetKey(KeyCode.RightControl))
        {
            if (Input.GetKeyDown(KeyCode.Z))
            {
                Undo();
            }
        }


        if (Input.GetKeyDown(KeyCode.LeftBracket))
        {

            lineRenderer.startWidth += 0.1f;
            lineRenderer.endWidth += 0.1f;

        }

        if (Input.GetKeyDown(KeyCode.RightBracket))
        {
            lineRenderer.startWidth -= 0.1f;
            lineRenderer.endWidth -= 0.1f;

        }


        if (Input.GetKeyDown(KeyCode.Alpha1))
        {
            lineRenderer.startColor = Color.white;
            lineRenderer.endColor = Color.white;
        }


        if (Input.GetKeyDown(KeyCode.Alpha2))
        {
            lineRenderer.startColor = Color.red;
            lineRenderer.endColor = Color.red;

        }

        if (Input.GetKeyDown(KeyCode.Q))
        {
            if (colorIndex >= lineColors.Count)
            {
                colorIndex = 0;
            }

            lineRenderer.startColor = lineColors[colorIndex];
            lineRenderer.endColor = lineColors[colorIndex];
            colorIndex++;

        }


        if (Input.GetKeyDown(KeyCode.E))
        {


            if (curveIndex >= lineCurves.Count)
            {
                curveIndex = 0;
            }

            lineRenderer.widthCurve = lineCurves[curveIndex];
            curveIndex++;

        }
    }

    void CreateLine()
    {
   
        currentLine = Instantiate(linePrefab);

        lines.Add(currentLine);


        lineRenderer = currentLine.GetComponent<LineRenderer>();
        edgeCollider = currentLine.GetComponent<EdgeCollider2D>();
        lineRenderer.widthCurve = lineCurves[0];

        // mousePositions.Clear();
        // mousePositions.Add(Camera.main.ScreenToWorldPoint(Input.mousePosition));


        // mousePositions.Add(Camera.main.ScreenToWorldPoint(Input.mousePosition));
        // lineRenderer.SetPosition(0, mousePositions[0]);
        // lineRenderer.SetPosition(1, mousePositions[1]);
        // edgeCollider.points = mousePositions.ToArray();

    }


    void EndLine()
    {
        // if (mousePositions.Count <= 1)
        // {
        //     // print("太短了");
        //     Destroy(currentLine);
        // }

        if (hasCreateLine == true)
        {
       BoxCollider2D boxCollider2D = currentLine.AddComponent<BoxCollider2D>();
        boxCollider2D.isTrigger = true;
        }
 
        // print("OK");
        // isStartingDraw = false;
    }

    void UpdateLine(Vector2 mousePos)
    {
        if (hasCreateLine == false)
        {
      
            CreateLine();
            hasCreateLine = true;
                //   lineRenderer.positionCount = 0;
        }

        // isStartingDraw = true;
        if (Input.GetKey(KeyCode.LeftShift) || Input.GetKey(KeyCode.RightShift))
        {

            Vector2 direction = mousePos - mousePositions[0]; // Calculate direction vector

            if (Mathf.Abs(direction.x) > Mathf.Abs(direction.y))
            {

                mousePos = new Vector2(mousePos.x, mousePositions[0].y);
            }
            else
            {

                mousePos = new Vector2(mousePositions[0].x, mousePos.y);
            }
        }


        //默认
        
        // print(lineRenderer.positionCount);
        
        // mousePositions.Add(mousePos);
        // lineRenderer.positionCount++;
        
        // lineRenderer.SetPosition(lineRenderer.positionCount-1, mousePos);
        // edgeCollider.points = mousePositions.ToArray();



        //Catmull-Rom样条曲线
        mousePositions.Add(mousePos);
        if (mousePositions.Count < 4) return; // 需要至少4个点来开始创建Catmull-Rom样条曲线
        lineRenderer.positionCount = (mousePositions.Count - 3) * 10;
        for (int i = 0; i < mousePositions.Count - 3; i++)
        {
            for (int j = 0; j < 10; j++)
            {
                float t = j / 10f;
                Vector2 point = CalculateCatmullRomPoint(t, mousePositions[i], mousePositions[i + 1], mousePositions[i + 2], mousePositions[i + 3]);
                lineRenderer.SetPosition(i * 10 + j, point);
            }
        }
        edgeCollider.points = mousePositions.ToArray();



        //贝塞尔
        // mousePositions.Add(mousePos);
        // if (mousePositions.Count < 3) return; 

        // lineRenderer.positionCount = (mousePositions.Count - 2) * 10;

        // for (int i = 0; i < mousePositions.Count - 2; i++) {
        //     for (int j = 0; j < 10; j++) {
        //         float t = j / 10f;
        //         Vector2 point = CalculateBezierPoint(t, mousePositions[i], mousePositions[i + 1], mousePositions[i + 2]);
        //         lineRenderer.SetPosition(i * 10 + j, point);
        //     }
        // }
        // edgeCollider.points = mousePositions.ToArray();
    }


    void Undo()
    {
        if (lines.Count == 0)
            return;
        Destroy(lines[lines.Count - 1]);
        lines.RemoveAt(lines.Count - 1); // 删除最后一个元素

    }






    Vector3 CalculateBezierPoint(float t, Vector3 p0, Vector3 p1, Vector3 p2)
    {
        float u = 1 - t;
        float tt = t * t;
        float uu = u * u;

        Vector3 p = uu * p0; //term 1
        p += 2 * u * t * p1; //term 2
        p += tt * p2; //term 3

        return p;
    }

    Vector2 CalculateCatmullRomPoint(float t, Vector2 p0, Vector2 p1, Vector2 p2, Vector2 p3)
    {
        float t2 = t * t;
        float t3 = t2 * t;

        float b1 = -0.5f * t3 + t2 - 0.5f * t;
        float b2 = 1.5f * t3 - 2.5f * t2 + 1;
        float b3 = -1.5f * t3 + 2 * t2 + 0.5f * t;
        float b4 = 0.5f * t3 - 0.5f * t2;

        Vector2 point = b1 * p0 + b2 * p1 + b3 * p2 + b4 * p3;
        return point;
    }
}

```





```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LineMerge : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {

    }

    private void OnMouseDown() {
        // print(DrawLine.Instance.gameObject.name);
        DrawLine.Instance.lineRenderer = gameObject.GetComponent<LineRenderer>();
        print("ok");
        
    }

    private void OnTriggerEnter2D(Collider2D other)
    {
        LineMerge lineMerge = other.GetComponent<LineMerge>();
        if (lineMerge != null)
        {

            if (other.transform.parent == null)
            {
                GameObject newParent = new GameObject("一个对象喵");
                // newParent.AddComponent<RandomMovementLeftRight>();
                other.transform.parent = newParent.transform;
                this.transform.parent = newParent.transform;

            }
            else
            {
                this.transform.parent= other.transform.parent;
                Debug.Log("This object has a parent");
            }


            // 设置父对象

        }
    }
}

```





# 昼夜系统



```c#
using System.Collections;
using UnityEngine;
using UnityEngine.Rendering.Universal;


public class DayNightSystem : MonoBehaviour
{

    public enum TimeType 
    {
        Dawn,
        Day,
        Noon,
        Dusk,
        Night,
        Midnight

    }

    private TimeType[] timeTypes = new TimeType[] { TimeType.Dawn, TimeType.Day, TimeType.Noon, TimeType.Dusk, TimeType.Night, TimeType.Midnight };
    private int timeTypeIndex = 0;

    private TimeType lastTimeType;
    public TimeType timeType;


    public Light2D globalLight;
    public Light2D playerLight;

    private float duration = 2.0f;

    private bool isChanging = false;

    public Light2D[] lights;



    private float coolDown = 60.0f;
    private float timer = 0;
    //让所有灯的亮度变为0

    public void intensityOfAllLights(float value)
    {
        foreach (var light in lights)
        {
            light.intensity = value;
        }
    }


    // Start is called before the first frame update
    void Start()
    {
        timeType = TimeType.Day;
        lastTimeType = timeType;


        //changeTo(TimeType.Dawn);
    }

    // Update is called once per frame
    void Update()
    {

        //当按下F键的适合，切换一个timeType
        if (Input.GetKeyDown(KeyCode.F)  && isChanging ==false)
        {
            if (timeTypeIndex >= timeTypes.Length)
            {
                timeTypeIndex = 0;
                
            }
            timeType = timeTypes[timeTypeIndex];
            StartCoroutine(changeTo(timeTypes[timeTypeIndex]));
            timeTypeIndex++;
        }

        timer += Time.deltaTime;
        if (timer > coolDown && isChanging == false)
        {
            timer = 0;


            if (timeTypeIndex >= timeTypes.Length)
            {
                timeTypeIndex = 0;

            }
            timeType = timeTypes[timeTypeIndex];
            StartCoroutine(changeTo(timeTypes[timeTypeIndex]));
            timeTypeIndex++;

        }
    }

    IEnumerator changeTo(TimeType timeType)
    {
        isChanging = true;
        Color globalLightColor = Color.white;
        float globalIntensity = 0.8f;


        Color initGlobalLightColor = globalLight.color;
        float initGlobalIntensity = globalLight.intensity;


        Color playerLightColor = Color.white;
        float playerIntensity = 1.0f;
        float playerLightOuterRadius = 5.0f;


        Color initPlayerLightColor = playerLight.color;
        float initPlayerIntensity = playerLight.intensity;
        float initPlayerLightOuterRadius = playerLight.pointLightOuterRadius;


        switch (timeType)
        {
            case TimeType.Dawn:
                globalLightColor = new Color(255 / 255.0f, 236 / 255.0f, 165 / 255.0f);
                globalIntensity = 0.5f;

                playerLightColor = new Color(87 / 255.0f, 87 / 255.0f, 87 / 255.0f);
                playerIntensity = 1.0f;
                playerLightOuterRadius = 6.0f;
                intensityOfAllLights(0.7f);
                FindObjectOfType<GPTDialog>().EnvCheck("到黎明了");



                break;
            case TimeType.Day:
                globalLightColor = new Color(255 / 255.0f, 255 / 255.0f, 255 / 255.0f);
                globalIntensity = 1.1f;

                playerLightColor = new Color(255 / 255.0f, 255 / 255.0f, 255 / 255.0f);
                playerIntensity = 0f;
                playerLightOuterRadius = 6.0f;
                intensityOfAllLights(0.5f);
                FindObjectOfType<GPTDialog>().GetInfo("到白天了");


                break;
            case TimeType.Noon:
                globalLightColor = new Color(255 / 255.0f, 246 / 255.0f, 213 / 255.0f);
                globalIntensity = 1.3f;

                playerLightColor = new Color(255 / 255.0f, 255 / 255.0f, 255 / 255.0f);
                playerIntensity = 1.0f;
                playerLightOuterRadius = 6.0f;
                intensityOfAllLights(0f);
                FindObjectOfType<GPTDialog>().GetInfo("到正午了");


                break;
            case TimeType.Dusk:
                globalLightColor = new Color(255 / 255.0f, 109 / 255.0f, 217 / 255.0f);
                globalIntensity = 0.8f;

                playerLightColor = new Color(255 / 255.0f, 255 / 255.0f, 255 / 255.0f);
                playerIntensity = 0.5f;
                playerLightOuterRadius = 6.0f;
                intensityOfAllLights(0.5f);
                FindObjectOfType<GPTDialog>().GetInfo("到黄昏了");
;
                break;
            case TimeType.Night:
                globalLightColor = new Color(42 / 255.0f, 116 / 255.0f, 197 / 255.0f);
                globalIntensity = 0.5f;

                playerLightColor = new Color(248 / 255.0f, 241 / 255.0f, 188 / 255.0f);
                playerIntensity = 1.5f;
                playerLightOuterRadius = 3f;
                intensityOfAllLights(1f);
                FindObjectOfType<GPTDialog>().GetInfo("到晚上了");

                break;
            case TimeType.Midnight:
                globalLightColor = new Color(5 / 255.0f, 23 / 255.0f, 48 / 255.0f);
                globalIntensity = 0.3f;

                playerLightColor = new Color(224 / 255.0f, 224 / 255.0f, 224 / 255.0f);
                playerIntensity = 1.5f;
                playerLightOuterRadius = 3f;
                intensityOfAllLights(1.5f);
                FindObjectOfType<GPTDialog>().EnvCheck("到深夜了");

                break;
            default:
                break;

              
        }

        //print("渐变前");
        float timer = 0;

        while (timer < duration)
        {
            //print("渐变中");

            playerLight.pointLightOuterRadius = Mathf.Lerp(initPlayerLightOuterRadius, playerLightOuterRadius, timer / duration);
            playerLight.intensity = Mathf.Lerp(initPlayerIntensity, playerIntensity, timer / duration);
            playerLight.color = Color.Lerp(initPlayerLightColor, playerLightColor, timer / duration);
            globalLight.intensity = Mathf.Lerp(initGlobalIntensity, globalIntensity, timer / duration);
            globalLight.color = Color.Lerp(initGlobalLightColor, globalLightColor, timer / duration);

            timer += Time.deltaTime;
            yield return null;
        }
        //print("渐变结束");
        playerLight.pointLightOuterRadius = playerLightOuterRadius;
        playerLight.intensity = playerIntensity;
        playerLight.color = playerLightColor;

        isChanging = false;


    }

}
```





# GPT对话

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.Events;
using System;

/// <summary>
/// //////////////发送给ChatGPT的数据
/// </summary>

[Serializable]
public class PostData
{
    //使用哪一个ChatGPT的模型
    public string model;
    //发送给ChatGPT的消息。
    //如果发送的列表含有多条消息，则ChatGPT会根据上下文来回复。
    public List<PostDataBody> messages;
}


[Serializable]
public class PostDataBody
{
    //说话的角色
    public string role;
    //说话的内容
    public string content;

    public PostDataBody() { }
    public PostDataBody(string role, string content)
    {
        this.role = role;
        this.content = content;
    }

}


/////////////ChatGPT回复我们的数据
[Serializable]
public class RespondedData
{
    public string id;
    public string created;
    public string model;
    public List<RespondedChoice> choices;
}
[Serializable]
public class RespondedChoice
{
    public RespondedDataBody message;
    public string finish_reason;
    public int index;
}
[Serializable]
public class RespondedDataBody
{
    [TextArea]
    public string role;
    [TextArea]
    public string content;
}







public class GPTDialog : MonoBehaviour
{

    string chatGptUrl = "https://api.openai.com/v1/chat/completions";
    //使用的ChatGPT的模型
    string chatGptModel = "gpt-3.5-turbo";
    //使用的ChatGPT的API Key
    public string chatGptApiKey ;
    //AI人设的提示词
    [TextArea(5, 10)]
    public string aiRolePrompt = "一个可爱的猫猫";
    [TextArea(5, 10)]
    public string prompt = "你好";
    public List<PostDataBody> records;//聊天记录







    /// <summary>
    /// 发送请求
    /// </summary>

    IEnumerator SendPostDataCoroutine(PostData postData, UnityAction<string> callback)
    {
        //1创建一个UnityWebRequest类的对象用于发送网络话求。POST表示向服务器发送数据。using关键字用于在执行完这段语句之后释放这个UnityWebRequest类的对象。
        using (UnityWebRequest request = new UnityWebRequest(chatGptUrl, "POST"))
        {
            //把传输的消息的对象转换为JSON格式的字符串。
            string jsonString = JsonUtility.ToJson(postData);
            //把JSON格式的字符串转换为字节数组,以便进行网络传输。
            byte[] data = System.Text.Encoding.UTF8.GetBytes(jsonString);
            //设置要上传到远程服务器的主体数据。
            request.uploadHandler = (UploadHandler)new UploadHandlerRaw(data);

            //设置从远程服务器接收到的主体数据。
            request.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
            //设置HTTP网络请求的标头。表示这个网络请求的正文采用JSON格式进行编码。
            request.SetRequestHeader("Content-Type", "application/json");
            //设置HTTP网络请求的标头。这里的写法是按照OpenAI官方要求来写的。
            request.SetRequestHeader("Authorization", string.Format("Bearer {0}", chatGptApiKey));
            //等待ChatGPT回复。
            yield return request.SendWebRequest();

            if (request.responseCode == 200)
            {
            
                //获取ChatGPT回复的字符串，此时它是一个JSON格式的字符串。
                string respondedString = request.downloadHandler.text;
                //  print(respondedString);
                //将ChatGPT回复的JSON格式的字符串转换为指定的类的对象。
                RespondedData respondedMessages = JsonUtility.FromJson<RespondedData>(respondedString);
                // print(respondedMessages.choices);
                //如果ChatGPT有回复我们，则我们就挑第0条消息来显示。
                if (respondedMessages != null && respondedMessages.choices.Count >= 0)
                {
                    string respondedMessage = respondedMessages.choices[0].message.content;
                    callback?.Invoke(respondedMessage);
                }


            }


        }
    }


    /// <summary>
    /// 不连续的对话
    /// </summary>
    public void DiscontinuousDialog()
    {
        //构造要发送的数据
        PostData postData = new PostData()
        {

            //使用的ChatGPT的模型。
            model = chatGptModel,
            //要发送的消息。
            messages = new List<PostDataBody>()
                {
                    new PostDataBody("system",aiRolePrompt),
                    new PostDataBody("user", prompt)
                }
        };

        StartCoroutine(SendPostDataCoroutine(postData, (content) =>
        {
            print(content);
        }));

    }



    private void Start()
    {
        records.Add(new PostDataBody("system", aiRolePrompt));
    }
    public void ContinuousDialog()
    {
        records.Add(new PostDataBody("user", prompt));
        //构造要发送的数据
        PostData postData = new PostData()
        {
            model = chatGptModel,
            messages = records
        };

        StartCoroutine(SendPostDataCoroutine(postData, (content) =>
        {
            print(content);
            records.Add(new PostDataBody("assistant", content));
        }));


    }


    void Update()
    {

        if (Input.GetKeyDown(KeyCode.E))
        {
            ContinuousDialog();

        }

    }

}

```





# unity使用python



```c#
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using UnityEngine;

public class PythonCall : MonoBehaviour
{
    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            string[] arr = new string[2];
            arr[0] = "10";
            arr[1] = "24";
            RunPythonScript(arr);
            //UnityEngine.EventSystems.c
        }
    }
    private static void RunPythonScript(string[] argvs)
    {
        Process p = new Process();
        //python文件的路径
        string path = @"C:\Users\17966\Documents\temp\test.py";
        foreach (string temp in argvs)
        {
            path += " " + temp;
        }
        //python 环境的目录
        p.StartInfo.FileName = @"C:\Users\17966\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe";

        p.StartInfo.UseShellExecute = false;
        p.StartInfo.Arguments = path;
        p.StartInfo.RedirectStandardOutput = true;
        p.StartInfo.RedirectStandardError = true;
        p.StartInfo.RedirectStandardInput = true;
        p.StartInfo.CreateNoWindow = true;

        p.Start();
        p.BeginOutputReadLine();
        p.OutputDataReceived += new DataReceivedEventHandler(Get_data);
        p.WaitForExit();
    }
    private static void Get_data(object sender, DataReceivedEventArgs eventArgs)
    {
        if (!string.IsNullOrEmpty(eventArgs.Data))
        {
            print(eventArgs.Data);
        }
    }
}

```





```python
import sys

def a_plus_b(a,b):
    a = int(a)
    b = int(b)
    return a+b

print(a_plus_b(sys.argv[1],sys.argv[2]))

```







# 调整网格

```c#
using UnityEngine;
using UnityEngine.UI;

[RequireComponent(typeof(MeshFilter))]
public class VerticesModifier : MonoBehaviour
{

    public Vector2 v0 = new Vector3(-0.5f, -0.5f, 0);
    public Vector2 v1 = new Vector3(0.5f, -0.5f, 0);
    public Vector2 v2 = new Vector3(-0.5f, 0.5f, 0);
    public Vector2 v3 = new Vector3(0.5f, 0.5f, 0);


    public Vector2 videoV0 = new Vector2(1,1);
    public Vector2 videoV1 = new Vector2(1, 1);
    public Vector2 videoV2 = new Vector2(1, 1);
    public Vector2 videoV3 = new Vector2(1, 1);

    private void Start()
    {
        Mesh mesh = GetComponent<MeshFilter>().mesh;

 
        Vector3[] vertices = mesh.vertices;

        print(vertices[0]);
        print(vertices[1]);
        print(vertices[2]);
        print(vertices[3]);

    }
    void Update()
    {
    
        Mesh mesh = GetComponent<MeshFilter>().mesh;


        Vector3[] vertices = mesh.vertices;

        //print(vertices[0]);

        //vertices[0] = v0;
        //vertices[1] = v1;
        //vertices[2] = v2;
        //vertices[3] = v3;

        RawImage rawImage = GetComponent<RawImage>();
        Rect rect = rawImage.rectTransform.rect;
        vertices[0] = new Vector3(rect.xMin * videoV0.x, rect.yMin * videoV0.y, 0); 
        vertices[1] = new Vector3(rect.xMax * videoV1.x, rect.yMin * videoV1.y, 0); 
        vertices[2] = new Vector3(rect.xMin* videoV2.x, rect.yMax * videoV2.y, 0); 
        vertices[3] = new Vector3(rect.xMax* videoV3.x, rect.yMax * videoV3.y, 0); 
        //print(rawImage.canvasRenderer);

        // 应用Mesh到RawImage
        rawImage.canvasRenderer.SetMesh(mesh);

        mesh.vertices = vertices;
        mesh.RecalculateBounds();
    }
}
```





灯光闪烁

```
public class LightFork : MonoBehaviour
{
    public float minIntensity = 0f; // 灯光的最小强度
    public float maxIntensity = 1f; // 灯光的最大强度
    public float flickerSpeed = 0.07f; // 灯光闪烁的速度

    private UnityEngine.Rendering.Universal.Light2D lightSource; 
    private float randomizer; 

    void Start()
    {
        lightSource = GetComponent<UnityEngine.Rendering.Universal.Light2D>(); // 获取灯光组件
    }

    void Update()
    {
        // 使用Perlin噪声函数来随机化闪烁的强度
        randomizer = Random.Range(0.0f, 1.0f);
        float noise = Mathf.PerlinNoise(randomizer, Time.time * flickerSpeed);
        lightSource.intensity = Mathf.Lerp(minIntensity, maxIntensity, noise);
    }
}

```



# 场景缩放

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

[Serializable]
public class ScaleObj
{
    public Transform objTransform;
    public Vector3 originScale;
}



//只需要给objTransform赋值即可，originScale会自动读取
public class ScenePerspective : MonoBehaviour
{
    public Transform firstChildObject;
    public Transform secondChildObject;
    public Transform thirdChildObject;
    public ScaleObj[] objs;

    private float scaleSize1;
    private float scaleSize2;
    private float scaleSize3;

    private Vector3 intersect;//玩家和直线的垂线的交点

    //DEBUG用
    public float dist1;
    public float dist2;
    public float dist3;

    public float scaleSize;



    //控制玩家移动速度
    private float playerSpeed;

    private DemoCharacterController playerController;

    // Start is called before the first frame update
    void Start()
    {
        scaleSize1 = firstChildObject.gameObject.GetComponent<ScalePointSize>().scaleSize;
        scaleSize2 = secondChildObject.gameObject.GetComponent<ScalePointSize>().scaleSize;
        if (thirdChildObject != null)
        {
            scaleSize3 = thirdChildObject.gameObject.GetComponent<ScalePointSize>().scaleSize;
        }


        foreach (ScaleObj scaleObj in objs)
        {
            scaleObj.originScale = scaleObj.objTransform.localScale;

            if (scaleObj.objTransform.gameObject.GetComponent<DemoCharacterController>() != null)
            {
                playerController = scaleObj.objTransform.gameObject.GetComponent<DemoCharacterController>();
                playerSpeed = playerController.speed;
            }

        }
    }



    // Update is called once per frame
    void Update()
    {

        //如果只有两个点，进入直线的模式
        if (thirdChildObject == null)
        {

            foreach (ScaleObj t in objs)
            {
                //  两点缩放(t);
            }
        }
        else
        {



            foreach (ScaleObj t in objs)
            {
                //如果有三个点，进入曲线的模式
                三点缩放(t);


            }


        }







        // Interpolate the scale based on the closest point found
        // float scale = Mathf.Lerp(scale0, scale2, closestT);

        // Apply the scale to the player
        // playerObj.localScale = new Vector3(scale, scale, scale);



    }



    // void  两点缩放( Transform playerObj)
    // {


    //      //当有两条线的时候
    //         Vector3 start = firstChildObject.position;
    //         Vector3 end = secondChildObject.position;
    //         //计算玩家到直线的垂线
    //         Vector3 dir = (end - start).normalized;

    //         Vector3 vec = playerObj.position - start;
    //         float t = Vector3.Dot(vec, dir);
    //         intersect = start + t * dir;



    //         //判断点是否在在线段内
    //         dist1 = Vector3.Distance(intersect, firstChildObject.position);
    //         dist2 = Vector3.Distance(intersect, secondChildObject.position);

    //         dist3 = Vector3.Distance(firstChildObject.position, secondChildObject.position);

    //         if (Mathf.Abs(dist1 + dist2 - dist3) < 0.1f)
    //         {
    //             Debug.Log("点在线内");

    //             float proportion = dist1 / dist3;


    //             scaleSize = Mathf.Lerp(scaleSize1, scaleSize2, proportion);
    //             // print(playerObj.localScale.x);
    //             playerObj.localScale = new Vector3(playerObj.localScale.x*scaleSize, playerObj.localScale.y*scaleSize, playerObj.localScale.z*scaleSize);

    //         }
    //         else
    //         {
    //             Debug.Log("点在线外");
    //         }

    // }


    void 三点缩放(ScaleObj playerObj)
    {


        float playerT = TFromPointToBezier(playerObj.objTransform.position);
        float point1T = 0;
        float point2T = TFromPointToBezier(secondChildObject.position);
        float point3T = 1;
        // print(point2T);
        if (playerT < point2T)
        {
            float proportion = playerT / point2T;
            scaleSize = Mathf.Lerp(scaleSize1, scaleSize2, proportion);
        }
        else
        {

            float proportion = (playerT - point2T) / (1 - point2T);
            scaleSize = Mathf.Lerp(scaleSize2, scaleSize3, proportion);
        }

        playerObj.objTransform.localScale = new Vector3(playerObj.originScale.x * scaleSize, playerObj.originScale.y * scaleSize, playerObj.originScale.z * scaleSize);

        playerController.speed = playerSpeed *scaleSize;
        


    }

    void OnDrawGizmos()
    {
        //绘制两点之间的线段
        Gizmos.color = Color.red;

        Gizmos.DrawLine(firstChildObject.position, secondChildObject.position);

        // Gizmos.DrawLine(playerObj.position, intersect);
        if (thirdChildObject == null)
        {
            return;
        }


        //绘制贝塞尔曲线
        // Transform point0, point1, point2;
        Gizmos.color = Color.white;
        for (float t = 0; t <= 1; t += 0.05f)
        {
            Vector3 p = CalculateBezierPoint(t, firstChildObject.position, secondChildObject.position, thirdChildObject.position);
            Gizmos.DrawSphere(p, 0.1f);
        }
        // float closestT = TFromPointToBezier(playerObj.position);

        // Gizmos.DrawLine(playerObj.position, CalculateBezierPoint(closestT, firstChildObject.position, secondChildObject.position, thirdChildObject.position));



    }

    //计算一个点到贝塞尔的最近点的T
    float TFromPointToBezier(Vector3 point)
    {
        float closestT = 0;
        float closestDistance = float.MaxValue;

        // Sample points along the bezier curve and find the closest to the player
        for (float t = 0; t <= 1; t += 0.01f)
        {
            Vector3 p = CalculateBezierPoint(t, firstChildObject.position, secondChildObject.position, thirdChildObject.position);
            float distance = Vector3.Distance(point, p);
            if (distance < closestDistance)
            {
                closestDistance = distance;
                closestT = t;
            }
        }
        return closestT;
    }



    Vector3 CalculateBezierPoint(float t, Vector3 p0, Vector3 p1, Vector3 p2)
    {
        float u = 1 - t;
        float tt = t * t;
        float uu = u * u;

        Vector3 p = uu * p0; //term 1
        p += 2 * u * t * p1; //term 2
        p += tt * p2; //term 3

        return p;
    }
}

```



```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ScalePointSize : MonoBehaviour
{
    public float scaleSize=1.0f;
   
}

```

![image-20231225132543813](C:\Users\17966\AppData\Roaming\Typora\typora-user-images\image-20231225132543813.png)









# NPC行为

```
using Crosstales;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using TMPro;
using UnityEngine;
using UnityEngine.InputSystem.EnhancedTouch;
using static GPTDialog;
using static UnityEditor.ShaderGraph.Internal.KeywordDependentCollection;


//NPC的需求值，值越低，越需要满足
[ExecuteInEditMode]
[Serializable]
public class NPCDemandValue
{
    //饥饿值
    public float  hungerLevel;
    public float HungerLevel
    {
        get
        {
            return hungerLevel;
        }
        set
        {
            hungerLevel = value;
        }
    }
    public AnimationCurve hungerCurve = AnimationCurve.EaseInOut(100, 100, 0, 0);

    //疲劳值
    public float tirednessLevel;
    public float TirednessLevel
    {
        get
        {
            return tirednessLevel;
        }
        set
        {
            tirednessLevel = value;
        }
    }

    public AnimationCurve tirednessCurve = AnimationCurve.EaseInOut(100, 100, 0, 0);

    //娱乐值
    public float funLevel;
    public float FunLevel
    {
        get
        {
            return funLevel;
        }
        set
        {
            funLevel = value;
        }
    }
    public AnimationCurve funCurve = AnimationCurve.EaseInOut(100, 100, 0, 0);


    public NPCDemandValue(int hungerLevel=50, int tirednessLevel = 100, int funLevel = 50)
    {
        this.hungerLevel = hungerLevel;
        this.tirednessLevel = tirednessLevel;
        this.funLevel = funLevel;
    }

    public void DailyCost()
    {
        hungerLevel = Mathf.Clamp(hungerLevel- 0.01f, 0, 100);
        tirednessLevel = Mathf.Clamp(tirednessLevel - 0.003f, 0, 100);
        funLevel = Mathf.Clamp(funLevel - 0.006f, 0, 100);
    }
    //获得饥饿值的权重
    public float GetWeightHunger()
    {
        return hungerCurve.Evaluate(hungerLevel);
    }

    //获得疲劳值的权重
    public float GetWeightTiredness()
    {
        return tirednessCurve.Evaluate(tirednessLevel);
    }

    //获得娱乐值的权重
    public float GetWeightFun()
    {
        return funCurve.Evaluate(funLevel);
    }

    //计算当前最想干什么
    public string WhattToDO()
    {
        SortedList<string, float> sortedList = new SortedList<string, float>();
        sortedList["吃"] = GetWeightHunger();
        sortedList["睡"] = GetWeightTiredness();
        sortedList["玩"] = GetWeightFun();
        //从大到小排序权重
        var temp = sortedList.OrderByDescending(x=>x.Value);

        //foreach (KeyValuePair<string, float> action in temp)
        //{
        //    Debug.Log("action: " + action.Key + ", value: " + action.Value);
        //}
        return temp.First().Key;
    }

    //回复值
    public void Recover(string action)
    {
        if (action == "吃")
        {
            hungerLevel = Mathf.Clamp(hungerLevel+0.1f,0,100);

        }
        else if (action == "睡")
        {
            tirednessLevel  = Mathf.Clamp(tirednessLevel + 0.05f, 0, 100);
        }
        else if (action == "玩")
        {
            funLevel  = Mathf.Clamp(funLevel + 0.1f, 0, 100);
        }
    }
}


public enum ActionType
{
    Daily,
    Realtime
}






public class NPCBehavior : MonoBehaviour
{
    [SerializeField]
    public NPCDemandValue npcDemandValue = new NPCDemandValue(10, 10, 10);

    public TMP_Text emojiText;
    private Rigidbody2D rb;
    private Dictionary<GameObject, string> objFeelDic = new Dictionary<GameObject, string>();

    private EnvCheck envChecks;

    public string action;

    public GameObject targetObj;

    private GPTDialog GPTDialog;

    //检测周期的float变量
    private float actionCoolTime = 3;
    private float actionTimer = 0;
    public bool canAction = true;

    private float dailyActionCoolTime = 10;
    public float dailyActionTimer = 20;
    public bool canDailyAction = true;



    public ActionType actoinType = ActionType.Daily;


    public float distance = 3.0f;
    public GameObject player;


    //指的是当前正在做的日常行为
    public string nowDailyAction = "";

    private AnimationScript anim;

    private void UpdateAction()
    { 
        actionTimer += Time.deltaTime;
        if (actionTimer >= actionCoolTime)
        {
            actionTimer = actionCoolTime+1;
            canAction = true;
        }
        else
        {
            canAction = false;
        }
    }

    private void UpdateDailyAction()
    { 
        dailyActionTimer += Time.deltaTime;
        if (dailyActionTimer >= dailyActionCoolTime)
        {
            dailyActionTimer = dailyActionCoolTime+1;
            canDailyAction = true;
        }
        else
        {
            canDailyAction = false;
        }
    }

    private void Start()
    {
        envChecks = GetComponentInChildren<EnvCheck>();
        rb = GetComponent<Rigidbody2D>();
        anim = GetComponentInChildren<AnimationScript>();

        //初始化的时候，加入玩家
        usefulDic.Add(player, "玩,睡");
    }
    private void Update()
    {
        UpdateAction();
        UpdateDailyAction();
        npcDemandValue.DailyCost();
        DoDailyAction();

       


        if (actoinType == ActionType.Daily)
        {
            if (targetObj == null)
            {
                return;
            }
            //靠近对方
            var dis = Vector2.Distance(transform.position, targetObj.transform.position);
            if (dis < distance)
            {

                switch (nowDailyAction)
                {
                    case "吃":
                        emojiText.text = "(^～^)嚼！";
                        break;
                    case "睡":
                        emojiText.text = "zZZ~";
                        break;
                    case "玩":
                        emojiText.text = "玩耍喵~~";
                        break;
                }
                anim.SetHorizontalMovement(0, 0, rb.velocity.y);
                //只有靠近了才会回复日常的值
                npcDemandValue.Recover(nowDailyAction);
                return;
            }
            else
            {
                emojiText.text = "";
                Vector2 dir = new Vector2(0, 0);
                if (targetObj != null)
                {
                    dir = (targetObj.transform.position - transform.position).normalized;
                }


                anim.SetHorizontalMovement(dir.x, dir.y, rb.velocity.y);
                if (dir.x > 0)
                {
                    anim.Flip(1);
                }
                if (dir.x < 0)
                {
                    anim.Flip(-1);
                }


                transform.Translate(dir * Time.deltaTime * 5.0f);
            }
        }
        else if (actoinType == ActionType.Realtime)
        {
            actoinType = ActionType.Daily;
            targetObj = null;
        }
    }

    public void DoAction()
    {
        //print("当前操作为：" + action);


    
        GameObject obj;
        obj = player;
        //if (envChecks.objectsInTrigger.Count == 0)
        //{
        //    obj = envChecks.lastObj;

        //}
        //else
        //{
        //    obj = envChecks.objectsInTrigger[0];
        //}


        if (action == "远离")
        {
            //isChase = false;
            //对方在右边
            Escape(obj);

        }
        else if (action == "靠近")
        {
            //对方在右边
            if (transform.position.x <= obj.transform.position.x)
            {

                rb.AddForce(Vector2.right * speed);
            }
            //在左边
            else if (transform.position.x > obj.transform.position.x)
            {
                rb.AddForce(Vector2.left * speed);

            }
            rb.AddForce(Vector2.left * speed);
        }
        else if (action == "保持不动")
        {
            //isChase = false;
        }
        else if (action == "高兴")
        {
            StartCoroutine(Jump());
        }
        else if (action == "左右看")
        {
            StartCoroutine(Wander());
        }
        else if (action == "追逐")
        {
            targetObj = obj;
            //isChase = true;
            //StartCoroutine(Chase());

        }
    }

    //当NPC遇到一个即时事件，会执行一个action
    public void DoAction(GameObject gameObject)
    {
        if (canAction == false)
        {
            actionTimer = 0;
            return;

        }
        //处理情绪
        objFeelDic.TryGetValue(gameObject, out string feel);
        if (feel == "高兴")
        {
            StartCoroutine(ShowEmoji("😊"));
            StartCoroutine(Jump());
        }
        else if (feel == "恐惧")
        {
            StartCoroutine(ShowEmoji("☹️"));
            //actoinType = ActionType.Realtime;
            Escape(gameObject);
            //actoinType = ActionType.Daily;
        }
        else //"没有感觉"
        {
            StartCoroutine(ShowEmoji("😒"));
            StartCoroutine(Wander());
        }
    }


    //当NPC第一次遇到一个物体的时候，会记录NPC对这个物体的感觉
    public void ProcessFirstFeel(string feel,GameObject obj)
    {
        //print(feel);
        if (feel.Contains("高兴"))
        {
            objFeelDic.Add(obj, "高兴");
        }
        else if (feel.Contains("恐惧"))
        {
            objFeelDic.Add(obj, "恐惧");
        }
        else if (feel.Contains("没有感觉"))
        {

            objFeelDic.Add(obj, "没有感觉");
        }
        DoAction(obj);
    }

    Dictionary<GameObject,string> usefulDic= new Dictionary<GameObject, string>();

    //当NPC第一次遇到一个物体的时候，会记录这个物体的用处
    public void ProcessFirstUseful( GameObject obj, string useful)
    {

        //如果这个玩意让自己害怕就不会去用
        objFeelDic.TryGetValue(obj, out string feel);
        if (feel == "恐惧")
        {
            return;
        }
       

        print(useful);
        if (useful.Contains("睡"))
        {
            usefulDic.Add(obj, "睡");
        }
        else if (useful.Contains("吃"))
        {
            usefulDic.Add(obj, "吃");
        }
        else if (useful.Contains("玩"))
        {
            usefulDic.Add(obj, "玩");
        }
    }


    IEnumerator ShowEmoji(string emoji)
    {
        emojiText.text = emoji;

        yield return new WaitForSeconds(3);

        emojiText.text = "";
    }


    public void DoDailyAction()
    {

        if (canDailyAction == false)
        {
            
            return;
        }
        print("执行日常");

        dailyActionTimer = 0;
        string whatToDo = npcDemandValue.WhattToDO();
        List<GameObject> playObjects = usefulDic.Where(pair => pair.Value.Contains(whatToDo)).Select(pair => pair.Key).ToList();
        print(playObjects.Count);
        if (playObjects.Count == 0)
        {
            return;
        }
        //如果当前正在做的日常行为和即将做的日常行为一样，就不做了
        //if (nowDailyAction == whatToDo)
        //{

        //    return;
        //}
        

        nowDailyAction = whatToDo;


        int index = UnityEngine.Random.Range(0, playObjects.Count);
        //追逐这个物体
        targetObj = playObjects[index];
        //GPTDialog.GetInfo("过了一会。你现在打算去" + envChecks.rememberedObjs[index] + "那里");
    }





    //情绪的表达
    IEnumerator Jump()
    {
        rb.AddForce(Vector2.up * speed);
        yield return new WaitForSeconds(0.5f);
        rb.AddForce(Vector2.up * speed);
        yield return new WaitForSeconds(0.5f);
    }
    IEnumerator Wander()
    {
        transform.localEulerAngles = new Vector3(0, 180, 0);
        yield return new WaitForSeconds(0.5f);
        transform.localEulerAngles = new Vector3(0, 0, 0);
        yield return new WaitForSeconds(0.5f);
        transform.localEulerAngles = new Vector3(0, 180, 0);
        yield return new WaitForSeconds(0.5f);
        transform.localEulerAngles = new Vector3(0, 0, 0);
        yield return new WaitForSeconds(0.5f);

    }


    float speed = 500.0f;


    //逃走,逃离
    public void Escape(GameObject target)
    {
        if (transform.position.x <= target.transform.position.x)
        {

            rb.AddForce(Vector2.left * speed*2);
        }
        //在左边
        else if (transform.position.x > target.transform.position.x)
        {
            rb.AddForce(Vector2.right * speed*2);

        }
    }



}

```

# 对话新



```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.Events;
using System;

/// <summary>
/// //////////////发送给ChatGPT的数据
/// </summary>

[Serializable]
public class PostData
{
    //使用哪一个ChatGPT的模型
    public string model;
    //发送给ChatGPT的消息。
    //如果发送的列表含有多条消息，则ChatGPT会根据上下文来回复。
    public List<PostDataBody> messages;
}


[Serializable]
public class PostDataBody
{
    //说话的角色
    public string role;
    //说话的内容
    public string content;

    public PostDataBody() { }
    public PostDataBody(string role, string content)
    {
        this.role = role;
        this.content = content;
    }

}


/////////////ChatGPT回复我们的数据
[Serializable]
public class RespondedData
{
    public string id;
    public string created;
    public string model;
    public List<RespondedChoice> choices;
}
[Serializable]
public class RespondedChoice
{
    public RespondedDataBody message;
    public string finish_reason;
    public int index;
}
[Serializable]
public class RespondedDataBody
{
    [TextArea]
    public string role;
    [TextArea]
    public string content;
}







public class GPTDialog : MonoBehaviour
{

    string chatGptUrl = "https://api.openai.com/v1/chat/completions";
    //使用的ChatGPT的模型
    string chatGptModel = "gpt-3.5-turbo";
    //使用的ChatGPT的API Key
    public string chatGptApiKey ;
    //AI人设的提示词
    [TextArea(5, 10)]
    public string aiRolePrompt = "一个可爱的猫猫";
    [TextArea(5, 10)]
    public string prompt = "你好";
    public List<PostDataBody> records;//聊天记录







    /// <summary>
    /// 发送请求
    /// </summary>

    IEnumerator SendPostDataCoroutine(PostData postData, UnityAction<string> callback)
    {
        //1创建一个UnityWebRequest类的对象用于发送网络话求。POST表示向服务器发送数据。using关键字用于在执行完这段语句之后释放这个UnityWebRequest类的对象。
        using (UnityWebRequest request = new UnityWebRequest(chatGptUrl, "POST"))
        {
            //把传输的消息的对象转换为JSON格式的字符串。
            string jsonString = JsonUtility.ToJson(postData);
            //把JSON格式的字符串转换为字节数组,以便进行网络传输。
            byte[] data = System.Text.Encoding.UTF8.GetBytes(jsonString);
            //设置要上传到远程服务器的主体数据。
            request.uploadHandler = (UploadHandler)new UploadHandlerRaw(data);

            //设置从远程服务器接收到的主体数据。
            request.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
            //设置HTTP网络请求的标头。表示这个网络请求的正文采用JSON格式进行编码。
            request.SetRequestHeader("Content-Type", "application/json");
            //设置HTTP网络请求的标头。这里的写法是按照OpenAI官方要求来写的。
            request.SetRequestHeader("Authorization", string.Format("Bearer {0}", chatGptApiKey));
            //等待ChatGPT回复。
            yield return request.SendWebRequest();

            if (request.responseCode == 200)
            {
            
                //获取ChatGPT回复的字符串，此时它是一个JSON格式的字符串。
                string respondedString = request.downloadHandler.text;
                //  print(respondedString);
                //将ChatGPT回复的JSON格式的字符串转换为指定的类的对象。
                RespondedData respondedMessages = JsonUtility.FromJson<RespondedData>(respondedString);
                // print(respondedMessages.choices);
                //如果ChatGPT有回复我们，则我们就挑第0条消息来显示。
                if (respondedMessages != null && respondedMessages.choices.Count >= 0)
                {
                    string respondedMessage = respondedMessages.choices[0].message.content;
                    callback?.Invoke(respondedMessage);
                }


            }


        }
    }


    /// <summary>
    /// 不连续的对话
    /// </summary>
    public void DiscontinuousDialog()
    {
        //构造要发送的数据
        PostData postData = new PostData()
        {

            //使用的ChatGPT的模型。
            model = chatGptModel,
            //要发送的消息。
            messages = new List<PostDataBody>()
                {
                    new PostDataBody("system",aiRolePrompt),
                    new PostDataBody("user", prompt)
                }
        };

        StartCoroutine(SendPostDataCoroutine(postData, (content) =>
        {
            print(content);
        }));

    }



    private void Start()
    {
        records.Add(new PostDataBody("system", aiRolePrompt));
    }
    public void ContinuousDialog()
    {
        records.Add(new PostDataBody("user", prompt));
        //构造要发送的数据
        PostData postData = new PostData()
        {
            model = chatGptModel,
            messages = records
        };

        StartCoroutine(SendPostDataCoroutine(postData, (content) =>
        {
            print(content);
            records.Add(new PostDataBody("assistant", content));
        }));


    }


    void Update()
    {

        if (Input.GetKeyDown(KeyCode.E))
        {
            ContinuousDialog();

        }

    }

}

```





# 跨窗口通信



```c#
using System.IO.MemoryMappedFiles;
using System.Text;
using UnityEngine;

public class MemoryMappedServer : MonoBehaviour
{
    void Start()
    {
        
        MemoryMappedFile mmf = MemoryMappedFile.CreateNew("sharedMemory", 1024);
        using (var stream = mmf.CreateViewStream())
        {
            byte[] message = Encoding.ASCII.GetBytes("Hello from Server");
            stream.Write(message, 0, message.Length);
        }
    }
}
```




```c#
using System.IO.MemoryMappedFiles;
using System.Text;
using UnityEngine;
using System.IO;

using TMPro;

public class SharedMemoryManager : MonoBehaviour
{
    private MemoryMappedFile mmf;
    private const string sharedMemoryName = "sharedMemory";
    private const int memorySize = 1024;


    public TMP_Text mP_Text;

    // 尝试打开现有的共享内存
    void Start()
    {
        

        try
        {
            // 尝试打开已经存在的共享内存
            mmf = MemoryMappedFile.OpenExisting(sharedMemoryName);
            Debug.Log("Shared memory exists, reading from it.");
            ReadSharedMemory();
        }
        catch (FileNotFoundException)
        {
            // 如果没有找到共享内存，创建新的
            Debug.Log("Shared memory not found, creating new one.");
            mmf = MemoryMappedFile.CreateNew(sharedMemoryName, memorySize);
            WriteToSharedMemory("Hello from new instance");
        }
    }

    // 从共享内存读取数据
    void ReadSharedMemory()
    {
        using (var stream = mmf.CreateViewStream())
        {
            byte[] buffer = new byte[memorySize];
            stream.Read(buffer, 0, buffer.Length);
            string message = Encoding.ASCII.GetString(buffer).TrimEnd('\0');
            //Debug.Log("Read from shared memory: " + message);
            mP_Text.text = message;
        }
    }

    // 写入数据到共享内存
    void WriteToSharedMemory(string message)
    {
        using (var stream = mmf.CreateViewStream())
        {
            byte[] buffer = Encoding.ASCII.GetBytes(message);
            stream.Write(buffer, 0, buffer.Length);
        }
    }

    // 释放共享内存
    void OnDestroy()
    {
        if (mmf != null)
        {
            mmf.Dispose();
        }
    }
}
```




 
```c#
using System.IO.MemoryMappedFiles;
using System.Text;
using UnityEngine;

public class MemoryMappedClient : MonoBehaviour
{
    void Start()
    {
        MemoryMappedFile mmf = MemoryMappedFile.OpenExisting("sharedMemory");
        using (var stream = mmf.CreateViewStream())
        {
            byte[] buffer = new byte[1024];
            stream.Read(buffer, 0, buffer.Length);
            Debug.Log(Encoding.ASCII.GetString(buffer));
        }
    }
}
```



# 多语言基本框架
```c#

using UnityEngine;
using UnityEngine.Localization.Settings;
using UnityEngine.Localization.Tables;
using UnityEngine.Localization;
using UnityEngine.ResourceManagement.AsyncOperations;
using System;

public enum TableType
{
    UI,//这里指代所有的静态文本
    Story,//指代所有的剧情和物体描述相关文本
    InnerWorld1,//世界1的ai文本
    InnerWorld2,//世界2的ai文本
}


public class LocalizationManager : Singleton<LocalizationManager>
{
    private StringTable tableUI;          //代码本地化表
    private StringTable tableStory;
    private StringTable tableInnerWorld1;
    private StringTable tableInnerWorld2;
    

    void Start()
    {
        if (LocalizationSettings.AvailableLocales.Locales.Count > 0)
        {
            GetLocalizationTable();
        }
        else
        {
            LocalizationSettings.InitializationOperation.Completed += OnLocalizationInitialized;
        }
        LocalizationSettings.SelectedLocaleChanged += OnLocaleChanged;
    }

    protected override void OnDestroy()
    {
        base.OnDestroy();
        LocalizationSettings.SelectedLocaleChanged -= OnLocaleChanged;
    }

    /// <summary>
    /// 本地化初始化完成
    /// </summary>
    private void OnLocalizationInitialized(AsyncOperationHandle<LocalizationSettings> handle)
    {
        if (handle.Status == AsyncOperationStatus.Succeeded)
        {
            Debug.Log("Localization initialized successfully!");
            GetLocalizationTable();
        }
        else
        {
            Debug.LogError("Localization initialization failed.");
        }
    }

    /// <summary>
    /// 切换语言
    /// </summary>
    public void OnLocaleChanged(Locale newLocale)
    {
        print("切换语言："+newLocale.Identifier.Code);
        LocalizationSettings.SelectedLocale = newLocale;
        GetLocalizationTable();
    }

    /// <summary>
    /// 获取本地化表
    /// </summary>
    public void GetLocalizationTable()
    {
        tableUI = LocalizationSettings.StringDatabase.GetTable("TableUI");

        tableStory = LocalizationSettings.StringDatabase.GetTable("TableStory");

        tableInnerWorld1 = LocalizationSettings.StringDatabase.GetTable("TableInnerWorld1");
        tableInnerWorld2 = LocalizationSettings.StringDatabase.GetTable("TableInnerWorld2");

        //Debug.LogWarning(ScriptStringTable.GetEntry("CommonTip_NoItem").GetLocalizedString());
    }

    /// <summary>
    /// 获取本地化文本
    /// </summary>
    public string GetLocalizedString(string key,TableType tableType)
    {
        try
        {
            if (tableType == TableType.UI)
            {
                return tableUI.GetEntry(key).GetLocalizedString();
            }
            else if (tableType == TableType.Story)
            {
                return tableStory.GetEntry(key).GetLocalizedString();
            }
            else if (tableType == TableType.InnerWorld1)
            {
                return tableInnerWorld1.GetEntry(key).GetLocalizedString();
            }
            else if (tableType == TableType.InnerWorld2)
            {
                return tableInnerWorld2.GetEntry(key).GetLocalizedString();
            }
            else
            {
                return null;
            }
        } catch (Exception e)
        {
            Debug.LogException(e);
            print($"{key} 有问题");
            return null;
        }

    }
}


```



# 鼠标拖动

## 鼠标中键控制画面（2D）

直接拖到摄像机上即可

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/// <summary>
/// 用于2D游戏中鼠标中键控制画面移动和缩放
/// </summary>
public class ViewController : MonoBehaviour
{
    Vector3 lastMousePosition;
    Vector3 nowMousePosition;
    bool isMouseDown;

    private Camera camera;

    void Start()
    {
        isMouseDown = false;
        camera = GetComponent<Camera>();
    }

    void Update()
    {
        if (Input.GetMouseButtonDown(2))
        {
            isMouseDown = true;
        }
        if (Input.GetMouseButtonUp(2))
        {
            isMouseDown = false;
            lastMousePosition = Vector3.zero;
        }
        if (isMouseDown)
        {
            nowMousePosition = Input.mousePosition;

            if (lastMousePosition != Vector3.zero)
            {
                Vector3 offset = nowMousePosition - lastMousePosition;
                transform.position = transform.position - offset * 0.05f;


            }
            lastMousePosition = nowMousePosition;
          
        }
        float m = Input.GetAxis("Mouse ScrollWheel");
        camera.orthographicSize += -m;

    }
}

```



## 鼠标中键拖动画面（3D）

直接挂载到摄像机上面即可

```c#
        if (Input.GetMouseButtonDown(2))
        {
            isMouseDown = true;
        }
        if (Input.GetMouseButtonUp(2))
        {
            isMouseDown = false;
            lastMousePosition = Vector3.zero;
        }
        if (isMouseDown)
        {
            nowMousePosition = Input.mousePosition;
      
            if (lastMousePosition != Vector3.zero)
            {
                Vector3 offset = nowMousePosition - lastMousePosition;
                //  print("offset:  " + offset);
                float temp;
                temp = offset.y;
                offset.y = offset.z;
                offset.z = temp;
                transform.position = transform.position - offset * 0.05f;

                // print("相机位置:  "+transform.position);

            }
            lastMousePosition = nowMousePosition;
            //lastMousePosition = Camera.main.ScreenToWorldPoint(Input.mousePosition);   //世界坐标系转换为屏幕坐标系
        }
    
```











# 物体的移动

Space.Self是指沿着自己的坐标系运动

```c#
 transform.Translate(0, 0.01f, 0,Space.Self);//自身坐标系
 transform.Translate(0, 0.01f, 0,Space.World);//世界坐标系
//或者
this.transform.Translate(0, 0.01f, 0);
```



## 匀速运动 

如果执行时间短，那么走得近，时间长走得远 

```c#
float step = 0.01f * Time.deltaTime;
transform.Translate(0, step, 0,Space.Self);
```

## 掉头运动

```c#
if (transform.position.y > 5) 
{
    transform.localEulerAngles = new Vector3(0, 0, 180);
}
if (transform.position.y < -5)
{
    transform.localEulerAngles = new Vector3(0, 0, 0);
}
float step = 10.0f * Time.deltaTime;
transform.Translate(0, step, 0, Space.Self);
```

## 转向某个物体 

```c#
//获取自身到目标对象的方向向量
Vector3 direction = GameObject.Find("target").transform.position-this.transform.position;

//计算自身方向转到这个方向需要多少角度
float degree = Vector3.SignedAngle(this.transform.up, direction,Vector3.forward);

//将自身角度转过去
this.transform.Rotate(0, 0, degree);
```








# 人物控制器
## 2D刚体

使用刚体移动

```c#
 void Update()
    {
     
     //其中，`transform.position`是玩家自身的位置，targetPosition是目标位置，后面那个是插值，也就是每次移动多少。moveSmooth可以设置为100


        rigid.MovePosition(Vector2.Lerp(transform.position, targetPosition, moveSmooth * Time.deltaTime));


        float x=  Input.GetAxisRaw("Horizontal");
        float y = Input.GetAxisRaw("Vertical");

        if (x != 0 || y != 0) {

            //射线检测
            collider.enabled = false;
            RaycastHit2D hitTest = Physics2D.Linecast(targetPosition,targetPosition+new Vector2(x,y));
            collider.enabled = true;

            if (hitTest.transform == null)
            {
                targetPosition += new Vector2(x, y);
            }
            else {
                switch (hitTest.collider.tag)
                {
                    case "fence":
                        hitTest.collider.SendMessage("getDamage");
                        animator.SetTrigger("attack");
                        break;
                    case "wall":

                        break;
                    case "food":
                        targetPosition += new Vector2(x, y);
                        break;
                }
            }
            freezingTime = 0;



            //敌人行动
            //GameObject.Find("Enemy1(Clone)").SendMessage("Action");
            GameObject[] enemys = GameObject.FindGameObjectsWithTag("enemy");
            foreach (GameObject enemy in enemys) { 
                enemy.SendMessage("Action");
            }
        }
    }
```











## 2D横板跳跃

1. 给底下木板设置刚体和碰撞器

2. 人物设置刚体和碰撞器

3. 代码

   ```c#
   public float jumpForce;
   private void Update()
   {
       if(Input.GetMouseButtonDown(0))
       {
           GetConent<Rigidbody2D>().velocity = Vector2.up * jumpForce;
       }
   }
   ```

   
## 2D ARPG人物控制器

```c#
 void FixedUpdate() {
        float horizontal = Input.GetAxis("Horizontal");//水平方向
        float vertical = Input.GetAxis("Vertical");//垂直方向
        //print(horizontal);

        Animator animator = GetComponent<Animator>();
        move = new Vector2(horizontal,vertical);
        if (!Mathf.Approximately(move.x, 0) || !Mathf.Approximately(move.y, 0)) 
        {
            animator.SetFloat("Speed", move.magnitude);
            //print(move.magnitude);
        }


        move.Normalize();
        animator.SetFloat("Look X", move.x);
        animator.SetFloat("Look Y", move.y);

        float speed = 5.0f;

        Vector2 position = transform.position;
        //position += speed * move * Time.deltaTime;
        position.x += Time.deltaTime * horizontal * speed;
        position.y += Time.deltaTime * vertical * speed;
        //transform.position = position;
        rigidbody2D.MovePosition(position);//防止抖动


  
 }
```




## 2D俯视角射击模板

```c#

public class MonsterController : MonoBehaviour
{

    public GameObject player;




    private float speed = 2f;

    // Start is called before the first frame update
    void Start()
    {
        player = GameObject.Find("主角");
    }

    // Update is called once per frame
    void Update()
    {
        Vector2 direction = (player.transform.position - transform.position).normalized;
        transform.Translate(direction * Time.deltaTime * speed);
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        Destroy(gameObject);
        Destroy(collision.gameObject);
        print("ok");
    }
}

```

## 人物一步一步移动

创建一个子对象，用子对象移动，每次人物靠近子对象即可

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CharacterController : MonoBehaviour
{
   private  Vector3 targetPosition;

    [Range(1,20)]
    public float speed;
    

    void Start()
    {
        targetPosition = transform.position;
    }
    void Update()
    {
        float x =  Input.GetAxisRaw("Horizontal");
        float y = Input.GetAxisRaw("Vertical");

        if (Vector3.Distance(transform.position, targetPosition) < 0.01f)
        {
            if (x != 0 || y != 0)
            {
                targetPosition += new Vector3(x, y, 0);
            }
        }

       
           

       transform.position  =  Vector3.MoveTowards(transform.position,targetPosition,speed*Time.deltaTime);
    }
}

```







# 2D世界屏幕坐标转世界坐标

```c#
Vector3 mouseWorldPosition = Camera.main.ScreenToWorldPoint(Input.mousePosition);
mouseWorldPosition.z = 0f;
```





# 2D俯视角射击

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CharacterController : MonoBehaviour
{

    public GameObject bullet;

    private float speed = 10.0f;

    void Start()
    {
        
    }


    void Update()
    {
        float x = Input.GetAxis("Horizontal");
        float y = Input.GetAxis("Vertical");
        transform.Translate(new Vector3(x,y)*Time.deltaTime* speed);

        if (Input.GetMouseButtonDown(0))
        {
            Shoot();
        }
    }


    //开枪
    void Shoot() 
    {
        GameObject tempBullet = Instantiate(bullet, transform.position, Quaternion.identity);
        Vector3 mousePos = Camera.main.ScreenToWorldPoint(Input.mousePosition);
        tempBullet.GetComponent<BulletController>().SetMoveDirecion(mousePos - transform.position);
    }
}

```





```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BulletController : MonoBehaviour
{
    private float speed=10f;

    public Vector2 moveDirection;

    void Start()
    {
        Destroy(gameObject, 3f);

    }


    void Update()
    {
        transform.Translate(moveDirection*Time.deltaTime*speed);
    }

    public void SetMoveDirecion(Vector2 direction)
    {
     
        moveDirection = direction.normalized;
  
    }
}

```



# 物体移动的7种方法

- 匀速直线运动

  ```c#
  public class test : MonoBehaviour
  {
      public float speed;
      void Update()
      {
          gameObject.transform.Translate(Vector3.right*speed*Time.deltaTime);
      }
  }
  
  ```

- 变速运动，lerp插值法

  ```c#
  public class test : MonoBehaviour
  {
      private Vector3 targetPosition = new Vector3(3,0,0);
  
      void Update()
      {
          gameObject.transform.position = 	Vector3.Lerp(transform.position,targetPosition,0.1f);
      }
  }
  
  ```

- 匀速运动，lerp插值法

  ```c#
  public class test : MonoBehaviour
  {
      private Vector3 targetPosition = new Vector3(3,0,0);
  
      void Update()
      {
          var t = 1 /( (transform.position - targetPosition).magnitude);
          gameObject.transform.position = Vector3.Lerp(transform.position,targetPosition, t*0.001f);
      }
  }
  
  ```

  

- 变速运动，SmoothDamp

  ```c#
  public class test : MonoBehaviour
  {
      private Vector3 refSpeed;//用来接受传出的速度
      private Vector3 targetPosition = new Vector3(3,0,0);
  
      void Update()
      {
          gameObject.transform.position = Vector3.SmoothDamp(transform.position, targetPosition, ref refSpeed, 1);
         }
  }
  ```

- 刚体运动，匀速直线运动

  ```c#
  public class test : MonoBehaviour
  {
      Rigidbody2D rigidbody2D;
  
      private void Start()
      {
          rigidbody2D = GetComponent<Rigidbody2D>();
          rigidbody2D.velocity = new Vector2(1,0);
      }
  }
  ```

- 匀加速直线运动，刚体一直受力

  ```c#
  public class test : MonoBehaviour
  {
      Rigidbody2D rigidbody2D;
  
      private void Start()
      {
          rigidbody2D = GetComponent<Rigidbody2D>();
        
      }
  
      private void FixedUpdate()
      {
          rigidbody2D.AddForce(new Vector2(0.01f*Time.deltaTime, 0));
      }
  
  }
  
  ```

- 匀速运动，刚体的MovePosition

  ```c#
  public class test : MonoBehaviour
  {
      Rigidbody2D rigidbody2D;
  
      private void Start()
      {
          rigidbody2D = GetComponent<Rigidbody2D>();
        
      }
  
      private void FixedUpdate()
      {
          rigidbody2D.MovePosition(transform.position+ Vector3.right*Time.deltaTime);
      }
  
  }
  
  ```

  








# 存储系统

```c#
using UnityEngine;

//二进制头文件
using System.Runtime.Serialization.Formatters.Binary;
using System.IO;



//XML头文件
using System.Xml;

//JSON头文件
using LitJson;

/// <summary>
/// 存储类，具体需要存储的数据需要玩家来自定义
/// </summary>

[System.Serializable]
public class SaveData
{
    public int testData;
}



public class SaveSystem : MonoBehaviour
{
    //存储文件的位置
    private string saveFilePath;

    private void Start()
    {
        saveFilePath = Application.dataPath + "/Save" + "/save.txt";
    }

    public int testData = 0;

    /// <summary>
    /// 从游戏中获得存储信息，并创建存储对象
    /// </summary>
    /// <returns>存储对象</returns>
    private SaveData GetGameData()
    {
        SaveData saveData = new SaveData();
        saveData.testData = testData;

        return saveData;
    }


    /// <summary>
    /// 将某个存储对象的数据加载到游戏中
    /// </summary>
    private void SetGameData(SaveData saveData)
    {
        testData = saveData.testData;
        print("获得数据！"+saveData.testData);
    }



    /// <summary>
    /// 使用二进制方式来存储游戏
    /// </summary>
    public void SaveByBin()
    {
        //获得游戏数据
        SaveData saveData = GetGameData();


        //创建一个二进制格式化程序
        BinaryFormatter bf = new BinaryFormatter();

        //创建一个文件流
        FileStream fileStream = File.Create(saveFilePath);

        //用二进制格式化程序的序列化方法来序列化Save对象,参数：创建的文件流和需要序列化的对象
        bf.Serialize(fileStream, saveData);
        //关闭流
        fileStream.Close();

        //如果文件存在，则显示保存成功
        if (File.Exists(saveFilePath))
        {
           print("保存成功");
        }
    }
    public void LoadByBin()
    {
        if (File.Exists(saveFilePath))
        {
            //反序列化过程
            //创建一个二进制格式化程序
            BinaryFormatter bf = new BinaryFormatter();
            //打开一个文件流
            FileStream fileStream = File.Open(saveFilePath, FileMode.Open);
            //调用格式化程序的反序列化方法，将文件流转换为一个Save对象
            SaveData save = (SaveData)bf.Deserialize(fileStream);
            //关闭文件流
            fileStream.Close();

            SetGameData(save);//重置存档

        }
        else
        {
            print("存档文件不存在");
        }

    }




    /// <summary>
    /// 使用XML的方式来保存游戏
    /// </summary>
    public void SaveByXML()
    {
        SaveData saveData = GetGameData();

        XmlDocument xmlDoc = new XmlDocument();//创建XML文档
        XmlElement root = xmlDoc.CreateElement("save");//创建根节点
        root.SetAttribute("name", "saveFile1");//设置根节点中的属性


        //创建具体的存储数据
        XmlElement testData = xmlDoc.CreateElement("testData");
        testData.InnerText = saveData.testData.ToString();

        root.AppendChild(testData);
        xmlDoc.AppendChild(root);

        xmlDoc.Save(saveFilePath);//保存

        if (File.Exists(saveFilePath))
        {
            print("保存成功");
        }

    }


    public void LoadByXml()
    {
        if (File.Exists(saveFilePath))
        {
            SaveData save = new SaveData();
            //加载XML文档
            XmlDocument xmlDoc = new XmlDocument();
            xmlDoc.Load(saveFilePath);
            XmlNodeList testData = xmlDoc.GetElementsByTagName("testData");
            //save.testData= testData
            save.testData  = int.Parse( testData[0].InnerText);
            SetGameData(save);
        }
        else
        {
            print("存档文件不存在");
        }

    }


    public void SaveByJson()
    {
        SaveData save = GetGameData();
      
        //利用JsonMapper将save对象转换为Json格式的字符串
        string saveJsonStr = JsonMapper.ToJson(save);
        //将这个字符串写入到文件中
        //创建一个StreamWriter，并将字符串写入文件中
        StreamWriter sw = new StreamWriter(saveFilePath);
        sw.Write(saveJsonStr);
        //关闭StreamWriter
        sw.Close();

       print("保存成功");
    }

    public void LoadByJson()
    {
       
        if (File.Exists(saveFilePath))
        {
            //创建一个StreamReader，用来读取流
            StreamReader sr = new StreamReader(saveFilePath);
            //将读取到的流赋值给jsonStr
            string jsonStr = sr.ReadToEnd();
            //关闭
            sr.Close();

            //将字符串jsonStr转换为Save对象
            SaveData save = JsonMapper.ToObject<SaveData>(jsonStr);
            SetGameData(save);
            print("保存成功");
        }
        else
        {
            print("存档文件不存在");
        }
    }

}


```



# 视角晃动

```c#
using UnityEngine;
using System.Collections;

public class ShakeView : MonoBehaviour
{
    // 震动标志位
    private bool isshakeCamera = false;

    // 震动幅度
    public float shakeLevel = 3f;
    // 震动时间
    public float setShakeTime = 0.2f;
    // 震动的FPS
    public float shakeFps = 45f;

    private float fps;
    private float shakeTime = 0.0f;
    private float frameTime = 0.0f;
    private float shakeDelta = 0.005f;
    private Camera selfCamera;

    private Rect changeRect;

    void Awake()
    {
        selfCamera = GetComponent<Camera>();
        changeRect = new Rect(0.0f, 0.0f, 1.0f, 1.0f);
    }

    // Use this for initialization
    void Start()
    {
        shakeTime = setShakeTime;
        fps = shakeFps;
        frameTime = 0.03f;
        shakeDelta = 0.005f;
    }

    // Update is called once per frame
    void Update()
    {
        if (isshakeCamera)
        {
            if (shakeTime > 0)
            {
                shakeTime -= Time.deltaTime;
                if (shakeTime <= 0)
                {
                    changeRect.xMin = 0.0f;
                    changeRect.yMin = 0.0f;
                    selfCamera.rect = changeRect;
                    isshakeCamera = false;
                    shakeTime = setShakeTime;
                    fps = shakeFps;
                    frameTime = 0.03f;
                    shakeDelta = 0.005f;
                }
                else
                {
                    frameTime += Time.deltaTime;

                    if (frameTime > 1.0 / fps)
                    {
                        frameTime = 0;
                        changeRect.xMin = shakeDelta * (-1.0f + shakeLevel * Random.value);
                        changeRect.yMin = shakeDelta * (-1.0f + shakeLevel * Random.value);
                        selfCamera.rect = changeRect;
                    }
                }
            }
        }
    }

    public void shake()
    {
        isshakeCamera = true;
    }
}
}

```





# 设计模式



# MVC架构





# UI框架



BasePanel，所有面板的基类

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;


abstract public class BasePanel : MonoBehaviour
{
    public abstract void OnEnter();
    public abstract void OnExit();

    public abstract void OnPause();


    public abstract void OnContinue();
}
```



UISystem，用来控制面板的pop，push等

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public enum PanelType
{
    ItemPanel
}



public class UISystem
{

    private static UISystem instance;
    public static UISystem Instance
    {
        get
        {
            if (instance == null)
            {
                instance = new UISystem();
            }
            return instance;
        }
    }

    private Stack<BasePanel> panels = new Stack<BasePanel>() { };



    public void PopPanel()
    {
        BasePanel temp = PeekPanel();
        temp.OnExit();
        panels.Pop();


    }
    public void PushPanel(BasePanel panel)
    {
        BasePanel tempPanel = PeekPanel();
         tempPanel?.OnPause();
 


        panels.Push(panel);
        panel.OnEnter();
    }

    public BasePanel PeekPanel()
    {
        if (panels.Count == 0)
        {
            return null;
        }
        return panels.Peek();
    }

    public void PauseGame()
    {
        Time.timeScale = 0;
    }
}

```





普通的面板

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class WinPanel : BasePanel
{
    public override void OnExit()
    {

    }

    public override void OnEnter()
    {
        gameObject.SetActive(true);
        

    }

    public override void OnPause()
    {

    }

    public override void OnContinue()
    {

    }


    public void NextLevel()
    {

    



    }
    public void GoBackToTitle()
    {
        SceneManager.LoadScene(0);
    }

}

```



# 流星滑落

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.EventSystems;


public class StartGame : MonoBehaviour, IPointerEnterHandler, IPointerExitHandler
{


    private RectTransform rectTransform;
    private TMP_Text tmpText;

    private Vector2 direction;
    private float speed;


    private bool isPointerIn;


    private void Awake()
    {
        tmpText = GetComponent<TMP_Text>();

        rectTransform = GetComponent<RectTransform>();
    }
    void Start()
    {

        
        switch (Random.Range(0, 1))
        {
            case 0:
                //流星
                //direction = Random.insideUnitCircle.normalized;
                direction =new Vector2(-1,-1).normalized;
                speed = Random.Range(30, 100);
                tmpText.fontSize = 40-speed/10;
                break;
        }
    }


    // Update is called once per frame
    void Update()
    {
        if (isPointerIn == true)
        {
            return;
        }

        Vector3 worldPos = rectTransform.transform.position;
        float leftX = worldPos.x - rectTransform.sizeDelta.x / 2;
        float rightX = worldPos.x + rectTransform.sizeDelta.x / 2;
        float upY = worldPos.y + rectTransform.sizeDelta.y / 2;
        float downY = worldPos.y - rectTransform.sizeDelta.y / 2;

        //超出了屏幕范围的时候
        if (leftX < 0|| downY<0)
        {
            transform.position = new Vector3(Screen.width, Screen.height, 0);

        }
        transform.Translate(direction * Time.deltaTime* speed, Space.World);
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        print("ok");


    }

    public void OnPointerEnter(PointerEventData eventData)
    {
        isPointerIn = true;
    }

    public void OnPointerExit(PointerEventData eventData)
    {
        isPointerIn = false;
    }
}

```




# Mesh编程




## 三角形序列

mesh包含了很多三角形

```c#
    MeshFilter meshFilter;
    // Start is called before the first frame update
    void Start()
    {
        meshFilter = GetComponent<MeshFilter>();
        
        foreach (int vertex in meshFilter.mesh.triangles)
        {
            Debug.Log(vertex);//36个
        }
   
    }
```



我的一个cube有36个索引，这个是怎么算出来的

一个立方体通常由6个面构成，每个面由两个三角形组成。每个三角形有三个顶点，所以一个立方体总共有6个面 x 2个三角形/面 x 3个顶点/三角形 = 36个索引。

在Unity中，创建一个立方体的话，可以使用Mesh类的静态函数Mesh.GenerateMesh()来生成一个具有正确顶点和索引的立方体网格。











## 创建mesh



```c#
    MeshFilter meshFilter;
    // Start is called before the first frame update
    void Start()
    {
        meshFilter = GetComponent<MeshFilter>();
        meshFilter.mesh.triangles = GetTriangle();
        meshFilter.mesh.vertices = GetVertical();
        meshFilter.mesh.uv = GetUV();
        meshFilter.mesh.name = "Test";
    }

//定义有哪些顶点
    private Vector3[] GetVertical() {
        Vector3[] v = new Vector3[4]
        {
            new Vector3(0,0,0), //0顶点
            new Vector3(0,1,0),//1顶点
            new Vector3(1,1,0),
            new Vector3(1,0,0)
        };

        return v;
    }


//定义哪三个顶点组成一个面片
    private int[] GetTriangle()
    {
        int[] v = new int[]
        {
           0,1,2,//左手法则，012可以被看到
           0,1 ,3
        };
        return v;
    }


    private Vector2[] GetUV()
    {
        Vector2[] v = new Vector2[4]
        {
            new Vector2(0,0),//第0个顶点的uv坐标
            new Vector2(0,1),
            new Vector2(1,1),
            new Vector2(1,0)
        };

        return v;

    }
```







## 创建面

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;


[RequireComponent(typeof(MeshFilter), typeof(MeshRenderer))]
public class CreatePlane : MonoBehaviour
{

    int x = 3;
    int y = 4;

    MeshFilter meshFilter;
    // Start is called before the first frame update
    void Start()
    {
        meshFilter = GetComponent<MeshFilter>();
        meshFilter.mesh = new Mesh();

        meshFilter.mesh.vertices = GetVertical();
        meshFilter.mesh.triangles = GetTriangle();
        meshFilter.mesh.uv = GetUV();

        //foreach (var item in meshFilter.mesh.triangles)
        //{
        //    Debug.Log(item);
        //}
    }


    private void OnDrawGizmos()
    {
        Gizmos.color = Color.red;
        for (int i = 0; i < meshFilter.mesh.vertices.Length; i++)
        {
            Gizmos.DrawSphere(meshFilter.mesh.vertices[i], 0.1f);
        }
    }

   
    private Vector2[] GetUV()
    {
        Vector2[] uv = new Vector2[(x + 1) * (y + 1)];
        int index = 0;
        for (int j = 0; j < y + 1; j++)
        {
            for (int i = 0; i < x + 1; i++)
            {
                uv[index] = new Vector2(i / (float)x, j / (float)y);
                index++;
            }
        }
        return uv;
    }

    private Vector3[] GetVertical()
    {
        Vector3[] vertices = new Vector3[(x + 1) * (y + 1)];//x×y个四边形，x+1,y+1个顶点

        int index = 0;


        for (int j = 0; j< y+1; j++)
        {
            for (int i = 0; i <x+1;i++)
            {
                vertices[index] = new Vector3(i, j);
                index++;
            }
        }
        return vertices;
    }


    private int[] GetTriangle()
    {
        int[] triangle = new int[x * y * 6];//一个四边形两个三角形，一个三角形三个顶点，x*y个四边形，x*y*6个顶点
        int index = 0;
        int length = x+1;//行宽

        for (int j = 0; j < y; j++)
            for (int i = 0; i < x; i++)
            {
                triangle[index++] = i;
                triangle[index++] = i+(j+1)*length;
                triangle[index++] = i+1;

                triangle[index++] = i + (j+1) * length;
                triangle[index++] = i + (j+1) * length+1;
                triangle[index++] = i + 1;
            }
        return triangle;

    }

}

```







# 人物2d捏



```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class DemoCharacterController : MonoBehaviour
{
    [Header("Movement")]
    public float speed = 10f;

    public int side = 1;


    [Header("Interact")]
    public Transform interactTips;

    private Rigidbody2D rb;
    private Collision coll;
    private AnimationScript anim;

    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        coll = GetComponent<Collision>();
        anim = GetComponentInChildren<AnimationScript>();
    }

    public float jumpHeight = 1f; // 跳跃的高度
    public float jumpTime = 0.5f; // 跳跃的时间

    private bool isJumping = false; // 标记角色是否正在跳跃
    private Vector3 originalPosition; // 角色原始位置

    // Update is called once per frame
    void Update()
    {
        float x = Input.GetAxis("Horizontal");
        float y = Input.GetAxis("Vertical");
        var dir = new Vector2(x, y);

        anim.SetHorizontalMovement(x, y, rb.velocity.y);





        Walk(dir);

        if (x > 0)
        {
            side = 1;
            anim.Flip(side);
        }
        if (x < 0)
        {
            side = -1;
            anim.Flip(side);
        }

        if (Input.GetButtonDown("Jump") && !isJumping)
        {
            originalPosition = transform.position;
            StartCoroutine(Jump());
        }
    }

    private void Walk(Vector2 dir)
    {
        rb.velocity = new Vector2(dir.x * speed, dir.y * speed);
    }


    IEnumerator Jump()
    {
        isJumping = true;
        float timer = 0;

        while (timer <= jumpTime)
        {
            timer += Time.deltaTime;

            Vector3 newPosition = originalPosition;
            float y = Mathf.Sin((Mathf.PI / jumpTime) * timer);
            newPosition.y += jumpHeight * y;

            //当下落时才进行跳板的检测
            if (timer > jumpTime / 2)
            {
                RaycastHit2D[] hits = Physics2D.RaycastAll(transform.position, -Vector2.up, 0.5f, LayerMask.GetMask("Ground"));
                foreach (RaycastHit2D hit in hits)
                {
                    // print("无敌");
                    if (hit.collider != null)
                    {
                        Debug.Log("Ground Detected!");
                        timer = 2 * jumpTime;//遇到跳板时，把跳跃中止。

                    }
                }
            }
            // 更新角色的位置
            transform.position = new Vector3(transform.position.x, newPosition.y, transform.position.z);
            yield return null;
        }
        // 重置角色的位置和跳跃状态
        // transform.position = originalPosition;
        isJumping = false;
    }

}

```





# mesh清除

```c#
public class mesh画画 : MonoBehaviour
{
    public NavMeshSurface Surface2D;


    private MeshRenderer meshRenderer;
    private Color originalColor;
    public float fadeAmount = 0.5f;

    public float size = 20f;

    void Start()
    {
        meshRenderer = GetComponent<MeshRenderer>();
        originalColor = meshRenderer.material.color;

        Surface2D.BuildNavMeshAsync();
    }


    void Update()
    {
        if (Input.GetMouseButton(0))
        {
            Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
            RaycastHit hit;

            if (Physics.Raycast(ray, out hit))
            {
                if (hit.collider.gameObject == gameObject) 
                {
                    Fade(hit.textureCoord);
                    
                }
            }
        }

        if (Input.GetMouseButtonUp(0))
        {
            //Surface2D.UpdateNavMesh(Surface2D.navMeshData);
            Surface2D.BuildNavMesh();
        }
    }



    void Fade(Vector2 uv)
    {
        Texture2D texture = meshRenderer.material.mainTexture as Texture2D;
        Texture2D texture2 = new Texture2D(texture.width, texture.height, TextureFormat.RGBA32, false);

        // 将原始纹理复制到texture2
        texture2.SetPixels(texture.GetPixels());
        texture2.Apply();

        Color[] colors = texture2.GetPixels();

        int width = texture2.width;
        int height = texture2.height;

        // 将原始纹理复制到texture2


        int x = Mathf.FloorToInt(uv.x * width);
        int y = Mathf.FloorToInt(uv.y * height);
        // 修改透明度
        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                Color color = colors[i * width + j];
                if (Mathf.Abs(i - y) < size && Mathf.Abs(j - x) < size)
                {
                    // 设置透明度为fadeAmount
                    color.a *= fadeAmount;
                }
                colors[i * width + j] = color;
            }
        }


        // 更新纹理
        texture2.SetPixels(colors);
        texture2.Apply();
        meshRenderer.material.mainTexture = texture2;
    }
    public Texture2D DeCompress(Texture2D source)
    {
        RenderTexture renderTex = RenderTexture.GetTemporary(
                    source.width,
                    source.height,
                    0,
                    RenderTextureFormat.Default,
                    RenderTextureReadWrite.Linear);

        Graphics.Blit(source, renderTex);
        RenderTexture previous = RenderTexture.active;
        RenderTexture.active = renderTex;
        Texture2D readableText = new Texture2D(source.width, source.height);
        readableText.ReadPixels(new Rect(0, 0, renderTex.width, renderTex.height), 0, 0);
        readableText.Apply();
        RenderTexture.active = previous;
        RenderTexture.ReleaseTemporary(renderTex);
        return readableText;
    }

}

```









主持人：剧情背景

这是一部根据斯蒂芬·金的《迷雾》改编的冷酷而戏剧化的角色扮演。

地球被一层乳白色的薄雾所覆盖。薄雾最初是从缅因州沙莫尔的一个军事基地扩散出来的，该基地正在进行箭头计划实验。薄雾弥漫在每个户外区域。室内区域通常是安全的，没有薄雾，但薄雾仍然可以通过打开的门或窗户慢慢渗入。薄雾很透气，但闻起来很难闻。薄雾很浓，只能透过几英尺的距离看到。薄雾掩盖了声音。人类很难在薄雾中穿行。由于薄雾对视觉和听觉的抑制作用，薄雾中的人类很容易被偷偷带入。

薄雾中栖息着成群体型各异的食肉怪物。怪物几乎与任何已知的生物都不相似。怪物都有bug级别的智力，并且只受本能的驱使。怪物攻击他们发现的任何人类或动物。怪物有时会互相攻击。怪物的动机是饥饿，会以尸体为食。怪物靠气味导航，不受薄雾的阻碍。薄雾中带有气味，使怪物能够很容易地在薄雾中探测到周围的环境。怪物在薄雾之外时会迷失方向。



故事开头：

当你们冲回车里并关上车门时，外面追赶你们的生物似乎失去了继续狩猎的心情。你们透过窗户看到它的轮廓，被雾气遮蔽，不自然地向另一个方向蹒跚而行。花了点时间祈祷它不会再次靠近之后，你们深深靠在椅背上，让狂跳的心跳和肾上腺素平静下来。尽管害怕，但你们仍有一线生机——你们有足够的汽油可以到达任何你想去的地方。但还有什么地方可去呢？世界上可能仅存你们四个人类了。



主持人：下面是人物介绍：

大学生：刚上大学的大学生，学的是医学专业。她通常在暑假期间在天主教会做志愿者，担任过儿童夏令营的负责人。她想要生存下去。她的生存技能不足，但她能很快学会。



家里蹲：三年前，在一次学校去博物馆的旅行中，有人把她推下楼梯。伤势严重，她失去了行走的能力。很长一段时间以来，她一直被同学们残忍地欺负，但她不知道是哪个施虐者把她推下了楼梯。在内心深处，她仇视一切人类。她的朋友们背弃了她，而她的父母很少在家，所以她饱受孤独之苦，感到被抛弃、被困。她经常做关于欺凌的噩梦。她患有精神病，但拒绝服药，把药丸藏在舌头下，然后偷偷吐出来。她只想尽快结束痛苦。她有4次自杀未遂。



任小川：任小川是一个典型的日本男生，喜欢玩电子游戏、看漫画和吃垃圾食品。任在生活的方方面面都很一般；他的成绩，他的朋友，甚至他的爱好都很正常。有一天，任决定，他厌倦了总是像NPC一样融入背景。任开始表现得像动漫中的“洋基”或罪犯。他戴着一顶学校帽，用凝胶做发型，垂下宽松的裤子，在白色t恤外面敞开着制服夹克。这一切都是为了让自己看起来像一个在学校里混迹的酷霸。任不顾一切地加入其中一个帮派，并将不惜一切代价被其他犯罪分子所接受。任试图欺负别人使自己看起来很酷，但失败得很惨。如果他选择的受害者开始哭泣，他会立即感到内疚并为自己的行为道歉。如果受害者根本不理他，任会继续纠缠他们，直到他有反应。任喜欢把目标对准女性，他认为这些女性很容易成为受害者。



历史老师：他是一名历史老师，业余时间也做家庭教师。他不喜欢花时间和青少年和年轻学生一起工作，认为他们即使在成年时也是轻浮的孩子。但他别无选择，因为他必须为父亲支付账单。父亲因长期酗酒而贷款，死于心脏骤停。他几乎不休息，为了获得更高的薪水，他把各种各样的工作都累垮了。他喜欢喝烈性酒和抽烟。



主持人：对话范例：



大学生：我们活下去了？

家里蹲：。。。

任小川：真是他妈的好险，我们竟然逃过了那个怪物的追捕。老子以为自己就要死了。

历史老师：现在高兴还太早。我们不知道怪物什么时候会回来。不过反正世界也都这样了，咱也是能活一天是一天了。

大学生：不要这么说啊，一定有办法活下来的！我们后备箱还有很多汽油。我们可以烧死这些怪物。

历史老师：你疯了吗，如果我们用了这些汽油，之后可以说是必死无疑了。











# unity和android相互调用原生api的方法

思路：

1. unity可以导出apk文件，但是并不能直接调用android的api
2. unity可以用AndroidJavaClass等类来调用java的代码和jar
3. 所以可以考虑用安卓原生开发unity的jar包，让unity直接运行原生api
4. 后来发现安卓原生会在运行时生成d类，而unity并不会生成这个类，导致很多api无法使用
5. 所以考虑让unity打包出安卓工程，然后用安卓studio再次进行打包



## unity调用java代码



1. 把java代码放到unity的Plugin文件夹中

   ```c#
   public class Test {
       public static  String LOG = "i am LOG";
       public  String name;
       public  static  void SetLOG(String log)
       {
           LOG = log;
           Log.d("LOG","LOG:");
   
       }
       public  static  String GetLOG()
       {
           Log.d("LOG","LOG:");
           return  LOG;
       }
   }
   ```
   
   



直接调用java代码

```c#
using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class JavaCaller : MonoBehaviour
{
    AndroidJavaClass javaClass;
    public TMP_Text text;
    string javaClassName = "com.example.exportjar.Test";
    int i = 0;
    void Start()
    {
        javaClass = new AndroidJavaClass(javaClassName);
        string result = javaClass.CallStatic<string>("GetLOG");
     
        text.text = result;
    }

    //public void Click()
    //{
    //    i++;
    //    javaClass = new AndroidJavaClass(javaClassName);
    //    int result = javaClass.CallStatic<int>("Add", 1, i);
    //    text.text = result.ToString();

    //}


    public void Click2()
    {
        AndroidJavaClass jc = new AndroidJavaClass("com.example.exportjar.Test");
        text.text = jc.CallStatic<string>("GetLOG");
        jc.CallStatic("SetLOG","testtesttest");
    }
}

```



## 安卓打包jar，并让unity调用

1. 新建active的空工程

2. 直接删掉初始提供的MainActivity文件（delete anyway）

3. 需要把build.gradle.kts中进行修改，后缀改成library

   ```java
   plugins {
       id("com.android.library")
   }
   ```

   把Android没用的配置删除

   ```java
   android {
       namespace = "com.example.exportjar"
       compileSdk = 34
   }
   ```

   

4. 在刚才删掉的MainActivity的地方新建java文件开始写代码

   ```java
   package com.example.exportjar;
   
   import android.widget.Toast;
   
   import android.util.Log;
   import android.os.Vibrator;
   import android.content.Context;
   
   
   public class Test {
       public static  String LOG = "i am LOG";
       public  String name;
       public  static  void SetLOG(String log)
       {
           LOG = log;
           Log.d("LOG","LOG:");
   
       }
       public  static  String GetLOG()
       {
           Log.d("LOG","LOG:");
           return  LOG;
       }
   }
   ```

   

5. 点击build -  make project

6. 打包之后的jar包会在 app-build-intermediates-arr_main_jar-debug-classes.jar

7. 直接导入unity即可，和调用java文件是一样的



## java调用unity的方法，以及传递context

https://blog.csdn.net/qq_19646129/article/details/105208638

1. 如果希望调用unity的方法，或者unity调用原生方法，就需要引入unity的库文件了。需要把unity的库文件导入到android studio中，才能让java访问到unity的代码

2. C:\Program Files\Unity\Hub\Editor\2022.3.18f1\Editor\Data\PlaybackEngines\AndroidPlayer\Variations\mono\Release\Classes  在这个目录下找到classes.jar

3. 把jar包复制到  app的libs下

4. 右击这个classes.jar，点击add as library

5. 配置manifest

   ```xml
      <application
         
           <meta-data android:name="unityplayer.UnityActivity" android:value="true" />
       </application>
   ```

   

6. 此时可以import数据，康康有没有成功导入

   ```java
   import  com.unity3d.player.UnityPlayer;
   ```

   

7. 配置为仅编译不依赖，不然会报错java.lang.RuntimeException: java.lang.RuntimeException: Duplicate class bitter.jnibridge.JNIBridge found in modules classes-2.jar (:mylibrary-debug:) and unity-classes.jar (unity-classes.jar)

   ```json
   plugins {
       id("com.android.library")
   }
   
   android {
       namespace = "com.example.androidapitest"
       compileSdk = 34
   }
   
   dependencies {
   
       implementation("androidx.appcompat:appcompat:1.6.1")
       implementation("com.google.android.material:material:1.11.0")
       implementation("androidx.constraintlayout:constraintlayout:2.1.4")
   //    implementation(files("libs\\classes.jar"))
       compileOnly(files("libs\\classes.jar"))
       testImplementation("junit:junit:4.13.2")
       androidTestImplementation("androidx.test.ext:junit:1.1.5")
       androidTestImplementation("androidx.test.espresso:espresso-core:3.5.1")
   }
   ```
   
8. 编写java代码，调用原生api

   ```java
   import com.unity3d.player.UnityPlayer;
   import android.widget.Toast;
   public static void UnityTest() {
       Toast.makeText(UnityPlayer.currentActivity, "hello", 0).show();
   }
   ```

9. 参考上一个的方法，导出jar包（别忘了删除之前的包）

10. 导入unity运行





## 对unity导出的项目进行原生的修改





1. 有时候在使用安卓原生的Drawable时，可能加载不出来资源，可以导出为安卓的项目重新打包
2. 导出安卓项目的时候勾选export project
3. 使用安卓studio打开project
4. 进行原生开发





# unity调用安卓原生api的模板



## 震动

直接在unity里面调用

```c#
Handheld.Vibrate();
```



## 消息提示

```java
import com.unity3d.player.UnityPlayer;
import android.widget.Toast;   
public  static  void UnityTest()
{
//        UnityPlayer.UnitySendMessage("游戏对象","方法名","");
    Toast.makeText(UnityPlayer.currentActivity,"hello",Toast.LENGTH_SHORT).show();
}
```



## 系统消息通知



注意unity是没有办法用R的

```java
package com.example.androidapitest;
import java.util.Calendar;

import android.app.NotificationChannel;
import android.content.Context;
import android.os.Vibrator;
import android.util.Log;
import android.widget.Toast;

import com.unity3d.player.UnityPlayer;


import android.app.PendingIntent;
import android.content.Intent;
import android.app.Notification;
import android.app.NotificationManager;
import android.os.Build;
import android.graphics.BitmapFactory;
import android.graphics.drawable.Drawable;

public class Test {
    public  static  void UnityTest()
    {
//        UnityPlayer.UnitySendMessage("游戏对象","方法名","");
        Toast.makeText(UnityPlayer.currentActivity,"hello",Toast.LENGTH_SHORT).show();
    }

    public  static  int NumTest()
    {
        Log.d("TAG", "这里是NumTest哦~");
        Toast.makeText(UnityPlayer.currentActivity,"成功！",Toast.LENGTH_SHORT).show();
        return  (int)(Math.random()*100);
    }


    public  static  void VibratorRun()
    {
        Vibrator  vibrator = (Vibrator) UnityPlayer.currentActivity.getSystemService(Context.VIBRATOR_SERVICE);
        if (vibrator != null ) {
            vibrator.vibrate((long)1000);
        }
        Toast.makeText(UnityPlayer.currentActivity,"震动！",Toast.LENGTH_SHORT).show();
    }

    private static int getResourceId(Context context, String resourceName, String resourceType) {
        return context.getResources().getIdentifier(resourceName, resourceType, context.getPackageName());
    }

    public  static  void NotifyTest()
    {
        Log.d("TAG", "成功执行了捏~");
        sendSimpleNotify(UnityPlayer.currentActivity,"标题捏","内容捏");
    }

    // 发送简单的通知消息（包括消息标题和消息内容）
    public static void sendSimpleNotify(Context context, String title, String message) {
        // 从系统服务中获取通知管理器
        NotificationManager notifyMgr = (NotificationManager)
                context.getSystemService(Context.NOTIFICATION_SERVICE);

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {

            NotificationChannel channel = new NotificationChannel("leo","测试通知",NotificationManager.IMPORTANCE_HIGH);
            notifyMgr.createNotificationChannel(channel);
            // Android 8.0开始必须给每个通知分配对应的渠道
//            builder = new Notification.Builder(context, context.getString(R.string.app_name));
        }

//        // 创建一个跳转到活动页面的意图
//        Intent clickIntent = new Intent(context, Test.class);
//        // 创建一个用于页面跳转的延迟意图
//        PendingIntent contentIntent = PendingIntent.getActivity(context,
//                R.string.app_name, clickIntent, PendingIntent.FLAG_UPDATE_CURRENT);
        // 创建一个通知消息的建造器
        Notification.Builder builder = new Notification.Builder(context,"leo");
//        setContentIntent(contentIntent) // 设置内容的点击意图

        int smallIconId = getResourceId(context, "ic_launcher", "drawable");
        Drawable smallIcon = context.getResources().getDrawable(smallIconId);

        builder
                .setAutoCancel(true) // 点击通知栏后是否自动清除该通知
                .setSmallIcon(smallIconId) // 设置应用名称左边的小图标
//                .setSubText("这里是副本") // 设置通知栏里面的附加说明文本
                // 设置通知栏右边的大图标
//                .setLargeIcon(BitmapFactory.decodeResource(context.getResources(), R.drawable.images))
                .setContentTitle(title) // 设置通知栏里面的标题文本
                .setContentText(message); // 设置通知栏里面的内容文本

        Notification notify = builder.build(); // 根据通知建造器构建一个通知对象



        // 使用通知管理器推送通知，然后在手机的通知栏就会看到该消息
        notifyMgr.notify(1, notify);
    }
}

```



如果发现api版本太旧，可以加一个配置

```xml

android {
    namespace = "com.example.androidapitest"
    compileSdk = 34
    defaultConfig {
        // ...
        minSdk = 16
        // ...
    }
}
```



然后点右上角的sync now







## 剪贴板的访问

```java
package com.example.androidapitest;

import com.unity3d.player.UnityPlayer;
import android.content.ClipData;
import android.content.ClipDescription;
import android.content.ClipboardManager;

import android.app.Fragment;
import android.content.Context;
import android.content.Intent;

public class ClipDataTest extends Fragment {
    private static final String TAG = "Plugin";
    private static ClipDataTest Instance = null;
    private String gameObjectName;

    public static ClipDataTest GetInstance(String gameObject) {
        if (Instance == null) {
            Instance = new ClipDataTest();
            Instance.gameObjectName = gameObject;
            UnityPlayer.currentActivity.getFragmentManager().beginTransaction().add(Instance, TAG).commit();
        }
        return Instance;
    }

    //拷贝String到剪贴板
    public  void onClickCopy(String str) {
        //获取剪贴板管理器：
        ClipboardManager cm = (ClipboardManager) getActivity().getSystemService(Context.CLIPBOARD_SERVICE);
        // 创建普通字符型ClipData
        ClipData mClipData = ClipData.newPlainText("Label", str); //Label是任意文字标签
        // 将ClipData内容放到系统剪贴板里。
        cm.setPrimaryClip(mClipData);
    }

    //粘贴
    public String onClickPaste() {
        ClipboardManager cm = (ClipboardManager) getActivity().getSystemService(Context.CLIPBOARD_SERVICE);
        String result = "";
        ClipData clipData = cm.getPrimaryClip();
        //result = cm.toString(); //ClipData{ text/plain "Label"{T:"str"}}; //取出的是ClipData
        //result = cm.getText().toString(); //"str" //方法deprecated
        ClipData.Item item = clipData.getItemAt(0); //这里获取第一条，也可以用遍历获取任意条
        CharSequence charSequence = item.coerceToText(getActivity().getApplicationContext());
        result = charSequence.toString();
        return result;
    }
}
```





```c#
public void Click3()
{
    AndroidJavaClass jc = new AndroidJavaClass("com.example.androidapitest.ClipDataTest"); 
    AndroidJavaObject jo = jc.CallStatic<AndroidJavaObject>("GetInstance", gameObject.name); //Main Camera
    text.text = jo.Call<string>("onClickPaste");
}
```





## 屏幕亮度的修改

```java
package com.example.androidapitest;
import android.app.Activity;
import android.provider.Settings;
import android.view.WindowManager;
import android.view.Window;
import com.unity3d.player.UnityPlayer;
public class BrightnessTest {
    public static void  ChangeBright(final int brightnessValue) {
        Activity activity =  UnityPlayer.currentActivity;
        activity.runOnUiThread(new Runnable() {
            @Override
            public void run() {
                Window window = activity.getWindow();
                WindowManager.LayoutParams lp = window.getAttributes();
                lp.screenBrightness = brightnessValue / 255.0f;
                window.setAttributes(lp);
            }
        });

    }

    public  static float GetBright()
    {
        Activity activity =  UnityPlayer.currentActivity;
        Window window = activity.getWindow();
        WindowManager.LayoutParams lp = window.getAttributes();
       return lp.screenBrightness ;

    }
}

```





```c#
    public void Click4()
    {
        
        AndroidJavaClass jc = new AndroidJavaClass("com.example.androidapitest.BrightnessTest");
        text.text = jc.CallStatic<float>("GetBright").ToString();
        jc.CallStatic("ChangeBright",10); 
    }
```





## 系统信息

```java
    public  static  String PhoneTest()
    {
        String model = Build.MODEL;
        Log.d("系统信息", "手机型号"+model);
        Log.d("系统信息", "语言"+ Locale.getDefault().getLanguage());
        Log.d("系统信息", "系统版本号"+ android.os.Build.VERSION.RELEASE);
        Log.d("系统信息", "手机厂商"+ android.os.Build.BRAND);
        return  model;
    }
```





## 录音



