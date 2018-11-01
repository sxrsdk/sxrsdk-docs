<script defer src="https://use.fontawesome.com/releases/v5.0.8/js/all.js"></script>

<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>

<style>

.md-flex a {
    color: white;
}

.md-flex a:hover {
    text-decoration: none;
}

.md-nav a {
    color: black;
}

.md-nav a:hover {
    text-decoration: none;
}

.md-footer a {
    color: white;
}

.md-footer a:hover {
    text-decoration: none;
}

/* Tooltip container */
.tooltip {
    position: relative;
    display: inline-block;
}

/* Tooltip text */
.tooltip .tooltiptext {
    visibility: hidden;
    width: 200px;
    background-color: black;
    color: #fff;
    text-align: center;
    padding: 5px 0;
    border-radius: 6px;
 
    /* Position the tooltip text - see examples below! */
    position: absolute;
    z-index: 1;
    bottom: 110%;
    left: 50%; 
    margin-left: -100px; /* Use half of the width (120/2 = 60), to center the tooltip */
}

/* Show the tooltip text when you mouse over the tooltip container */
.tooltip:hover .tooltiptext {
    visibility: visible;
}

.centered {
    display: block;
    margin-right: auto;
    margin-left: auto;
    text-align:center;
}

.intro_item {
    float: left;
    width: 20%;
}

/*Clear fix*/
.group:after {
  content: "";
  display: table;
  clear: both;
}

/*Sections*/

.section {
    height: 400px;
}

.section h1 {
    color: #ffffff;
    font-weight: bold;
}

.item {
    padding-top: 30px;
    padding-bottom: 20px;
}

.center_parent {
  position: relative;
}

