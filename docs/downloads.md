# SDK Downloads

Latest Snapshot Version: `5.0.1-SNAPSHOT`

Latest Stable Version: `5.0.0`

| Platform | Description      | Download                      |
|----------|------------------|-------------------------------|
| Android  | SXR Android SDK  | [sxr-android-sdk-source](https://github.com/sxrsdk/sxrsdk) |
| Unity    | SXR Unity Plugin | [sxr-unity-plugin.unitypackage](/files/SXR_UnityPlugin_Beta.90.0.UnityPackage) |

!!! note
    Add the following lines to the `build.gradle` to use the latest SXR sdk

```
ext.gearvrfVersion='5.0.0'
dependencies {
    implementation "org.gearvrf:framework:$gearvrfVersion"
}
```

   To use the Oculus backend add this to the dependencies:
```
    implementation "org.gearvrf:backend_oculus:$gearvrfVersion"
```

   To use the Daydream backend add this to the dependencies:
```
    implementation "org.gearvrf:backend_daydream:$gearvrfVersion"
```

   To use the Monoscopic backend add this to the dependencies:
```
    implementation "org.gearvrf:backend_monoscopic:$gearvrfVersion"
```

   Support for more than one backend should not be added to an app. Consider using product flavors if an app wants to target more than one backend.
