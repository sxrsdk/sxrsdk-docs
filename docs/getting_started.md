## Software Requirements

Before starting to use the SXR SDK, make sure you download the following SDKs

* [Android Studio](https://developer.android.com/studio/index.html)
* [JDK 1.7 or above](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
* [Oculus Mobile SDK](https://developer.oculus.com/downloads/package/oculus-mobile-sdk/) (If developing for Samsung GearVR)
* [Google VR SDK](https://developers.google.com/vr/android/download) (If developing for Google DayDream)

## Hardware Requirements

* A Samsung XR [supported devices](/overview/supported_devices)

## Getting Started

Getting started with the SXR SDK in few simple steps

1. Download the [template project](https://github.com/sxrsdk/sxrsdk-demos/tree/master/template/SXRApplication)
1. Rename your project by changine the folder name
1. Open the project with Android Studio
1. Rename your Android App by updating `app_name` field of `app/src/main/res/values/strings.xml`
1. (For Gear VR only) Make sure to download your [Oculus signature file](https://developer.oculus.com/osig/) and copy it under `app\src\main\assets` folder
1. (For DayDream only) remove following code
    1. in `app/build.gradle` 

        ```
    compile "com.samsungxr:backend_oculus:$gearvrfVersion"
        ```

    1. in `AndroidManifest.xml`

        ```
    <meta-data android:name="com.samsung.android.vr.application.mode" android:value="vr_only"/>
        ```

1. (For DayDream only) add following code [(read more)](https://developers.google.com/vr/distribute/daydream/functionality-requirements)
    1. in `AndroidManifest.xml` 

        <pre><code class="xml">
&lt;intent-filter&gt;
    &lt;action android:name="android.intent.action.MAIN" /&gt;
    &lt;!-- intent-filter for DayDream--&gt;
    &lt;category android:name="com.google.intent.category.DAYDREAM"/&gt;
    &lt;!-- End intent-filter for DayDream--&gt;
&lt;/intent-filter&gt;
        </code></pre>

1. Update the applicationID in `app/build.gradle` to avoid conflict between other SXR apps.
1. Click Run button and put on your XR device

## Device Setup

### Gear VR

After you build the application, click `Start` and your device will install Oculus automatically.

!!! note
	You can test VR apps without a VR headset, by enabling Samsung VR service developer mode.
	Settings > Apps > manage applications > Gear VR Service > Storage > Manage Storage - press the "VR Service Version" 6 times. After that a 'You are a developer' message will appear.

!!! note
	Make sure to install your VR app with a valid oculus signature on the device first. Otherwise you'll see a 'You are not a developer' message.

!!! warning
	Screen will start blinking after you turn on the developer mode
	
### DayDream

Enable Google VR Service from "Settings" => "Apps" => "Google VR Service" make sure it has the permission it required to run.

### Project Aurora
