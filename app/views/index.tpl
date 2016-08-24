
<!doctype html>
<html >

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="C:\Users\Krishna\Desktop\Projects\pesproject\app\public\assets\css\bootstrap.min.css">
    <link rel="stylesheet" href="C:\Users\Krishna\Desktop\Projects\pesproject\app\public\assets\css\own.css">
    
    <title> Welcome</title>
</head>

<body>
    <h1 class="text-center text-primary indextext">noName</h1>
    <div class="container top-30" >
        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <div class="panel panel-login">
                    <div class="panel-heading">
                        <div class="row">
                            <div class="col-xs-6">
                                <a href="#" class="active" id="login-form-link">Login</a>
                            </div>
                            <div class="col-xs-6">
                                <a href="#" id="register-form-link">Register</a>
                            </div>
                        </div>
                        <hr>
                    </div>
                    <div class="panel-body">
                        <div class="row">
                            <div class="col-lg-12">
                                <form id="login-form"  style="display: block;" >
                                 

                                    <div class="form-group">
                                        <input type="text"  id="username" tabindex="1" class="form-control" placeholder="Email"  >
                                    </div>
                                    <div class="form-group">
                                        <input type="password"  id="password" tabindex="2" class="form-control" placeholder="Password" >
                                    </div>
                                    <br/>
                                    <div class="form-group">
                                        <div class="row">
                                            <div class="col-sm-6 col-sm-offset-3">
                                                <button id="login-submit" tabindex="4" class="form-control btn btn-primary" >Login</button>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="form-group text-center">
                                        <input type="checkbox" tabindex="3" class="" name="remember" id="remember">
                                        <label for="remember"> Remember Me</label>
                                    </div>
                                    <div class="form-group">
                                        <div class="row">
                                            <div class="col-lg-12">
                                                <div class="text-center">
                                                    <a href="" tabindex="5" class="forgot-password">Forgot Password?</a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </form>
                                <form id="register-form"  style="display: none;" >
                                 
                                    <div class="form-group">
                                        <input type="email"  id="email" tabindex="1" class="form-control" placeholder="Email Address"  >
                                    </div>
                                    <div class="form-group">
                                        <input type="password"  id="password" tabindex="2" class="form-control" placeholder="Password" >
                                    </div>
                                    <div class="form-group">
                                        <input type="password"  id="confirm-password" tabindex="2" class="form-control" placeholder="Confirm Password" >
                                    </div>


                                    <br/>
                                    <div class="form-group">
                                        <div class="row">
                                            <div class="col-sm-6 col-sm-offset-3">
                                                <button   id="register-submit" tabindex="4" class="form-control btn btn-primary" >Register</button>
                                            </div>
                                        </div>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="C:\Users\Krishna\Desktop\Projects\pesproject\app\public\assets\js\jquery.min.js"></script>
    <script src="C:\Users\Krishna\Desktop\Projects\pesproject\app\public\assets\css\bootstrap.min.css"></script>
    <script src="C:\Users\Krishna\Desktop\Projects\pesproject\app\public\assets\js\own.js"></script>

</body>

</html>
