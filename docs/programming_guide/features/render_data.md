The render data component is what makes a scene object visible. It provides both geometry and appearance properties. The geometry is a single SXRMesh object which contains a set of indexed vertices. The appearance is a SXRMaterial object which contains a set of key/value pairs defining the variables to be sent to the shader. The shader is a program that executes on the GPU. During rendering, SXR manages data flow between your application and the GPU, sending the meshes and materials to the GPU as they are needed. This may require SXR to compile and load a shader into the GPU while your application is running. This may happen when you add something to the scene using SXRScene.addSceneObject. The render data component also controls how your mesh is rendered. You can enable or disable lighting, display an object only on one eye and control the order of rendering using its functions.

|SXRRenderData Function|Description|
|---|---|
|enableLighting|Enable light sources in the shader|
|disableLighting|Disable light sources in the shader|
|setAlphaBlend|Enable / disable alpha blending|
|setAlphaToCoverage|Enable / disable alpha to coverage|
|setAlphaBlendFunc|Set alpha blend functions|
|setCullTest|Enable / disable backface culling|
|setCullFace|Designate back or front faces for culling|
|setDepthTest|Enable / disable depth testing (Z buffer)|
|setDepthMask|Enable / disable depth mask|
|setDrawMode|Designate triangles, lines or points|
|setRenderMask|Designate rendering left, right or both eyes|
|setRenderingOrder|Establish rendering order|
|setSampleCoverage|Specifies coverage of modification mask|
|setInvertCoverageMask|Designates whether modification mask is inverted|
|setOffset|Enables /disables polygon fill offset|
|setOffsetFactor|Specifies polygon fill offset factor|
|setOffsetUnits|Specifies polygon fill offset units|
|setCastShadows|Enable / disable shadow casting|
|setMesh|Designate the mesh to render|
|setMaterial|Specify material properties for shader|


## Render Passes

A render pass lets you render the same scene object multiple times with different settings. This is useful to achieve effects like cartoon rendering or adding glow around an object. The benefit of using a render pass as opposed to duplicating the object is that culling, transformation and skinning are only performed once. A render pass encapsulates the material and rendering properties (but not the mesh).

This example shows how to implement a multi-sided material using render passes. It uses a red material for the front faces and a blue material for the back faces. 

```java
SXRSceneObject cube = new SXRCubeSceneObject(sxrContext);
SXRRenderData rdata = cube.getRenderData();
SXRMaterial red = rdata.getMaterial();
SXRMaterial blue = new SXRMaterial(sxrContext);
SXRRenderPass pass = new SXRRenderPass(sxrContext);

red.setDiffuseColor(1, 0, 0, 1);
blue.setDiffuseColor(0, 0, 1, 0);
rdata.setCullFace(SXRCullFaceEnum.Front);
pass.setMaterial(blue);
pass.setCullFace(SXRCullFaceEnum.Back);
rdata.addPass(pass);
```
