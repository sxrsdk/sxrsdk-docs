# Overview

This tutorial will walk you through the steps to build SXR SDK from [source code](https://github.com/sxrsdk/sxrsdk).

!!!note
    If you're looking for prebuilt sxr libraries, checkout the download page [here](https://github.com/sxrsdk/sxrsdk/releases)

## Prerequisites

Before you start, make sure you install the softwares required in [Getting Started Guide](/getting_started)

## Building the SDK

Here are the steps to build the Samsung XR sdk

1. Download/Clone the source code from [github](https://github.com/sxrsdk/sxrsdk)
1. Create a global `gradle.properties` file at gradle home directory, ususall at `~/.gradle/gradle.properties`
1. Add __OVR_MOBILE_SDK__ to `gradle.properties` and set it to the path to the Oculus Mobile SDK.
1. Add __ANDROID_NDK_HOME__ to `gradle.properties` and set it to the path to the Android NDK installation.
1. Open Android Studio and navigate to the sxrsdk folder and open the project under `sxrsdk/SXR/SDK`
1. Click `Build` -> `Make Project`

## Generate Javadocs

When building locally, you can optionally generate Javadoc files with details about the API.

1. Install [JDK](https://www.oracle.com/technetwork/java/javase/overview/index.html) and make sure javadoc is available to the commandline
1. Create a folder named `javadoc` at the __same level__ as `sxrsdk` directory
1. run following command in the `javadoc` folder

```shell
javadoc -Xdoclint:none -d .\SDK -sourcepath ..\sxrsdk\SXR\SDK\sxrsdk\src\main\java -subpackages com.samsungxr -encoding UTF-8 -charset UTF-8 -quiet
```