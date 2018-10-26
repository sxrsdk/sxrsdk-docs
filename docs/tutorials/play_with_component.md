## Overview

The SXR SDK follows component-entity mode, each Node consists of multiple components that control different aspects of the Node such as transformation, rendering, collision detection. When we use functions like `getTransform()` or `getRenderData()`, it actually uses `getComponent()` underneath.

In this tutorial, we're going to create our own component for the Node and use it in your app/game.

##Create Project
Create an SXR project by copying the [template project](https://github.com/sxrsdk/sxrsdk-demos/tree/master/template/SXRApplication) 

Perform the following steps to make sure your project runs correctly

1. (if developing for Gear VR) Copy your [Oculus signature file](https://developer.oculus.com/osig/) to `app/src/main/assets` folder.
1. Change the `applicationId` in `build.gradle` to a unique name to avoid naming conflict when you test the app later
1. Change the `app_name` in `res/values/strings.xml` to avoid confusion when you debug the app.

## Create a new component
To create a new component, simply create a new class that extends `SXRBehavior`.

In this case, we create a class called `RotateBehavior`, simply makes `Node` to rotate.

```java
public class RotateBehavior extends SXRBehavior {

    private static final long TYPE_Rotate_behavior = newComponentType(RotateBehavior.class);

    float mRotationSpeed = 1.0f;

    protected RotateBehavior(SXRContext sxrContext) {
        super(sxrContext);
        mType = TYPE_Rotate_behavior;
    }

    public static long getComponentType(){ return TYPE_Rotate_behavior;}

}
```

Note that we have a static field called `TYPE_Rotate_behavior` as well as a function `getComponentType()`.

It will be useful when we need to access this component from a `Node` later.

!!!note
    If we want to access this component from a `Node` we can use `Node.getComponent(RotateBehavior.getComponentType())`

## Customize logic
`SXRBehavior` provides couple methods that you can override to customize your behavior.

* `onAttach()` will trigger when the component is attached to a `Node`
* `onDetach` will trigger when the component is detached from the `Node`
* `onDrawFrame` will trigger everytime a new frame is drawn

In this case, we're going to use `onDrawFrame` because `RotationBehavior` will change the rotation of the `Node` every frame.

Override the `onDrawFrame` as following
```java
    @Override
    public void onDrawFrame(float frameTime) {
        super.onDrawFrame(frameTime);

        getOwnerObject().getTransform().rotateByAxis(mRotationSpeed, 0,1,0);
    }
```

Basically, this means to rotate the object 1 degree on each frame.

## Use components

In order to see our newly created component in action, we need to attach it to a `Node`. Simply call `attachComponent()`.

To access the component on a `Node`, use `getComponent(RotateBehavior.getComponentType())`

## Source Code
Complete [Source Code](https://github.com/nitosan/sxrsdk-samples/tree/master/sample_billboard) for this sample 
