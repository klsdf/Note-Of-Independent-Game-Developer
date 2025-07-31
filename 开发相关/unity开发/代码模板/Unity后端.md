
# Server


``` c# 
using System;
using System.Collections;
using System.Collections.Generic;
using System.Net;
using UnityEngine;

public class Server : MonoBehaviour 
{
    private HttpListener httpListener;
    private readonly string prefix = "http://localhost:8848/";

    private void Start()
    {
        // DontDestroyOnLoad(this.gameObject);
        UnityDispatcher.Initialize();
        StartServer();
    }

    private void StartServer()
    {
        httpListener = new HttpListener();
        httpListener.Prefixes.Add(prefix);
        
        try
        {
            httpListener.Start();
            Debug.Log("Server started on " + prefix);
            // 开始异步监听请求
            StartCoroutine(ListenForRequests());
        }
        catch (System.Exception e)
        {
            Debug.LogError($"Failed to start server: {e.Message}");
        }
    }


    private IEnumerator ListenForRequests()
    {
        while (httpListener.IsListening)
        {
            // 使用异步方式获取context
            var contextAsync = httpListener.BeginGetContext(new AsyncCallback(ListenerCallback), httpListener);
            
            // 等待下一帧继续
            yield return null;
        }
    }

    private void ListenerCallback(IAsyncResult result)
    {
        if (!httpListener.IsListening) return;
        
        try 
        {
            HttpListenerContext context = httpListener.EndGetContext(result);
            HttpListenerResponse response = context.Response;
            // 添加 CORS 头部
            response.Headers.Add("Access-Control-Allow-Origin", "*");
            response.Headers.Add("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
            response.Headers.Add("Access-Control-Allow-Headers", "Content-Type, Accept");
    
            UnityDispatcher.InvokeOnAppThread(() =>
            {
                try
                {
                    response = RequestHandler.Instance.Handle(context,response);
                }
                catch (System.Exception e)
                {
                    Debug.LogError($"Error processing request: {e.Message}");
                }
                finally
                {
                    response.Close();
                }
            });
        }
        catch (System.Exception e)
        {
            Debug.LogError($"Error in callback: {e.Message}");
        }
    }


    private void OnDestroy()
    {
        if (httpListener != null && httpListener.IsListening)
        {
            httpListener.Stop();
            httpListener.Close();
        }
    }
}



public class UnityDispatcher : MonoBehaviour
{
    private static UnityDispatcher instance = null;
    private static readonly Queue<Action> executeOnMainThread = new Queue<Action>();
    private static readonly object queueLock = new object();

    public static void Initialize()
    {
        if (instance == null)
        {
            instance = new GameObject("UnityDispatcher").AddComponent<UnityDispatcher>();
            DontDestroyOnLoad(instance.gameObject);
        }
    }

    public static void InvokeOnAppThread(Action action)
    {
        if (action == null) return;

        lock (queueLock)
        {
            executeOnMainThread.Enqueue(action);
        }
    }

    private void Awake()
    {
        if (instance == null)
        {
            instance = this;
            // DontDestroyOnLoad(this.gameObject);
        }
    }

    private void Update()
    {
        lock (queueLock)
        {
            while (executeOnMainThread.Count > 0)
            {
                executeOnMainThread.Dequeue().Invoke();
            }
        }
    }
}
```







# RequestHandler

