# Blender Addon

SXR SDK Blender Plugin provides a way for the Blender users to preview their creation in Gear VR.

## Prerequisite

* [Blender](https://www.blender.org)
* Download and build [sxrsdk-demos](https://github.com/sxrsdk/sxrsdk-demos) project

## Installation

Download the SXR SDK project from github, and you can find the plugin in `SXR/tools/blender_addon` folder.

Create a zip file of the `sxr_exporter` folder and import it through the add-ons tab of Blender User Preferences.

![](/images/tutorials/blender_import_addon.jpg)

## Usage

Open or create a blender project ([sample project](https://github.com/dsazulay/blender-sample-projects))

Enable `Import-Export: Export to SXR` plugin in User preference

![](/images/tutorials/blender_enable_addon.jpg)

Build and run the `sxr-remote-scripting` from `sxrsdk-demos` project on a device

Switch to Import-Export tab of Blender and
Choose the directory to export (default dir is SXRExportWorkspace located on user's home directory)
Set Client's IP field to reflect the client's device IP address
Click on "Export" button and preview the blender project in VR

![](/images/tutorials/blender_use_addon.jpg)

## Q&A
1. Blender addon report error "Connect attempt failed"
Make sure the IP address is correct, also make sure the computer and Gear VR device is on the same network

