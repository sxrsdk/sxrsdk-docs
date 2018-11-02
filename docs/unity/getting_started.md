## Software Requirements

* [Unity 2017.3.0 or later](https://unity3d.com/get-unity/download) with Android support
* [SXR Unity Plugin](https://unity3d.com/get-unity/download)

## Hardware Requirements

* A Samsung XR [supported devices](/overview/supported_devices)

## Import Plugin

* In Unity select `Assets` -> `Import Package` -> `Custom Package` 
* Select `SXR_UnityPlugin.unitypackage`, import everything from the package

## Prepare your Unity project

In order for SXR to track user movement, the first-person camera needs to be converted to a `GVRCamera`

* In Unity select `Gear VR` -> `Prepare VR Camera`

![Prepare Camera](/images/unity/unity_prepare_camera.png)

* Find and select the "Main Camera" of your app in Unity's Hierarchy window

![Select Camera](/images/unity/unity_prepare_camera_before.png)

* With your "Main Camera" selected, click on "Prepare VR Camera" in the sub window, this would process the "Main Camera" and convert it to be compatible with SXR. If the process is successful, you will see a fiew more GameObjects added to the 'Main Camera' as children.

![Prepared Camera](/images/unity/unity_prepared_camera.png)

!!! note
    If you have multiple game scenes, you should perform this on every scene

* You can tweak the camera settings with `GVREventSystem`

Recommended settings

![Event system settings](/images/unity/gvr_event_system_setting.jpg)

* `Use Fixed Update`- Use the fixed update for camera rendering (uses in more CPU cycles).
* `Use Chromatic Aberration`- Correct chromatic aberration (requires more CPU processing time).
* `Use Antialiasing`- Enable antialiasing optimized with the SXR plugin. Unity's antialiasing will be overwritten by the plugin.
* `Eye Buffer Size`- Size of each sys buffer
* `Use Multiple Camera`- Currently not supported.

## Build Settings

Use the following steps to build a SXR project

1. Switch Platform to `Android`

    ![Switch Platform](/images/unity/sxr_switch_platform.png)

1. Make sure `Player Settings` -> `Resolution And Presentation` -> `Landscape Left` is selected.

1. Turn off `Player Settings` -> `XR Settings` -> `Virtual Reality Supported`

1. Turn off `Player Settings` -> `Other Settings` -> `Multithreaded Rendering`

Now you're ready to build your SXR game or app