.center_child {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.brand_title {
  position: absolute;
  top: 80%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.background_brand {
    background:url('images/gear-vr_phoneplus_new_vr_img.png');
    background-repeat: no-repeat;
    background-position: center;
    background-size: 300px 120px;
    position: relative;
}

.background_cta {
    background:url('images/gear_vr_cta.png');
    background-repeat: no-repeat;
    background-position: left;
    background-color: #c0c0c0;
    position: relative;   
}

.layer {
    background-color: rgba(0, 0, 0, 0.4);
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}

.btn_red {
    display:inline-block;
    text-decoration:none;
    background-color:#f9443e;
    color:white;
    cursor:pointer;
    font-family:Helvetica,Arial,sans-serif;
    font-size:20px;
    line-height:50px;
    text-align:center;
    margin:0;
    height:50px;
    padding:0px 33px;
    border-radius:15px;
    max-width:100%;
    white-space:nowrap;
    overflow:hidden;
    text-overflow:ellipsis;
    font-weight:bold;
    -webkit-font-smoothing:antialiased;
    -moz-osx-font-smoothing:grayscale;
}

.btn_blue {
    display:inline-block;
    text-decoration:none;
    background-color:#267DDD;
    color:white;
    cursor:pointer;
    font-family:Helvetica,Arial,sans-serif;
    font-size:20px;
    line-height:50px;
    text-align:center;
    margin:0;
    height:50px;
    padding:0px 33px;
    border-radius:15px;
    max-width:100%;
    white-space:nowrap;
    overflow:hidden;
    text-overflow:ellipsis;
    font-weight:bold;
    -webkit-font-smoothing:antialiased;
    -moz-osx-font-smoothing:grayscale;
}

.sample_card {
    height: 380px;
    box-shadow: 0px 2px 4px -1px rgba(0, 0, 0, 0.2), 0px 4px 5px 0px rgba(0, 0, 0, 0.14), 0px 1px 10px 0px rgba(0, 0, 0, 0.12);
    transition: box-shadow 0.28s cubic-bezier(0.4, 0, 0.2, 1);
}

/*Small devices (landscape phones, 576px and up)*/
@media (min-width: 576px) {
    
}

/*Medium devices (tablets, 768px and up)*/
@media (min-width: 768px) {
    .item {
        height: 400px;
        padding-top: 50px;
        padding-bottom: 0px;
    }

    .background_brand {
        background:url('images/gear-vr_phoneplus_new_vr_img.png');
        background-repeat: no-repeat;
        background-position: center;
        background-size: 740px 298px;
        position: relative;
    }

    .brand_title {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }
}

/*Large devices (desktops, 992px and up)*/
@media (min-width: 992px) {
    
}

/*/Extra large devices (large desktops, 1200px and up)*/
@media (min-width: 1200px) {
    
}

</style>

<div class="container-fluid">
    <div class="row section">
        <div class="col-12 col-lg-6 mx-auto">
            <img class="center_child" src="images/SXR_Logo_Blue_Text_Inline.png">
        </div>
      </div>
      <div class="row section">
        <div class="col center_parent background_brand">
            <div class="layer">
                <h1 class="brand_title">POWERFUL XR SDK <br>FOR MOBILE</h1>
            </div>
        </div>
      </div>
      <div class="row justify-content-center">
        <div class="col-12 col-lg-2">
            <div class="centered item">
                <h4>Simple</h4>
                <i class="fas fa-5x fa-child"></i>
                <br><br>
                <span>Simple API enables rapid prototyping</span>
            </div>
        </div>
        <div class="col-12 col-lg-2">
            <div class="centered item">
                <h4>Powerful</h4>
                <i class="fas fa-5x fa-shipping-fast"></i>
                <br><br>
                <span>XR-specific rendering optimizations</span>
            </div>
        </div>
        <div class="col-12 col-lg-2">
            <div class="centered item">
                <h4>Mobile Centric</h4>
                <i class="fab fa-5x fa-android"></i>
                <br><br>
                <span>Built with focus on mobile performance</span>
            </div>
        </div>
        <div class="col-12 col-lg-2">
            <div class="centered item">
                <h4>Open Source</h4>
                <i class="fab fa-5x fa-github"></i>
                <br><br>
                <span>No licensing fees or royalties ever</span>
            </div>
        </div>
        <div class="col-12 col-lg-2">
            <div class="centered item">
                <h4>Cross Platform</h4>
                <i class="fas fa-5x fa-cogs"></i>
                <br><br>
                <span>Write code once and works for Gear VR, Daydream, and AR Applications</span>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col section background_cta center_parent">
            <div class="center_child">
                <a class="button btn_red"  style="color: white;" href="getting_started">
                    Getting Started
                </a>
                <a class="typeform-share button btn_blue" style="color: white;" href="https://nitosan.typeform.com/to/fw9Ylx" data-mode="popup" style="" target="_blank">
                    Leave Feedback
                </a>
            </div>
        </div>
    </div>
    <div class="row" style="margin-top: 30px;">
        <div class="col-12 centered">
            <h1>Sample Highlights</h1>
        </div>
        <div class="col-12 col-lg-3">
            <div class="card mb-4 sample_card">
                <img class="card-img-top" src="/images/samples/img_1_360photo.png" alt="360 Photo">
                <div class="card-body">
                    <h5 class="card-title">360 Photo</h5>
                    <p class="card-text">A minimal sample showing how to display an equirectangular (360) photo.</p>
                </div>
                <div class="card-footer">
                    <a href="https://github.com/sxrsdk/sxrsdk-demos/tree/master/sxr-360photo" class="btn btn-primary" style="color:white;">Source</a>
                </div>
            </div>
        </div>
        <div class="col-12 col-lg-3" >
            <div class="card mb-4 sample_card">
                <img class="card-img-top" src="/images/samples/img_2_360video.png" alt="360 Video">
                <div class="card-body">
                    <h5 class="card-title">360 Video</h5>
                    <p class="card-text">A minimal sample showing how to display an equirectangular (360) video.</p>
                </div>
                <div class="card-footer">
                    <a href="https://github.com/sxrsdk/sxrsdk-demos/tree/master/sxr-360video" class="btn btn-primary" style="color:white;">Source</a>
                </div>
            </div>
        </div>
        <div class="col-12 col-lg-3">
            <div class="card mb-4 sample_card">
                <img class="card-img-top" src="/images/samples/img_3_3dcursor.png" alt="3D Cursor">
                <div class="card-body">
                    <h5 class="card-title">3D Cursor</h5>
                    <p class="card-text">A simplified version of the sxr-3dcursor sample that shows how to use the 3DCursor plugin.</p>
                </div>
                <div class="card-footer">
                    <a href="https://github.com/sxrsdk/sxrsdk-demos/tree/master/sxr-3dcursor" class="btn btn-primary" style="color:white;">Source</a>
                </div>
            </div>
        </div>
        <div class="col-12 col-lg-3">
            <div class="card mb-4 sample_card">
                <img class="card-img-top" src="/images/samples/img_4_accessibility.png" alt="Accessibility">
                <div class="card-body">
                    <h5 class="card-title">Accessibility</h5>
                    <p class="card-text">Shows how to use SXR's accessibility classes. For example: InvertedColors, TextToSpeech, and Zoom.</p>
                </div>
                <div class="card-footer">
                    <a href="https://github.com/sxrsdk/sxrsdk-demos/tree/master/sxr-accessibility" class="btn btn-primary" style="color:white;">Source</a>
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-12 col-lg-3">
            <div class="card mb-4 sample_card">
                <img class="card-img-top" src="/images/samples/img_9_controller.png" alt="Controller">
                <div class="card-body">
                    <h5 class="card-title">Controller</h5>
                    <p class="card-text">A simple sample that demostrates how to use VR controller.</p>
                </div>
                <div class="card-footer">
                    <a href="https://github.com/sxrsdk/sxrsdk-demos/tree/master/sxr-controller" class="btn btn-primary" style="color:white;">Source</a>
                </div>
            </div>
        </div>
        <div class="col-12 col-lg-3">
            <div class="card mb-4 sample_card">
                <img class="card-img-top" src="/images/samples/img_32_solarsystem.png" alt="Controller">
                <div class="card-body">
                    <h5 class="card-title">Solar System</h5>
                    <p class="card-text">A sample that shows both heirarchy and animation.</p>
                </div>
                <div class="card-footer">
                    <a href="https://github.com/sxrsdk/sxrsdk-demos/tree/master/sxr-solarsystem" class="btn btn-primary" style="color:white;">Source</a>
                </div>
            </div>
        </div>
        <div class="col-12 col-lg-3">
            <div class="card mb-4 sample_card">
                <img class="card-img-top" src="/images/samples/img_15_immersepedia.png" alt="Immersivepedia">
                <div class="card-body">
                    <h5 class="card-title">Immersivepedia</h5>
                    <p class="card-text">A larger sample that shows a concept of an immersive virtual museum.</p>
                </div>
                <div class="card-footer">
                    <a href="https://github.com/sxrsdk/sxrsdk-demos/tree/master/sxr-immersivepedia" class="btn btn-primary" style="color:white;">Source</a>
                </div>
            </div>
        </div>
        <div class="col-12 col-lg-3">
            <div class="card mb-4 sample_card">
                <img class="card-img-top" src="/images/samples/img_16_javascript.png" alt="Javascript">
                <div class="card-body">
                    <h5 class="card-title">Javascript</h5>
                    <p class="card-text">A minimal example showing how an application can be written with Javascript.</p>
                </div>
                <div class="card-footer">
                    <a href="https://github.com/sxrsdk/sxrsdk-demos/tree/master/sxr-javascript" class="btn btn-primary" style="color:white;">Source</a>
                </div>
            </div>
        </div>
    </div>
</div>

<script> (function() { var qs,js,q,s,d=document, gi=d.getElementById, ce=d.createElement, gt=d.getElementsByTagName, id="typef_orm_share", b="https://embed.typeform.com/"; if(!gi.call(d,id)){ js=ce.call(d,"script"); js.id=id; js.src=b+"embed.js"; q=gt.call(d,"script")[0]; q.parentNode.insertBefore(js,q) } })() 
</script>