```c#
using System.Net;
using UnityEngine;

public class RequestHandler : Singleton<RequestHandler>
{
    [System.Serializable]
    public class PostData
    {
        public string unlock;
    }

    [System.Serializable]
    public class PositionData
    {
        public string type;
        public Position position;
    }

    [System.Serializable]
    public class Position
    {
        public float left;
        public float top;
    }
    // 假设你有一个Prefab的引用
    public GameObject wallPrefab;
    public GameObject lightPrefab;
    public GameObject violiaPrefab;
    public bool isGetSprite = false;
    public HttpListenerResponse Handle(HttpListenerContext context, HttpListenerResponse response)
    {
        if (context.Request.HttpMethod == "GET")
        {
            if (context.Request.Url.LocalPath == "/test")
            {
                string responseText = "Hello from Unity Server!";
                byte[] buffer = System.Text.Encoding.UTF8.GetBytes(responseText);

                response.ContentLength64 = buffer.Length;
                response.ContentType = "text/plain";
                response.OutputStream.Write(buffer, 0, buffer.Length);
            }

            if (context.Request.Url.LocalPath == "/showViolia")
            {
                Debug.Log("Received showViolia request");
                // violiaPrefab.SetActive(true);
                DialogController.Instance.ShowMsg("卧室上似乎出现了什么东西。");
                violiaPrefab.GetComponent<LyraPhoto>().ChangeSpriteToNoEyeBall();
            }

            if (context.Request.Url.LocalPath == "/GetSprite")
            {
                DialogController.Instance.ShowMsg("你获得了光明，在黑夜中奔跑时，它会起到作用。");
                Debug.Log("Received GetSprite request");
                isGetSprite = true;
            }

            if (context.Request.Url.LocalPath == "/isGetSprite")
            {
                Debug.Log("Received isGetSprite request");
                string responseText = isGetSprite.ToString();
                byte[] buffer = System.Text.Encoding.UTF8.GetBytes(responseText);
                response.ContentLength64 = buffer.Length;
                response.ContentType = "text/plain";
                response.OutputStream.Write(buffer, 0, buffer.Length);
            }

            if (context.Request.Url.LocalPath == "/playMusicLyra")
            {
                Debug.Log("Received playMusicLyra request");
                AudioController.Instance.PlayWebLyra();
            }

            if (context.Request.Url.LocalPath == "/returnToGame")
            {
                Debug.Log("Received returnToGame request");
                // GameController.Instance.GameResume();
            }

            if (context.Request.Url.LocalPath == "/showMom")
            {
                Debug.Log("Received showMom request");
                DesktopPetManager.Instance.MovePetToRight();
            }
            if (context.Request.Url.LocalPath == "/hideMom")
            {
                Debug.Log("Received hideMom request");
                DesktopPetManager.Instance.MoveOutOfScreenLeft();
            }
            if (context.Request.Url.LocalPath == "/hideMomHalf")
            {
                Debug.Log("Received hideMomHalf request");
                DesktopPetManager.Instance.MoveOutOfHalfScreenLeft();
            }


            if (context.Request.Url.LocalPath == "/changeMomToSmile")
            {
                Debug.Log("Received changeMomToSmile request");
                DesktopPetManager.Instance.ChangeExpression(PetExpression.Smile);
            }
            if (context.Request.Url.LocalPath == "/changeMomToAngry")
            {
                Debug.Log("Received changeMomToAngry request");
                DesktopPetManager.Instance.ChangeExpression(PetExpression.Angry);
            }
            if (context.Request.Url.LocalPath == "/changeMomToCrazy")
            {
                Debug.Log("Received changeMomToCrazy request");
                DesktopPetManager.Instance.ChangeExpression(PetExpression.Crazy);
            }
            if (context.Request.Url.LocalPath == "/changeMomToNormal")
            {
                Debug.Log("Received changeMomToNormal request");
                DesktopPetManager.Instance.ChangeExpression(PetExpression.Normal);
            }



            if (context.Request.Url.LocalPath == "/openConsoleAndRun")
            {
                Debug.Log("Received openConsoleAndRun request");
                MouseController.Instance.OpenConsoleAndRun();
            }
        }
        else if (context.Request.HttpMethod == "POST")
        {
            if (context.Request.Url.LocalPath == "/OpenPrefab")
            {
                wallPrefab.SetActive(true);
            }
            if (context.Request.Url.LocalPath == "/ClosePrefab")
            {
                wallPrefab.SetActive(false);
            }
            if (context.Request.Url.LocalPath == "/SetPicturePosition")
            {

                Debug.Log("Received SetPicturePosition request");


                using (var reader = new System.IO.StreamReader(context.Request.InputStream, context.Request.ContentEncoding))
                {
                    string requestBody = reader.ReadToEnd();
                    Debug.Log("Received POST data: " + requestBody);

                    // 解析JSON数据
                    var positionData = JsonUtility.FromJson<PositionData>(requestBody);
                    Debug.Log($"Image Source: {positionData.type}");
                    Debug.Log($"Position - Left: {positionData.position.left}, Top: {positionData.position.top}");

                    // 移动Prefab到指定位置
                    MovePrefabToPosition(positionData.type,positionData.position);
                }

                string responseText = "Position data received!";
                byte[] buffer = System.Text.Encoding.UTF8.GetBytes(responseText);

                response.ContentLength64 = buffer.Length;
                response.ContentType = "text/plain";
                response.OutputStream.Write(buffer, 0, buffer.Length);
            }

            if (context.Request.Url.LocalPath == "/unlockDoor")
            {
                using (var reader = new System.IO.StreamReader(context.Request.InputStream, context.Request.ContentEncoding))
                {
                    string requestBody = reader.ReadToEnd();
                    Debug.Log("Received POST data: " + requestBody);
                    PostData postData = JsonUtility.FromJson<PostData>(requestBody);
                    PuzzleController.Instance.UnlockDoor(postData.unlock);
                    DialogController.Instance.ShowMsg("门已经解锁：" + postData.unlock);
                }

                string responseText = "POST request received!";
                byte[] buffer = System.Text.Encoding.UTF8.GetBytes(responseText);

                response.ContentLength64 = buffer.Length;
                response.ContentType = "text/plain";
                response.OutputStream.Write(buffer, 0, buffer.Length);
            }
        }
        return response;
    }


    private void MovePrefabToPosition(string type,Position position)
    {
        
        GameObject targetPrefab = null;

        switch (type)
        {
            case "wall":
                targetPrefab = wallPrefab;
                break;
            case "light":
                targetPrefab = lightPrefab;
                break;
        }



        
        if (targetPrefab != null)
        {
            // 确保相机是主相机
            Camera cam = Camera.main;
            if (cam != null)
            {
                // 将屏幕坐标转换为世界坐标
                Vector3 screenPosition = new Vector3(position.left, Screen.height - position.top, cam.nearClipPlane);
                Vector3 worldPosition = cam.ScreenToWorldPoint(screenPosition);

                // 更新Prefab的位置
                targetPrefab.transform.position = new Vector3(worldPosition.x, worldPosition.y, targetPrefab.transform.position.z);
                Debug.Log($"Moved prefab to: {worldPosition}");
            }
            else
            {
                Debug.LogError("Main camera not found.");
            }
        }
        else
        {
            Debug.LogError("Target prefab is not assigned.");
        }
    }
}
```