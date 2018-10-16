
## Setting Up Cameras

SXR will create the camera rig by default. Its parameters do not need to be adjusted; however, applications may move the camera rig.

The HMD sensor automatically adjusts camera orientation; your app does not need code for this. Camera background color can be set for each eye; however, they are typically the same. Camera background color and post-effect data can be set by the application. Post-effects are applied to each camera.

__To set the background of the cameras and the position of the camera rig:__

```java
	// set camera background color
	SXRCameraRig cameraRig = mSXRContext.getMainScene().getMainCameraRig();
	cameraRig.getLeftCamera().setBackgroundColor(0.0f, 0.0f, 0.0f, 1.0f);
	cameraRig.getRightCamera().setBackgroundColor(0.0f, 0.0f, 0.0f, 1.0f);

	// set up camerarig position (default)
	cameraRig.getHeadTransform().setPosition(0.0f, 0.0f, 0.0f);
```

## Scene Graph

The scene graph - the VR world - is a hierarchical tree of scene objects. Each scene object is a tree node with one parent and one or more child scene objects. Applications must build a scene graph. Your app needs to set up cameraRig for the root scene object of the scene graph, but does not need to set up cameraRig for each lower-level scene object. To create a scene graph at initialization time, get the SXR main scene (the root scene object) from SXRContext.

__To create the scene graph by getting its root scene object:__

```java
	SXRScene scene = mSXRContext.getMainScene();
```

### Creating the Scene Objects

Populate your VR world's scene graph scene object tree by adding scene objects to the root scene object and to other lower-level scene objects.

The most common way is to load models using the SXR wrapped Assimp library.Assimp can load many 3D file formats and construct SXR scene object hierarchies from them. The materials, textures and shaders are automatically attached to the appropriate scene object and the model is added to the scene. The [asset loader](programming_guide/features/loading_assets) uses the SXRPhongShader class as the shader template for all imported objects.

__To create a scene object from from a file:__

```java
	// load mesh using assimp
	SXRSceneObject model = sxrContext.getAssetLoader().loadModel("sphere.obj", SXRResourceVolume.VolumeType.ANDROID_ASSETS, sxrScene);
```

Usually it is more efficient to let the asset loader create the meshes and textures for you. Bu you can also load only a mesh and construct the scene object, material and render data programmatically. 

__To create a scene object with shader-only material via render data:__

```java
	// load mesh object
	SXRMesh sphereMesh = sxrContext.getAssetLoader().loadMesh("sphere.obj");

	// get material
	SXRMaterial sphereMaterial = new SXRMaterial(sxrContext, mScreenShader.getShaderId());

	// create render data
	SXRRenderData sphereRenderData = new SXRRenderData(sxrContext);

	// set mesh and material for render data
	sphereRenderData.setMesh(sphereMesh);
	sphereRenderData.setMaterial(sphereMaterial);

	// create scene object
	sphereObject = new SXRSceneObject(sxrContext);
	sphereObject.attachRenderData(sphereRenderData);
```

## Managing Transforms in a Scene Graph

After scene objects are added to the scene graph, each scene object can be controlled by transforms.

__To set the position of a scene object and rotate it about an axis with a pivot point:__

```java
	SXRSceneObject rotator = new SXRSceneObject(mSXRContext, 2.0f, 1.0f, rotatorTextures.get(i));
	rotator.getTransform().setPosition(0.0f, 0.0f, -5.0f);
	float degree = 360.0f * i / (rotatorTextures.size() + 1);
	rotator.getTransform().rotateByAxisWithPivot(degree, 0.0f, 1.0f, 0.0f, 0.0f, 0.0f, 0.0f);
```
