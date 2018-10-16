
The SXR SDK supports loading of 3D content files both synchronously and asynchronously. Your application may issue a blocking load and wait for the asset or get a callback when the asset loading is finished. The SXR SDK can import .OBJ, .FBX, Collada  (.dae) and X3D file formats, as well as all file formats supported by [Assimp](http://www.assimp.org/main_features_formats.html). The SXR SDK can also read all commonly used bitmap file formats.

## Loading a 3D Model

Loading models is handled by the SXRAssetLoader class which is accessible from the context by calling SXRContext.getAssetLoader(). The asset loader can load models from a variety of places. If you are providing a file name, a prefix on the name indicates the origin of the file:

* "sd:" designates the model on the phone SD card.
* "http:" or "https:" designates the model is on the internet.
* No prefix meaqns the filename is relative to the "assets" directory.

For more flexibility, you can use the *SXRAndroidResource* class which lets you import assets from resources in your application or from an already open Android stream. Both models and textures can be loaded from SXRAndroidResource objects.

| SXRAndroidResource Constructors | Volume Type | Input source |
|---------------------------------|-------------|--------------|
| SXRAndroidResource(String path) | ResourceType.LINUX_FILESYSTEM  | SD card |
| SXRAndroidResource(File file)   | ResourceType.LINUX_FILESYSTEM  | SD card |
| SXRAndroidResource(SXRContext, int resourceID) | ResourceType.ANDROID_RESOURCE | res directory |
| SXRAndroidResource(Context, int resourceID) | ResourceType.ANDROID_RESOURCE | res directory |
| SXRAndroidResource(SXRContext, String path) | ResourceType.ANDROID_ASSETS | assets directory |
| SXRAndroidResource(SXRContext, URL url) | ResourceType.NETWORK | internet |
| SXRAndroidResource(SXRContext, InputStream stream) | ResourceType.INPUT_STREAM | input stream |

The `SXRAssetLoader.loadModel` function loads a model from a device and returns as soon as the model geometry has been parsed and accumulated. This model may not have been added to the scene yet. If you pass the current SXRScene as an argument, the asset loader will wait until all of the textures in the model have been loaded and then add it to the scene. If you omit the argument, the model is not added to the scene and you will need to add it in your own code.

## Model Loading Examples

This example shows how to load a model from a URL and another from the application resources. The textures are loaded in the background in another thread. The model will be added to the scene when all of its textures have completed loading. The model returned may not be completely loaded but all of the geometry will be accessible. Usually assets are loaded in the onInit function of your main script.

```java
public void onInit(SXRContext context)
{
    SXRScene scene = context.getMainScene();
    try
    {
        String url = "https://raw.githubusercontent.com/gearvrf/sxrsdk-demos/master/sxrjassimpmodelloader/assets/trees/trees9.3ds";
        SXRSceneObject model1 = context.getAssetLoader().loadModel(url, scene);
        model1.getTransform().setPosition(0.0f, -4.0f, -20.0f);

        SXRAndroidResource resource = new SXRAndroidResource(context, R.raw.spaceship);
    	EnumSet<SXRImportSettings> settings = SXRImportSettings.getRecommendedSettings();
    	SXRSceneObject model2 = context.getAssetLoader().loadModel(resource, settings, true, scene);
        model2.getTransform().setPositionZ(-10.0f);
    }
    catch (IOException e)
    {
        Log.e("ERROR", "Failed to load model: %s", e);
    }
}
```

## Import Settings

The *SXRImportSettings* object controls how the asset is imported. Depending on what your application is going to do with the model, import settings can help optimize performance. By default, all models are imported in full fidelity - all vertex components, light sources, cameras and textures are included. If you are not using light sources, it is more efficient to omit normals from the meshes and to not import any light sources in the model. Similarly, if you do not plan to animate the model, importing without animation will be faster and will suppress bone indices and bone weights from your meshes, which will cause the SXR SDK to use a more efficient shader.

| Setting | What it does |
|---------|--------------|
| NO_LIGHTING | Suppress import of normals and light sources |
| NO_ANIMATION | Suppress import of animation (bones, bone indices, bone weights and animation clips) |
| NO_TEXTURING | Suppress import of textures and texture coordinates |
| START_ANIMATIONS | Automatically start animations |
| CALCULATE_TANGENTS | Calculate tangents required for normal mapping |
| JOIN_IDENTICAL_VERTICES* | Join vertices when possible |
| TRIANGULATE* | Triangulate all meshes (required for SXR) |
| CALCULATE_NORMALS | Calculate normals if not present |
| CALCULATE_SMOOTH_NORMALS | Calculate and smooth normals |
| LIMIT_BONE_WEIGHT* | Limit bone weight to 4 (required for SXR) |
| IMPROVE_VERTEX_CACHE_LOCALITY | reorder vertices for cache locality |
| SORTBY_PRIMITIVE_TYPE* | Split meshes by primitive type |
| OPTIMIZE_MESHES | Combine meshes when possible |
| OPTIMIZE_GRAPH | Merge nodes without bones |
| FLIP_UV* | Flip UV coordinates |

Typically you will get the recommended settings (they are starred in the table) and add to them since a few of these settings are required for SXR to function properly. Only indexed triangle meshes are supported and meshes may only have four bones.


## Asynchronous Loading

The asset loader can also asynchronously load geometry and textures. You have the option of providing an asset event handler which will notify your application when textures and geometry are loaded and when the asset and all of its textures have finished loading. In this case, a model is placed in the scene and the asset loader adds the imported scene objects as children. You can also request the asset loader to replace the entire scene.

The asynchronous forms of *loadModel* specify the input asset as a *SXRResourceVolume* object. This object allows multiple assets to be loaded from a single input stream, such as a ZIP file. You can also subclass *SXRResourceVolume* to get complete control over the asset loading process.

This example waits for a model to be loaded from the assets directory and then centers it before adding it to the scene.
```java
SXRScene scene;
SXRSceneObject root = new SXRSceneObject(context);
SXRResourceVolume volume = new SXRResourceVolume(context, "models/mymodel.fbx");

context.getAssetLoader().loadModel(root, volume, new IAssetEvents()
{
	public void onAssetLoaded(SXRContext context, SXRSceneObject model, String filePath, String errors);
    {
    	BoundingVolume bv = model.getBoundingVolume();
        Vector3f c = bv.center();
        model.getTransform().setPosition(-c.x, -c.y, -c.z - 1.0f);
    }
    public void onModelLoaded(SXRContext context, SXRSceneObject model, String filePath) { }
    public void onTextureLoaded(SXRContext context, SXRTexture texture, String filePath) { }
    public void onModelError(SXRContext context, String error, String filePath) { }
    public void onTextureError(SXRContext context, String error, String filePath) { }
});
}
```
## Loading Textures

Imported 3D assets tyically create bitmap textures but the asset loader can import textures directly in many other formats. You can import cubemaps, compressed cubemaps, floating point textures as well as compressed and uncompressed bitmaps.

All textures are loaded asynchronously in a background thread. The asset loader immediately returns a *SXRTexture* object but the SXRImage providing the data for the texture may not be available yet. The SXR SDK will not render a mesh until all of the textures it requires are loaded. Typically your application does not need to know when textures are loaded but, if this is necessary, the asset loader provides a callback mechanism for this purpose.

This example shows how to load a cubemap texture from a ZIP file and apply use it as a skybox.

```java
SXRTexture tex = ctx.getAssetLoader().loadCubemapTexture(new SXRAndroidResource(ctx, R.raw.beach));
SXRMaterial cubeMapMtl = new SXRMaterial(ctx, SXRMaterial.SXRShaderType.Cubemap.ID);
SXRSceneObject skybox = new SXRCubeSceneObject(ctx, false, cubeMapMtl);

cubeMapMtl.setTexture("u_texture", tex);
skybox.getTransform().setScale(10, 10, 10);
skybox.setName("background");
scene.addSceneObject(skybox);
```
