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
    implementation "org.gearvrf:backend_daydream:$gearvrfVersion"
    implementation "org.gearvrf:backend_oculus:$gearvrfVersion"
}
```


