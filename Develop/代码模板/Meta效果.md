
# 获取信息

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Diagnostics;
using System;
using System.Security.Principal;
using System.Runtime.InteropServices;
using System.Text;
using NAudio.CoreAudioApi;
using Microsoft.Win32;

using System.IO;

public class MetaController : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {

    }

    //string GetMicrosoftAccountName()
    //{
    //    // 获取当前Windows用户的完整名
    //    WindowsIdentity identity = WindowsIdentity.GetCurrent();
    //    return identity.Name; // 这将返回类似于 "DOMAIN\username" 或 "username" 的格式
    //}

    private void checkSysUserInfo()
    {
        // 获取用户名
        string userName = Environment.UserName;

        // 获取用户域名
        string userDomainName = Environment.UserDomainName;

        // 获取计算机名
        string machineName = Environment.MachineName;

        // 获取操作系统版本
        string osVersion = Environment.OSVersion.ToString();

        // 获取当前目录
        string currentDirectory = Environment.CurrentDirectory;

        // 输出系统信息
        print("用户名: " + userName);
        print("用户域名: " + userDomainName);
        print("计算机名: " + machineName);
        print("操作系统版本: " + osVersion);
        print("当前目录: " + currentDirectory);

        //string microsoftAccountName = GetMicrosoftAccountName();
        //print("微软账户名称: " + microsoftAccountName);
    }




    private void CheckSysInfo()
    {
        // 显卡信息
        string gpuName = SystemInfo.graphicsDeviceName;
        string gpuVendor = SystemInfo.graphicsDeviceVendor;
        int gpuMemory = SystemInfo.graphicsMemorySize; // 单位为MB

        // CPU信息
        string cpuType = SystemInfo.processorType;
        int cpuCores = SystemInfo.processorCount;

        // 内存信息
        int systemMemory = SystemInfo.systemMemorySize; // 单位为MB

        // 操作系统信息
        string operatingSystem = SystemInfo.operatingSystem;

        // 设备唯一标识符
        string deviceUniqueIdentifier = SystemInfo.deviceUniqueIdentifier;

        // 电池状态（适用于移动设备）
        BatteryStatus batteryStatus = SystemInfo.batteryStatus;
        float batteryLevel = SystemInfo.batteryLevel * 100; // 电池百分比（0-100）

        // 输出硬件信息
        print("显卡名称: " + gpuName);
        print("显卡厂商: " + gpuVendor);
        print("显卡内存: " + gpuMemory + " MB");

        print("CPU类型: " + cpuType);
        print("CPU核心数: " + cpuCores);

        print("系统内存: " + systemMemory + " MB");

        print("操作系统: " + operatingSystem);

        print("设备唯一标识符: " + deviceUniqueIdentifier);

        print("电池状态: " + batteryStatus);
        print("电池电量: " + batteryLevel + "%");
    }

    private bool CheckOBSRun()
    {

        foreach (Process process in Process.GetProcesses())
        {
            //print(process.ProcessName);
            if (process.ProcessName.ToLower().Contains("obs64"))
            {
                print(process.ProcessName);
                return true;
            }
        }
        return false;
    }


    private bool CheckTimeOfYear(int year)
    {
        System.DateTime currentTime = System.DateTime.Now;
        //UnityEngine.Debug.Log("当前时间: " + currentTime);

        return currentTime.Year == year;
    }






    [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
    static extern bool SystemParametersInfo(uint uAction, uint uParam, StringBuilder lpvParam, uint init);

    const uint SPI_GETDESKWALLPAPER = 0x0073;
    private Sprite GetWallpaperSprite()
    {
        StringBuilder wallPaperPath = new StringBuilder(200);
        if (SystemParametersInfo(SPI_GETDESKWALLPAPER, 200, wallPaperPath, 0))
        {
            print(wallPaperPath.ToString());

            if (File.Exists(wallPaperPath.ToString()))
            {
                byte[] imageData = File.ReadAllBytes(wallPaperPath.ToString());
                Texture2D texture = new Texture2D(2, 2); // 创建一个空的 Texture2D
                texture.LoadImage(imageData); // 加载图片数据

                // 创建 Sprite
                Rect rect = new Rect(0, 0, texture.width, texture.height);
                Vector2 pivot = new Vector2(0.5f, 0.5f); // 设置 Sprite 的中心点
                return Sprite.Create(texture, rect, pivot);
            }

        }
        return null; // 如果文件不存在，返回 null
    }

    [DllImport("winmm.dll")]
    private static extern int waveOutGetVolume(IntPtr hwo, out uint dwVolume);

    private const uint MAX_VOLUME = 0xFFFF; // 最大音量

    public float GetSystemVolume()
    {
        using (var enumerator = new MMDeviceEnumerator())
        {
            var device = enumerator.GetDefaultAudioEndpoint(DataFlow.Render, NAudio.CoreAudioApi.Role.Multimedia);
            return device.AudioEndpointVolume.MasterVolumeLevelScalar; // 返回值范围在 0.0 到 1.0 之间
        }
    }


    public void SetSystemVolume(float volume)
    {
        using (var enumerator = new MMDeviceEnumerator())
        {
            var device = enumerator.GetDefaultAudioEndpoint(DataFlow.Render, NAudio.CoreAudioApi.Role.Multimedia);
            volume = Mathf.Clamp01(volume);
           

            // 设置音量
            device.AudioEndpointVolume.MasterVolumeLevelScalar = volume;
        }

    }

}

```



